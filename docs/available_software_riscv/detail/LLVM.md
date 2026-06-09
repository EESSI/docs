---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    The LLVM Core libraries provide a modern source- and target-independent

    optimizer, along with code generation support for many popular CPUs

    (as well as some less common ones!) These libraries are built around a well

    specified code representation known as the LLVM intermediate representation

    ("LLVM IR"). The LLVM Core libraries are well documented, and it is

    particularly easy to invent your own language (or port an existing compiler)

    to use LLVM as an optimizer and code generator.

    '
  license: Not confirmed
  name: LLVM
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
  softwareVersion: '[''20.1.8'']'
  url: https://llvm.org/
---
# LLVM



The LLVM Core libraries provide a modern source- and target-independent
optimizer, along with code generation support for many popular CPUs
(as well as some less common ones!) These libraries are built around a well
specified code representation known as the LLVM intermediate representation
("LLVM IR"). The LLVM Core libraries are well documented, and it is
particularly easy to invent your own language (or port an existing compiler)
to use LLVM as an optimizer and code generator.


<small>homepage: </small><span class="software-link">[https://llvm.org/](https://llvm.org/)</span>

## Available installations


|LLVM version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|20.1.8|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`LLVM/20.1.8-GCCcore-14.3.0`|