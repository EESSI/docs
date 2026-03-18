---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "This is the RStudio Server version.\nRStudio is a set of integrated\
    \ tools designed to help you be more productive with R.\n\nThe server can be started\
    \ with:\n  rserver --server-daemonize=0 --www-port=8787\n\nIf you need a database\
    \ config one can be created with:\n  MYTMP=`mktemp -d` && echo -e \"provider=sqlite\\\
    ndirectory=${MYTMP}/sqlite\" > \"${MYTMP}/db.conf\"\nand then used with:\n  rserver\
    \ ... --database-config-file=\"${MYTMP}/db.conf\"\n"
  license: Not confirmed
  name: RStudio-Server
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
  softwareVersion: '[''2024.12.0+467'', ''2024.09.0+375'']'
  url: https://www.rstudio.com/
---
# RStudio-Server


This is the RStudio Server version.
RStudio is a set of integrated tools designed to help you be more productive with R.

The server can be started with:
  rserver --server-daemonize=0 --www-port=8787

If you need a database config one can be created with:
  MYTMP=`mktemp -d` && echo -e "provider=sqlite\ndirectory=${MYTMP}/sqlite" > "${MYTMP}/db.conf"
and then used with:
  rserver ... --database-config-file="${MYTMP}/db.conf"


<small>homepage: </small><span class="software-link">[https://www.rstudio.com/](https://www.rstudio.com/)</span>

## Available installations


|RStudio-Server version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|2024.09.0+375|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`RStudio-Server/2024.09.0+375-foss-2023b-Java-11-R-4.4.1`|
|2024.12.0+467|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`RStudio-Server/2024.12.0+467-foss-2024a-R-4.4.2`|