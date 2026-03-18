---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI\
    \ functionality\n to the Linux operating system."
  license: Not confirmed
  name: alsa-lib
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
  softwareVersion: '[''1.2.14'']'
  url: https://www.alsa-project.org
---
# alsa-lib


The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI functionality
 to the Linux operating system.

<small>homepage: </small><span class="software-link">[https://www.alsa-project.org](https://www.alsa-project.org)</span>

## Available installations


|alsa-lib version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.2.14|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`alsa-lib/1.2.14-GCCcore-14.3.0`|