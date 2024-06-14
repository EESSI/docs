# Installing EESSI with Windows Subsystem for Linux

## Basic commands with WSL

### List the available linux distributions for installation

```
C:/users/user>wsl --list --online
The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.

NAME                                   FRIENDLY NAME
Ubuntu                                 Ubuntu
Debian                                 Debian GNU/Linux
kali-linux                             Kali Linux Rolling
Ubuntu-18.04                           Ubuntu 18.04 LTS
Ubuntu-20.04                           Ubuntu 20.04 LTS
Ubuntu-22.04                           Ubuntu 22.04 LTS
Ubuntu-24.04                           Ubuntu 24.04 LTS
OracleLinux_7_9                        Oracle Linux 7.9
OracleLinux_8_7                        Oracle Linux 8.7
OracleLinux_9_1                        Oracle Linux 9.1
openSUSE-Leap-15.5                     openSUSE Leap 15.5
SUSE-Linux-Enterprise-Server-15-SP4    SUSE Linux Enterprise Server 15 SP4
SUSE-Linux-Enterprise-15-SP5           SUSE Linux Enterprise 15 SP5
openSUSE-Tumbleweed                    openSUSE Tumbleweed
```

### List the installed machines

```
C:/users/user>wsl --list --verbose
  NAME      STATE           VERSION
* Debian    Stopped         2
```

### Reconnecting to a Virtual machine with wsl

```
C:/users/user>wsl --distribution Debian
user@id:~$
```

For more documentation on using WSL you can check out the following pages:

* [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

* [Basic commands for WSL](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)

## Installing a linux distribution with WSL

```
C:/users/user>wsl --install --distribution Debian
Debian GNU/Linux is already installed.
Launching Debian GNU/Linux...
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: user
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
```

## Installing EESSI in the virtual machine

``` { .bash .copy }
# Installation commands for Debian-based distros like Ubuntu, ...

# install CernVM-FS
sudo apt-get install lsb-release
sudo apt-get install wget
wget https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-release-latest_all.deb
sudo dpkg -i cvmfs-release-latest_all.deb
rm -f cvmfs-release-latest_all.deb
sudo apt-get update
sudo apt-get install -y cvmfs

# install EESSI configuration for CernVM-FS
wget https://github.com/EESSI/filesystem-layer/releases/download/latest/cvmfs-config-eessi_latest_all.deb
sudo dpkg -i cvmfs-config-eessi_latest_all.deb

# create client configuration file for CernVM-FS (no squid proxy, 10GB local CernVM-FS client cache)
sudo bash -c "echo 'CVMFS_CLIENT_PROFILE="single"' > /etc/cvmfs/default.local"
sudo bash -c "echo 'CVMFS_QUOTA_LIMIT=10000' >> /etc/cvmfs/default.local"

# make sure that EESSI CernVM-FS repository is accessible
sudo cvmfs_config setup
```

## Start cernVM-FS in Windows Subsystem for Linux

When the virtual machine is restarted CernVM-FS needs to be remounted with following command.

``` { .bash .copy }
# start CernVM-FS on WSL
sudo cvmfs_config wsl2_start
```

If you do not wish to do this you can set up the automounter. Examples are available [here](https://klust.github.io/windows-client-HPC/4_Cluster_Stack/4_01_EESSI/#example-setup-on-fedora-remix-in-wsl2).

EESSI should now be available in the virtual machine

```
user@id:~$ source /cvmfs/software.eessi.io/versions/2023.06/init/bash
  Found EESSI repo @ /cvmfs/software.eessi.io/versions/2023.06!
  archdetect says x86_64/intel/haswell
  Using x86_64/intel/haswell as software subdirectory.
  Found Lmod configuration file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/.lmod/lmodrc.lua
  Found Lmod SitePackage.lua file at /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/.lmod/SitePackage.lua
  Using /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/modules/all as the directory to be added to MODULEPATH.
  Using /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/intel/haswell/modules/all as the site extension directory to be added to MODULEPATH.
  Initializing Lmod...
  Prepending /cvmfs/software.eessi.io/versions/2023.06/software/linux/x86_64/intel/haswell/modules/all to $MODULEPATH...
  Prepending site path /cvmfs/software.eessi.io/host_injections/2023.06/software/linux/x86_64/intel/haswell/modules/all to $MODULEPATH...
  Environment set up to use EESSI (2023.06), have fun!
```

## Cleanup of the virtual machine

```
C:/users/user>wsl --terminate Debian
C:/users/user>wsl --unregister Debian
```

