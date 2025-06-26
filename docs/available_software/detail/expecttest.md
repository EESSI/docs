---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: This library implements expect tests (also known as "golden" tests).
    Expect tests are a method of writing tests where instead of hard-coding the expected
    output of a test, you run the test to get the output, and the test framework automatically
    populates the expected output. If the output of the test changes, you can rerun
    the test with the environment variable EXPECTTEST_ACCEPT=1 to automatically update
    the expected output.
  license: Not confirmed
  name: expecttest
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
  softwareVersion: '[''expecttest/0.1.5-GCCcore-12.3.0'']'
  url: https://github.com/ezyang/expecttest
---

expecttest
==========


This library implements expect tests (also known as "golden" tests). Expect tests are a method of writing tests where instead of hard-coding the expected output of a test, you run the test to get the output, and the test framework automatically populates the expected output. If the output of the test changes, you can rerun the test with the environment variable EXPECTTEST_ACCEPT=1 to automatically update the expected output.

https://github.com/ezyang/expecttest
# Available modules


The overview below shows which expecttest installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using expecttest, load one of these modules using a `module load` command like:

```shell
module load expecttest/0.1.5-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|expecttest/0.1.5-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
