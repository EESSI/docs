---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'This is the RStudio Server version.RStudio is a set of integrated
    tools designed to help you be more productive with R.The server can be started
    with:  rserver --server-daemonize=0 --www-port=8787If you need a database config
    one can be created with:  MYTMP=`mktemp -d` && echo -e "provider=sqlite\ndirectory=${MYTMP}/sqlite"
    > "${MYTMP}/db.conf"and then used with:  rserver ... --database-config-file="${MYTMP}/db.conf'
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
  softwareVersion: '[''RStudio-Server/2024.09.0+375-foss-2023b-Java-11-R-4.4.1'']'
  url: https://www.rstudio.com/
---

RStudio-Server
==============


This is the RStudio Server version.RStudio is a set of integrated tools designed to help you be more productive with R.The server can be started with:  rserver --server-daemonize=0 --www-port=8787If you need a database config one can be created with:  MYTMP=`mktemp -d` && echo -e "provider=sqlite\ndirectory=${MYTMP}/sqlite" > "${MYTMP}/db.conf"and then used with:  rserver ... --database-config-file="${MYTMP}/db.conf

https://www.rstudio.com/
# Available modules


The overview below shows which RStudio-Server installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using RStudio-Server, load one of these modules using a `module load` command like:

```shell
module load RStudio-Server/2024.09.0+375-foss-2023b-Java-11-R-4.4.1
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|RStudio-Server/2024.09.0+375-foss-2023b-Java-11-R-4.4.1|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
