---
hide:
  - toc
---
{% set eessi_202306_n = '<span class="software-eessi-version-202306">2023.06: N</span>' %}
{% set eessi_202306_x = '<span class="software-eessi-version-202306">2023.06: x</span>' %}
{% set eessi_202506_n = '<span class="software-eessi-version-202506">2025.06: N</span>' %}
{% set eessi_202506_x = '<span class="software-eessi-version-202506">2025.06: x</span>' %}

# GPU targets

## NVIDIA

Each version of EESSI includes optimized software installations for a selected range of major NVIDIA GPU CUDA Compute Capabilities,
for all CPU targets listed in [CPU targets](cpu_targets.md).

NVIDIA guarantees forward compatibility within a major CUDA Compute Capability, i.e. a GPU with CUDA Compute Capability 8.6 can run code built for CUDA Compute Capability 8.0.
This means that a given EESSI version supports all NVIDIA GPUs with Compute Capability X.Y if the table below includes support for Compute Capability X.0.
On the [NVIDIA website](https://developer.nvidia.com/cuda/gpus) you can find the Compute Capability of your GPU.

The decision to only ship code optimized for the major GPU architectures was made to keep the number of software builds that need to be done at a reasonable level.
Even just building a single application for five major CUDA Compute Capabilities for all CPU targets supported by EESSI version 2025.06 would require 75 builds in total (15 CPU targets times 5 GPU targets).

Not all builds are done natively, i.e. on a system actually containing a CPU and GPU of the type that is being built for.

The table below shows an overview of the supported CPU/GPU architectures for the different EESSI versions (marked with `x`).
The combinations marked with an '`N`' are built natively; others are built on a CPU-only system.

<table>
    <thead>
        <tr>
            <th></th>
            <th colspan=5><div align="center">CUDA compute capability</div></th>
        </tr>
        <tr>
            <th><div align="center">CPU microarchitecture</div></th>
            <th>7.0</th>
            <th>8.0</th>
            <th>9.0</th>
            <th>10.0</th>
            <th>12.0</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>aarch64/generic</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>aarch64/a64fx</code></td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
        </tr>
        <tr>
            <td><code>aarch64/neoverse_n1</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>aarch64/neoverse_v1</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>aarch64/nvidia/grace</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_n }} {{ eessi_202506_n }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td colspan=6></td>
        </tr>
        <tr>
            <td><code>x86_64/generic</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/intel/haswell</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/intel/skylake_avx512</code></td>
            <td>{{ eessi_202306_n }} {{ eessi_202506_n }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/intel/cascadelake</code></td>
            <td>{{ eessi_202306_n }} {{ eessi_202506_n }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/intel/icelake</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_n }} {{ eessi_202506_n }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/intel/sapphirerapids</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/amd/zen2</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/amd/zen3</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_n }} {{ eessi_202506_n }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/amd/zen4</code></td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_x }} {{ eessi_202506_x }}</td>
            <td>{{ eessi_202306_n }} {{ eessi_202506_n }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
        </tr>
        <tr>
            <td><code>x86_64/amd/zen5</code></td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_x }}</td>
            <td>{{ eessi_202506_n }}</td>
        </tr>
    </tbody>
</table>

!!! info "No NVIDIA GPU support for A64FX"
    Note that there is no NVIDIA GPU support for A64FX at the moment, as we are not aware of any systems with A64FX CPUs and NVIDIA GPUs.

## AMD

Support for AMD GPUs is a work in progress ([see recent blog post](../blog/posts/2025/08/eessi-rocm.md)).
