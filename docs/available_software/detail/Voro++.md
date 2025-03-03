---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Voro++ is a software library for carrying out three-dimensional computations
    of the Voronoitessellation. A distinguishing feature of the Voro++ library is
    that it carries out cell-based calculations,computing the Voronoi cell for each
    particle individually. It is particularly well-suited for applications thatrely
    on cell-based statistics, where features of Voronoi cells (eg. volume, centroid,
    number of faces) can be usedto analyze a system of particles.
  license: Not confirmed
  name: Voro++
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
  softwareVersion: '[''Voro++/0.4.6-GCCcore-12.3.0'', ''Voro++/0.4.6-GCCcore-13.2.0'']'
  url: http://math.lbl.gov/voro++/
---

Voro++
======


Voro++ is a software library for carrying out three-dimensional computations of the Voronoitessellation. A distinguishing feature of the Voro++ library is that it carries out cell-based calculations,computing the Voronoi cell for each particle individually. It is particularly well-suited for applications thatrely on cell-based statistics, where features of Voronoi cells (eg. volume, centroid, number of faces) can be usedto analyze a system of particles.

http://math.lbl.gov/voro++/
# Available modules


The overview below shows which Voro++ installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Voro++, load one of these modules using a `module load` command like:

```shell
module load Voro++/0.4.6-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Voro++/0.4.6-GCCcore-13.2.0|x|x|x|x|x|x|x|x|x|x|
|Voro++/0.4.6-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|
