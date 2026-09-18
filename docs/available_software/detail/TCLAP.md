---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'TCLAP is a small, flexible library that provides a simple interface
    for defining and accessing

    command line arguments. It was initially inspired by the user friendly CLAP library.'
  license: Not confirmed
  name: TCLAP
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
  softwareVersion: '[''1.4.0-rc2'']'
  url: http://tclap.sourceforge.net/
---
# TCLAP


TCLAP is a small, flexible library that provides a simple interface for defining and accessing
command line arguments. It was initially inspired by the user friendly CLAP library.

<small>homepage: </small><span class="software-link">[http://tclap.sourceforge.net/](http://tclap.sourceforge.net/)</span>

## Available installations


|TCLAP version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.4.0-rc2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`TCLAP/1.4.0-rc2-GCCcore-14.3.0`|