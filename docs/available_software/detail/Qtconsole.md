---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'A rich Qt-based console for working with Jupyter kernels, supporting
    rich media

    output, session export, and more.

    The Qtconsole is a very lightweight application that largely feels like a

    terminal, but provides a number of enhancements only possible in a GUI, such as

    inline figures, proper multiline editing with syntax highlighting, graphical

    calltips, and more.'
  license: Not confirmed
  name: Qtconsole
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
  softwareVersion: '[''5.7.0'']'
  url: https://jupyter.org/
---
# Qtconsole


A rich Qt-based console for working with Jupyter kernels, supporting rich media
output, session export, and more.
The Qtconsole is a very lightweight application that largely feels like a
terminal, but provides a number of enhancements only possible in a GUI, such as
inline figures, proper multiline editing with syntax highlighting, graphical
calltips, and more.

<small>homepage: </small><span class="software-link">[https://jupyter.org/](https://jupyter.org/)</span>

## Available installations


|Qtconsole version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.7.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Qtconsole/5.7.0-GCCcore-14.3.0`|