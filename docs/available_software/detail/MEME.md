---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "The MEME Suite allows you to: * discover motifs using MEME, DREME\
    \ (DNA only) or\n GLAM2 on groups of related DNA or protein sequences, * search\
    \ sequence databases with motifs using\n MAST, FIMO, MCAST or GLAM2SCAN, * compare\
    \ a motif to all motifs in a database of motifs, * associate\n motifs with Gene\
    \ Ontology terms via their putative target genes, and * analyse motif enrichment\n\
    \ using SpaMo or CentriMo."
  license: Not confirmed
  name: MEME
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
  softwareVersion: '[''5.5.9'']'
  url: https://meme-suite.org/meme/index.html
---
# MEME


The MEME Suite allows you to: * discover motifs using MEME, DREME (DNA only) or
 GLAM2 on groups of related DNA or protein sequences, * search sequence databases with motifs using
 MAST, FIMO, MCAST or GLAM2SCAN, * compare a motif to all motifs in a database of motifs, * associate
 motifs with Gene Ontology terms via their putative target genes, and * analyse motif enrichment
 using SpaMo or CentriMo.

<small>homepage: </small><span class="software-link">[https://meme-suite.org/meme/index.html](https://meme-suite.org/meme/index.html)</span>

## Available installations


|MEME version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.5.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`MEME/5.5.9-gompi-2025a`|