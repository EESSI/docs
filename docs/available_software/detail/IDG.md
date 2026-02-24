# IDG


Image Domain Gridding (IDG) is a fast method for convolutional resampling (gridding/degridding)
of radio astronomical data (visibilities). Direction dependent effects (DDEs) or A-tems can be applied
in the gridding process.
The algorithm is described in "Image Domain Gridding: a fast method for convolutional resampling of visibilities",
Van der Tol (2018).
The implementation is described in "Radio-astronomical imaging on graphics processors", Veenboer (2020).
Please cite these papers in publications using IDG.


<small>homepage: </small><span class="software-link">[https://idg.readthedocs.io/](https://idg.readthedocs.io/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|1.2.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`IDG/1.2.0-foss-2023b`|

## Extensions

Overview of extensions included in IDG installations
