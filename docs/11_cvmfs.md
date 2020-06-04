CernVM File System (CernVM-FS)
==============================

* File system used to distribute software, originally used for High Energy Physics (HEP) software from CERN
* https://cernvm.cern.ch/portal/filesystem
* Distribution layer
  * Redundant
  * Multiple cache layers (Stratum-0, Stratum-1, local squid)
  * Atomic deployment
  * Transparent pull model
* Deploys once => available everywhere
* Carries whatever files we put on it
* Clients mount file system read-only via a FUSE (File System in Userspace) module
