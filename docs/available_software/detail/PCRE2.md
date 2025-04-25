---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: The PCRE library is a set of functions that implement regular expression
    pattern matching using the same syntax and semantics as Perl 5.
  license: Not confirmed
  name: PCRE2
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
  softwareVersion: '[''PCRE2/10.40-GCCcore-12.2.0'', ''PCRE2/10.42-GCCcore-12.3.0'',
    ''PCRE2/10.42-GCCcore-13.2.0'']'
  url: https://www.pcre.org/
---

PCRE2
=====


The PCRE library is a set of functions that implement regular expression pattern matching using the same syntax and semantics as Perl 5.

https://www.pcre.org/
# Available modules


The overview below shows which PCRE2 installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PCRE2, load one of these modules using a `module load` command like:

```shell
module load PCRE2/10.42-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PCRE2/10.42-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|
|PCRE2/10.42-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|
|PCRE2/10.40-GCCcore-12.2.0|x|x|x|x|x|x|x|x|x|x|x|
