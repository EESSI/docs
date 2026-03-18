---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'unifdef - selectively remove C preprocessor conditionals

    The unifdef utility selectively processes conditional C preprocessor

    and the additional text that they delimit, while otherwise leaving the

    file alone.'
  license: Not confirmed
  name: unifdef
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
  softwareVersion: '[''2.12'']'
  url: https://github.com/fanf2/unifdef
---
# unifdef


unifdef - selectively remove C preprocessor conditionals
The unifdef utility selectively processes conditional C preprocessor
and the additional text that they delimit, while otherwise leaving the
file alone.

<small>homepage: </small><span class="software-link">[https://github.com/fanf2/unifdef](https://github.com/fanf2/unifdef)</span>

## Available installations


|unifdef version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.12|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`unifdef/2.12-GCCcore-12.3.0`|