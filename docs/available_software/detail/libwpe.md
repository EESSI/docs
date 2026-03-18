---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'WPE is the reference WebKit port for embedded and

    low-consumption computer devices. It has been designed from the

    ground-up with performance, small footprint, accelerated content

    rendering, and simplicity of deployment in mind, bringing the

    excellence of the WebKit engine to countless platforms and target devices.'
  license: Not confirmed
  name: libwpe
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
  softwareVersion: '[''1.16.0'']'
  url: https://webkit.org/wpe
---
# libwpe


WPE is the reference WebKit port for embedded and
low-consumption computer devices. It has been designed from the
ground-up with performance, small footprint, accelerated content
rendering, and simplicity of deployment in mind, bringing the
excellence of the WebKit engine to countless platforms and target devices.

<small>homepage: </small><span class="software-link">[https://webkit.org/wpe](https://webkit.org/wpe)</span>

## Available installations


|libwpe version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.16.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libwpe/1.16.0-GCCcore-12.3.0`|