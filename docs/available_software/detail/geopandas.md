---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: GeoPandas is a project to add support for geographic data to pandas
    objects.It currently implements GeoSeries and GeoDataFrame types which are subclasses
    of pandas.Seriesand pandas.DataFrame respectively. GeoPandas objects can act on
    shapely geometry objects andperform geometric operations.
  license: Not confirmed
  name: geopandas
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
  softwareVersion: '[''geopandas/0.14.2-foss-2023a'']'
  url: https://geopandas.org
---

geopandas
=========


GeoPandas is a project to add support for geographic data to pandas objects.It currently implements GeoSeries and GeoDataFrame types which are subclasses of pandas.Seriesand pandas.DataFrame respectively. GeoPandas objects can act on shapely geometry objects andperform geometric operations.

https://geopandas.org
# Available modules


The overview below shows which geopandas installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using geopandas, load one of these modules using a `module load` command like:

```shell
module load geopandas/0.14.2-foss-2023a
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|geopandas/0.14.2-foss-2023a|x|x|x|x|x|x|x|x|-|x|


### geopandas/0.14.2-foss-2023a

This is a list of extensions included in the module:

geopandas-0.14.2, mapclassify-2.6.1