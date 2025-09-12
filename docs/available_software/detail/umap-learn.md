---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Uniform Manifold Approximation and Projection (UMAP) is a dimension
    reduction techniquethat can be used for visualisation similarly to t-SNE, but
    also for general non-lineardimension reduction.
  license: Not confirmed
  name: umap-learn
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
  softwareVersion: '[''umap-learn/0.5.5-foss-2023a'']'
  url: https://umap-learn.readthedocs.io/en/latest/
---

umap-learn
==========


Uniform Manifold Approximation and Projection (UMAP) is a dimension reduction techniquethat can be used for visualisation similarly to t-SNE, but also for general non-lineardimension reduction.

https://umap-learn.readthedocs.io/en/latest/
# Available modules


The overview below shows which umap-learn installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using umap-learn, load one of these modules using a `module load` command like:

```shell
module load umap-learn/0.5.5-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|umap-learn/0.5.5-foss-2023a|x|-|x|x|x|x|x|x|x|x|x|x|x|x|


### umap-learn/0.5.5-foss-2023a

This is a list of extensions included in the module:

pynndescent-0.5.11, umap-learn-0.5.5