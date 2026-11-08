---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'NbClassic provides a backwards compatible Jupyter Notebook interface

    that you can install side-by-side with the latest versions: That way, you can
    fearlessly

    upgrade without worrying about your classic extensions and customizations breaking.'
  license: Not confirmed
  name: nbclassic
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
  softwareVersion: '[''1.3.3'']'
  url: https://jupyter.org/
---
# nbclassic


NbClassic provides a backwards compatible Jupyter Notebook interface
that you can install side-by-side with the latest versions: That way, you can fearlessly
upgrade without worrying about your classic extensions and customizations breaking.

<small>homepage: </small><span class="software-link">[https://jupyter.org/](https://jupyter.org/)</span>

## Available installations


|nbclassic version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`, `aws/graviton4`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`, `graniterapids`<br/>|*(none)*|<span class="software-eessi-version-202606">2026.06</span>|`nbclassic/1.3.3-GCCcore-15.2.0`|
|1.3.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`nbclassic/1.3.3-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in nbclassic installations


### ipython_genutils


|`ipython_genutils` version|nbclassic modules that include it|
| --- | --- |
|0.2.0|`nbclassic/1.3.3-GCCcore-15.2.0`|

### nbclassic


|`nbclassic` version|nbclassic modules that include it|
| --- | --- |
|1.3.3|`nbclassic/1.3.3-GCCcore-15.2.0`|