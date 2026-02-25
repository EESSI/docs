# PyTables


PyTables is a package for managing hierarchical datasets and designed to efficiently and easily cope
 with extremely large amounts of data. PyTables is built on top of the HDF5 library, using the Python language and the
 NumPy package. It features an object-oriented interface that, combined with C extensions for the performance-critical
 parts of the code (generated using Cython), makes it a fast, yet extremely easy to use tool for interactively browsing,
 processing and searching very large amounts of data. One important feature of PyTables is that it optimizes memory and
 disk resources so that data takes much less space (specially if on-flight compression is used) than other solutions
 such as relational or object oriented databases.

<small>homepage: </small><span class="software-link">[https://www.pytables.org](https://www.pytables.org)</span>

## Available installations


|PyTables version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.9.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`PyTables/3.9.2-foss-2023b`|

## Extensions

Overview of extensions included in PyTables installations


### blosc2


|`blosc2` version|PyTables modules that include it|
| --- | --- |
|2.5.1|`PyTables/3.9.2-foss-2023b`|

### ndindex


|`ndindex` version|PyTables modules that include it|
| --- | --- |
|1.8|`PyTables/3.9.2-foss-2023b`|

### tables


|`tables` version|PyTables modules that include it|
| --- | --- |
|3.9.2|`PyTables/3.9.2-foss-2023b`|