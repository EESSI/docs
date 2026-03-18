---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Wraps the wxWidgets C++ toolkit and provides access to the user interface
    portions of the wxWidgets

    API, enabling Python applications to have a native GUI on Windows, Macs or Unix
    systems, with a native look and feel

    and requiring very little (if any) platform specific code.'
  license: Not confirmed
  name: wxPython
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
  softwareVersion: '[''4.2.1'']'
  url: https://www.wxpython.org/
---
# wxPython


Wraps the wxWidgets C++ toolkit and provides access to the user interface portions of the wxWidgets
API, enabling Python applications to have a native GUI on Windows, Macs or Unix systems, with a native look and feel
and requiring very little (if any) platform specific code.

<small>homepage: </small><span class="software-link">[https://www.wxpython.org/](https://www.wxpython.org/)</span>

## Available installations


|wxPython version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.2.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`wxPython/4.2.1-foss-2023a`|