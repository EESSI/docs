---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "\n The numactl program allows you to run your application program\
    \ on specific\n cpu's and memory nodes. It does this by supplying a NUMA memory\
    \ policy to\n the operating system before running your program. The libnuma library\
    \ provides\n convenient ways for you to add NUMA memory policies into your own\
    \ program.\n"
  license: Not confirmed
  name: numactl
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
  softwareVersion: '[''2.0.19'']'
  url: https://github.com/numactl/numactl
---
# numactl



 The numactl program allows you to run your application program on specific
 cpu's and memory nodes. It does this by supplying a NUMA memory policy to
 the operating system before running your program. The libnuma library provides
 convenient ways for you to add NUMA memory policies into your own program.


<small>homepage: </small><span class="software-link">[https://github.com/numactl/numactl](https://github.com/numactl/numactl)</span>

## Available installations


|numactl version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2.0.19|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`numactl/2.0.19-GCCcore-14.3.0`|
|2.0.19|`generic`: `riscv64`<br/><span class="software-cpu-arm">Arm</span>: <br/><span class="software-cpu-amd">AMD</span>: <br/><span class="software-cpu-intel">Intel</span>: <br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`numactl/2.0.19-GCCcore-14.2.0`|