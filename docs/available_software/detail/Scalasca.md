---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n Scalasca is a software tool that supports the performance optimization\
    \ of\n parallel programs by measuring and analyzing their runtime behavior. The\n\
    \ analysis identifies potential performance bottlenecks -- in particular\n those\
    \ concerning communication and synchronization -- and offers guidance\n in exploring\
    \ their causes.\n"
  license: Not confirmed
  name: Scalasca
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
  softwareVersion: '[''2.6.2'']'
  url: https://www.scalasca.org/
---
# Scalasca



 Scalasca is a software tool that supports the performance optimization of
 parallel programs by measuring and analyzing their runtime behavior. The
 analysis identifies potential performance bottlenecks -- in particular
 those concerning communication and synchronization -- and offers guidance
 in exploring their causes.


<small>homepage: </small><span class="software-link">[https://www.scalasca.org/](https://www.scalasca.org/)</span>

## Available installations


|Scalasca version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.6.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Scalasca/2.6.2-gompi-2025b`|
|2.6.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Scalasca/2.6.2-lompi-2025b`|