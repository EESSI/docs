---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\nWayland is a project to define a protocol for a compositor to talk\
    \ to\n its clients as well as a library implementation of the protocol.  The\n\
    \ compositor can be a standalone display server running on Linux kernel\n modesetting\
    \ and evdev input devices, an X application, or a wayland\n client itself.  The\
    \ clients can be traditional applications, X servers\n (rootless or fullscreen)\
    \ or other display servers.\n"
  license: Not confirmed
  name: Wayland
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
  softwareVersion: '[''1.24.0'', ''1.23.92'', ''1.23.0'', ''1.22.0'']'
  url: https://wayland.freedesktop.org/
---
# Wayland



Wayland is a project to define a protocol for a compositor to talk to
 its clients as well as a library implementation of the protocol.  The
 compositor can be a standalone display server running on Linux kernel
 modesetting and evdev input devices, an X application, or a wayland
 client itself.  The clients can be traditional applications, X servers
 (rootless or fullscreen) or other display servers.


<small>homepage: </small><span class="software-link">[https://wayland.freedesktop.org/](https://wayland.freedesktop.org/)</span>

## Available installations


|Wayland version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.22.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Wayland/1.22.0-GCCcore-12.3.0`|
|1.22.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Wayland/1.22.0-GCCcore-13.2.0`|
|1.23.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Wayland/1.23.0-GCCcore-13.3.0`|
|1.23.92|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Wayland/1.23.92-GCCcore-14.2.0`|
|1.24.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Wayland/1.24.0-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in Wayland installations


### wayland


|`wayland` version|Wayland modules that include it|
| --- | --- |
|1.22.0|`Wayland/1.22.0-GCCcore-12.3.0`<br/>`Wayland/1.22.0-GCCcore-13.2.0`|
|1.23.0|`Wayland/1.23.0-GCCcore-13.3.0`|
|1.23.92|`Wayland/1.23.92-GCCcore-14.2.0`|
|1.24.0|`Wayland/1.24.0-GCCcore-14.3.0`|

### wayland-protocols


|`wayland-protocols` version|Wayland modules that include it|
| --- | --- |
|1.32|`Wayland/1.22.0-GCCcore-12.3.0`<br/>`Wayland/1.22.0-GCCcore-13.2.0`|
|1.36|`Wayland/1.23.0-GCCcore-13.3.0`|
|1.44|`Wayland/1.23.92-GCCcore-14.2.0`|
|1.45|`Wayland/1.24.0-GCCcore-14.3.0`|

### wayland-utils


|`wayland-utils` version|Wayland modules that include it|
| --- | --- |
|1.2.0|`Wayland/1.23.0-GCCcore-13.3.0`<br/>`Wayland/1.23.92-GCCcore-14.2.0`<br/>`Wayland/1.24.0-GCCcore-14.3.0`|