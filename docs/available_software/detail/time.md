---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The `time' command runs another program, then displays information
    about the resources used by that program, collected by the system while the program
    was running.
  license: Not confirmed
  name: time
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
  softwareVersion: '[''time/1.9-GCCcore-12.2.0'']'
  url: https://www.gnu.org/software/time/
---

time
====


The `time' command runs another program, then displays information about the resources used by that program, collected by the system while the program was running.

https://www.gnu.org/software/time/
# Available modules


The overview below shows which time installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using time, load one of these modules using a `module load` command like:

```shell
module load time/1.9-GCCcore-12.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|time/1.9-GCCcore-12.2.0|x|x|x|x|x|x|x|x|-|x|
