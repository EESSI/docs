---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "FastTree infers approximately-maximum-likelihood phylogenetic trees\
    \ from alignments of nucleotide\n or protein sequences. FastTree can handle alignments\
    \ with up to a million of sequences in a reasonable amount of\n time and memory. "
  license: Not confirmed
  name: FastTree
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
  softwareVersion: '[''2.2'']'
  url: https://morgannprice.github.io/fasttree/
---
# FastTree


FastTree infers approximately-maximum-likelihood phylogenetic trees from alignments of nucleotide
 or protein sequences. FastTree can handle alignments with up to a million of sequences in a reasonable amount of
 time and memory. 

<small>homepage: </small><span class="software-link">[https://morgannprice.github.io/fasttree/](https://morgannprice.github.io/fasttree/)</span>

## Available installations


|FastTree version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FastTree/2.2-GCCcore-14.2.0`|