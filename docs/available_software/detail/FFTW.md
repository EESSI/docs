---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: FFTW is a C subroutine library for computing the discrete Fourier transform
    (DFT)in one or more dimensions, of arbitrary input size, and of both real and
    complex data.
  license: Not confirmed
  name: FFTW
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
  softwareVersion: '[''FFTW/3.3.10-GCC-12.2.0'', ''FFTW/3.3.10-GCC-12.3.0'', ''FFTW/3.3.10-GCC-13.2.0'']'
  url: https://www.fftw.org
---

FFTW
====


FFTW is a C subroutine library for computing the discrete Fourier transform (DFT)in one or more dimensions, of arbitrary input size, and of both real and complex data.

https://www.fftw.org
# Available modules


The overview below shows which FFTW installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using FFTW, load one of these modules using a `module load` command like:

```shell
module load FFTW/3.3.10-GCC-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|FFTW/3.3.10-GCC-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|FFTW/3.3.10-GCC-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
|FFTW/3.3.10-GCC-12.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|
