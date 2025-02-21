---
hide:
- toc
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'tmux is a terminal multiplexer: it enables a number ofterminals to
    be created, accessed, and controlled from a single screen. tmuxmay be detached
    from a screen and continue running in the background, thenlater reattached.'
  license: Not confirmed
  name: tmux
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
  softwareVersion: '[''tmux/3.3a-GCCcore-12.3.0'']'
  url: https://github.com/tmux/tmux/
---

tmux
====


tmux is a terminal multiplexer: it enables a number ofterminals to be created, accessed, and controlled from a single screen. tmuxmay be detached from a screen and continue running in the background, thenlater reattached.

https://github.com/tmux/tmux/
# Available modules


The overview below shows which tmux installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using tmux, load one of these modules using a `module load` command like:

```shell
module load tmux/3.3a-GCCcore-12.3.0
```

*(This data was automatically generated on {{ generated_time }})*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/sapphirerapids|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|tmux/3.3a-GCCcore-12.3.0|x|x|x|x|x|x|x|x|-|x|
