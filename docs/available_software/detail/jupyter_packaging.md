---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Tools to help build and install Jupyter Python packages

    that require a pre-build step that may include JavaScript build steps.'
  license: Not confirmed
  name: jupyter_packaging
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
  softwareVersion: '[''0.12.3'']'
  url: http://jupyter.org/
---
# jupyter_packaging


Tools to help build and install Jupyter Python packages
that require a pre-build step that may include JavaScript build steps.

<small>homepage: </small><span class="software-link">[http://jupyter.org/](http://jupyter.org/)</span>

## Available installations


|jupyter_packaging version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.12.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`jupyter_packaging/0.12.3-GCCcore-13.2.0`|