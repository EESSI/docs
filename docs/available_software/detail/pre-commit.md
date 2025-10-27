---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: A framework for managing and maintaining multi-language pre-commit
    hooks.Git hook scripts are useful for identifying simple issues before submission
    to code review. We run our hooks on every commit to automatically point out issues
    in code such as missing semicolons, trailing whitespace, and debug statements.
    By pointing these issues out before code review, this allows a code reviewer to
    focus on the architecture of a change while not wasting time with trivial style
    nitpicks.
  license: Not confirmed
  name: pre-commit
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
  softwareVersion: '[''pre-commit/3.7.0-GCCcore-13.2.0'']'
  url: https://pre-commit.com/
---

pre-commit
==========


A framework for managing and maintaining multi-language pre-commit hooks.Git hook scripts are useful for identifying simple issues before submission to code review. We run our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

https://pre-commit.com/
# Available modules


The overview below shows which pre-commit installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using pre-commit, load one of these modules using a `module load` command like:

```shell
module load pre-commit/3.7.0-GCCcore-13.2.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pre-commit/3.7.0-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### pre-commit/3.7.0-GCCcore-13.2.0

This is a list of extensions included in the module:

cfgv-3.4.0, identify-2.5.35, nodeenv-1.8.0, pre-commit-3.7.0