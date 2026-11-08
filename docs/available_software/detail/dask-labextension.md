---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This package provides a JupyterLab extension to manage Dask clusters,
    as well

    as embed Dask''s dashboard plots directly into JupyterLab panes.'
  license: Not confirmed
  name: dask-labextension
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
  softwareVersion: '[''7.0.0'']'
  url: https://github.com/dask/dask-labextension
---
# dask-labextension


This package provides a JupyterLab extension to manage Dask clusters, as well
as embed Dask's dashboard plots directly into JupyterLab panes.

<small>homepage: </small><span class="software-link">[https://github.com/dask/dask-labextension](https://github.com/dask/dask-labextension)</span>

## Available installations


|dask-labextension version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|7.0.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`dask-labextension/7.0.0-gfbf-2026.1`|

## Extensions

Overview of extensions included in dask-labextension installations


### dask_labextension


|`dask_labextension` version|dask-labextension modules that include it|
| --- | --- |
|7.0.0|`dask-labextension/7.0.0-gfbf-2026.1`|