---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "A framework for managing and maintaining multi-language pre-commit\
    \ hooks.\n\nGit hook scripts are useful for identifying simple issues before submission\
    \ to code review.\n We run our hooks on every commit to automatically point out\
    \ issues in code such as missing semicolons,\n trailing whitespace, and debug\
    \ statements. By pointing these issues out before code review,\n this allows a\
    \ code reviewer to focus on the architecture of a change while not wasting time\n\
    \ with trivial style nitpicks."
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
  softwareVersion: '[''3.7.0'']'
  url: https://pre-commit.com/
---
# pre-commit


A framework for managing and maintaining multi-language pre-commit hooks.

Git hook scripts are useful for identifying simple issues before submission to code review.
 We run our hooks on every commit to automatically point out issues in code such as missing semicolons,
 trailing whitespace, and debug statements. By pointing these issues out before code review,
 this allows a code reviewer to focus on the architecture of a change while not wasting time
 with trivial style nitpicks.

<small>homepage: </small><span class="software-link">[https://pre-commit.com/](https://pre-commit.com/)</span>

## Available installations


|pre-commit version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.7.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`pre-commit/3.7.0-GCCcore-13.2.0`|

## Extensions

Overview of extensions included in pre-commit installations


### cfgv


|`cfgv` version|pre-commit modules that include it|
| --- | --- |
|3.4.0|`pre-commit/3.7.0-GCCcore-13.2.0`|

### identify


|`identify` version|pre-commit modules that include it|
| --- | --- |
|2.5.35|`pre-commit/3.7.0-GCCcore-13.2.0`|

### nodeenv


|`nodeenv` version|pre-commit modules that include it|
| --- | --- |
|1.8.0|`pre-commit/3.7.0-GCCcore-13.2.0`|

### pre-commit


|`pre-commit` version|pre-commit modules that include it|
| --- | --- |
|3.7.0|`pre-commit/3.7.0-GCCcore-13.2.0`|