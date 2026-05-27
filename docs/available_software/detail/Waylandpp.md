---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Wayland is an object oriented display protocol, which

    features request and events. Requests can be seen as method calls on

    certain objects, whereas events can be seen as signals of an object.

    This makes the Wayland protocol a perfect candidate for a C++ binding.


    The goal of this library is to create such a C++ binding for Wayland

    using the most modern C++ technology currently available, providing

    an easy to use C++ API to Wayland.'
  license: Not confirmed
  name: Waylandpp
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
  softwareVersion: '[''1.0.0'']'
  url: https://github.com/NilsBrause/waylandpp
---
# Waylandpp


Wayland is an object oriented display protocol, which
features request and events. Requests can be seen as method calls on
certain objects, whereas events can be seen as signals of an object.
This makes the Wayland protocol a perfect candidate for a C++ binding.

The goal of this library is to create such a C++ binding for Wayland
using the most modern C++ technology currently available, providing
an easy to use C++ API to Wayland.

<small>homepage: </small><span class="software-link">[https://github.com/NilsBrause/waylandpp](https://github.com/NilsBrause/waylandpp)</span>

## Available installations


|Waylandpp version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Waylandpp/1.0.0-GCCcore-12.3.0`|