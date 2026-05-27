---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Code to parse output from hmmsearch, hmmscan, phmmer and nhmmer, compatible

    with both version 2 and version 3 of the HMMER package from http://hmmer.org.'
  license: Not confirmed
  name: Bio-SearchIO-hmmer
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
  softwareVersion: '[''1.7.3'']'
  url: https://metacpan.org/pod/Bio::SearchIO::hmmer3
---
# Bio-SearchIO-hmmer


Code to parse output from hmmsearch, hmmscan, phmmer and nhmmer, compatible
with both version 2 and version 3 of the HMMER package from http://hmmer.org.

<small>homepage: </small><span class="software-link">[https://metacpan.org/pod/Bio::SearchIO::hmmer3](https://metacpan.org/pod/Bio::SearchIO::hmmer3)</span>

## Available installations


|Bio-SearchIO-hmmer version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.7.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Bio-SearchIO-hmmer/1.7.3-GCC-12.2.0`|