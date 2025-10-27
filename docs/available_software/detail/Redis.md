---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Redis is an open source (BSD licensed), in-memory data structure store,
    used asa database, cache, and message broker. Redis provides data structures such
    asstrings, hashes, lists, sets, sorted sets with range queries, bitmaps,hyperloglogs,
    geospatial indexes, and streams. Redis has built-in replication,Lua scripting,
    LRU eviction, transactions, and different levels of on-diskpersistence, and provides
    high availability via Redis Sentinel and automaticpartitioning with Redis Cluster.
  license: Not confirmed
  name: Redis
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
  softwareVersion: '[''Redis/7.2.3-GCCcore-12.3.0'']'
  url: https://redis.io
---

Redis
=====


Redis is an open source (BSD licensed), in-memory data structure store, used asa database, cache, and message broker. Redis provides data structures such asstrings, hashes, lists, sets, sorted sets with range queries, bitmaps,hyperloglogs, geospatial indexes, and streams. Redis has built-in replication,Lua scripting, LRU eviction, transactions, and different levels of on-diskpersistence, and provides high availability via Redis Sentinel and automaticpartitioning with Redis Cluster.

https://redis.io
# Available modules


The overview below shows which Redis installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using Redis, load one of these modules using a `module load` command like:

```shell
module load Redis/7.2.3-GCCcore-12.3.0
```

*(This data was automatically generated on Wed, 22 Oct 2025 at 15:10:37 CEST)*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Redis/7.2.3-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
