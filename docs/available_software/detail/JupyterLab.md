---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: JupyterLab is the next-generation user interface for Project Jupyter
    offering all the familiar building blocks of the classic Jupyter Notebook (notebook,
    terminal, text editor, file browser, rich outputs, etc.) in a flexible and powerful
    user interface. JupyterLab will eventually replace the classic Jupyter Notebook.
  license: Not confirmed
  name: JupyterLab
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
  softwareVersion: '[''JupyterLab/4.0.5-GCCcore-12.3.0'']'
  url: https://jupyter.org/
---

JupyterLab
==========


JupyterLab is the next-generation user interface for Project Jupyter offering all the familiar building blocks of the classic Jupyter Notebook (notebook, terminal, text editor, file browser, rich outputs, etc.) in a flexible and powerful user interface. JupyterLab will eventually replace the classic Jupyter Notebook.

https://jupyter.org/
# Available modules


The overview below shows which JupyterLab installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using JupyterLab, load one of these modules using a `module load` command like:

```shell
module load JupyterLab/4.0.5-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|JupyterLab/4.0.5-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|


### JupyterLab/4.0.5-GCCcore-12.3.0

This is a list of extensions included in the module:

async-lru-2.0.4, json5-0.9.14, jupyter-lsp-2.2.0, jupyterlab-4.0.5, jupyterlab_server-2.24.0