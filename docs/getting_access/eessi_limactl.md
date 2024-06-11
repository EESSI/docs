# Installing EESSI with limactl on MacOS

## Istallation of Lima

see lima documentation: [https://lima-vm.io/docs/installation/](https://lima-vm.io/docs/installation/)

``` { .bash .copy }
brew install lima
```

## Installing EESSI in limactl with EESSI template

### Example `eessi.yaml` file

Use the EESSI template to install a virtual machine with eessi installed. Create a `eessi.yaml` file

=== "Install a virtual machine with a Debian image"
    ``` { .bash .copy }
    # A template to use the EESSI software stack (see https://eessi.io) on macOS
    # $ limactl start ./eessi.yaml
    # $ limactl shell eessi

    images:
    # Try to use release-yyyyMMdd image if available. Note that release-yyyyMMdd will be removed after several months.
    - location: "https://cloud.debian.org/images/cloud/bookworm/20240429-1732/debian-12-genericcloud-amd64-20240429-1732.qcow2"
      arch: "x86_64"
      digest: "sha512:6cc752d71b390c7fea64b0b598225914a7f4adacd4a33fa366187fac01094648628e0681a109ae9320b9a79aba2832f33395fa13154dad636465b7d9cdbed599"
    - location: "https://cloud.debian.org/images/cloud/bookworm/20240429-1732/debian-12-genericcloud-arm64-20240429-1732.qcow2"
      arch: "aarch64"
      digest: "sha512:59afc40ad0062ca100c9280a281256487348c8aa23b3e70c329a6d6f29b5343b628622e63e0b9b4fc3987dd691d5f3c657233186b3271878d5e0aa0b4d264b06"
    # Fallback to the latest release image.
    # Hint: run `limactl prune` to invalidate the cache
    - location: "https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-genericcloud-amd64.qcow2"
      arch: "x86_64"
    - location: "https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-genericcloud-arm64.qcow2"
      arch: "aarch64"

    mounts:
    - location: "~"
    - location: "/tmp/lima"
      writable: true
    containerd:
      system: false
      user: false
    provision:
    - mode: system
      script: |
        #!/bin/bash
        wget -P /tmp https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest_all.deb
        sudo dpkg -i /tmp/cvmfs-release-latest_all.deb
        rm -f /tmp/cvmfs-release-latest_all.deb
        sudo apt-get update
        sudo apt-get install -y cvmfs
        if [ ! -f /etc/cvmfs/default.local ]; then
            sudo echo "CVMFS_HTTP_PROXY=DIRECT" >> /etc/cvmfs/default.local
            sudo echo "CVMFS_QUOTA_LIMIT=10000" >> /etc/cvmfs/default.local
        fi
        sudo cvmfs_config setup
    probes:
    - script: |
        #!/bin/bash
        set -eux -o pipefail
        if ! timeout 30s bash -c "until ls /cvmfs/software.eessi.io >/dev/null 2>&1; do sleep 3; done"; then
          echo >&2 "EESSI repository is not available yet"
          exit 1
        fi
      hint: See "/var/log/cloud-init-output.log" in the guest
    ```
=== "Install a virtual machine with an Ubuntu image"
    ``` { .bash .copy }
    # A template to use the EESSI software stack (see https://eessi.io) on macOS
    # $ limactl start ./eessi.yaml
    # $ limactl shell eessi

    images:
    # Try to use release-yyyyMMdd image if available. Note that release-yyyyMMdd will be removed after several months.
    - location: "https://cloud-images.ubuntu.com/releases/22.04/release-20240514/ubuntu-22.04-server-cloudimg-amd64.img"
      arch: "x86_64"
      digest: "sha256:1718f177dde4c461148ab7dcbdcf2f410c1f5daa694567f6a8bbb239d864b525"
    - location: "https://cloud-images.ubuntu.com/releases/22.04/release-20240514/ubuntu-22.04-server-cloudimg-arm64.img"
      arch: "aarch64"
      digest: "sha256:f6bf7305207a2adb9a2e2f701dc71f5747e5ba88f7b67cdb44b3f5fa6eea94a3"
    # Fallback to the latest release image.
    # Hint: run `limactl prune` to invalidate the cache
    - location: "https://cloud-images.ubuntu.com/releases/22.04/release/ubuntu-22.04-server-cloudimg-amd64.img"
      arch: "x86_64"
    - location: "https://cloud-images.ubuntu.com/releases/22.04/release/ubuntu-22.04-server-cloudimg-arm64.img"
      arch: "aarch64"

    mounts:
    - location: "~"
    - location: "/tmp/lima"
      writable: true
    containerd:
      system: false
      user: false
    provision:
    - mode: system
      script: |
        #!/bin/bash
        wget -P /tmp https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest_all.deb
        sudo dpkg -i /tmp/cvmfs-release-latest_all.deb
        rm -f /tmp/cvmfs-release-latest_all.deb
        sudo apt-get update
        sudo apt-get install -y cvmfs
        if [ ! -f /etc/cvmfs/default.local ]; then
            sudo echo "CVMFS_HTTP_PROXY=DIRECT" >> /etc/cvmfs/default.local
            sudo echo "CVMFS_QUOTA_LIMIT=10000" >> /etc/cvmfs/default.local
        fi
        sudo cvmfs_config setup
    probes:
    - script: |
        #!/bin/bash
        set -eux -o pipefail
        if ! timeout 30s bash -c "until ls /cvmfs/software.eessi.io >/dev/null 2>&1; do sleep 3; done"; then
          echo >&2 "EESSI repository is not available yet"
          exit 1
        fi
       hint: See "/var/log/cloud-init-output.log" in the guest
    ```

### Create the virtual machine with the `eessi.yaml` file:

``` { .bash .copy }
limactl create --name eessi ./eessi.yaml
```

### Start and enter the virtual machine

``` { .bash .copy }
limactl start eessi
limactl shell eessi
```

EESSI should now be available in the virtual machine

```
user@machine:/Users/user$ source /cvmfs/software.eessi.io/versions/2023.06/init/bash
  Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
  archdetect says x86_64/intel/haswell
  Using x86_64/intel/haswell as software subdirectory.
  Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/.lmod/lmodrc.lua
  Found Lmod SitePackage.lua file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/.lmod/SitePackage.lua
  Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/modules/all as the directory to be added to MODULEPATH.
  Using /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/intel/haswell/modules/all as the site extension directory to be added to MODULEPATH.
  Initializing Lmod...
  Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/modules/all to $MODULEPATH...
  EPrepending site path /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/intel/haswell/modules/all to $MODULEPATH...
  Environment set up to use EESSI (2023.06), have fun!
```

### Cleanup virtual machine

``` { .bash .copy }
limactl stop eessi
limactl delete eessi
limactl prune
``` 

### Advanced: Set resources for new virtual machine

``` { .bash .copy }
# Set resources
RATIO_RAM=0.5
RAM=$(numfmt --to=none --to-unit=1073741824 --format=%.0f  $(echo $(sysctl hw.memsize_usable | awk '{print $2}' ) "*$RATIO_RAM" | bc -l))
CPUS=$(sysctl hw.physicalcpu | awk '{print $2}')
# Create VM
limactl create --cpus $CPUS --memory $RAM --name eessi ./eessi.yaml
limactl list
```
