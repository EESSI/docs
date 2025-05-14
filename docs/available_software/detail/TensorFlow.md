---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: An open-source software library for Machine Intelligence
  license: Not confirmed
  name: TensorFlow
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
  softwareVersion: '[''TensorFlow/2.13.0-foss-2023a'']'
  url: https://www.tensorflow.org/
---

TensorFlow
==========


An open-source software library for Machine Intelligence

https://www.tensorflow.org/
# Available modules


The overview below shows which TensorFlow installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using TensorFlow, load one of these modules using a `module load` command like:

```shell
module load TensorFlow/2.13.0-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|TensorFlow/2.13.0-foss-2023a|x|x|x|x|x|x|x|x|x|x|x|


### TensorFlow/2.13.0-foss-2023a

This is a list of extensions included in the module:

absl-py-1.4.0, astor-0.8.1, astunparse-1.6.3, cachetools-5.3.1, google-auth-2.22.0, google-auth-oauthlib-1.0.0, google-pasta-0.2.0, grpcio-1.57.0, gviz-api-1.10.0, keras-2.13.1, Markdown-3.4.4, oauthlib-3.2.2, opt-einsum-3.3.0, portpicker-1.5.2, pyasn1-modules-0.3.0, requests-oauthlib-1.3.1, rsa-4.9, tblib-2.0.0, tensorboard-2.13.0, tensorboard-data-server-0.7.1, tensorboard-plugin-profile-2.13.1, tensorboard-plugin-wit-1.8.1, TensorFlow-2.13.0, tensorflow-estimator-2.13.0, termcolor-2.3.0, Werkzeug-2.3.7, wrapt-1.15.0