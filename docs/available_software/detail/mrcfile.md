---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "mrcfile is a Python implementation of the MRC2014 file format, which\
    \ is used in\nstructural biology to store image and volume data.\n\nIt allows\
    \ MRC files to be created and opened easily using a very simple API,\nwhich exposes\
    \ the file\u2019s header and data as numpy arrays. The code runs in\nPython 2\
    \ and 3 and is fully unit-tested.\n\nThis library aims to allow users and developers\
    \ to read and write standard-\ncompliant MRC files in Python as easily as possible,\
    \ and with no dependencies on\nany compiled libraries except numpy. You can use\
    \ it interactively to inspect\nfiles, correct headers and so on, or in scripts\
    \ and larger software packages to\nprovide basic MRC file I/O functions. "
  license: Not confirmed
  name: mrcfile
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
  softwareVersion: '[''1.5.4'']'
  url: https://github.com/ccpem/mrcfile
---
# mrcfile


mrcfile is a Python implementation of the MRC2014 file format, which is used in
structural biology to store image and volume data.

It allows MRC files to be created and opened easily using a very simple API,
which exposes the file’s header and data as numpy arrays. The code runs in
Python 2 and 3 and is fully unit-tested.

This library aims to allow users and developers to read and write standard-
compliant MRC files in Python as easily as possible, and with no dependencies on
any compiled libraries except numpy. You can use it interactively to inspect
files, correct headers and so on, or in scripts and larger software packages to
provide basic MRC file I/O functions. 

<small>homepage: </small><span class="software-link">[https://github.com/ccpem/mrcfile](https://github.com/ccpem/mrcfile)</span>

## Available installations


|mrcfile version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.5.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`mrcfile/1.5.4-gfbf-2025a`|