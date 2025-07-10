---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'ml_dtypes is a stand-alone implementation of several NumPy dtype extensions
    usedin machine learning libraries, including:bfloat16: an alternative to the standard
    float16 formatfloat8_*: several experimental 8-bit floating point representations
    including:float8_e4m3b11fnuzfloat8_e4m3fnfloat8_e4m3fnuzfloat8_e5m2float8_e5m2fnuz'
  license: Not confirmed
  name: ml_dtypes
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
  softwareVersion: '[''ml_dtypes/0.3.2-gfbf-2023a'']'
  url: https://github.com/jax-ml/ml_dtypes
---

ml_dtypes
=========


ml_dtypes is a stand-alone implementation of several NumPy dtype extensions usedin machine learning libraries, including:bfloat16: an alternative to the standard float16 formatfloat8_*: several experimental 8-bit floating point representations including:float8_e4m3b11fnuzfloat8_e4m3fnfloat8_e4m3fnuzfloat8_e5m2float8_e5m2fnuz

https://github.com/jax-ml/ml_dtypes
# Available modules


The overview below shows which ml_dtypes installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using ml_dtypes, load one of these modules using a `module load` command like:

```shell
module load ml_dtypes/0.3.2-gfbf-2023a
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ml_dtypes/0.3.2-gfbf-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|


### ml_dtypes/0.3.2-gfbf-2023a

This is a list of extensions included in the module:

etils-1.6.0, ml_dtypes-0.3.2, opt_einsum-3.3.0