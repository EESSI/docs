---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'KrakenUniq: confident and fast metagenomics classification using unique
    k-mer counts'
  license: Not confirmed
  name: KrakenUniq
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
  softwareVersion: '[''1.0.4'']'
  url: https://github.com/fbreitwieser/krakenuniq/
---
# KrakenUniq


KrakenUniq: confident and fast metagenomics classification using unique k-mer counts

<small>homepage: </small><span class="software-link">[https://github.com/fbreitwieser/krakenuniq/](https://github.com/fbreitwieser/krakenuniq/)</span>

## Available installations


|KrakenUniq version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.0.4|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`KrakenUniq/1.0.4-GCC-14.3.0`|