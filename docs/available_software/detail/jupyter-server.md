---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The Jupyter Server provides the backend (i.e. the core services, APIs,
    and RESTendpoints) for Jupyter web applications like Jupyter notebook, JupyterLab,
    andVoila.
  license: Not confirmed
  name: jupyter-server
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
  softwareVersion: '[''jupyter-server/2.7.2-GCCcore-12.3.0'']'
  url: https://jupyter.org/
---

jupyter-server
==============


The Jupyter Server provides the backend (i.e. the core services, APIs, and RESTendpoints) for Jupyter web applications like Jupyter notebook, JupyterLab, andVoila.

https://jupyter.org/
# Available modules


The overview below shows which jupyter-server installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using jupyter-server, load one of these modules using a `module load` command like:

```shell
module load jupyter-server/2.7.2-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|jupyter-server/2.7.2-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|


### jupyter-server/2.7.2-GCCcore-12.3.0

This is a list of extensions included in the module:

anyio-3.7.1, argon2-cffi-bindings-21.2.0, argon2_cffi-23.1.0, arrow-1.2.3, bleach-6.0.0, comm-0.1.4, debugpy-1.6.7.post1, defusedxml-0.7.1, deprecation-2.1.0, fastjsonschema-2.18.0, hatch_jupyter_builder-0.8.3, hatch_nodejs_version-0.3.1, ipykernel-6.25.1, ipython_genutils-0.2.0, ipywidgets-8.1.0, jsonschema-4.18.0, jsonschema_specifications-2023.7.1, jupyter_client-8.3.0, jupyter_core-5.3.1, jupyter_events-0.7.0, jupyter_packaging-0.12.3, jupyter_server-2.7.2, jupyter_server_terminals-0.4.4, jupyterlab_pygments-0.2.2, jupyterlab_widgets-3.0.8, mistune-3.0.1, nbclient-0.8.0, nbconvert-7.7.4, nbformat-5.9.2, nest_asyncio-1.5.7, notebook_shim-0.2.3, overrides-7.4.0, pandocfilters-1.5.0, prometheus_client-0.17.1, python-json-logger-2.0.7, referencing-0.30.2, rfc3339_validator-0.1.4, rfc3986_validator-0.1.1, rpds_py-0.9.2, Send2Trash-1.8.2, sniffio-1.3.0, terminado-0.17.1, tinycss2-1.2.1, websocket-client-1.6.1, widgetsnbextension-4.0.8