---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and\n some\
    \ other packages. It was written by Fabio Fiorina, and has been shipped as\n part\
    \ of GnuTLS for some time but is now a proper GNU package."
  license: Not confirmed
  name: libtasn1
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
  softwareVersion: '[''4.20.0'', ''4.19.0'']'
  url: https://www.gnu.org/software/libtasn1/
---
# libtasn1


Libtasn1 is the ASN.1 library used by GnuTLS, GNU Shishi and
 some other packages. It was written by Fabio Fiorina, and has been shipped as
 part of GnuTLS for some time but is now a proper GNU package.

<small>homepage: </small><span class="software-link">[https://www.gnu.org/software/libtasn1/](https://www.gnu.org/software/libtasn1/)</span>

## Available installations


|libtasn1 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.19.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`libtasn1/4.19.0-GCCcore-12.3.0`|
|4.20.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`libtasn1/4.20.0-GCCcore-14.3.0`|