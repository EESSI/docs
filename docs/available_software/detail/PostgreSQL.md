---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: PostgreSQL is a powerful, open source object-relational database system.
    It is fully ACID compliant, has full support for foreign keys, joins, views, triggers,
    and stored procedures (in multiple languages). It includes most SQL:2008 data
    types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and
    TIMESTAMP. It also supports storage of binary large objects, including pictures,
    sounds, or video. It has native programming interfaces for C/C++, Java, .Net,
    Perl, Python, Ruby, Tcl, ODBC, among others, and exceptional documentation.
  license: Not confirmed
  name: PostgreSQL
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
  softwareVersion: '[''PostgreSQL/16.1-GCCcore-12.3.0'', ''PostgreSQL/16.1-GCCcore-13.2.0'']'
  url: https://www.postgresql.org/
---

PostgreSQL
==========


PostgreSQL is a powerful, open source object-relational database system. It is fully ACID compliant, has full support for foreign keys, joins, views, triggers, and stored procedures (in multiple languages). It includes most SQL:2008 data types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and TIMESTAMP. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others, and exceptional documentation.

https://www.postgresql.org/
# Available modules


The overview below shows which PostgreSQL installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using PostgreSQL, load one of these modules using a `module load` command like:

```shell
module load PostgreSQL/16.1-GCCcore-13.2.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|aarch64/nvidia/grace|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PostgreSQL/16.1-GCCcore-13.2.0|x|x|x|-|x|x|x|x|x|x|x|x|
|PostgreSQL/16.1-GCCcore-12.3.0|x|x|x|-|x|x|x|x|x|x|x|x|
