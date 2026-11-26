---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'FLAIR (Full-Length Alternative Isoform analysis of RNA)

    for the correction, isoform definition, and alternative splicing analysis of noisy
    reads.

    FLAIR has primarily been used for nanopore cDNA, native RNA, and PacBio sequencing
    reads.'
  license: Not confirmed
  name: FLAIR
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
  softwareVersion: '[''3.0.1'']'
  url: https://github.com/BrooksLabUCSC/flair
---
# FLAIR


FLAIR (Full-Length Alternative Isoform analysis of RNA)
for the correction, isoform definition, and alternative splicing analysis of noisy reads.
FLAIR has primarily been used for nanopore cDNA, native RNA, and PacBio sequencing reads.

<small>homepage: </small><span class="software-link">[https://github.com/BrooksLabUCSC/flair](https://github.com/BrooksLabUCSC/flair)</span>

## Available installations


|FLAIR version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.0.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`FLAIR/3.0.1-foss-2025b`|

## Extensions

Overview of extensions included in FLAIR installations


### flair-brookslab


|`flair-brookslab` version|FLAIR modules that include it|
| --- | --- |
|3.0.1|`FLAIR/3.0.1-foss-2025b`|

### mappy


|`mappy` version|FLAIR modules that include it|
| --- | --- |
|2.30|`FLAIR/3.0.1-foss-2025b`|

### ncls


|`ncls` version|FLAIR modules that include it|
| --- | --- |
|0.0.70|`FLAIR/3.0.1-foss-2025b`|

### pipettor


|`pipettor` version|FLAIR modules that include it|
| --- | --- |
|1.2.1|`FLAIR/3.0.1-foss-2025b`|