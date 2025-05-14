---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GNU Wget is a free software package for retrieving files using HTTP,
    HTTPS and FTP, the most widely-used Internet protocols. It is a non-interactive
    commandline tool, so it may easily be called from scripts, cron jobs, terminals
    without X-Windows support, etc.
  license: Not confirmed
  name: wget
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
  softwareVersion: '[''wget/1.21.4-GCCcore-13.2.0'', ''wget/1.24.5-GCCcore-12.3.0'']'
  url: https://www.gnu.org/software/wget
---

wget
====


GNU Wget is a free software package for retrieving files using HTTP, HTTPS and FTP, the most widely-used Internet protocols. It is a non-interactive commandline tool, so it may easily be called from scripts, cron jobs, terminals without X-Windows support, etc.

https://www.gnu.org/software/wget
# Available modules


The overview below shows which wget installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using wget, load one of these modules using a `module load` command like:

```shell
module load wget/1.24.5-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|wget/1.24.5-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|wget/1.21.4-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
