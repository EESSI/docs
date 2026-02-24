# minimap2


Minimap2 is a fast sequence mapping and alignment
program that can find overlaps between long noisy reads, or map long
reads or their assemblies to a reference genome optionally with detailed
alignment (i.e. CIGAR). At present, it works efficiently with query
sequences from a few kilobases to ~100 megabases in length at an error
rate ~15%. Minimap2 outputs in the PAF or the SAM format. On limited
test data sets, minimap2 is over 20 times faster than most other
long-read aligners. It will replace BWA-MEM for long reads and contig
alignment.

<small>homepage: </small><span class="software-link">[https://github.com/lh3/minimap2](https://github.com/lh3/minimap2)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2.30|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`minimap2/2.30-GCCcore-14.3.0`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://github.com/lh3/minimap2', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'GCCcore', 'version': '14.3.0'}, 'toolchain_families_compatibility': ['2025b_foss'], 'module': {'full_module_name': 'minimap2/2.30-GCCcore-14.3.0', 'module_name': 'minimap2', 'module_version': '2.30-GCCcore-14.3.0'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/14.3.0', 'module_name': 'GCCcore', 'module_version': '14.3.0'}, {'full_module_name': 'minimap2/2.30-GCCcore-14.3.0', 'module_name': 'minimap2', 'module_version': '2.30-GCCcore-14.3.0'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Minimap2 is a fast sequence mapping and alignment\nprogram that can find overlaps between long noisy reads, or map long\nreads or their assemblies to a reference genome optionally with detailed\nalignment (i.e. CIGAR). At present, it works efficiently with query\nsequences from a few kilobases to ~100 megabases in length at an error\nrate ~15%. Minimap2 outputs in the PAF or the SAM format. On limited\ntest data sets, minimap2 is over 20 times faster than most other\nlong-read aligners. It will replace BWA-MEM for long reads and contig\nalignment.', 'version': '2.30', 'versionsuffix': '', 'extensions': []}], 'homepage': 'https://github.com/lh3/minimap2', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'Minimap2 is a fast sequence mapping and alignment\nprogram that can find overlaps between long noisy reads, or map long\nreads or their assemblies to a reference genome optionally with detailed\nalignment (i.e. CIGAR). At present, it works efficiently with query\nsequences from a few kilobases to ~100 megabases in length at an error\nrate ~15%. Minimap2 outputs in the PAF or the SAM format. On limited\ntest data sets, minimap2 is over 20 times faster than most other\nlong-read aligners. It will replace BWA-MEM for long reads and contig\nalignment.'} installations
