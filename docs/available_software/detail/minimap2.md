---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Minimap2 is a fast sequence mapping and alignment

    program that can find overlaps between long noisy reads, or map long

    reads or their assemblies to a reference genome optionally with detailed

    alignment (i.e. CIGAR). At present, it works efficiently with query

    sequences from a few kilobases to ~100 megabases in length at an error

    rate ~15%. Minimap2 outputs in the PAF or the SAM format. On limited

    test data sets, minimap2 is over 20 times faster than most other

    long-read aligners. It will replace BWA-MEM for long reads and contig

    alignment.'
  license: Not confirmed
  name: minimap2
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
  softwareVersion: '[''2.30'']'
  url: https://github.com/lh3/minimap2
---
# minimap2


Minimap2 is a fast sequence mapping and alignment
program that can find overlaps between long noisy reads, or map long
reads or their assemblies to a reference genome optionally with detailed
alignment (i.e. CIGAR). At present, it works efficiently with query
sequences from a few kilobases to ~100 megabases in length at an error
rate ~15%. Minimap2 outputs in the PAF or the SAM format. On limited
test data sets, minimap2 is over 20 times faster than most other
long-read aligners. It will replace BWA-MEM for long reads and contig
alignment.

<small>homepage: </small><span class="software-link">[https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)</span>

## Available installations


|minimap2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.30|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`minimap2/2.30-GCCcore-14.3.0`|