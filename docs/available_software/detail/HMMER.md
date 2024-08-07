---
hide:
  - toc
---

HMMER
=====


HMMER is used for searching sequence databases for homologs of protein sequences, and for making protein sequence alignments. It implements methods using probabilistic models called profile hidden Markov models (profile HMMs).  Compared to BLAST, FASTA, and other sequence alignment and database search tools based on older scoring methodology, HMMER aims to be significantly more accurate and more able to detect remote homologs because of the strength of its underlying mathematical models. In the past, this strength came at significant computational expense, but in the new HMMER3 project, HMMER is now essentially as fast as BLAST.

http://hmmer.org/
# Available modules


The overview below shows which HMMER installations are available per target architecture in EESSI, ordered based on software version (new to old).

To start using HMMER, load one of these modules using a `module load` command like:

```shell
module load HMMER/3.4-gompi-2023a
```

*(This data was automatically generated on Wed, 07 Aug 2024 at 12:36:59 UTC)*  

| |aarch64/generic|aarch64/neoverse_n1|aarch64/neoverse_v1|x86_64/generic|x86_64/amd/zen2|x86_64/amd/zen3|x86_64/amd/zen4|x86_64/intel/haswell|x86_64/intel/skylake_avx512|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|HMMER/3.4-gompi-2023a|x|x|x|x|x|x|x|x|x|
