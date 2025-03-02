---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Audio and music processing in Python
  license: Not confirmed
  name: librosa
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
  softwareVersion: '[''librosa/0.10.1-foss-2023a'']'
  url: https://librosa.org/
---

librosa
=======


Audio and music processing in Python

https://librosa.org/
# Available modules


The overview below shows which librosa installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using librosa, load one of these modules using a `module load` command like:

```shell
module load librosa/0.10.1-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|librosa/0.10.1-foss-2023a|x|x|x|x|x|x|x|x|x|


### librosa/0.10.1-foss-2023a

This is a list of extensions included in the module:

audioread-3.0.1, lazy_loader-0.3, librosa-0.10.1, resampy-0.4.3, soundfile-0.12.1, soxr-0.3.7