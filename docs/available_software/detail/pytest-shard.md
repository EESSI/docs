# pytest-shard


pytest plugin to support parallelism across multiple machines.

Shards tests based on a hash of their test name enabling easy parallelism across machines,
suitable for a wide variety of continuous integration services.
Tests are split at the finest level of granularity, individual test cases,
enabling parallelism even if all of your tests are in a single file
(or even single parameterized test method).


<small>homepage: </small><span class="software-link">[https://github.com/AdamGleave/pytest-shard](https://github.com/AdamGleave/pytest-shard)</span>

## Available installations


|pytest-shard version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`pytest-shard/0.1.2-GCCcore-12.3.0`|
|0.1.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`pytest-shard/0.1.2-GCCcore-13.3.0`|