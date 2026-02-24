# Check



Check is a unit testing framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are
run in a separate address space, so both assertion failures and code errors
that cause segmentation faults or other signals can be caught. Test results
are reportable in the following: Subunit, TAP, XML, and a generic logging
format.

<small>homepage: </small><span class="software-link">[https://libcheck.github.io/check/](https://libcheck.github.io/check/)</span>

## Available installations


|Check version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.15.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Check/0.15.2-GCCcore-14.2.0`|
|0.15.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Check/0.15.2-GCCcore-14.3.0`|