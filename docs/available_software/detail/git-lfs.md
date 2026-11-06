---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Git Large File Storage (LFS) replaces large files such as audio\n\
    \ samples, videos, datasets, and graphics with text pointers inside Git, while\n\
    \ storing the file contents on a remote server like GitHub.com"
  license: Not confirmed
  name: git-lfs
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
  softwareVersion: '[''3.7.1'']'
  url: https://git-lfs.github.com
---
# git-lfs


Git Large File Storage (LFS) replaces large files such as audio
 samples, videos, datasets, and graphics with text pointers inside Git, while
 storing the file contents on a remote server like GitHub.com

<small>homepage: </small><span class="software-link">[https://git-lfs.github.com](https://git-lfs.github.com)</span>

## Available installations


|git-lfs version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.7.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`git-lfs/3.7.1`|