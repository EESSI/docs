---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Prodigal (Prokaryotic Dynamic Programming Genefinding Algorithm)\n\
    \   is a microbial (bacterial and archaeal) gene finding program developed\n \
    \  at Oak Ridge National Laboratory and the University of Tennessee."
  license: Not confirmed
  name: prodigal
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
  softwareVersion: '[''2.6.3'']'
  url: https://github.com/hyattpd/Prodigal/
---
# prodigal


Prodigal (Prokaryotic Dynamic Programming Genefinding Algorithm)
   is a microbial (bacterial and archaeal) gene finding program developed
   at Oak Ridge National Laboratory and the University of Tennessee.

<small>homepage: </small><span class="software-link">[https://github.com/hyattpd/Prodigal/](https://github.com/hyattpd/Prodigal/)</span>

## Available installations


|prodigal version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.6.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`prodigal/2.6.3-GCCcore-14.3.0`|