---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    Rivet toolkit (Robust Independent Validation of Experiment and Theory)


    To use your own analysis you must append the path to `RIVET_ANALYSIS_PATH`.

    '
  license: Not confirmed
  name: Rivet
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
  softwareVersion: '[''3.1.9'']'
  url: https://gitlab.com/hepcedar/rivet
---
# Rivet



Rivet toolkit (Robust Independent Validation of Experiment and Theory)

To use your own analysis you must append the path to `RIVET_ANALYSIS_PATH`.


<small>homepage: </small><span class="software-link">[https://gitlab.com/hepcedar/rivet](https://gitlab.com/hepcedar/rivet)</span>

## Available installations


|Rivet version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.1.9|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Rivet/3.1.9-gompi-2023a-HepMC3-3.2.6`|