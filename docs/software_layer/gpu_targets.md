---
hide:
  - toc
---

# GPU targets

## NVIDIA

Each version of EESSI includes optimized software installations for a selected range of major NVIDIA GPU CUDA Compute Capabilities,
for all CPU targets listed in [CPU targets](cpu_targets.md).

NVIDIA guarantees forward compatibility within a major CUDA Compute Capability, i.e. a GPU with CUDA Compute Capability 8.6 can run code built for CUDA Compute Capability 8.0.
This means that a given EESSI version supports all NVIDIA GPUs with Compute Capability X.Y if the table below includes support for Compute Capability X.0.
On the [NVIDIA website](https://developer.nvidia.com/cuda/gpus) you can find the Compute Capability of your GPU.

The decision to only ship code optimized for the major GPU architectures was made to keep the number of software builds that need to be done at a reasonable level.
Even just building for three major CUDA Compute Capabilities for all CPU targets supported by EESSI version 2023.06 would require 39 builds in total (13 CPU targets times 3 GPU targets).

Not all builds are done natively, i.e. on a system actually containing a CPU and GPU of the type that is being built for.

The table below shows an overview of the supported CPU/GPU architectures for the different EESSI versions (marked with `x`).
The combinations marked with an '`N`' are built natively; others are built on a CPU-only system.

<table>
    <thead>
        <tr>
            <th colspan=3></th>
            <th colspan=5><div align="center">CUDA compute capability</div></th>
        </tr>
        <tr>
            <th colspan=3><div align="center">CPU microarchitecture</div></th>
            <th>7.0</th>
            <th>8.0</th>
            <th>9.0</th>
            <th>10.0</th>
            <th>12.0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=5>aarch64</td>
            <td colspan=2>generic</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td colspan=2>a64fx</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td colspan=2>neoverse_n1</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td colspan=2>neoverse_v1</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>nvidia</td>
            <td>grace</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: N</span><span class="software-eessi-version-202506">2025.06: N</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td colspan=8></td>
        </tr>
        <tr>
            <td rowspan=10>x86_64</td>
            <td colspan=2>generic</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td rowspan=5>intel</td>
            <td>haswell</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>skylake_avx512</td>
            <td><span class="software-eessi-version-202306">2023.06: N</span><span class="software-eessi-version-202506">2025.06: N</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>cascadelake</td>
            <td><span class="software-eessi-version-202306">2023.06: N</span><span class="software-eessi-version-202506">2025.06: N</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>icelake</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: N</span><span class="software-eessi-version-202506">2025.06: N</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>sapphirerapids</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td rowspan=4>amd</td>
            <td>zen2</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>zen3</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: N</span><span class="software-eessi-version-202506">2025.06: N</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>zen4</td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: x</span><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202306">2023.06: N</span><span class="software-eessi-version-202506">2025.06: N</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
        </tr>
        <tr>
            <td>zen5</td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: x</span></td>
            <td><span class="software-eessi-version-202506">2025.06: N</span></td>
        </tr>
    </tbody>
</table>

!!! info "No NVIDIA GPU support for A64FX"
    Note that there is no NVIDIA GPU support for A64FX at the moment, as we are not aware of any systems with A64FX CPUs and NVIDIA GPUs.

## AMD

Support for AMD GPUs is a work in progress ([see recent blog post](../blog/posts/2025/08/eessi-rocm.md)).
