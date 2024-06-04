# Configuring site-specific Lmod hooks
You may want to customize what happens when certain modules are loaded, for example, you may want to set additional environment variables. This is possible with [LMOD hooks](https://lmod.readthedocs.io/en/latest/170_hooks.html). A typical example would be when you want to tune the OpenMPI module for your system by setting additional environment variables when an OpenMPI module is loaded.


## Location of the hooks
The EESSI software stack provides its own set of hooks in `$LMOD_PACKAGE_PATH/SitePackage.lua`. This `SitePackage.lua` also searches for site-specific hooks in two additonal locations:

- `$EESSI_CVMFS_REPO/host_injections/$EESSI_VERSION/.lmod/SitePackage.lua`
- `$EESSI_CVMFS_REPO/host_injections/$EESSI_VERSION/software/$EESSI_OS_TYPE/$EESSI_SOFTWARE_SUBDIR/.lmod/SitePackage.lua`

The first allows for hooks that need to be executed for that system, irrespective of the CPU architecture. The second allows for hooks specific to a certain architecture.

## Architecture-independent hooks
Hooks are written in Lua and can use any of the standard Lmod functionality as described in the [Lmod documentation](https://lmod.readthedocs.io/en/latest/170_hooks.html). While there are many types of hooks, you most likely want to specify a load or unload hook. Note that the EESSI hooks provide a nice example of what you can do with hooks. Here, as an example, we will define a `load` hook that environment variable `MY_ENV_VAR` to `1` whenever an `OpenMPI` module is loaded.

First, you typically want to load the necessary Lua packages:
```lua
-- $EESSI_CVMFS_REPO/host_injections/$EESSI_VERSION/.lmod/SitePackage.lua

-- The Strict package checks for the use of undeclared variables:
require("strict")

-- Load the Lmod Hook package
local hook=require("Hook")
```

Next, we define a function that we want to use as a hook. Unfortunately, registering multiple hooks of the same type (e.g. multiple `load` hooks) is only supported in Lmod 8.7.35+. EESSI version 2023.06 uses Lmod 8.7.30. Thus, we define our function without the local keyword, so that we can still add to it later in an architecture-specific hook (if we wanted to):

```lua
-- Define a function for the hook
-- Note that we define this without 'local' keyword
-- That way we can still add to this function in an architecture-specific hook
function set_my_env_var_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('MY_ENV_VAR', '1')
    end
end
```

for the same reason that multiple hooks cannot be registered, we need to combine this function for our site-specific (architecture-independent) with the function that specifies the EESSI `load` hook. Note that all EESSI hooks will be called `eessi_<hook_type>_hook` by convention.

```lua
-- Registering multiple hook functions, e.g. multiple load hooks is only supported in Lmod 8.7.35+
-- EESSI version 2023.06 uses lmod 8.7.30. Thus, we first have to combine all functions into a single one,
-- before registering it as a hook
local function combined_load_hook(t)
    -- Call the EESSI load hook (if it exists)
    -- Note that if you wanted to overwrite the EESSI hooks (not recommended!), you would ommit this
    if eessi_load_hook ~= nil then
        eessi_load_hook(t)
    end
    -- Call the site-specific load hook
    set_my_env_var_openmpi(t)
end
```

Then, we can finally register this function as an Lmod hook:

```lua
hook.register("load", combined_load_hook)
```

Thus, our complete `$EESSI_CVMFS_REPO/host_injections/$EESSI_VERSION/.lmod/SitePackage.lua` now looks like this (omitting the comments):

```lua
require("strict")
local hook=require("Hook")

function set_my_env_var_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('MY_ENV_VAR', '1')
    end
end

local function combined_load_hook(t)
    if eessi_load_hook ~= nil then
        eessi_load_hook(t)
    end
    set_my_env_var_openmpi(t)
end

hook.register("load", combined_load_hook)
```

Note that for future EESSI versions, if they use Lmod 8.7.35+, this would be simplified to:

```lua
require("strict")
local hook=require("Hook")

local function set_my_env_var_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('MY_ENV_VAR', '1')
    end
end

hook.register("load", set_my_env_var_openmpi, "append")
```

## Architecture-dependent hooks
Now, assume that in addition we want to set an environment variable `MY_SECOND_ENV_VAR` to `5`, but only for nodes that have the `zen3` architecture. First, again, you typically want to load the necessary Lua packages:

```lua
-- $EESSI_CVMFS_REPO/host_injections/$EESSI_VERSION/software/linux/x86_64/amd/zen3/.lmod/SitePackage.lua

-- The Strict package checks for the use of undeclared variables:
require("strict")

-- Load the Lmod Hook package
local hook=require("Hook")
```

Next, we define the function for the hook itself

```lua
-- Define a function for the hook
-- This time, we can define it as a local function, as there are no hooks more specific than this 
local function set_my_second_env_var_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('MY_SECOND_ENV_VAR', '5')
    end
end
```

Then, we combine the functions into one

```lua
local function combined_load_hook(t)
    -- Call the EESSI load hook first
    if eessi_load_hook ~= nil then
        eessi_load_hook(t)
    end
    -- Then call the architecture-independent load hook
    if set_my_env_var_openmpi(t) ~= nil then
        set_my_env_var_openmpi(t)
    end
    -- And finally the architecture-dependent load hook we just defined
    set_my_second_env_var_openmpi(t)
end
```

before finally registering it as an Lmod hook

```lua
hook.register("load", combined_load_hook)
```

Thus, our full `$EESSI_CVMFS_REPO/host_injections/$EESSI_VERSION/software/linux/x86_64/amd/zen3/.lmod/SitePackage.lua` now looks like this (ommitting the comments):

```lua
require("strict")
local hook=require("Hook")

local function set_my_second_env_var_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('MY_SECOND_ENV_VAR', '5')
    end
end

local function combined_load_hook(t)
    if eessi_load_hook ~= nil then
        eessi_load_hook(t)
    end
    if set_my_env_var_openmpi(t) ~= nil then
        set_my_env_var_openmpi(t)
    end
    set_my_second_env_var_openmpi(t)
end

hook.register("load", combined_load_hook)
```

Again, note that for future EESSI versions, if they use Lmod 8.7.35+, this would simplify to

```lua
require("strict")
local hook=require("Hook")

local function set_my_second_env_var_openmpi(t)
    local simpleName = string.match(t.modFullName, "(.-)/")
    if simpleName == 'OpenMPI' then
        setenv('MY_SECOND_ENV_VAR', '5')
    end
end

hook.register("load", set_my_second_var_openmpi, "append")
```
