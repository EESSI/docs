---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'The greenlet package is a spin-off of Stackless, a version of CPython
    that

    supports micro-threads called "tasklets". Tasklets run pseudo-concurrently (typically
    in a single

    or a few OS-level threads) and are synchronized with data exchanges on "channels".

    A "greenlet", on the other hand, is a still more primitive notion of micro-thread
    with no implicit

    scheduling; coroutines, in other words. This is useful when you want to control
    exactly when your code runs.

    '
  license: Not confirmed
  name: Greenlet
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
  softwareVersion: '[''3.1.1'', ''3.0.3'']'
  url: https://github.com/python-greenlet/greenlet
---
# Greenlet


The greenlet package is a spin-off of Stackless, a version of CPython that
supports micro-threads called "tasklets". Tasklets run pseudo-concurrently (typically in a single
or a few OS-level threads) and are synchronized with data exchanges on "channels".
A "greenlet", on the other hand, is a still more primitive notion of micro-thread with no implicit
scheduling; coroutines, in other words. This is useful when you want to control exactly when your code runs.


<small>homepage: </small><span class="software-link">[https://github.com/python-greenlet/greenlet](https://github.com/python-greenlet/greenlet)</span>

## Available installations


|Greenlet version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Greenlet/3.0.3-GCCcore-13.2.0`|
|3.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Greenlet/3.1.1-GCCcore-13.3.0`|