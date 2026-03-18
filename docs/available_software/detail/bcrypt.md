---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Acceptable password hashing for your software and your servers (but
    you should

    really use argon2id or scrypt)

    '
  license: Not confirmed
  name: bcrypt
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
  softwareVersion: '[''4.0.1'']'
  url: https://github.com/pyca/bcrypt/
---
# bcrypt


Acceptable password hashing for your software and your servers (but you should
really use argon2id or scrypt)


<small>homepage: </small><span class="software-link">[https://github.com/pyca/bcrypt/](https://github.com/pyca/bcrypt/)</span>

## Available installations


|bcrypt version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`bcrypt/4.0.1-GCCcore-12.3.0`|