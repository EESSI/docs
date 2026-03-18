---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "This library implements expect tests (also known as \"golden\" tests).\
    \ Expect tests are a method of\n writing tests where instead of hard-coding the\
    \ expected output of a test, you run the test to get the output, and\n the test\
    \ framework automatically populates the expected output. If the output of the\
    \ test changes, you can rerun\n the test with the environment variable EXPECTTEST_ACCEPT=1\
    \ to automatically update the expected output."
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
  softwareVersion: '[''0.2.1'', ''0.1.5'']'
  url: https://github.com/ezyang/expecttest
---
# expecttest


This library implements expect tests (also known as "golden" tests). Expect tests are a method of
 writing tests where instead of hard-coding the expected output of a test, you run the test to get the output, and
 the test framework automatically populates the expected output. If the output of the test changes, you can rerun
 the test with the environment variable EXPECTTEST_ACCEPT=1 to automatically update the expected output.

<small>homepage: </small><span class="software-link">[https://github.com/ezyang/expecttest](https://github.com/ezyang/expecttest)</span>

## Available installations


|expecttest version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.1.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`expecttest/0.1.5-GCCcore-12.3.0`|
|0.2.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`expecttest/0.2.1-GCCcore-13.3.0`|