# Cereal


cereal is a header-only C++11 serialization library. cereal takes arbitrary data types and reversibly
turns them into different representations, such as compact binary encodings, XML, or JSON. cereal was designed to be
fast, light-weight, and easy to extend - it has no external dependencies and can be easily bundled with other code or
used standalone.

<small>homepage: </small><span class="software-link">[https://uscilab.github.io/cereal/](https://uscilab.github.io/cereal/)</span>

## Available installations


|Cereal version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.3.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Cereal/1.3.2`|