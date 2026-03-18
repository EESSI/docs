---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Gotcha is a library that wraps functions. Tools can use gotcha to
    install hooks into other

    libraries, for example putting a wrapper function around libc''s malloc. It is
    similar to LD_PRELOAD, but

    operates via a programmable API. This enables easy methods of accomplishing tasks
    like code instrumentation

    or wholesale replacement of mechanisms in programs without disrupting their source
    code.'
  license: Not confirmed
  name: GOTCHA
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
  softwareVersion: '[''1.0.8'']'
  url: https://gotcha.readthedocs.io/en/latest/
---
# GOTCHA


Gotcha is a library that wraps functions. Tools can use gotcha to install hooks into other
libraries, for example putting a wrapper function around libc's malloc. It is similar to LD_PRELOAD, but
operates via a programmable API. This enables easy methods of accomplishing tasks like code instrumentation
or wholesale replacement of mechanisms in programs without disrupting their source code.

<small>homepage: </small><span class="software-link">[https://gotcha.readthedocs.io/en/latest/](https://gotcha.readthedocs.io/en/latest/)</span>

## Available installations


|GOTCHA version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.8|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`GOTCHA/1.0.8-GCCcore-14.2.0`|