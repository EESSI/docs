---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Jupyter Widgets are interactive browser controls for Jupyter notebooks
  license: Not confirmed
  name: ipywidgets
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
  softwareVersion: '[''8.1.2'']'
  url: https://jupyter.org/
---
# ipywidgets


Jupyter Widgets are interactive browser controls for Jupyter notebooks

<small>homepage: </small><span class="software-link">[https://jupyter.org/](https://jupyter.org/)</span>

## Available installations


|ipywidgets version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|8.1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`ipywidgets/8.1.2-GCCcore-13.2.0`|

## Extensions

Overview of extensions included in ipywidgets installations


### comm


|`comm` version|ipywidgets modules that include it|
| --- | --- |
|0.2.2|`ipywidgets/8.1.2-GCCcore-13.2.0`|

### ipywidgets


|`ipywidgets` version|ipywidgets modules that include it|
| --- | --- |
|8.1.2|`ipywidgets/8.1.2-GCCcore-13.2.0`|

### jupyterlab_widgets


|`jupyterlab_widgets` version|ipywidgets modules that include it|
| --- | --- |
|3.0.10|`ipywidgets/8.1.2-GCCcore-13.2.0`|

### widgetsnbextension


|`widgetsnbextension` version|ipywidgets modules that include it|
| --- | --- |
|4.0.10|`ipywidgets/8.1.2-GCCcore-13.2.0`|