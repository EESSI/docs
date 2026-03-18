---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The AOFlagger is a tool that can find and remove radio-frequency interference
    (RFI)

    in radio astronomical observations. It can make use of Lua scripts to make flagging
    strategies flexible,

    and the tools are applicable to a wide set of telescopes.'
  license: Not confirmed
  name: AOFlagger
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
  softwareVersion: '[''3.4.0'']'
  url: https://aoflagger.readthedocs.io/
---
# AOFlagger


The AOFlagger is a tool that can find and remove radio-frequency interference (RFI)
in radio astronomical observations. It can make use of Lua scripts to make flagging strategies flexible,
and the tools are applicable to a wide set of telescopes.

<small>homepage: </small><span class="software-link">[https://aoflagger.readthedocs.io/](https://aoflagger.readthedocs.io/)</span>

## Available installations


|AOFlagger version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.4.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`AOFlagger/3.4.0-foss-2023b`|