# Using EESSI with Apple Silicon on macOS 26

> **Requirements**
>
> - Mac with **Apple Silicon** (M-series chip)
> - **macOS 26** (Tahoe) or later
> - internet connection (EESSI software is streamed on demand from CVMFS Stratum 1 servers)/Other advanced solutions are also possible

---

## 1. Install the `container` tool

Download the latest signed installer package (`.pkg`) from the
[`apple/container` GitHub releases page](https://github.com/apple/container/releases).

Double-click the downloaded `.pkg` file and follow the on-screen instructions.
When prompted, enter your administrator password to allow the installer to place
files under `/usr/local`

Alternatively, using [Homebrew](https://formulae.brew.sh/):

```
brew install container
```

Verify the installation:

```
container --version
```

You should see output similar to:

```
container CLI version 0.10.0 (build: release, commit: unspeci)
```

---

## 2. Start the `container` system service

The `container` tool requires a background API server. Start it with:

```
container system start
```

To confirm the service is running:

```
container system status
```

---

## 3. Pull the EESSI client container image

Pull the EESSI `ubuntu22.04-macOS-26` image from the GitHub Container Registry:

```
container image pull ghcr.io/eessi/client:ubuntu22.04-macOS-26
```

This [image](https://github.com/EESSI/filesystem-layer/blob/main/containers/Dockerfile.EESSI-client-ubuntu22.04-macOS-26) is an `arm64` (Apple Silicon) Ubuntu 22.04 image that includes the
CernVM-FS client pre-installed and configured for EESSI.


## 4. Start an interactive EESSI session

Run the container interactively:

```
container run -it --rm --name eessi ghcr.io/eessi/client:ubuntu22.04-macOS-26
```
**Note**: `-it` provides an interactive session inside the container and `--rm` keeps your system clean by automatically removing the stopped container after you exit.

---

## 5. Once inside the container shell

Verify that the EESSI repository is accessible:

```
ls /cvmfs/software.eessi.io
```

You should see output similar to:

```
README.eessi  defaults  host_injections  init  versions
```

Initialize the EESSI environment:

```
source /cvmfs/software.eessi.io/versions/2023.06/init/lmod/bash
```
Expected output:

**Note**: EESSI currenly supports NVIDIA GPUs, so the message **EESSI did not identify an accelerator on the system** is expected.

```
Module for EESSI/2023.06 loaded successfully
EESSI has selected aarch64/neoverse_n1 as the compatible CPU target for EESSI/2023.06
EESSI did not identify an accelerator on the system
(for debug information when loading the EESSI module, set the environment variable EESSI_MODULE_DEBUG_INIT)
```
EESSI is now ready to use inside the container.

---

## 7. Use EESSI software

List available modules:

```
module avail
```

Search for a specific package:

```
module avail TensorFlow
```

Load and use a module:

```
module load TensorFlow/2.13.0-foss-2023a
python3 -c "import tensorflow as tf; print(tf.__version__)"
```

---

## Cleanup

Remove the pulled image:

```
container image rm ghcr.io/eessi/client:ubuntu22.04-macOS-26
```
Stop the `container` system service when it is no longer needed:

```
container system stop
```

---

