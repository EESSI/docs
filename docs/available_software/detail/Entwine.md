---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Entwine is a data organization library for massive

    point clouds, designed to conquer datasets of hundreds of billions of

    points as well as desktop-scale point clouds. Entwine can index

    anything that is PDAL-readable, and can read/write to a variety of

    sources like S3 or Dropbox. Builds are completely lossless, so no

    points will be discarded even for terabyte-scale datasets.'
  license: Not confirmed
  name: Entwine
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
  softwareVersion: '[''3.2.1'']'
  url: https://entwine.io
---
# Entwine


Entwine is a data organization library for massive
point clouds, designed to conquer datasets of hundreds of billions of
points as well as desktop-scale point clouds. Entwine can index
anything that is PDAL-readable, and can read/write to a variety of
sources like S3 or Dropbox. Builds are completely lossless, so no
points will be discarded even for terabyte-scale datasets.

<small>homepage: </small><span class="software-link">[https://entwine.io](https://entwine.io)</span>

## Available installations


|Entwine version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.2.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Entwine/3.2.1-foss-2025b`|