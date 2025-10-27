---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Provides a way to load and enumerate PKCS#11 modules. Provides a standard
    configuration setup for installing PKCS#11 modules in such a way that they're
    discoverable. Also solves problems with coordinating the use of PKCS#11 by different
    components or libraries living in the same process.
  license: Not confirmed
  name: p11-kit
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
  softwareVersion: '[''p11-kit/0.25.3-GCCcore-12.3.0'']'
  url: https://p11-glue.freedesktop.org/p11-kit.html
---

p11-kit
=======


Provides a way to load and enumerate PKCS#11 modules. Provides a standard configuration setup for installing PKCS#11 modules in such a way that they're discoverable. Also solves problems with coordinating the use of PKCS#11 by different components or libraries living in the same process.

https://p11-glue.freedesktop.org/p11-kit.html
# Available modules


The overview below shows which p11-kit installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using p11-kit, load one of these modules using a `module load` command like:

```shell
module load p11-kit/0.25.3-GCCcore-12.3.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|p11-kit/0.25.3-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
