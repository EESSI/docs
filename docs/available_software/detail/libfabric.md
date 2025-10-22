---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Libfabric is a core component of OFI. It is the library that defines
    and exportsthe user-space API of OFI, and is typically the only software that
    applicationsdeal with directly. It works in conjunction with provider libraries,
    which areoften integrated directly into libfabric.
  license: Not confirmed
  name: libfabric
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
  softwareVersion: '[''libfabric/1.19.0-GCCcore-13.2.0'']'
  url: https://ofiwg.github.io/libfabric/
---

libfabric
=========


Libfabric is a core component of OFI. It is the library that defines and exportsthe user-space API of OFI, and is typically the only software that applicationsdeal with directly. It works in conjunction with provider libraries, which areoften integrated directly into libfabric.

https://ofiwg.github.io/libfabric/
# Available modules


The overview below shows which libfabric installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using libfabric, load one of these modules using a `module load` command like:

```shell
module load libfabric/1.19.0-GCCcore-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 12:11:37 CEST)*

| |scv64/generic|
| :---: | :---: |
|libfabric/1.19.0-GCCcore-13.2.0|x|
