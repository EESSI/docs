# enchant-2


Enchant aims to provide a simple but comprehensive abstraction for dealing
with different spell checking libraries in a consistent way. A client, such
as a text editor or word processor, need not know anything about a specific
spell-checker, and since all back-ends are plugins, new spell-checkers can
be added without needing any change to the program using Enchant.

<small>homepage: </small><span class="software-link">[http://rrthomas.github.io/enchant/](http://rrthomas.github.io/enchant/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.6.5|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`enchant-2/2.6.5-GCCcore-12.3.0`|