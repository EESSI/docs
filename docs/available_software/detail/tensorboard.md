---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: TensorBoard is a suite of web applications for inspecting andunderstanding
    your TensorFlow runs and graphs.
  license: Not confirmed
  name: tensorboard
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
  softwareVersion: '[''tensorboard/2.15.1-gfbf-2023a'']'
  url: https://github.com/tensorflow/tensorboard
---

tensorboard
===========


TensorBoard is a suite of web applications for inspecting andunderstanding your TensorFlow runs and graphs.

https://github.com/tensorflow/tensorboard
# Available modules


The overview below shows which tensorboard installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using tensorboard, load one of these modules using a `module load` command like:

```shell
module load tensorboard/2.15.1-gfbf-2023a
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|tensorboard/2.15.1-gfbf-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### tensorboard/2.15.1-gfbf-2023a

This is a list of extensions included in the module:

absl-py-2.1.0, cachetools-5.3.2, google-auth-2.26.2, google-auth-oauthlib-1.2.0, gviz-api-1.10.0, Markdown-3.5.2, oauthlib-3.2.2, pyasn1_modules-0.3.0, requests-oauthlib-1.3.1, rsa-4.9, tensorboard-2.15.1, tensorboard-plugin-profile-2.15.1, tensorboard_data_server-0.7.2, Werkzeug-3.0.1