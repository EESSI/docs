---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "HOMER (Hypergeometric Optimization of Motif EnRichment) is a suite\
    \ of tools for Motif Discovery and\n next-gen sequencing analysis.  It is a collection\
    \ of command line programs for unix-style operating systems written\n in Perl\
    \ and C++. HOMER was primarily written as a de novo motif discovery algorithm\
    \ and is well suited for finding\n 8-20 bp motifs in large scale genomics data.\
    \  HOMER contains many useful tools for analyzing ChIP-Seq, GRO-Seq,\n RNA-Seq,\
    \ DNase-Seq, Hi-C and numerous other types of functional genomics sequencing data\
    \ sets."
  license: Not confirmed
  name: HOMER
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
  softwareVersion: '[''5.1'']'
  url: http://homer.ucsd.edu/homer/
---
# HOMER


HOMER (Hypergeometric Optimization of Motif EnRichment) is a suite of tools for Motif Discovery and
 next-gen sequencing analysis.  It is a collection of command line programs for unix-style operating systems written
 in Perl and C++. HOMER was primarily written as a de novo motif discovery algorithm and is well suited for finding
 8-20 bp motifs in large scale genomics data.  HOMER contains many useful tools for analyzing ChIP-Seq, GRO-Seq,
 RNA-Seq, DNase-Seq, Hi-C and numerous other types of functional genomics sequencing data sets.

<small>homepage: </small><span class="software-link">[http://homer.ucsd.edu/homer/](http://homer.ucsd.edu/homer/)</span>

## Available installations


|HOMER version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`HOMER/5.1-foss-2025a-R-4.5.1`|