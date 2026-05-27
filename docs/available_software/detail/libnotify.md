---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'libnotify is a library for sending desktop notifications to a notification
    daemon, as defined in the

    org.freedesktop.Notifications Desktop Specification. These notifications can be
    used to inform the user about an event

    or display some form of information without getting in the user''s way.'
  license: Not confirmed
  name: libnotify
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
  softwareVersion: '[''0.8.7'']'
  url: https://gitlab.gnome.org/GNOME/libnotify
---
# libnotify


libnotify is a library for sending desktop notifications to a notification daemon, as defined in the
org.freedesktop.Notifications Desktop Specification. These notifications can be used to inform the user about an event
or display some form of information without getting in the user's way.

<small>homepage: </small><span class="software-link">[https://gitlab.gnome.org/GNOME/libnotify](https://gitlab.gnome.org/GNOME/libnotify)</span>

## Available installations


|libnotify version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.8.7|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libnotify/0.8.7-GCCcore-14.3.0`|