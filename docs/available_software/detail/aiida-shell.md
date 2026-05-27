---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'AiiDA plugin that makes running shell commands easy.

    Run any shell executable without writing a dedicated plugin or parser.

    '
  license: Not confirmed
  name: aiida-shell
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
  softwareVersion: '[''0.8.2'']'
  url: https://aiida-shell.readthedocs.io/en/latest/
---
# aiida-shell


AiiDA plugin that makes running shell commands easy.
Run any shell executable without writing a dedicated plugin or parser.


<small>homepage: </small><span class="software-link">[https://aiida-shell.readthedocs.io/en/latest/](https://aiida-shell.readthedocs.io/en/latest/)</span>

## Available installations


|aiida-shell version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.8.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`aiida-shell/0.8.2-foss-2023a`|

## Extensions

Overview of extensions included in aiida-shell installations


### aiida-shell


|`aiida-shell` version|aiida-shell modules that include it|
| --- | --- |
|0.8.2|`aiida-shell/0.8.2-foss-2023a`|