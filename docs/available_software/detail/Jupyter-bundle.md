---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    This bundle collects a range of Jupyter interfaces (Lab, Notebook and nbclassic),

    extensions (Jupyter Server Proxy, Jupyter Resource Monitor, Jupyter Lmod) and

    the JupyterHub.

    '
  license: Not confirmed
  name: Jupyter-bundle
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
  softwareVersion: '[''20251112'']'
  url: https://jupyter.org/
---
# Jupyter-bundle



This bundle collects a range of Jupyter interfaces (Lab, Notebook and nbclassic),
extensions (Jupyter Server Proxy, Jupyter Resource Monitor, Jupyter Lmod) and
the JupyterHub.


<small>homepage: </small><span class="software-link">[https://jupyter.org/](https://jupyter.org/)</span>

## Available installations


|Jupyter-bundle version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|20251112|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Jupyter-bundle/20251112-GCCcore-14.3.0`|