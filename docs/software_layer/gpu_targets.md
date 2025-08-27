# GPU targets

## NVIDIA

EESSI includes optimized software installations for major NVIDIA GPU CUDA Compute Capabilities 7.0, 8.0 and 9.0, for all CPU targets listed in [CPU targets](cpu_targets.md).

NVIDIA guarantees forwards compatibility within a major CUDA Compute Capability (i.e. a GPU with CUDA Compute Capability 8.6 can run code built for CUDA Compute Capability 8.0).
This means that all NVIDIA GPUs with Compute Capability 7.x, 8.x and 9.x are supported (see also [here](https://developer.nvidia.com/cuda-gpus)).

The decision to only ship code optimized for the major GPU architectures was made to keep the amount of software builds that need to be done at a reasonable level.
Even just building for the major CUDA Compute Capabilities for all CPU targets currently requires 39 builds (13 CPU targets times 3 GPU targets).

Not all builds are done natively, i.e. on a system actually containing a CPU and GPU of the type that is being built for.

The table below shows an overview of the supported CPU/GPU architectures (marked with `x`).
The combinations marked with an '`N`' are built natively; others are built on a CPU-only system.

<table>
    <thead>
        <tr>
            <th colspan=3></th>
            <th colspan=3><div align="center">CUDA compute capability</div></th>
        </tr>
        <tr>
            <th colspan=3><div align="center">CPU microarchitecture</div></th>
            <th>7.0</th>
            <th>8.0</th>
            <th>9.0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>aarch64</td>
            <td colspan=2>generic</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td colspan=2>neoverse_n1</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td colspan=2>neoverse_v1</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td>nvidia</td>
            <td>grace</td>
            <td>x</td>
            <td>x</td>
            <td>N</td>
        </tr>
        <tr>
            <td colspan=6></td>
        </tr>
        <tr>
            <td rowspan=9>x86_64</td>
            <td colspan=2>generic</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td rowspan=5>intel</td>
            <td>haswell</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td>skylake_avx512</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td>cascadelake</td>
            <td>N</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td>icelake</td>
            <td>x</td>
            <td>N</td>
            <td>x</td>
        </tr>
        <tr>
            <td>sapphirerapids</td>
            <td>x</td>
            <td>x</td>
            <td>x</td>
        </tr>
        <tr>
            <td rowspan=3>amd</td>
            <td>zen2</td>
            <td>x</td>
            <td>N</td>
            <td>x</td>
        </tr>
        <tr>
            <td>zen3</td>
            <td>x</td>
            <td>N</td>
            <td>x</td>
        </tr>
        <tr>
            <td>zen4</td>
            <td>x</td>
            <td>x</td>
            <td>N</td>
        </tr>
    </tbody>
</table>

## AMD

Support for AMD GPUs is a work in progress ([see recent blog post](../blog/posts/2025/08/eessi-rocm.md)).
