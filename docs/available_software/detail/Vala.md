---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Vala is a programming language using modern high level abstractions
    without imposing additional runtime

    requirements and without using a different ABI compared to applications and libraries
    written in C.'
  license: Not confirmed
  name: Vala
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
  softwareVersion: '[''0.56.18'']'
  url: https://wiki.gnome.org/Projects/Vala
---
# Vala


Vala is a programming language using modern high level abstractions without imposing additional runtime
requirements and without using a different ABI compared to applications and libraries written in C.

<small>homepage: </small><span class="software-link">[https://wiki.gnome.org/Projects/Vala](https://wiki.gnome.org/Projects/Vala)</span>

## Available installations


|Vala version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.56.18|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Vala/0.56.18-GCCcore-14.3.0`|