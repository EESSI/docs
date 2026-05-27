---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'p7zip is a quick port of 7z.exe and 7za.exe (CLI version of

    7zip) for Unix. 7-Zip is a file archiver with highest compression ratio.'
  license: Not confirmed
  name: p7zip
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
  softwareVersion: '[''17.05'']'
  url: https://github.com/p7zip-project/p7zip/
---
# p7zip


p7zip is a quick port of 7z.exe and 7za.exe (CLI version of
7zip) for Unix. 7-Zip is a file archiver with highest compression ratio.

<small>homepage: </small><span class="software-link">[https://github.com/p7zip-project/p7zip/](https://github.com/p7zip-project/p7zip/)</span>

## Available installations


|p7zip version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|17.05|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`p7zip/17.05-GCCcore-13.3.0`|