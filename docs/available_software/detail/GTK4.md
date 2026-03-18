---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "GTK+ is the primary library used to construct user interfaces in GNOME.\
    \ It\n provides all the user interface controls, or widgets, used in a common\n\
    \ graphical application. Its object-oriented API allows you to construct\n user\
    \ interfaces without dealing with the low-level details of drawing and\n device\
    \ interaction.\n"
  license: Not confirmed
  name: GTK4
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
  softwareVersion: '[''4.20.2'', ''4.13.1'']'
  url: https://docs.gtk.org/gtk4/
---
# GTK4


GTK+ is the primary library used to construct user interfaces in GNOME. It
 provides all the user interface controls, or widgets, used in a common
 graphical application. Its object-oriented API allows you to construct
 user interfaces without dealing with the low-level details of drawing and
 device interaction.


<small>homepage: </small><span class="software-link">[https://docs.gtk.org/gtk4/](https://docs.gtk.org/gtk4/)</span>

## Available installations


|GTK4 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.13.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`GTK4/4.13.1-GCC-12.3.0`|
|4.20.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`GTK4/4.20.2-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in GTK4 installations


### adwaita-icon-theme


|`adwaita-icon-theme` version|GTK4 modules that include it|
| --- | --- |
|45.0|`GTK4/4.13.1-GCC-12.3.0`|
|49.0|`GTK4/4.20.2-GCCcore-14.3.0`|

### GTK


|`GTK` version|GTK4 modules that include it|
| --- | --- |
|4.13.1|`GTK4/4.13.1-GCC-12.3.0`|
|4.20.2|`GTK4/4.20.2-GCCcore-14.3.0`|

### hicolor-icon-theme


|`hicolor-icon-theme` version|GTK4 modules that include it|
| --- | --- |
|0.17|`GTK4/4.13.1-GCC-12.3.0`|
|0.18|`GTK4/4.20.2-GCCcore-14.3.0`|