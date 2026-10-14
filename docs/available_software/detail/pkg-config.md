---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n pkg-config is a helper tool used when compiling applications and\
    \ libraries.\n It helps you insert the correct compiler options on the command\
    \ line so an\n application can use gcc -o test test.c `pkg-config --libs --cflags\
    \ glib-2.0`\n for instance, rather than hard-coding values on where to find glib\
    \ (or other\n libraries).\n"
  license: Not confirmed
  name: pkg-config
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
  softwareVersion: '[''0.29.2'']'
  url: https://www.freedesktop.org/wiki/Software/pkg-config/
---
# pkg-config



 pkg-config is a helper tool used when compiling applications and libraries.
 It helps you insert the correct compiler options on the command line so an
 application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
 for instance, rather than hard-coding values on where to find glib (or other
 libraries).


<small>homepage: </small><span class="software-link">[https://www.freedesktop.org/wiki/Software/pkg-config/](https://www.freedesktop.org/wiki/Software/pkg-config/)</span>

## Available installations


|pkg-config version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.29.2|`generic`: <br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`pkg-config/0.29.2-GCCcore-12.3.0`|