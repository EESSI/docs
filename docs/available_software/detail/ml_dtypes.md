# ml_dtypes



ml_dtypes is a stand-alone implementation of several NumPy dtype extensions used
in machine learning libraries, including:

bfloat16: an alternative to the standard float16 format
float8_*: several experimental 8-bit floating point representations including:
float8_e4m3b11fnuz
float8_e4m3fn
float8_e4m3fnuz
float8_e5m2
float8_e5m2fnuz


<small>homepage: </small><span class="software-link">[https://github.com/jax-ml/ml_dtypes](https://github.com/jax-ml/ml_dtypes)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|0.3.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`ml_dtypes/0.3.2-gfbf-2023a`|

## Extensions

Overview of extensions included in ml_dtypes installations


### etils


|`etils` version|ml_dtypes modules that include it|
| --- | --- |
|1.6.0|`ml_dtypes/0.3.2-gfbf-2023a`|

### ml_dtypes


|`ml_dtypes` version|ml_dtypes modules that include it|
| --- | --- |
|0.3.2|`ml_dtypes/0.3.2-gfbf-2023a`|

### opt_einsum


|`opt_einsum` version|ml_dtypes modules that include it|
| --- | --- |
|3.3.0|`ml_dtypes/0.3.2-gfbf-2023a`|