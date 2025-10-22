---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The greenlet package is a spin-off of Stackless, a version of CPython
    thatsupports micro-threads called "tasklets". Tasklets run pseudo-concurrently
    (typically in a singleor a few OS-level threads) and are synchronized with data
    exchanges on "channels".A "greenlet", on the other hand, is a still more primitive
    notion of micro-thread with no implicitscheduling; coroutines, in other words.
    This is useful when you want to control exactly when your code runs.
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
  softwareVersion: '[''Greenlet/3.0.3-GCCcore-13.2.0'']'
  url: https://github.com/python-greenlet/greenlet
---

Greenlet
========


The greenlet package is a spin-off of Stackless, a version of CPython thatsupports micro-threads called "tasklets". Tasklets run pseudo-concurrently (typically in a singleor a few OS-level threads) and are synchronized with data exchanges on "channels".A "greenlet", on the other hand, is a still more primitive notion of micro-thread with no implicitscheduling; coroutines, in other words. This is useful when you want to control exactly when your code runs.

https://github.com/python-greenlet/greenlet
# Available modules


The overview below shows which Greenlet installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Greenlet, load one of these modules using a `module load` command like:

```shell
module load Greenlet/3.0.3-GCCcore-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 12:19:02 CEST)*

| |scv64/generic|
| :---: | :---: |
|Greenlet/3.0.3-GCCcore-13.2.0|x|
