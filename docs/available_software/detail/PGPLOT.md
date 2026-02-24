# PGPLOT


The PGPLOT Graphics Subroutine Library is a Fortran- or C-callable,
device-independent graphics package for making simple scientific graphs. It is intended
for making graphical images of publication quality with minimum effort on the part of
the user. For most applications, the program can be device-independent, and the output
can be directed to the appropriate device at run time.

<small>homepage: </small><span class="software-link">[https://sites.astro.caltech.edu/~tjp/pgplot/](https://sites.astro.caltech.edu/~tjp/pgplot/)</span>

## Available installations


|PGPLOT version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|5.2.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`PGPLOT/5.2.2-GCCcore-13.2.0`|