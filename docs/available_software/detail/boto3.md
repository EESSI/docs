---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: Boto3 is the Amazon Web Services (AWS) Software Development Kit(SDK)
    for Python, which allows Python developers to write software that makesuse of
    services like Amazon S3 and Amazon EC2.
  license: Not confirmed
  name: boto3
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
  softwareVersion: '[''boto3/1.28.70-GCCcore-12.3.0'']'
  url: https://github.com/boto/boto3
---

boto3
=====


Boto3 is the Amazon Web Services (AWS) Software Development Kit(SDK) for Python, which allows Python developers to write software that makesuse of services like Amazon S3 and Amazon EC2.

https://github.com/boto/boto3
# Available modules


The overview below shows which boto3 installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using boto3, load one of these modules using a `module load` command like:

```shell
module load boto3/1.28.70-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*

| |aarch64/generic|aarch64/a64fx|aarch64/neoverse_n1|aarch64/neoverse_v1|aarch64/nvidia/grace|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/cascadelake|x86_64/intel/haswell|x86_64/intel/icelake|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|boto3/1.28.70-GCCcore-12.3.0|x|x|x|x|x|x|x|x|x|x|x|x|x|x|


### boto3/1.28.70-GCCcore-12.3.0

This is a list of extensions included in the module:

boto3-1.28.70, botocore-1.31.70, jmespath-1.0.1, s3transfer-0.7.0