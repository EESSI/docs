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


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2024.09.0+375|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`RStudio-Server/2024.09.0+375-foss-2023b-Java-11-R-4.4.1`|
|2024.12.0+467|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`RStudio-Server/2024.12.0+467-foss-2024a-R-4.4.2`|

## Extensions

Overview of extensions included in RStudio-Server installations
