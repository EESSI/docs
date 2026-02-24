# Greenlet


The greenlet package is a spin-off of Stackless, a version of CPython that
supports micro-threads called "tasklets". Tasklets run pseudo-concurrently (typically in a single
or a few OS-level threads) and are synchronized with data exchanges on "channels".
A "greenlet", on the other hand, is a still more primitive notion of micro-thread with no implicit
scheduling; coroutines, in other words. This is useful when you want to control exactly when your code runs.


<small>homepage: </small><span class="software-link">[https://github.com/python-greenlet/greenlet](https://github.com/python-greenlet/greenlet)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|3.0.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Greenlet/3.0.3-GCCcore-13.2.0`|
|3.1.1|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`Greenlet/3.1.1-GCCcore-13.3.0`|

## Extensions

Overview of extensions included in Greenlet installations
