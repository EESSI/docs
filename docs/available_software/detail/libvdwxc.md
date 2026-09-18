---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'libvdwxc is a general library for evaluating energy and potential
    for

    exchange-correlation (XC) functionals from the vdW-DF family that can be used
    with various

    of density functional theory (DFT) codes.'
  license: Not confirmed
  name: libvdwxc
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
  softwareVersion: '[''0.5.0'']'
  url: https://libvdwxc.materialsmodeling.org/
---
# libvdwxc


libvdwxc is a general library for evaluating energy and potential for
exchange-correlation (XC) functionals from the vdW-DF family that can be used with various
of density functional theory (DFT) codes.

<small>homepage: </small><span class="software-link">[https://libvdwxc.materialsmodeling.org/](https://libvdwxc.materialsmodeling.org/)</span>

## Available installations


|libvdwxc version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.5.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libvdwxc/0.5.0-foss-2025a`|