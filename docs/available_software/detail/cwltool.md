---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: This is the reference implementation of the Common Workflow Language
    openstandards. It is intended to be feature complete and provide comprehensivevalidation
    of CWL files as well as provide other tools related to working withCWL.
  license: Not confirmed
  name: cwltool
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
  softwareVersion: '[''cwltool/3.1.20250110105449-foss-2023b'']'
  url: https://cwltool.readthedocs.io/
---

cwltool
=======


This is the reference implementation of the Common Workflow Language openstandards. It is intended to be feature complete and provide comprehensivevalidation of CWL files as well as provide other tools related to working withCWL.

https://cwltool.readthedocs.io/
# Available modules


The overview below shows which cwltool installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using cwltool, load one of these modules using a `module load` command like:

```shell
module load cwltool/3.1.20250110105449-foss-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|cwltool/3.1.20250110105449-foss-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### cwltool/3.1.20250110105449-foss-2023b

This is a list of extensions included in the module:

argcomplete-3.6.2, coloredlogs-15.0.1, cwl-upgrader-1.2.12, cwl-utils-0.38, cwltool-3.1.20250110105449, humanfriendly-10.0, mistune-3.0.2, mypy-extensions-1.1.0, prov-1.5.1, rich-argparse-1.7.1, schema-salad-8.9.20250408123006, spython-0.3.14