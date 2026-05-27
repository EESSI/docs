---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Unified Form Language (UFL) is a domain-specific language for defining
    variational forms
  license: Not confirmed
  name: FEniCS-UFL
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
  softwareVersion: '[''2024.2.0'']'
  url: https://github.com/FEniCS/ufl
---
# FEniCS-UFL


The Unified Form Language (UFL) is a domain-specific language for defining variational forms

<small>homepage: </small><span class="software-link">[https://github.com/FEniCS/ufl](https://github.com/FEniCS/ufl)</span>

## Available installations


|FEniCS-UFL version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2024.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`FEniCS-UFL/2024.2.0-gfbf-2023b`|