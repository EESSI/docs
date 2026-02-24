# pkg-config



 pkg-config is a helper tool used when compiling applications and libraries.
 It helps you insert the correct compiler options on the command line so an
 application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
 for instance, rather than hard-coding values on where to find glib (or other
 libraries).


<small>homepage: </small><span class="software-link">[https://www.freedesktop.org/wiki/Software/pkg-config/](https://www.freedesktop.org/wiki/Software/pkg-config/)</span>

## Available installations


|pkg-config version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.29.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`pkg-config/0.29.2-GCCcore-12.3.0`|