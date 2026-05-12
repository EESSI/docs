---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "R is a free software environment for statistical computing\n and graphics."
  license: Not confirmed
  name: R
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
  softwareVersion: '[''4.5.1'', ''4.4.2'', ''4.4.1'', ''4.3.2'']'
  url: https://www.r-project.org/
---
# R


R is a free software environment for statistical computing
 and graphics.

<small>homepage: </small><span class="software-link">[https://www.r-project.org/](https://www.r-project.org/)</span>

## Available installations


|R version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.5.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`R/4.5.1-gfbf-2025a`|
|4.4.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`R/4.4.2-gfbf-2024a`|
|4.4.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`R/4.4.1-gfbf-2023b`|
|4.3.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`R/4.3.2-gfbf-2023a`|

## Extensions

Overview of extensions included in R installations


### askpass


|`askpass` version|R modules that include it|
| --- | --- |
|1.2.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|1.2.0|`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### b


|`b` version|R modules that include it|
| --- | --- |
|a|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### base64enc


|`base64enc` version|R modules that include it|
| --- | --- |
|0.1-3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### brew


|`brew` version|R modules that include it|
| --- | --- |
|1.0-10|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.0-8|`R/4.3.2-gfbf-2023a`|

### brio


|`brio` version|R modules that include it|
| --- | --- |
|1.1.5|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.1.3|`R/4.3.2-gfbf-2023a`|

### bslib


|`bslib` version|R modules that include it|
| --- | --- |
|0.9.0|`R/4.5.1-gfbf-2025a`|
|0.8.0|`R/4.4.2-gfbf-2024a`|
|0.7.0|`R/4.4.1-gfbf-2023b`|
|0.5.1|`R/4.3.2-gfbf-2023a`|

### c


|`c` version|R modules that include it|
| --- | --- |
|o|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### cachem


|`cachem` version|R modules that include it|
| --- | --- |
|1.1.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.0.8|`R/4.3.2-gfbf-2023a`|

### callr


|`callr` version|R modules that include it|
| --- | --- |
|3.7.6|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|3.7.3|`R/4.3.2-gfbf-2023a`|

### cli


|`cli` version|R modules that include it|
| --- | --- |
|3.6.5|`R/4.5.1-gfbf-2025a`|
|3.6.3|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|3.6.1|`R/4.3.2-gfbf-2023a`|

### clipr


|`clipr` version|R modules that include it|
| --- | --- |
|0.8.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### commonmark


|`commonmark` version|R modules that include it|
| --- | --- |
|2.0.0|`R/4.5.1-gfbf-2025a`|
|1.9.2|`R/4.4.2-gfbf-2024a`|
|1.9.1|`R/4.4.1-gfbf-2023b`|
|1.9.0|`R/4.3.2-gfbf-2023a`|

### cpp11


|`cpp11` version|R modules that include it|
| --- | --- |
|0.5.2|`R/4.5.1-gfbf-2025a`|
|0.5.0|`R/4.4.2-gfbf-2024a`|
|0.4.7|`R/4.4.1-gfbf-2023b`|
|0.4.6|`R/4.3.2-gfbf-2023a`|

### crayon


|`crayon` version|R modules that include it|
| --- | --- |
|1.5.3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.5.2|`R/4.3.2-gfbf-2023a`|

### credentials


|`credentials` version|R modules that include it|
| --- | --- |
|2.0.3|`R/4.5.1-gfbf-2025a`|
|2.0.2|`R/4.4.2-gfbf-2024a`|
|2.0.1|`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### curl


|`curl` version|R modules that include it|
| --- | --- |
|7.0.0|`R/4.5.1-gfbf-2025a`|
|6.0.1|`R/4.4.2-gfbf-2024a`|
|5.2.1|`R/4.4.1-gfbf-2023b`|
|5.1.0|`R/4.3.2-gfbf-2023a`|

### d


|`d` version|R modules that include it|
| --- | --- |
|a|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### desc


|`desc` version|R modules that include it|
| --- | --- |
|1.4.3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.4.2|`R/4.3.2-gfbf-2023a`|

### devtools


|`devtools` version|R modules that include it|
| --- | --- |
|2.4.6|`R/4.5.1-gfbf-2025a`|
|2.4.5|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### diffobj


|`diffobj` version|R modules that include it|
| --- | --- |
|0.3.6|`R/4.5.1-gfbf-2025a`|
|0.3.5|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### digest


|`digest` version|R modules that include it|
| --- | --- |
|0.6.37|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|0.6.36|`R/4.4.1-gfbf-2023b`|
|0.6.33|`R/4.3.2-gfbf-2023a`|

### downlit


|`downlit` version|R modules that include it|
| --- | --- |
|0.4.4|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|0.4.3|`R/4.3.2-gfbf-2023a`|

### ellipsis


|`ellipsis` version|R modules that include it|
| --- | --- |
|0.3.2|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### evaluate


|`evaluate` version|R modules that include it|
| --- | --- |
|1.0.5|`R/4.5.1-gfbf-2025a`|
|1.0.1|`R/4.4.2-gfbf-2024a`|
|0.24.0|`R/4.4.1-gfbf-2023b`|
|0.23|`R/4.3.2-gfbf-2023a`|

### fansi


|`fansi` version|R modules that include it|
| --- | --- |
|1.0.6|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.0.5|`R/4.3.2-gfbf-2023a`|

### fastmap


|`fastmap` version|R modules that include it|
| --- | --- |
|1.2.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.1.1|`R/4.3.2-gfbf-2023a`|

### fontawesome


|`fontawesome` version|R modules that include it|
| --- | --- |
|0.5.3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|0.5.2|`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### fs


|`fs` version|R modules that include it|
| --- | --- |
|1.6.6|`R/4.5.1-gfbf-2025a`|
|1.6.5|`R/4.4.2-gfbf-2024a`|
|1.6.4|`R/4.4.1-gfbf-2023b`|
|1.6.3|`R/4.3.2-gfbf-2023a`|

### g


|`g` version|R modules that include it|
| --- | --- |
|r|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### gert


|`gert` version|R modules that include it|
| --- | --- |
|2.1.5|`R/4.5.1-gfbf-2025a`|
|2.1.4|`R/4.4.2-gfbf-2024a`|
|2.0.1|`R/4.4.1-gfbf-2023b`|
|2.0.0|`R/4.3.2-gfbf-2023a`|

### gh


|`gh` version|R modules that include it|
| --- | --- |
|1.5.0|`R/4.5.1-gfbf-2025a`|
|1.4.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.4.0|`R/4.3.2-gfbf-2023a`|

### gitcreds


|`gitcreds` version|R modules that include it|
| --- | --- |
|0.1.2|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### glue


|`glue` version|R modules that include it|
| --- | --- |
|1.8.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|1.7.0|`R/4.4.1-gfbf-2023b`|
|1.6.2|`R/4.3.2-gfbf-2023a`|

### highr


|`highr` version|R modules that include it|
| --- | --- |
|0.11|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|0.10|`R/4.3.2-gfbf-2023a`|

### htmltools


|`htmltools` version|R modules that include it|
| --- | --- |
|0.5.8.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|0.5.7|`R/4.3.2-gfbf-2023a`|

### htmlwidgets


|`htmlwidgets` version|R modules that include it|
| --- | --- |
|1.6.4|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.6.2|`R/4.3.2-gfbf-2023a`|

### httpuv


|`httpuv` version|R modules that include it|
| --- | --- |
|1.6.16|`R/4.5.1-gfbf-2025a`|
|1.6.15|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.6.12|`R/4.3.2-gfbf-2023a`|

### httr


|`httr` version|R modules that include it|
| --- | --- |
|1.4.7|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### httr2


|`httr2` version|R modules that include it|
| --- | --- |
|1.2.1|`R/4.5.1-gfbf-2025a`|
|1.0.6|`R/4.4.2-gfbf-2024a`|
|1.0.1|`R/4.4.1-gfbf-2023b`|
|0.2.3|`R/4.3.2-gfbf-2023a`|

### ini


|`ini` version|R modules that include it|
| --- | --- |
|0.3.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### jquerylib


|`jquerylib` version|R modules that include it|
| --- | --- |
|0.1.4|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### jsonlite


|`jsonlite` version|R modules that include it|
| --- | --- |
|2.0.0|`R/4.5.1-gfbf-2025a`|
|1.8.9|`R/4.4.2-gfbf-2024a`|
|1.8.8|`R/4.4.1-gfbf-2023b`|
|1.8.7|`R/4.3.2-gfbf-2023a`|

### knitr


|`knitr` version|R modules that include it|
| --- | --- |
|1.50|`R/4.5.1-gfbf-2025a`|
|1.49|`R/4.4.2-gfbf-2024a`|
|1.47|`R/4.4.1-gfbf-2023b`|
|1.45|`R/4.3.2-gfbf-2023a`|

### later


|`later` version|R modules that include it|
| --- | --- |
|1.4.4|`R/4.5.1-gfbf-2025a`|
|1.3.2|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.3.1|`R/4.3.2-gfbf-2023a`|

### lifecycle


|`lifecycle` version|R modules that include it|
| --- | --- |
|1.0.4|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.0.3|`R/4.3.2-gfbf-2023a`|

### m


|`m` version|R modules that include it|
| --- | --- |
|e|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### magrittr


|`magrittr` version|R modules that include it|
| --- | --- |
|2.0.4|`R/4.5.1-gfbf-2025a`|
|2.0.3|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### memoise


|`memoise` version|R modules that include it|
| --- | --- |
|2.0.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### mime


|`mime` version|R modules that include it|
| --- | --- |
|0.13|`R/4.5.1-gfbf-2025a`|
|0.12|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### miniUI


|`miniUI` version|R modules that include it|
| --- | --- |
|0.1.2|`R/4.5.1-gfbf-2025a`|
|0.1.1.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### openssl


|`openssl` version|R modules that include it|
| --- | --- |
|2.3.4|`R/4.5.1-gfbf-2025a`|
|2.2.2|`R/4.4.2-gfbf-2024a`|
|2.2.0|`R/4.4.1-gfbf-2023b`|
|2.1.1|`R/4.3.2-gfbf-2023a`|

### p


|`p` version|R modules that include it|
| --- | --- |
|a|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### pillar


|`pillar` version|R modules that include it|
| --- | --- |
|1.11.1|`R/4.5.1-gfbf-2025a`|
|1.9.0|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### pkgbuild


|`pkgbuild` version|R modules that include it|
| --- | --- |
|1.4.8|`R/4.5.1-gfbf-2025a`|
|1.4.5|`R/4.4.2-gfbf-2024a`|
|1.4.4|`R/4.4.1-gfbf-2023b`|
|1.4.2|`R/4.3.2-gfbf-2023a`|

### pkgconfig


|`pkgconfig` version|R modules that include it|
| --- | --- |
|2.0.3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### pkgdown


|`pkgdown` version|R modules that include it|
| --- | --- |
|2.1.3|`R/4.5.1-gfbf-2025a`|
|2.1.1|`R/4.4.2-gfbf-2024a`|
|2.0.9|`R/4.4.1-gfbf-2023b`|
|2.0.7|`R/4.3.2-gfbf-2023a`|

### pkgload


|`pkgload` version|R modules that include it|
| --- | --- |
|1.4.1|`R/4.5.1-gfbf-2025a`|
|1.4.0|`R/4.4.2-gfbf-2024a`|
|1.3.4|`R/4.4.1-gfbf-2023b`|
|1.3.3|`R/4.3.2-gfbf-2023a`|

### praise


|`praise` version|R modules that include it|
| --- | --- |
|1.0.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### prettyunits


|`prettyunits` version|R modules that include it|
| --- | --- |
|1.2.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### processx


|`processx` version|R modules that include it|
| --- | --- |
|3.8.6|`R/4.5.1-gfbf-2025a`|
|3.8.4|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|3.8.2|`R/4.3.2-gfbf-2023a`|

### profvis


|`profvis` version|R modules that include it|
| --- | --- |
|0.4.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|0.3.8|`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### promises


|`promises` version|R modules that include it|
| --- | --- |
|1.3.3|`R/4.5.1-gfbf-2025a`|
|1.3.0|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.2.1|`R/4.3.2-gfbf-2023a`|

### ps


|`ps` version|R modules that include it|
| --- | --- |
|1.9.1|`R/4.5.1-gfbf-2025a`|
|1.8.1|`R/4.4.2-gfbf-2024a`|
|1.7.6|`R/4.4.1-gfbf-2023b`|
|1.7.5|`R/4.3.2-gfbf-2023a`|

### purrr


|`purrr` version|R modules that include it|
| --- | --- |
|1.1.0|`R/4.5.1-gfbf-2025a`|
|1.0.2|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### R6


|`R6` version|R modules that include it|
| --- | --- |
|2.6.1|`R/4.5.1-gfbf-2025a`|
|2.5.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### ragg


|`ragg` version|R modules that include it|
| --- | --- |
|1.5.0|`R/4.5.1-gfbf-2025a`|
|1.3.3|`R/4.4.2-gfbf-2024a`|
|1.3.2|`R/4.4.1-gfbf-2023b`|
|1.2.6|`R/4.3.2-gfbf-2023a`|

### rappdirs


|`rappdirs` version|R modules that include it|
| --- | --- |
|0.3.3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### rcmdcheck


|`rcmdcheck` version|R modules that include it|
| --- | --- |
|1.4.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### Rcpp


|`Rcpp` version|R modules that include it|
| --- | --- |
|1.1.0|`R/4.5.1-gfbf-2025a`|
|1.0.13-1|`R/4.4.2-gfbf-2024a`|
|1.0.12|`R/4.4.1-gfbf-2023b`|
|1.0.11|`R/4.3.2-gfbf-2023a`|

### rematch2


|`rematch2` version|R modules that include it|
| --- | --- |
|2.1.2|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### remotes


|`remotes` version|R modules that include it|
| --- | --- |
|2.5.0|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|2.4.2.1|`R/4.3.2-gfbf-2023a`|

### rlang


|`rlang` version|R modules that include it|
| --- | --- |
|1.1.6|`R/4.5.1-gfbf-2025a`|
|1.1.4|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.1.2|`R/4.3.2-gfbf-2023a`|

### rmarkdown


|`rmarkdown` version|R modules that include it|
| --- | --- |
|2.30|`R/4.5.1-gfbf-2025a`|
|2.29|`R/4.4.2-gfbf-2024a`|
|2.27|`R/4.4.1-gfbf-2023b`|
|2.25|`R/4.3.2-gfbf-2023a`|

### roxygen2


|`roxygen2` version|R modules that include it|
| --- | --- |
|7.3.3|`R/4.5.1-gfbf-2025a`|
|7.3.2|`R/4.4.2-gfbf-2024a`|
|7.3.1|`R/4.4.1-gfbf-2023b`|
|7.2.3|`R/4.3.2-gfbf-2023a`|

### rprojroot


|`rprojroot` version|R modules that include it|
| --- | --- |
|2.1.1|`R/4.5.1-gfbf-2025a`|
|2.0.4|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### rstudioapi


|`rstudioapi` version|R modules that include it|
| --- | --- |
|0.17.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|0.16.0|`R/4.4.1-gfbf-2023b`|
|0.15.0|`R/4.3.2-gfbf-2023a`|

### rversions


|`rversions` version|R modules that include it|
| --- | --- |
|2.1.2|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### s


|`s` version|R modules that include it|
| --- | --- |
|t|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|
|p|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### sass


|`sass` version|R modules that include it|
| --- | --- |
|0.4.10|`R/4.5.1-gfbf-2025a`|
|0.4.9|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|0.4.7|`R/4.3.2-gfbf-2023a`|

### sessioninfo


|`sessioninfo` version|R modules that include it|
| --- | --- |
|1.2.3|`R/4.5.1-gfbf-2025a`|
|1.2.2|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### shiny


|`shiny` version|R modules that include it|
| --- | --- |
|1.11.1|`R/4.5.1-gfbf-2025a`|
|1.9.1|`R/4.4.2-gfbf-2024a`|
|1.8.1.1|`R/4.4.1-gfbf-2023b`|
|1.7.5.1|`R/4.3.2-gfbf-2023a`|

### sourcetools


|`sourcetools` version|R modules that include it|
| --- | --- |
|0.1.7-1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### stringi


|`stringi` version|R modules that include it|
| --- | --- |
|1.8.7|`R/4.5.1-gfbf-2025a`|
|1.8.4|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.7.12|`R/4.3.2-gfbf-2023a`|

### stringr


|`stringr` version|R modules that include it|
| --- | --- |
|1.5.2|`R/4.5.1-gfbf-2025a`|
|1.5.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.5.0|`R/4.3.2-gfbf-2023a`|

### sys


|`sys` version|R modules that include it|
| --- | --- |
|3.4.3|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|3.4.2|`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### systemfonts


|`systemfonts` version|R modules that include it|
| --- | --- |
|1.3.1|`R/4.5.1-gfbf-2025a`|
|1.1.0|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.0.5|`R/4.3.2-gfbf-2023a`|

### t


|`t` version|R modules that include it|
| --- | --- |
|o|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|
|c|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### testthat


|`testthat` version|R modules that include it|
| --- | --- |
|3.2.3|`R/4.5.1-gfbf-2025a`|
|3.2.1.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|3.2.0|`R/4.3.2-gfbf-2023a`|

### textshaping


|`textshaping` version|R modules that include it|
| --- | --- |
|1.0.3|`R/4.5.1-gfbf-2025a`|
|0.4.0|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|0.3.7|`R/4.3.2-gfbf-2023a`|

### tibble


|`tibble` version|R modules that include it|
| --- | --- |
|3.3.0|`R/4.5.1-gfbf-2025a`|
|3.2.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### tinytex


|`tinytex` version|R modules that include it|
| --- | --- |
|0.57|`R/4.5.1-gfbf-2025a`|
|0.54|`R/4.4.2-gfbf-2024a`|
|0.51|`R/4.4.1-gfbf-2023b`|
|0.48|`R/4.3.2-gfbf-2023a`|

### u


|`u` version|R modules that include it|
| --- | --- |
|t|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### urlchecker


|`urlchecker` version|R modules that include it|
| --- | --- |
|1.0.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### usethis


|`usethis` version|R modules that include it|
| --- | --- |
|3.2.1|`R/4.5.1-gfbf-2025a`|
|3.0.0|`R/4.4.2-gfbf-2024a`|
|2.2.3|`R/4.4.1-gfbf-2023b`|
|2.2.2|`R/4.3.2-gfbf-2023a`|

### utf8


|`utf8` version|R modules that include it|
| --- | --- |
|1.2.6|`R/4.5.1-gfbf-2025a`|
|1.2.4|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### vctrs


|`vctrs` version|R modules that include it|
| --- | --- |
|0.6.5|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|0.6.4|`R/4.3.2-gfbf-2023a`|

### waldo


|`waldo` version|R modules that include it|
| --- | --- |
|0.6.2|`R/4.5.1-gfbf-2025a`|
|0.6.1|`R/4.4.2-gfbf-2024a`|
|0.5.2|`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### whisker


|`whisker` version|R modules that include it|
| --- | --- |
|0.4.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### withr


|`withr` version|R modules that include it|
| --- | --- |
|3.0.2|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|3.0.0|`R/4.4.1-gfbf-2023b`|
|2.5.2|`R/4.3.2-gfbf-2023a`|

### xfun


|`xfun` version|R modules that include it|
| --- | --- |
|0.53|`R/4.5.1-gfbf-2025a`|
|0.49|`R/4.4.2-gfbf-2024a`|
|0.45|`R/4.4.1-gfbf-2023b`|
|0.41|`R/4.3.2-gfbf-2023a`|

### xml2


|`xml2` version|R modules that include it|
| --- | --- |
|1.4.0|`R/4.5.1-gfbf-2025a`|
|1.3.6|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.3.5|`R/4.3.2-gfbf-2023a`|

### xopen


|`xopen` version|R modules that include it|
| --- | --- |
|1.0.1|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|1.0.0|`R/4.3.2-gfbf-2023a`|

### xtable


|`xtable` version|R modules that include it|
| --- | --- |
|1.8-4|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`<br/>`R/4.3.2-gfbf-2023a`|

### yaml


|`yaml` version|R modules that include it|
| --- | --- |
|2.3.10|`R/4.5.1-gfbf-2025a`<br/>`R/4.4.2-gfbf-2024a`|
|2.3.8|`R/4.4.1-gfbf-2023b`|
|2.3.7|`R/4.3.2-gfbf-2023a`|

### zip


|`zip` version|R modules that include it|
| --- | --- |
|2.3.3|`R/4.5.1-gfbf-2025a`|
|2.3.1|`R/4.4.2-gfbf-2024a`<br/>`R/4.4.1-gfbf-2023b`|
|2.3.0|`R/4.3.2-gfbf-2023a`|