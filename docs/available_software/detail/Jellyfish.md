---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Jellyfish is a tool for fast, memory-efficient counting of k-mers in
    DNA.
  license: Not confirmed
  name: Jellyfish
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
  softwareVersion: '[''2.3.1'']'
  url: http://www.genome.umd.edu/jellyfish.html
---
# Jellyfish


Jellyfish is a tool for fast, memory-efficient counting of k-mers in DNA.

<small>homepage: </small><span class="software-link">[http://www.genome.umd.edu/jellyfish.html](http://www.genome.umd.edu/jellyfish.html)</span>

## Available installations


|Jellyfish version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.3.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Jellyfish/2.3.1-GCC-14.3.0`|