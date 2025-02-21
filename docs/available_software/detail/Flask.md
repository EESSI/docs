---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Flask is a lightweight WSGI web application framework. It is designed
    to makegetting started quick and easy, with the ability to scale up to complexapplications.This
    module includes the Flask extensions: Flask-Cors'
  license: Not confirmed
  name: Flask
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
  softwareVersion: '[''Flask/2.2.3-GCCcore-12.2.0'']'
  url: https://www.palletsprojects.com/p/flask/
---

Flask
=====


Flask is a lightweight WSGI web application framework. It is designed to makegetting started quick and easy, with the ability to scale up to complexapplications.This module includes the Flask extensions: Flask-Cors

https://www.palletsprojects.com/p/flask/
# Available modules


The overview below shows which Flask installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Flask, load one of these modules using a `module load` command like:

```shell
module load Flask/2.2.3-GCCcore-12.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Flask/2.2.3-GCCcore-12.2.0|x|x|x|x|x|x|x|x|-|x|


### Flask/2.2.3-GCCcore-12.2.0

This is a list of extensions included in the module:

asgiref-3.6.0, cachelib-0.10.2, Flask-2.2.3, Flask-Cors-3.0.10, Flask-Session-0.4.0, itsdangerous-2.1.2, Werkzeug-2.2.3