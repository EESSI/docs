---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Jupyter Server Proxy lets you run arbitrary external processes

    (such as RStudio, Shiny Server, Syncthing, PostgreSQL, Code Server, etc)

    alongside your notebook server and provide authenticated web access to them

    using a path like /rstudio next to others like /lab. Alongside the python

    package that provides the main functionality, the JupyterLab extension

    (@jupyterlab/server-proxy) provides buttons in the JupyterLab launcher window

    to get to RStudio for example.'
  license: Not confirmed
  name: jupyter-server-proxy
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
  softwareVersion: '[''4.1.2'']'
  url: https://github.com/jupyterhub/jupyter-server-proxy
---
# jupyter-server-proxy


Jupyter Server Proxy lets you run arbitrary external processes
(such as RStudio, Shiny Server, Syncthing, PostgreSQL, Code Server, etc)
alongside your notebook server and provide authenticated web access to them
using a path like /rstudio next to others like /lab. Alongside the python
package that provides the main functionality, the JupyterLab extension
(@jupyterlab/server-proxy) provides buttons in the JupyterLab launcher window
to get to RStudio for example.

<small>homepage: </small><span class="software-link">[https://github.com/jupyterhub/jupyter-server-proxy](https://github.com/jupyterhub/jupyter-server-proxy)</span>

## Available installations


|jupyter-server-proxy version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`jupyter-server-proxy/4.1.2-GCCcore-13.2.0`|

## Extensions

Overview of extensions included in jupyter-server-proxy installations


### jupyter_server_proxy


|`jupyter_server_proxy` version|jupyter-server-proxy modules that include it|
| --- | --- |
|4.1.2|`jupyter-server-proxy/4.1.2-GCCcore-13.2.0`|

### simpervisor


|`simpervisor` version|jupyter-server-proxy modules that include it|
| --- | --- |
|1.0.0|`jupyter-server-proxy/4.1.2-GCCcore-13.2.0`|