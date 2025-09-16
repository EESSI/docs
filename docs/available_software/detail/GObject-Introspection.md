---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GObject introspection is a middleware layer between C libraries (using
    GObject) and language bindings. The C library can be scanned at compile time and
    generate a metadata file, in addition to the actual native C library. Then at
    runtime, language bindings can read this metadata and automatically provide bindings
    to call into the C library.
  license: Not confirmed
  name: GObject-Introspection
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
  softwareVersion: '[''GObject-Introspection/1.74.0-GCCcore-12.2.0'', ''GObject-Introspection/1.76.1-GCCcore-12.3.0'',
    ''GObject-Introspection/1.78.1-GCCcore-13.2.0'']'
  url: https://gi.readthedocs.io/en/latest/
---

GObject-Introspection
=====================


GObject introspection is a middleware layer between C libraries (using GObject) and language bindings. The C library can be scanned at compile time and generate a metadata file, in addition to the actual native C library. Then at runtime, language bindings can read this metadata and automatically provide bindings to call into the C library.

https://gi.readthedocs.io/en/latest/
# Available modules


The overview below shows which GObject-Introspection installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using GObject-Introspection, load one of these modules using a `module load` command like:

```shell
module load GObject-Introspection/1.78.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|GObject-Introspection/1.78.1-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GObject-Introspection/1.76.1-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|GObject-Introspection/1.74.0-GCCcore-12.2.0|x|-|x|x|x|x|x|x|x|x|x|x|x|x|
