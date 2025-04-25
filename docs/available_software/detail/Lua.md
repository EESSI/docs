---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Lua is a powerful, fast, lightweight, embeddable scripting language.
    Lua combines simple procedural syntax with powerful data description constructs
    based on associative arrays and extensible semantics. Lua is dynamically typed,
    runs by interpreting bytecode for a register-based virtual machine, and has automatic
    memory management with incremental garbage collection, making it ideal for configuration,
    scripting, and rapid prototyping.
  license: Not confirmed
  name: Lua
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''Lua/5.4.4-GCCcore-12.2.0'', ''Lua/5.4.6-GCCcore-12.3.0'', ''Lua/5.4.6-GCCcore-13.2.0'']'
  url: https://www.lua.org/
---

Lua
===


Lua is a powerful, fast, lightweight, embeddable scripting language. Lua combines simple procedural syntax with powerful data description constructs based on associative arrays and extensible semantics. Lua is dynamically typed, runs by interpreting bytecode for a register-based virtual machine, and has automatic memory management with incremental garbage collection, making it ideal for configuration, scripting, and rapid prototyping.

https://www.lua.org/
# Available modules


The overview below shows which Lua installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Lua, load one of these modules using a `module load` command like:

```shell
module load Lua/5.4.6-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Lua/5.4.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|Lua/5.4.6-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|Lua/5.4.4-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
