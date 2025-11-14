---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "MAFFT is a multiple sequence alignment program for unix-like operating\
    \ systems.It offers a range of multiple alignment methods, L-INS-i (accurate;\
    \ for alignmentof <\u223C200 sequences), FFT-NS-2 (fast; for alignment of <\u223C\
    30,000 sequences), etc."
  license: Not confirmed
  name: MAFFT
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
  softwareVersion: '[''MAFFT/7.505-GCC-12.2.0-with-extensions'', ''MAFFT/7.520-GCC-12.3.0-with-extensions'']'
  url: https://mafft.cbrc.jp/alignment/software/source.html
---

MAFFT
=====


MAFFT is a multiple sequence alignment program for unix-like operating systems.It offers a range of multiple alignment methods, L-INS-i (accurate; for alignmentof <∼200 sequences), FFT-NS-2 (fast; for alignment of <∼30,000 sequences), etc.

https://mafft.cbrc.jp/alignment/software/source.html
# Available modules


The overview below shows which MAFFT installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using MAFFT, load one of these modules using a `module load` command like:

```shell
module load MAFFT/7.520-GCC-12.3.0-with-extensions
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MAFFT/7.520-GCC-12.3.0-with-extensions|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|MAFFT/7.505-GCC-12.2.0-with-extensions|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
