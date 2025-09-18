---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: MLflow is a platform to streamline machine learning development, including
    tracking experiments,packaging code into reproducible runs, and sharing and deploying
    models.
  license: Not confirmed
  name: MLflow
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
  softwareVersion: '[''MLflow/2.10.2-gfbf-2023a'', ''MLflow/2.18.0-gfbf-2023b'']'
  url: https://mlflow.org
---

MLflow
======


MLflow is a platform to streamline machine learning development, including tracking experiments,packaging code into reproducible runs, and sharing and deploying models.

https://mlflow.org
# Available modules


The overview below shows which MLflow installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using MLflow, load one of these modules using a `module load` command like:

```shell
module load MLflow/2.18.0-gfbf-2023b
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|MLflow/2.18.0-gfbf-2023b|x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|MLflow/2.10.2-gfbf-2023a|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### MLflow/2.18.0-gfbf-2023b

This is a list of extensions included in the module:

alembic-1.14.0, cachetools-5.5.0, databricks_sdk-0.36.0, docker-7.1.0, google-auth-2.35.0, graphene-3.4.1, graphql-relay-3.2.0, graphql_core-3.2.5, gunicorn-23.0.0, mlflow-2.18.0, mlflow_skinny-2.18.0, opentelemetry_api-1.27.0, opentelemetry_sdk-1.27.0, opentelemetry_semantic_conventions-0.48b0, pyasn1-modules-0.4.1, rsa-4.9, sqlparse-0.5.1

### MLflow/2.10.2-gfbf-2023a

This is a list of extensions included in the module:

docker-7.0.0, entrypoints-0.4, gunicorn-21.2.0, Markdown-3.5.2, mlflow-2.10.2, querystring_parser-1.2.4, sqlparse-0.4.4