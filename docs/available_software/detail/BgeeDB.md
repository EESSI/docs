---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Annotation and gene expression data retrieval from Bgee database.

    TopAnat, an anatomical entities Enrichment Analysis tool for UBERON ontology.'
  license: Not confirmed
  name: BgeeDB
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
  softwareVersion: '[''2.36.0'']'
  url: https://github.com/BgeeDB/BgeeDB_R
---
# BgeeDB


Annotation and gene expression data retrieval from Bgee database.
TopAnat, an anatomical entities Enrichment Analysis tool for UBERON ontology.

<small>homepage: </small><span class="software-link">[https://github.com/BgeeDB/BgeeDB_R](https://github.com/BgeeDB/BgeeDB_R)</span>

## Available installations


|BgeeDB version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.36.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`BgeeDB/2.36.0-foss-2025a-R-4.5.1`|

## Extensions

Overview of extensions included in BgeeDB installations


### anndata


|`anndata` version|BgeeDB modules that include it|
| --- | --- |
|0.8.0|`BgeeDB/2.36.0-foss-2025a-R-4.5.1`|

### BgeeDB


|`BgeeDB` version|BgeeDB modules that include it|
| --- | --- |
|2.36.0|`BgeeDB/2.36.0-foss-2025a-R-4.5.1`|

### bread


|`bread` version|BgeeDB modules that include it|
| --- | --- |
|0.4.1|`BgeeDB/2.36.0-foss-2025a-R-4.5.1`|

### topGO


|`topGO` version|BgeeDB modules that include it|
| --- | --- |
|2.62.0|`BgeeDB/2.36.0-foss-2025a-R-4.5.1`|