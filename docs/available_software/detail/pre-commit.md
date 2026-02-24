# pre-commit


A framework for managing and maintaining multi-language pre-commit hooks.

Git hook scripts are useful for identifying simple issues before submission to code review.
 We run our hooks on every commit to automatically point out issues in code such as missing semicolons,
 trailing whitespace, and debug statements. By pointing these issues out before code review,
 this allows a code reviewer to focus on the architecture of a change while not wasting time
 with trivial style nitpicks.

<small>homepage: </small><span class="software-link">[https://pre-commit.com/](https://pre-commit.com/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|3.7.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`pre-commit/3.7.0-GCCcore-13.2.0`|

## Extensions

Overview of extensions included in pre-commit installations


### cfgv


|`cfgv` version|pre-commit modules that include it|
| --- | --- |
|3.4.0|`pre-commit/3.7.0-GCCcore-13.2.0`|

### identify


|`identify` version|pre-commit modules that include it|
| --- | --- |
|2.5.35|`pre-commit/3.7.0-GCCcore-13.2.0`|

### nodeenv


|`nodeenv` version|pre-commit modules that include it|
| --- | --- |
|1.8.0|`pre-commit/3.7.0-GCCcore-13.2.0`|

### pre-commit


|`pre-commit` version|pre-commit modules that include it|
| --- | --- |
|3.7.0|`pre-commit/3.7.0-GCCcore-13.2.0`|