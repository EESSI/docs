---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Program Database Toolkit (PDT) is a framework for analyzing source\
    \ code\n written in several programming languages and for making rich program\n\
    \ knowledge accessible to developers of static and dynamic analysis tools.\n PDT\
    \ implements a standard program representation, the program database\n (PDB),\
    \ that can be accessed in a uniform way through a class library\n supporting common\
    \ PDB operations.\n"
  license: Not confirmed
  name: PDT
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
  softwareVersion: '[''3.25.2'']'
  url: https://www.cs.uoregon.edu/research/pdt/
---
# PDT



 Program Database Toolkit (PDT) is a framework for analyzing source code
 written in several programming languages and for making rich program
 knowledge accessible to developers of static and dynamic analysis tools.
 PDT implements a standard program representation, the program database
 (PDB), that can be accessed in a uniform way through a class library
 supporting common PDB operations.


<small>homepage: </small><span class="software-link">[https://www.cs.uoregon.edu/research/pdt/](https://www.cs.uoregon.edu/research/pdt/)</span>

## Available installations


|PDT version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.25.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`PDT/3.25.2-GCCcore-13.2.0`|