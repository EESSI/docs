# R-bundle-Bioconductor


Bioconductor provides tools for the analysis and coprehension
 of high-throughput genomic data.

<small>homepage: </small><span class="software-link">[https://bioconductor.org](https://bioconductor.org)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|3.16|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://bioconductor.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2022b'}, 'toolchain_families_compatibility': ['2022b_foss'], 'module': {'full_module_name': 'R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2', 'module_name': 'R-bundle-Bioconductor', 'module_version': '3.16-foss-2022b-R-4.2.2'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.2.0', 'module_name': 'GCCcore', 'module_version': '12.2.0'}, {'full_module_name': 'GCC/12.2.0', 'module_name': 'GCC', 'module_version': '12.2.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.2.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.2.0'}, {'full_module_name': 'libxml2/2.10.3-GCCcore-12.2.0', 'module_name': 'libxml2', 'module_version': '2.10.3-GCCcore-12.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.2.0'}, {'full_module_name': 'hwloc/2.8.0-GCCcore-12.2.0', 'module_name': 'hwloc', 'module_version': '2.8.0-GCCcore-12.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.2.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.2.0'}, {'full_module_name': 'UCX/1.13.1-GCCcore-12.2.0', 'module_name': 'UCX', 'module_version': '1.13.1-GCCcore-12.2.0'}, {'full_module_name': 'libfabric/1.16.1-GCCcore-12.2.0', 'module_name': 'libfabric', 'module_version': '1.16.1-GCCcore-12.2.0'}, {'full_module_name': 'PMIx/4.2.2-GCCcore-12.2.0', 'module_name': 'PMIx', 'module_version': '4.2.2-GCCcore-12.2.0'}, {'full_module_name': 'UCC/1.1.0-GCCcore-12.2.0', 'module_name': 'UCC', 'module_version': '1.1.0-GCCcore-12.2.0'}, {'full_module_name': 'OpenMPI/4.1.4-GCC-12.2.0', 'module_name': 'OpenMPI', 'module_version': '4.1.4-GCC-12.2.0'}, {'full_module_name': 'OpenBLAS/0.3.21-GCC-12.2.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.21-GCC-12.2.0'}, {'full_module_name': 'FlexiBLAS/3.2.1-GCC-12.2.0', 'module_name': 'FlexiBLAS', 'module_version': '3.2.1-GCC-12.2.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.2.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.2.0'}, {'full_module_name': 'gompi/2022b', 'module_name': 'gompi', 'module_version': '2022b'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2022b', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2022b'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2022b-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2022b-fb'}, {'full_module_name': 'foss/2022b', 'module_name': 'foss', 'module_version': '2022b'}, {'full_module_name': 'expat/2.4.9-GCCcore-12.2.0', 'module_name': 'expat', 'module_version': '2.4.9-GCCcore-12.2.0'}, {'full_module_name': 'libpng/1.6.38-GCCcore-12.2.0', 'module_name': 'libpng', 'module_version': '1.6.38-GCCcore-12.2.0'}, {'full_module_name': 'Brotli/1.0.9-GCCcore-12.2.0', 'module_name': 'Brotli', 'module_version': '1.0.9-GCCcore-12.2.0'}, {'full_module_name': 'freetype/2.12.1-GCCcore-12.2.0', 'module_name': 'freetype', 'module_version': '2.12.1-GCCcore-12.2.0'}, {'full_module_name': 'fontconfig/2.14.1-GCCcore-12.2.0', 'module_name': 'fontconfig', 'module_version': '2.14.1-GCCcore-12.2.0'}, {'full_module_name': 'xorg-macros/1.19.3-GCCcore-12.2.0', 'module_name': 'xorg-macros', 'module_version': '1.19.3-GCCcore-12.2.0'}, {'full_module_name': 'X11/20221110-GCCcore-12.2.0', 'module_name': 'X11', 'module_version': '20221110-GCCcore-12.2.0'}, {'full_module_name': 'gzip/1.12-GCCcore-12.2.0', 'module_name': 'gzip', 'module_version': '1.12-GCCcore-12.2.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-12.2.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-12.2.0'}, {'full_module_name': 'zstd/1.5.2-GCCcore-12.2.0', 'module_name': 'zstd', 'module_version': '1.5.2-GCCcore-12.2.0'}, {'full_module_name': 'libdrm/2.4.114-GCCcore-12.2.0', 'module_name': 'libdrm', 'module_version': '2.4.114-GCCcore-12.2.0'}, {'full_module_name': 'libglvnd/1.6.0-GCCcore-12.2.0', 'module_name': 'libglvnd', 'module_version': '1.6.0-GCCcore-12.2.0'}, {'full_module_name': 'libunwind/1.6.2-GCCcore-12.2.0', 'module_name': 'libunwind', 'module_version': '1.6.2-GCCcore-12.2.0'}, {'full_module_name': 'LLVM/15.0.5-GCCcore-12.2.0', 'module_name': 'LLVM', 'module_version': '15.0.5-GCCcore-12.2.0'}, {'full_module_name': 'Mesa/22.2.4-GCCcore-12.2.0', 'module_name': 'Mesa', 'module_version': '22.2.4-GCCcore-12.2.0'}, {'full_module_name': 'libGLU/9.0.2-GCCcore-12.2.0', 'module_name': 'libGLU', 'module_version': '9.0.2-GCCcore-12.2.0'}, {'full_module_name': 'pixman/0.42.2-GCCcore-12.2.0', 'module_name': 'pixman', 'module_version': '0.42.2-GCCcore-12.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.2.0'}, {'full_module_name': 'PCRE2/10.40-GCCcore-12.2.0', 'module_name': 'PCRE2', 'module_version': '10.40-GCCcore-12.2.0'}, {'full_module_name': 'GLib/2.75.0-GCCcore-12.2.0', 'module_name': 'GLib', 'module_version': '2.75.0-GCCcore-12.2.0'}, {'full_module_name': 'cairo/1.17.4-GCCcore-12.2.0', 'module_name': 'cairo', 'module_version': '1.17.4-GCCcore-12.2.0'}, {'full_module_name': 'Tcl/8.6.12-GCCcore-12.2.0', 'module_name': 'Tcl', 'module_version': '8.6.12-GCCcore-12.2.0'}, {'full_module_name': 'SQLite/3.39.4-GCCcore-12.2.0', 'module_name': 'SQLite', 'module_version': '3.39.4-GCCcore-12.2.0'}, {'full_module_name': 'NASM/2.15.05-GCCcore-12.2.0', 'module_name': 'NASM', 'module_version': '2.15.05-GCCcore-12.2.0'}, {'full_module_name': 'libjpeg-turbo/2.1.4-GCCcore-12.2.0', 'module_name': 'libjpeg-turbo', 'module_version': '2.1.4-GCCcore-12.2.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-12.2.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-12.2.0'}, {'full_module_name': 'libdeflate/1.15-GCCcore-12.2.0', 'module_name': 'libdeflate', 'module_version': '1.15-GCCcore-12.2.0'}, {'full_module_name': 'LibTIFF/4.4.0-GCCcore-12.2.0', 'module_name': 'LibTIFF', 'module_version': '4.4.0-GCCcore-12.2.0'}, {'full_module_name': 'Java/11.0.27', 'module_name': 'Java', 'module_version': '11.0.27'}, {'full_module_name': 'Java/11', 'module_name': 'Java', 'module_version': '11'}, {'full_module_name': 'Tk/8.6.12-GCCcore-12.2.0', 'module_name': 'Tk', 'module_version': '8.6.12-GCCcore-12.2.0'}, {'full_module_name': 'cURL/7.86.0-GCCcore-12.2.0', 'module_name': 'cURL', 'module_version': '7.86.0-GCCcore-12.2.0'}, {'full_module_name': 'GMP/6.2.1-GCCcore-12.2.0', 'module_name': 'GMP', 'module_version': '6.2.1-GCCcore-12.2.0'}, {'full_module_name': 'NLopt/2.7.1-GCCcore-12.2.0', 'module_name': 'NLopt', 'module_version': '2.7.1-GCCcore-12.2.0'}, {'full_module_name': 'libogg/1.3.5-GCCcore-12.2.0', 'module_name': 'libogg', 'module_version': '1.3.5-GCCcore-12.2.0'}, {'full_module_name': 'FLAC/1.4.2-GCCcore-12.2.0', 'module_name': 'FLAC', 'module_version': '1.4.2-GCCcore-12.2.0'}, {'full_module_name': 'libvorbis/1.3.7-GCCcore-12.2.0', 'module_name': 'libvorbis', 'module_version': '1.3.7-GCCcore-12.2.0'}, {'full_module_name': 'libopus/1.3.1-GCCcore-12.2.0', 'module_name': 'libopus', 'module_version': '1.3.1-GCCcore-12.2.0'}, {'full_module_name': 'LAME/3.100-GCCcore-12.2.0', 'module_name': 'LAME', 'module_version': '3.100-GCCcore-12.2.0'}, {'full_module_name': 'libsndfile/1.2.0-GCCcore-12.2.0', 'module_name': 'libsndfile', 'module_version': '1.2.0-GCCcore-12.2.0'}, {'full_module_name': 'ICU/72.1-GCCcore-12.2.0', 'module_name': 'ICU', 'module_version': '72.1-GCCcore-12.2.0'}, {'full_module_name': 'Szip/2.1.1-GCCcore-12.2.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-12.2.0'}, {'full_module_name': 'HDF5/1.14.0-gompi-2022b', 'module_name': 'HDF5', 'module_version': '1.14.0-gompi-2022b'}, {'full_module_name': 'UDUNITS/2.2.28-GCCcore-12.2.0', 'module_name': 'UDUNITS', 'module_version': '2.2.28-GCCcore-12.2.0'}, {'full_module_name': 'GSL/2.7-GCC-12.2.0', 'module_name': 'GSL', 'module_version': '2.7-GCC-12.2.0'}, {'full_module_name': 'ATK/2.38.0-GCCcore-12.2.0', 'module_name': 'ATK', 'module_version': '2.38.0-GCCcore-12.2.0'}, {'full_module_name': 'at-spi2-core/2.46.0-GCCcore-12.2.0', 'module_name': 'at-spi2-core', 'module_version': '2.46.0-GCCcore-12.2.0'}, {'full_module_name': 'at-spi2-atk/2.38.0-GCCcore-12.2.0', 'module_name': 'at-spi2-atk', 'module_version': '2.38.0-GCCcore-12.2.0'}, {'full_module_name': 'Gdk-Pixbuf/2.42.10-GCCcore-12.2.0', 'module_name': 'Gdk-Pixbuf', 'module_version': '2.42.10-GCCcore-12.2.0'}, {'full_module_name': 'HarfBuzz/5.3.1-GCCcore-12.2.0', 'module_name': 'HarfBuzz', 'module_version': '5.3.1-GCCcore-12.2.0'}, {'full_module_name': 'FriBidi/1.0.12-GCCcore-12.2.0', 'module_name': 'FriBidi', 'module_version': '1.0.12-GCCcore-12.2.0'}, {'full_module_name': 'Pango/1.50.12-GCCcore-12.2.0', 'module_name': 'Pango', 'module_version': '1.50.12-GCCcore-12.2.0'}, {'full_module_name': 'libepoxy/1.5.10-GCCcore-12.2.0', 'module_name': 'libepoxy', 'module_version': '1.5.10-GCCcore-12.2.0'}, {'full_module_name': 'GTK3/3.24.35-GCCcore-12.2.0', 'module_name': 'GTK3', 'module_version': '3.24.35-GCCcore-12.2.0'}, {'full_module_name': 'Ghostscript/10.0.0-GCCcore-12.2.0', 'module_name': 'Ghostscript', 'module_version': '10.0.0-GCCcore-12.2.0'}, {'full_module_name': 'JasPer/4.0.0-GCCcore-12.2.0', 'module_name': 'JasPer', 'module_version': '4.0.0-GCCcore-12.2.0'}, {'full_module_name': 'LittleCMS/2.14-GCCcore-12.2.0', 'module_name': 'LittleCMS', 'module_version': '2.14-GCCcore-12.2.0'}, {'full_module_name': 'ImageMagick/7.1.0-53-GCCcore-12.2.0', 'module_name': 'ImageMagick', 'module_version': '7.1.0-53-GCCcore-12.2.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-12.2.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-12.2.0'}, {'full_module_name': 'nodejs/18.12.1-GCCcore-12.2.0', 'module_name': 'nodejs', 'module_version': '18.12.1-GCCcore-12.2.0'}, {'full_module_name': 'Python/3.10.8-GCCcore-12.2.0', 'module_name': 'Python', 'module_version': '3.10.8-GCCcore-12.2.0'}, {'full_module_name': 'netCDF/4.9.0-gompi-2022b', 'module_name': 'netCDF', 'module_version': '4.9.0-gompi-2022b'}, {'full_module_name': 'GEOS/3.11.1-GCC-12.2.0', 'module_name': 'GEOS', 'module_version': '3.11.1-GCC-12.2.0'}, {'full_module_name': 'PCRE/8.45-GCCcore-12.2.0', 'module_name': 'PCRE', 'module_version': '8.45-GCCcore-12.2.0'}, {'full_module_name': 'nlohmann_json/3.11.2-GCCcore-12.2.0', 'module_name': 'nlohmann_json', 'module_version': '3.11.2-GCCcore-12.2.0'}, {'full_module_name': 'PROJ/9.1.1-GCCcore-12.2.0', 'module_name': 'PROJ', 'module_version': '9.1.1-GCCcore-12.2.0'}, {'full_module_name': 'libgeotiff/1.7.1-GCCcore-12.2.0', 'module_name': 'libgeotiff', 'module_version': '1.7.1-GCCcore-12.2.0'}, {'full_module_name': 'gfbf/2022b', 'module_name': 'gfbf', 'module_version': '2022b'}, {'full_module_name': 'pybind11/2.10.3-GCCcore-12.2.0', 'module_name': 'pybind11', 'module_version': '2.10.3-GCCcore-12.2.0'}, {'full_module_name': 'SciPy-bundle/2023.02-gfbf-2022b', 'module_name': 'SciPy-bundle', 'module_version': '2023.02-gfbf-2022b'}, {'full_module_name': 'libtirpc/1.3.3-GCCcore-12.2.0', 'module_name': 'libtirpc', 'module_version': '1.3.3-GCCcore-12.2.0'}, {'full_module_name': 'HDF/4.2.15-GCCcore-12.2.0', 'module_name': 'HDF', 'module_version': '4.2.15-GCCcore-12.2.0'}, {'full_module_name': 'Boost/1.81.0-GCC-12.2.0', 'module_name': 'Boost', 'module_version': '1.81.0-GCC-12.2.0'}, {'full_module_name': 'arpack-ng/3.8.0-foss-2022b', 'module_name': 'arpack-ng', 'module_version': '3.8.0-foss-2022b'}, {'full_module_name': 'Armadillo/11.4.3-foss-2022b', 'module_name': 'Armadillo', 'module_version': '11.4.3-foss-2022b'}, {'full_module_name': 'CFITSIO/4.2.0-GCCcore-12.2.0', 'module_name': 'CFITSIO', 'module_version': '4.2.0-GCCcore-12.2.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-12.2.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-12.2.0'}, {'full_module_name': 'json-c/0.16-GCCcore-12.2.0', 'module_name': 'json-c', 'module_version': '0.16-GCCcore-12.2.0'}, {'full_module_name': 'Xerces-C++/3.2.4-GCCcore-12.2.0', 'module_name': 'Xerces-C++', 'module_version': '3.2.4-GCCcore-12.2.0'}, {'full_module_name': 'Imath/3.1.6-GCCcore-12.2.0', 'module_name': 'Imath', 'module_version': '3.1.6-GCCcore-12.2.0'}, {'full_module_name': 'OpenEXR/3.1.5-GCCcore-12.2.0', 'module_name': 'OpenEXR', 'module_version': '3.1.5-GCCcore-12.2.0'}, {'full_module_name': 'Highway/1.0.3-GCCcore-12.2.0', 'module_name': 'Highway', 'module_version': '1.0.3-GCCcore-12.2.0'}, {'full_module_name': 'Brunsli/0.1-GCCcore-12.2.0', 'module_name': 'Brunsli', 'module_version': '0.1-GCCcore-12.2.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-12.2.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-12.2.0'}, {'full_module_name': 'LERC/4.0.0-GCCcore-12.2.0', 'module_name': 'LERC', 'module_version': '4.0.0-GCCcore-12.2.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-12.2.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-12.2.0'}, {'full_module_name': 'GDAL/3.6.2-foss-2022b', 'module_name': 'GDAL', 'module_version': '3.6.2-foss-2022b'}, {'full_module_name': 'MPFR/4.2.0-GCCcore-12.2.0', 'module_name': 'MPFR', 'module_version': '4.2.0-GCCcore-12.2.0'}, {'full_module_name': 'libgit2/1.5.0-GCCcore-12.2.0', 'module_name': 'libgit2', 'module_version': '1.5.0-GCCcore-12.2.0'}, {'full_module_name': 'Abseil/20230125.2-GCCcore-12.2.0', 'module_name': 'Abseil', 'module_version': '20230125.2-GCCcore-12.2.0'}, {'full_module_name': 'protobuf/23.0-GCCcore-12.2.0', 'module_name': 'protobuf', 'module_version': '23.0-GCCcore-12.2.0'}, {'full_module_name': 'jq/1.6-GCCcore-12.2.0', 'module_name': 'jq', 'module_version': '1.6-GCCcore-12.2.0'}, {'full_module_name': 'R/4.2.2-foss-2022b', 'module_name': 'R', 'module_version': '4.2.2-foss-2022b'}, {'full_module_name': 'snappy/1.1.9-GCCcore-12.2.0', 'module_name': 'snappy', 'module_version': '1.1.9-GCCcore-12.2.0'}, {'full_module_name': 'RapidJSON/1.1.0-GCCcore-12.2.0', 'module_name': 'RapidJSON', 'module_version': '1.1.0-GCCcore-12.2.0'}, {'full_module_name': 'RE2/2023-03-01-GCCcore-12.2.0', 'module_name': 'RE2', 'module_version': '2023-03-01-GCCcore-12.2.0'}, {'full_module_name': 'utf8proc/2.8.0-GCCcore-12.2.0', 'module_name': 'utf8proc', 'module_version': '2.8.0-GCCcore-12.2.0'}, {'full_module_name': 'Arrow/11.0.0-gfbf-2022b', 'module_name': 'Arrow', 'module_version': '11.0.0-gfbf-2022b'}, {'full_module_name': 'arrow-R/11.0.0.3-foss-2022b-R-4.2.2', 'module_name': 'arrow-R', 'module_version': '11.0.0.3-foss-2022b-R-4.2.2'}, {'full_module_name': 'R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2', 'module_name': 'R-bundle-Bioconductor', 'module_version': '3.16-foss-2022b-R-4.2.2'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Bioconductor provides tools for the analysis and coprehension\n of high-throughput genomic data.', 'version': '3.16', 'versionsuffix': '-R-4.2.2', 'extensions': [{'type': 'r', 'name': 'BiocGenerics', 'version': '0.44.0'}, {'type': 'r', 'name': 'Biobase', 'version': '2.58.0'}, {'type': 'r', 'name': 'S4Vectors', 'version': '0.36.2'}, {'type': 'r', 'name': 'IRanges', 'version': '2.32.0'}, {'type': 'r', 'name': 'GenomeInfoDbData', 'version': '1.2.9'}, {'type': 'r', 'name': 'GenomeInfoDb', 'version': '1.34.9'}, {'type': 'r', 'name': 'zlibbioc', 'version': '1.44.0'}, {'type': 'r', 'name': 'XVector', 'version': '0.38.0'}, {'type': 'r', 'name': 'Biostrings', 'version': '2.66.0'}, {'type': 'r', 'name': 'KEGGREST', 'version': '1.38.0'}, {'type': 'r', 'name': 'AnnotationDbi', 'version': '1.60.2'}, {'type': 'r', 'name': 'GenomicRanges', 'version': '1.50.2'}, {'type': 'r', 'name': 'BiocParallel', 'version': '1.32.5'}, {'type': 'r', 'name': 'Rhtslib', 'version': '2.0.0'}, {'type': 'r', 'name': 'Rsamtools', 'version': '2.14.0'}, {'type': 'r', 'name': 'MatrixGenerics', 'version': '1.10.0'}, {'type': 'r', 'name': 'DelayedArray', 'version': '0.24.0'}, {'type': 'r', 'name': 'SummarizedExperiment', 'version': '1.28.0'}, {'type': 'r', 'name': 'GenomicAlignments', 'version': '1.34.1'}, {'type': 'r', 'name': 'ShortRead', 'version': '1.56.1'}, {'type': 'r', 'name': 'graph', 'version': '1.76.0'}, {'type': 'r', 'name': 'affyio', 'version': '1.68.0'}, {'type': 'r', 'name': 'preprocessCore', 'version': '1.60.2'}, {'type': 'r', 'name': 'BiocManager', 'version': '1.30.20'}, {'type': 'r', 'name': 'affy', 'version': '1.76.0'}, {'type': 'r', 'name': 'GO.db', 'version': '3.16.0'}, {'type': 'r', 'name': 'limma', 'version': '3.54.2'}, {'type': 'r', 'name': 'RBGL', 'version': '1.74.0'}, {'type': 'r', 'name': 'org.Hs.eg.db', 'version': '3.16.0'}, {'type': 'r', 'name': 'AnnotationForge', 'version': '1.40.1'}, {'type': 'r', 'name': 'annaffy', 'version': '1.70.0'}, {'type': 'r', 'name': 'gcrma', 'version': '2.70.0'}, {'type': 'r', 'name': 'oligoClasses', 'version': '1.60.0'}, {'type': 'r', 'name': 'edgeR', 'version': '3.40.2'}, {'type': 'r', 'name': 'PFAM.db', 'version': '3.16.0'}, {'type': 'r', 'name': 'perm', 'version': '1.0-0.2'}, {'type': 'r', 'name': 'baySeq', 'version': '2.31.0'}, {'type': 'r', 'name': 'qvalue', 'version': '2.30.0'}, {'type': 'r', 'name': 'impute', 'version': '1.72.3'}, {'type': 'r', 'name': 'shinyFiles', 'version': '0.9.3'}, {'type': 'r', 'name': 'samr', 'version': '3.0'}, {'type': 'r', 'name': 'DEGseq', 'version': '1.52.0'}, {'type': 'r', 'name': 'hgu133plus2.db', 'version': '3.13.0'}, {'type': 'r', 'name': 'illuminaio', 'version': '0.40.0'}, {'type': 'r', 'name': 'BiocIO', 'version': '1.8.0'}, {'type': 'r', 'name': 'restfulr', 'version': '0.0.15'}, {'type': 'r', 'name': 'rtracklayer', 'version': '1.58.0'}, {'type': 'r', 'name': 'filelock', 'version': '1.0.2'}, {'type': 'r', 'name': 'BiocFileCache', 'version': '2.6.1'}, {'type': 'r', 'name': 'biomaRt', 'version': '2.54.0'}, {'type': 'r', 'name': 'GenomicFeatures', 'version': '1.50.4'}, {'type': 'r', 'name': 'bumphunter', 'version': '1.40.0'}, {'type': 'r', 'name': 'multtest', 'version': '2.54.0'}, {'type': 'r', 'name': 'scrime', 'version': '1.3.5'}, {'type': 'r', 'name': 'siggenes', 'version': '1.72.0'}, {'type': 'r', 'name': 'DynDoc', 'version': '1.76.0'}, {'type': 'r', 'name': 'NOISeq', 'version': '2.42.0'}, {'type': 'r', 'name': 'Rgraphviz', 'version': '2.42.0'}, {'type': 'r', 'name': 'RNASeqPower', 'version': '1.38.0'}, {'type': 'r', 'name': 'annotate', 'version': '1.76.0'}, {'type': 'r', 'name': 'GSEABase', 'version': '1.60.0'}, {'type': 'r', 'name': 'genefilter', 'version': '1.80.3'}, {'type': 'r', 'name': 'Category', 'version': '2.64.0'}, {'type': 'r', 'name': 'GOstats', 'version': '2.64.0'}, {'type': 'r', 'name': 'BSgenome', 'version': '1.66.3'}, {'type': 'r', 'name': 'VariantAnnotation', 'version': '1.44.1'}, {'type': 'r', 'name': 'interactiveDisplayBase', 'version': '1.36.0'}, {'type': 'r', 'name': 'BiocVersion', 'version': '3.16.0'}, {'type': 'r', 'name': 'AnnotationHub', 'version': '3.6.0'}, {'type': 'r', 'name': 'AnnotationFilter', 'version': '1.22.0'}, {'type': 'r', 'name': 'ProtGenerics', 'version': '1.30.0'}, {'type': 'r', 'name': 'ensembldb', 'version': '2.22.0'}, {'type': 'r', 'name': 'biovizBase', 'version': '1.46.0'}, {'type': 'r', 'name': 'OrganismDbi', 'version': '1.40.0'}, {'type': 'r', 'name': 'ggbio', 'version': '1.46.0'}, {'type': 'r', 'name': 'geneplotter', 'version': '1.76.0'}, {'type': 'r', 'name': 'DESeq2', 'version': '1.38.3'}, {'type': 'r', 'name': 'ReportingTools', 'version': '2.38.0'}, {'type': 'r', 'name': 'Glimma', 'version': '2.8.0'}, {'type': 'r', 'name': 'affycoretools', 'version': '1.70.0'}, {'type': 'r', 'name': 'TxDb.Hsapiens.UCSC.hg19.knownGene', 'version': '3.2.2'}, {'type': 'r', 'name': 'Homo.sapiens', 'version': '1.3.1'}, {'type': 'r', 'name': 'BSgenome.Hsapiens.UCSC.hg19', 'version': '1.4.3'}, {'type': 'r', 'name': 'AgiMicroRna', 'version': '2.48.0'}, {'type': 'r', 'name': 'geneLenDataBase', 'version': '1.34.0'}, {'type': 'r', 'name': 'goseq', 'version': '1.50.0'}, {'type': 'r', 'name': 'KEGGgraph', 'version': '1.58.3'}, {'type': 'r', 'name': 'GEOquery', 'version': '2.66.0'}, {'type': 'r', 'name': 'rARPACK', 'version': '0.11-0'}, {'type': 'r', 'name': 'mixOmics', 'version': '6.22.0'}, {'type': 'r', 'name': 'Rhdf5lib', 'version': '1.20.0'}, {'type': 'r', 'name': 'rhdf5filters', 'version': '1.10.0'}, {'type': 'r', 'name': 'rhdf5', 'version': '2.42.0'}, {'type': 'r', 'name': 'HDF5Array', 'version': '1.26.0'}, {'type': 'r', 'name': 'sparseMatrixStats', 'version': '1.10.0'}, {'type': 'r', 'name': 'DelayedMatrixStats', 'version': '1.20.0'}, {'type': 'r', 'name': 'minfi', 'version': '1.44.0'}, {'type': 'r', 'name': 'FDb.InfiniumMethylation.hg19', 'version': '2.2.0'}, {'type': 'r', 'name': 'methylumi', 'version': '2.44.0'}, {'type': 'r', 'name': 'lumi', 'version': '2.50.0'}, {'type': 'r', 'name': 'widgetTools', 'version': '1.76.0'}, {'type': 'r', 'name': 'tkWidgets', 'version': '1.76.0'}, {'type': 'r', 'name': 'Mfuzz', 'version': '2.58.0'}, {'type': 'r', 'name': 'venn', 'version': '1.11'}, {'type': 'r', 'name': 'maSigPro', 'version': '1.70.0'}, {'type': 'r', 'name': 'SPIA', 'version': '2.50.0'}, {'type': 'r', 'name': 'Gviz', 'version': '1.42.1'}, {'type': 'r', 'name': 'cummeRbund', 'version': '2.40.0'}, {'type': 'r', 'name': 'GenomicFiles', 'version': '1.34.0'}, {'type': 'r', 'name': 'derfinderHelper', 'version': '1.32.0'}, {'type': 'r', 'name': 'derfinder', 'version': '1.32.0'}, {'type': 'r', 'name': 'polyester', 'version': '1.34.0'}, {'type': 'r', 'name': 'Rsubread', 'version': '2.12.3'}, {'type': 'r', 'name': 'pcaMethods', 'version': '1.90.0'}, {'type': 'r', 'name': 'marray', 'version': '1.76.0'}, {'type': 'r', 'name': 'CGHbase', 'version': '1.58.0'}, {'type': 'r', 'name': 'Wrench', 'version': '1.16.0'}, {'type': 'r', 'name': 'lpsymphony', 'version': '1.26.3'}, {'type': 'r', 'name': 'IHW', 'version': '1.26.0'}, {'type': 'r', 'name': 'metagenomeSeq', 'version': '1.40.0'}, {'type': 'r', 'name': 'gdsfmt', 'version': '1.34.0'}, {'type': 'r', 'name': 'SNPRelate', 'version': '1.32.2'}, {'type': 'r', 'name': 'biomformat', 'version': '1.26.0'}, {'type': 'r', 'name': 'phyloseq', 'version': '1.42.0'}, {'type': 'r', 'name': 'NADA', 'version': '1.6-1.1'}, {'type': 'r', 'name': 'zCompositions', 'version': '1.4.0-1'}, {'type': 'r', 'name': 'RcppZiggurat', 'version': '0.1.6'}, {'type': 'r', 'name': 'Rfast', 'version': '2.0.7'}, {'type': 'r', 'name': 'ALDEx2', 'version': '1.30.0'}, {'type': 'r', 'name': 'dada2', 'version': '1.26.0'}, {'type': 'r', 'name': 'LEA', 'version': '3.10.2'}, {'type': 'r', 'name': 'tximport', 'version': '1.26.1'}, {'type': 'r', 'name': 'SingleCellExperiment', 'version': '1.20.0'}, {'type': 'r', 'name': 'beachmat', 'version': '2.14.0'}, {'type': 'r', 'name': 'RcppAnnoy', 'version': '0.0.20'}, {'type': 'r', 'name': 'RcppHNSW', 'version': '0.4.1'}, {'type': 'r', 'name': 'BiocNeighbors', 'version': '1.16.0'}, {'type': 'r', 'name': 'rsvd', 'version': '1.0.5'}, {'type': 'r', 'name': 'ScaledMatrix', 'version': '1.6.0'}, {'type': 'r', 'name': 'BiocSingular', 'version': '1.14.0'}, {'type': 'r', 'name': 'scuttle', 'version': '1.8.4'}, {'type': 'r', 'name': 'RcppML', 'version': '0.3.7'}, {'type': 'r', 'name': 'sitmo', 'version': '2.0.2'}, {'type': 'r', 'name': 'dqrng', 'version': '0.3.0'}, {'type': 'r', 'name': 'uwot', 'version': '0.1.14'}, {'type': 'r', 'name': 'ggrastr', 'version': '1.0.1'}, {'type': 'r', 'name': 'scater', 'version': '1.26.1'}, {'type': 'r', 'name': 'bluster', 'version': '1.8.0'}, {'type': 'r', 'name': 'metapod', 'version': '1.6.0'}, {'type': 'r', 'name': 'scran', 'version': '1.26.2'}, {'type': 'r', 'name': 'SC3', 'version': '1.26.2'}, {'type': 'r', 'name': 'ComplexHeatmap', 'version': '2.14.0'}, {'type': 'r', 'name': 'GENIE3', 'version': '1.20.0'}, {'type': 'r', 'name': 'dupRadar', 'version': '1.28.0'}, {'type': 'r', 'name': 'DNAcopy', 'version': '1.72.3'}, {'type': 'r', 'name': 'sva', 'version': '3.46.0'}, {'type': 'r', 'name': 'ballgown', 'version': '2.30.0'}, {'type': 'r', 'name': 'DropletUtils', 'version': '1.18.1'}, {'type': 'r', 'name': 'DeconRNASeq', 'version': '1.40.0'}, {'type': 'r', 'name': 'GSVA', 'version': '1.46.0'}, {'type': 'r', 'name': 'PureCN', 'version': '2.4.0'}, {'type': 'r', 'name': 'globaltest', 'version': '5.52.0'}, {'type': 'r', 'name': 'GlobalAncova', 'version': '4.16.0'}, {'type': 'r', 'name': 'vsn', 'version': '3.66.0'}, {'type': 'r', 'name': 'mzID', 'version': '1.36.0'}, {'type': 'r', 'name': 'mzR', 'version': '2.32.0'}, {'type': 'r', 'name': 'MsCoreUtils', 'version': '1.10.0'}, {'type': 'r', 'name': 'MSnbase', 'version': '2.24.2'}, {'type': 'r', 'name': 'MassSpecWavelet', 'version': '1.64.1'}, {'type': 'r', 'name': 'MsFeatures', 'version': '1.6.0'}, {'type': 'r', 'name': 'xcms', 'version': '3.20.0'}, {'type': 'r', 'name': 'CAMERA', 'version': '1.54.0'}, {'type': 'r', 'name': 'fgsea', 'version': '1.24.0'}, {'type': 'r', 'name': 'GWASExactHW', 'version': '1.01'}, {'type': 'r', 'name': 'quantsmooth', 'version': '1.64.0'}, {'type': 'r', 'name': 'GWASTools', 'version': '1.44.0'}, {'type': 'r', 'name': 'SeqArray', 'version': '1.38.0'}, {'type': 'r', 'name': 'SeqVarTools', 'version': '1.36.0'}, {'type': 'r', 'name': 'GENESIS', 'version': '2.28.0'}, {'type': 'r', 'name': 'MLInterfaces', 'version': '1.78.0'}, {'type': 'r', 'name': 'pRoloc', 'version': '1.38.2'}, {'type': 'r', 'name': 'pRolocdata', 'version': '1.36.0'}, {'type': 'r', 'name': 'fresh', 'version': '0.2.0'}, {'type': 'r', 'name': 'waiter', 'version': '0.2.5'}, {'type': 'r', 'name': 'shinydashboardPlus', 'version': '2.0.3'}, {'type': 'r', 'name': 'shinyhelper', 'version': '0.3.2'}, {'type': 'r', 'name': 'anytime', 'version': '0.3.9'}, {'type': 'r', 'name': 'shinyWidgets', 'version': '0.7.6'}, {'type': 'r', 'name': 'pRolocGUI', 'version': '2.8.0'}, {'type': 'r', 'name': 'EBImage', 'version': '4.40.0'}, {'type': 'r', 'name': 'GenomicScores', 'version': '2.10.0'}, {'type': 'r', 'name': 'BSgenome.Mmusculus.UCSC.mm10', 'version': '1.4.3'}, {'type': 'r', 'name': 'TxDb.Mmusculus.UCSC.mm10.knownGene', 'version': '3.10.0'}, {'type': 'r', 'name': 'regioneR', 'version': '1.30.0'}, {'type': 'r', 'name': 'InteractionSet', 'version': '1.26.1'}, {'type': 'r', 'name': 'ChIPpeakAnno', 'version': '3.32.0'}, {'type': 'r', 'name': 'seqLogo', 'version': '1.64.0'}, {'type': 'r', 'name': 'rGADEM', 'version': '2.46.0'}, {'type': 'r', 'name': 'MotifDb', 'version': '1.40.0'}, {'type': 'r', 'name': 'poweRlaw', 'version': '0.70.6'}, {'type': 'r', 'name': 'CNEr', 'version': '1.34.0'}, {'type': 'r', 'name': 'DirichletMultinomial', 'version': '1.40.0'}, {'type': 'r', 'name': 'TFMPvalue', 'version': '0.0.9'}, {'type': 'r', 'name': 'TFBSTools', 'version': '1.36.0'}, {'type': 'r', 'name': 'motifStack', 'version': '1.42.0'}, {'type': 'r', 'name': 'ATACseqQC', 'version': '1.22.0'}, {'type': 'r', 'name': 'ResidualMatrix', 'version': '1.8.0'}, {'type': 'r', 'name': 'batchelor', 'version': '1.14.1'}, {'type': 'r', 'name': 'gsmoothr', 'version': '0.1.7'}, {'type': 'r', 'name': 'Ringo', 'version': '1.62.0'}, {'type': 'r', 'name': 'R.devices', 'version': '2.17.1'}, {'type': 'r', 'name': 'R.filesets', 'version': '2.15.0'}, {'type': 'r', 'name': 'aroma.light', 'version': '3.28.0'}, {'type': 'r', 'name': 'PSCBS', 'version': '0.66.0'}, {'type': 'r', 'name': 'aroma.core', 'version': '3.3.0'}, {'type': 'r', 'name': 'R.huge', 'version': '0.9.0'}, {'type': 'r', 'name': 'aroma.apd', 'version': '0.6.1'}, {'type': 'r', 'name': 'aroma.affymetrix', 'version': '3.2.1'}, {'type': 'r', 'name': 'Repitools', 'version': '1.44.0'}, {'type': 'r', 'name': 'BSgenome.Hsapiens.UCSC.hg38', 'version': '1.4.5'}, {'type': 'r', 'name': 'MEDIPS', 'version': '1.50.0'}, {'type': 'r', 'name': 'RProtoBufLib', 'version': '2.10.0'}, {'type': 'r', 'name': 'cytolib', 'version': '2.10.1'}, {'type': 'r', 'name': 'flowCore', 'version': '2.10.0'}, {'type': 'r', 'name': 'mutoss', 'version': '0.1-13'}, {'type': 'r', 'name': 'qqconf', 'version': '1.3.1'}, {'type': 'r', 'name': 'metap', 'version': '1.8'}, {'type': 'r', 'name': 'scattermore', 'version': '0.8'}, {'type': 'r', 'name': 'SeuratObject', 'version': '4.1.3'}, {'type': 'r', 'name': 'Seurat', 'version': '4.3.0'}, {'type': 'r', 'name': 'ALL', 'version': '1.40.0'}, {'type': 'r', 'name': 'ConsensusClusterPlus', 'version': '1.62.0'}, {'type': 'r', 'name': 'flowViz', 'version': '1.62.0'}, {'type': 'r', 'name': 'ncdfFlow', 'version': '2.44.0'}, {'type': 'r', 'name': 'aws.signature', 'version': '0.6.0'}, {'type': 'r', 'name': 'aws.s3', 'version': '0.3.21'}, {'type': 'r', 'name': 'flowWorkspace', 'version': '4.10.1'}, {'type': 'r', 'name': 'ash', 'version': '1.0-15'}, {'type': 'r', 'name': 'hdrcde', 'version': '3.4'}, {'type': 'r', 'name': 'rainbow', 'version': '3.7'}, {'type': 'r', 'name': 'fds', 'version': '1.8'}, {'type': 'r', 'name': 'fda', 'version': '6.0.5'}, {'type': 'r', 'name': 'flowStats', 'version': '4.10.0'}, {'type': 'r', 'name': 'flowClust', 'version': '3.36.0'}, {'type': 'r', 'name': 'openCyto', 'version': '2.10.1'}, {'type': 'r', 'name': 'ggcyto', 'version': '1.26.4'}, {'type': 'r', 'name': 'CytoML', 'version': '2.10.0'}, {'type': 'r', 'name': 'colorRamps', 'version': '2.3.1'}, {'type': 'r', 'name': 'ggnewscale', 'version': '0.4.8'}, {'type': 'r', 'name': 'ggpointdensity', 'version': '0.1.0'}, {'type': 'r', 'name': 'FlowSOM', 'version': '2.6.0'}, {'type': 'r', 'name': 'HMMcopy', 'version': '1.40.0'}, {'type': 'r', 'name': 'diffcyt', 'version': '1.18.0'}, {'type': 'r', 'name': 'blme', 'version': '1.0-5'}, {'type': 'r', 'name': 'remaCor', 'version': '0.0.11'}, {'type': 'r', 'name': 'variancePartition', 'version': '1.28.7'}, {'type': 'r', 'name': 'muscat', 'version': '1.12.1'}, {'type': 'r', 'name': 'IlluminaHumanMethylation450kmanifest', 'version': '0.4.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICmanifest', 'version': '0.3.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylation450kanno.ilmn12.hg19', 'version': '0.6.1'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICanno.ilm10b2.hg19', 'version': '0.6.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICanno.ilm10b4.hg19', 'version': '0.6.0'}, {'type': 'r', 'name': 'conumee', 'version': '1.32.0'}, {'type': 'r', 'name': 'BSgenome.Cfamiliaris.UCSC.canFam3', 'version': '1.4.0'}, {'type': 'r', 'name': 'ExperimentHub', 'version': '2.6.0'}, {'type': 'r', 'name': 'SingleR', 'version': '2.0.0'}, {'type': 'r', 'name': 'FlowSorted.Blood.EPIC', 'version': '2.2.0'}, {'type': 'r', 'name': 'FlowSorted.CordBloodCombined.450k', 'version': '1.14.0'}, {'type': 'r', 'name': 'DRIMSeq', 'version': '1.26.0'}, {'type': 'r', 'name': 'stageR', 'version': '1.20.0'}, {'type': 'r', 'name': 'isva', 'version': '1.9'}, {'type': 'r', 'name': 'org.Mm.eg.db', 'version': '3.16.0'}, {'type': 'r', 'name': 'org.Rn.eg.db', 'version': '3.16.0'}, {'type': 'r', 'name': 'ROC', 'version': '1.74.0'}, {'type': 'r', 'name': 'wateRmelon', 'version': '2.4.0'}, {'type': 'r', 'name': 'GLAD', 'version': '2.62.0'}, {'type': 'r', 'name': 'missMethyl', 'version': '1.32.0'}, {'type': 'r', 'name': 'MethylSeekR', 'version': '1.38.0'}, {'type': 'r', 'name': 'affxparser', 'version': '1.70.0'}, {'type': 'r', 'name': 'ccdata', 'version': '1.24.0'}, {'type': 'r', 'name': 'lsa', 'version': '0.73.3'}, {'type': 'r', 'name': 'ccmap', 'version': '1.24.0'}, {'type': 'r', 'name': 'oligo', 'version': '1.62.2'}, {'type': 'r', 'name': 'SMVar', 'version': '1.3.4'}, {'type': 'r', 'name': 'metaMA', 'version': '3.1.3'}, {'type': 'r', 'name': 'randomcoloR', 'version': '1.1.0.1'}, {'type': 'r', 'name': 'shinyBS', 'version': '0.61.1'}, {'type': 'r', 'name': 'shinypanel', 'version': '0.1.5'}, {'type': 'r', 'name': 'crossmeta', 'version': '1.24.0'}, {'type': 'r', 'name': 'snpStats', 'version': '1.48.0'}, {'type': 'r', 'name': 'mixsqp', 'version': '0.3-48'}, {'type': 'r', 'name': 'susieR', 'version': '0.12.35'}, {'type': 'r', 'name': 'coloc', 'version': '5.1.0.1'}, {'type': 'r', 'name': 'SCANVIS', 'version': '1.12.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v86', 'version': '2.99.0'}, {'type': 'r', 'name': 'agricolae', 'version': '1.3-5'}, {'type': 'r', 'name': 'bookdown', 'version': '0.33'}, {'type': 'r', 'name': 'BiocStyle', 'version': '2.26.0'}, {'type': 'r', 'name': 'estimability', 'version': '1.4.1'}, {'type': 'r', 'name': 'emmeans', 'version': '1.8.5'}, {'type': 'r', 'name': 'ggdendro', 'version': '0.1.23'}, {'type': 'r', 'name': 'pmp', 'version': '1.10.0'}, {'type': 'r', 'name': 'MultiDataSet', 'version': '1.26.0'}, {'type': 'r', 'name': 'BiocBaseUtils', 'version': '1.0.0'}, {'type': 'r', 'name': 'MultiAssayExperiment', 'version': '1.24.0'}, {'type': 'r', 'name': 'ropls', 'version': '1.30.0'}, {'type': 'r', 'name': 'ontologyIndex', 'version': '2.10'}, {'type': 'r', 'name': 'rols', 'version': '2.26.0'}, {'type': 'r', 'name': 'struct', 'version': '1.10.0'}, {'type': 'r', 'name': 'ggthemes', 'version': '4.2.4'}, {'type': 'r', 'name': 'structToolbox', 'version': '1.10.1'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v75', 'version': '2.99.0'}, {'type': 'r', 'name': 'ggseqlogo', 'version': '0.1'}, {'type': 'r', 'name': 'sparsesvd', 'version': '0.2-2'}, {'type': 'r', 'name': 'docopt', 'version': '0.7.1'}, {'type': 'r', 'name': 'qlcMatrix', 'version': '0.9.7'}, {'type': 'r', 'name': 'Signac', 'version': '1.9.0'}, {'type': 'r', 'name': 'motifmatchr', 'version': '1.20.0'}, {'type': 'r', 'name': 'extraDistr', 'version': '1.9.1'}, {'type': 'r', 'name': 'PRROC', 'version': '1.3.1'}, {'type': 'r', 'name': 'TSP', 'version': '1.2-3'}, {'type': 'r', 'name': 'qap', 'version': '0.1-2'}, {'type': 'r', 'name': 'ca', 'version': '0.71.1'}, {'type': 'r', 'name': 'seriation', 'version': '1.4.2'}, {'type': 'r', 'name': 'egg', 'version': '0.4.5'}, {'type': 'r', 'name': 'heatmaply', 'version': '1.4.2'}, {'type': 'r', 'name': 'OUTRIDER', 'version': '1.16.3'}, {'type': 'r', 'name': 'FRASER', 'version': '1.10.2'}, {'type': 'r', 'name': 'JASPAR2020', 'version': '0.99.10'}, {'type': 'r', 'name': 'AUCell', 'version': '1.20.2'}, {'type': 'r', 'name': 'RcisTarget', 'version': '1.18.2'}, {'type': 'r', 'name': 'NMF', 'version': '0.25'}, {'type': 'r', 'name': 'densEstBayes', 'version': '1.0-2.1'}, {'type': 'r', 'name': 'reldist', 'version': '1.7-2'}, {'type': 'r', 'name': 'M3Drop', 'version': '1.24.0'}, {'type': 'r', 'name': 'bsseq', 'version': '1.34.0'}, {'type': 'r', 'name': 'DSS', 'version': '2.46.0'}, {'type': 'r', 'name': 'pathview', 'version': '1.38.0'}, {'type': 'r', 'name': 'chromVAR', 'version': '1.20.2'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v79', 'version': '2.99.0'}, {'type': 'r', 'name': 'WGCNA', 'version': '1.72-1'}, {'type': 'r', 'name': 'DNABarcodes', 'version': '1.28.0'}, {'type': 'r', 'name': 'CAGEr', 'version': '2.4.0'}, {'type': 'r', 'name': 'SPOTlight', 'version': '1.2.0'}, {'type': 'r', 'name': 'CGHcall', 'version': '2.60.0'}, {'type': 'r', 'name': 'QDNAseq', 'version': '1.34.0'}, {'type': 'r', 'name': 'HiCcompare', 'version': '1.20.0'}, {'type': 'r', 'name': 'ROntoTools', 'version': '2.26.0'}, {'type': 'r', 'name': 'scDblFinder', 'version': '1.12.0'}, {'type': 'r', 'name': 'treeio', 'version': '1.22.0'}, {'type': 'r', 'name': 'ggtree', 'version': '3.6.2'}, {'type': 'r', 'name': 'scistreer', 'version': '1.1.0'}, {'type': 'r', 'name': 'numbat', 'version': '1.2.2'}, {'type': 'r', 'name': 'HiCBricks', 'version': '1.16.0'}, {'type': 'r', 'name': 'dir.expiry', 'version': '1.6.0'}, {'type': 'r', 'name': 'basilisk.utils', 'version': '1.10.0'}, {'type': 'r', 'name': 'basilisk', 'version': '1.10.2'}, {'type': 'r', 'name': 'zellkonverter', 'version': '1.8.0'}, {'type': 'r', 'name': 'DO.db', 'version': '2.9'}, {'type': 'r', 'name': 'GOSemSim', 'version': '2.24.0'}, {'type': 'r', 'name': 'HDO.db', 'version': '0.99.1'}, {'type': 'r', 'name': 'DOSE', 'version': '3.24.2'}, {'type': 'r', 'name': 'enrichplot', 'version': '1.18.3'}, {'type': 'r', 'name': 'gson', 'version': '0.1.0'}, {'type': 'r', 'name': 'clusterProfiler', 'version': '4.6.2'}, {'type': 'r', 'name': 'reactome.db', 'version': '1.82.0'}, {'type': 'r', 'name': 'graphite', 'version': '1.44.0'}, {'type': 'r', 'name': 'ReactomePA', 'version': '1.42.0'}, {'type': 'r', 'name': 'flowClean', 'version': '1.36.0'}, {'type': 'r', 'name': 'flowAI', 'version': '1.28.0'}, {'type': 'r', 'name': 'flowFP', 'version': '1.56.3'}, {'type': 'r', 'name': 'simplifyEnrichment', 'version': '1.8.0'}, {'type': 'r', 'name': 'RPMG', 'version': '2.2-3'}, {'type': 'r', 'name': 'Rwave', 'version': '2.6-5'}, {'type': 'r', 'name': 'RSEIS', 'version': '4.1-4'}, {'type': 'r', 'name': 'splancs', 'version': '2.01-43'}, {'type': 'r', 'name': 'MBA', 'version': '0.1-0'}, {'type': 'r', 'name': 'GEOmap', 'version': '2.5-0'}, {'type': 'r', 'name': 'RFOC', 'version': '3.4-6'}, {'type': 'r', 'name': 'flowDensity', 'version': '1.32.0'}, {'type': 'r', 'name': 'flowPeaks', 'version': '1.44.0'}, {'type': 'r', 'name': 'SamSPECTRAL', 'version': '1.52.0'}, {'type': 'r', 'name': 'ddPCRclust', 'version': '1.18.0'}, {'type': 'r', 'name': 'feature', 'version': '1.2.15'}, {'type': 'r', 'name': 'flowMerge', 'version': '2.46.0'}, {'type': 'r', 'name': 'SpatialExperiment', 'version': '1.8.1'}, {'type': 'r', 'name': 'TrajectoryUtils', 'version': '1.6.0'}, {'type': 'r', 'name': 'slingshot', 'version': '2.6.0'}, {'type': 'r', 'name': 'TreeSummarizedExperiment', 'version': '2.6.0'}, {'type': 'r', 'name': 'decontam', 'version': '1.18.0'}, {'type': 'r', 'name': 'DECIPHER', 'version': '2.26.0'}, {'type': 'r', 'name': 'mia', 'version': '1.6.0'}, {'type': 'r', 'name': 'ANCOMBC', 'version': '2.0.2'}, {'type': 'r', 'name': 'decoupleR', 'version': '2.4.0'}, {'type': 'r', 'name': 'UCell', 'version': '2.2.0'}, {'type': 'r', 'name': 'intervals', 'version': '0.15.4'}, {'type': 'r', 'name': 'oompaBase', 'version': '3.2.9'}, {'type': 'r', 'name': 'oompaData', 'version': '3.1.3'}, {'type': 'r', 'name': 'TailRank', 'version': '3.2.2'}, {'type': 'r', 'name': 'RnBeads', 'version': '2.16.0'}, {'type': 'r', 'name': 'RnBeads.hg19', 'version': '1.30.0'}, {'type': 'r', 'name': 'RnBeads.hg38', 'version': '1.30.0'}, {'type': 'r', 'name': 'RnBeads.mm9', 'version': '1.30.0'}, {'type': 'r', 'name': 'RnBeads.mm10', 'version': '2.6.0'}, {'type': 'r', 'name': 'RnBeads.rn5', 'version': '1.30.0'}, {'type': 'r', 'name': 'log4r', 'version': '0.4.3'}, {'type': 'r', 'name': 'MSstatsConvert', 'version': '1.8.3'}, {'type': 'r', 'name': 'MSstats', 'version': '4.6.5'}, {'type': 'r', 'name': 'MSstatsTMT', 'version': '2.6.1'}, {'type': 'r', 'name': 'MSstatsPTM', 'version': '2.0.3'}, {'type': 'r', 'name': 'factoextra', 'version': '1.0.7'}, {'type': 'r', 'name': 'MSstatsLiP', 'version': '1.4.1'}, {'type': 'r', 'name': 'babelgene', 'version': '22.9'}, {'type': 'r', 'name': 'msigdbr', 'version': '7.5.1'}, {'type': 'r', 'name': 'escape', 'version': '1.8.0'}]}, {'homepage': 'https://bioconductor.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023a'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2', 'module_name': 'R-bundle-Bioconductor', 'module_version': '3.18-foss-2023a-R-4.3.2'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.3.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.3.0'}, {'full_module_name': 'libxml2/2.11.4-GCCcore-12.3.0', 'module_name': 'libxml2', 'module_version': '2.11.4-GCCcore-12.3.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.3.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.3.0'}, {'full_module_name': 'hwloc/2.9.1-GCCcore-12.3.0', 'module_name': 'hwloc', 'module_version': '2.9.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.3.0'}, {'full_module_name': 'UCX/1.14.1-GCCcore-12.3.0', 'module_name': 'UCX', 'module_version': '1.14.1-GCCcore-12.3.0'}, {'full_module_name': 'libfabric/1.18.0-GCCcore-12.3.0', 'module_name': 'libfabric', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'PMIx/4.2.4-GCCcore-12.3.0', 'module_name': 'PMIx', 'module_version': '4.2.4-GCCcore-12.3.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-12.3.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenMPI/4.1.5-GCC-12.3.0', 'module_name': 'OpenMPI', 'module_version': '4.1.5-GCC-12.3.0'}, {'full_module_name': 'OpenBLAS/0.3.23-GCC-12.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.23-GCC-12.3.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-12.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-12.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.3.0'}, {'full_module_name': 'gompi/2023a', 'module_name': 'gompi', 'module_version': '2023a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023a-fb'}, {'full_module_name': 'foss/2023a', 'module_name': 'foss', 'module_version': '2023a'}, {'full_module_name': 'gfbf/2023a', 'module_name': 'gfbf', 'module_version': '2023a'}, {'full_module_name': 'expat/2.5.0-GCCcore-12.3.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'libpng/1.6.39-GCCcore-12.3.0', 'module_name': 'libpng', 'module_version': '1.6.39-GCCcore-12.3.0'}, {'full_module_name': 'Brotli/1.0.9-GCCcore-12.3.0', 'module_name': 'Brotli', 'module_version': '1.0.9-GCCcore-12.3.0'}, {'full_module_name': 'freetype/2.13.0-GCCcore-12.3.0', 'module_name': 'freetype', 'module_version': '2.13.0-GCCcore-12.3.0'}, {'full_module_name': 'fontconfig/2.14.2-GCCcore-12.3.0', 'module_name': 'fontconfig', 'module_version': '2.14.2-GCCcore-12.3.0'}, {'full_module_name': 'xorg-macros/1.20.0-GCCcore-12.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.0-GCCcore-12.3.0'}, {'full_module_name': 'X11/20230603-GCCcore-12.3.0', 'module_name': 'X11', 'module_version': '20230603-GCCcore-12.3.0'}, {'full_module_name': 'gzip/1.12-GCCcore-12.3.0', 'module_name': 'gzip', 'module_version': '1.12-GCCcore-12.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-12.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-12.3.0'}, {'full_module_name': 'zstd/1.5.5-GCCcore-12.3.0', 'module_name': 'zstd', 'module_version': '1.5.5-GCCcore-12.3.0'}, {'full_module_name': 'libdrm/2.4.115-GCCcore-12.3.0', 'module_name': 'libdrm', 'module_version': '2.4.115-GCCcore-12.3.0'}, {'full_module_name': 'libglvnd/1.6.0-GCCcore-12.3.0', 'module_name': 'libglvnd', 'module_version': '1.6.0-GCCcore-12.3.0'}, {'full_module_name': 'libunwind/1.6.2-GCCcore-12.3.0', 'module_name': 'libunwind', 'module_version': '1.6.2-GCCcore-12.3.0'}, {'full_module_name': 'LLVM/16.0.6-GCCcore-12.3.0', 'module_name': 'LLVM', 'module_version': '16.0.6-GCCcore-12.3.0'}, {'full_module_name': 'Mesa/23.1.4-GCCcore-12.3.0', 'module_name': 'Mesa', 'module_version': '23.1.4-GCCcore-12.3.0'}, {'full_module_name': 'libGLU/9.0.3-GCCcore-12.3.0', 'module_name': 'libGLU', 'module_version': '9.0.3-GCCcore-12.3.0'}, {'full_module_name': 'pixman/0.42.2-GCCcore-12.3.0', 'module_name': 'pixman', 'module_version': '0.42.2-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'PCRE2/10.42-GCCcore-12.3.0', 'module_name': 'PCRE2', 'module_version': '10.42-GCCcore-12.3.0'}, {'full_module_name': 'GLib/2.77.1-GCCcore-12.3.0', 'module_name': 'GLib', 'module_version': '2.77.1-GCCcore-12.3.0'}, {'full_module_name': 'cairo/1.17.8-GCCcore-12.3.0', 'module_name': 'cairo', 'module_version': '1.17.8-GCCcore-12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'NASM/2.16.01-GCCcore-12.3.0', 'module_name': 'NASM', 'module_version': '2.16.01-GCCcore-12.3.0'}, {'full_module_name': 'libjpeg-turbo/2.1.5.1-GCCcore-12.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '2.1.5.1-GCCcore-12.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-12.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-12.3.0'}, {'full_module_name': 'libdeflate/1.18-GCCcore-12.3.0', 'module_name': 'libdeflate', 'module_version': '1.18-GCCcore-12.3.0'}, {'full_module_name': 'LibTIFF/4.5.0-GCCcore-12.3.0', 'module_name': 'LibTIFF', 'module_version': '4.5.0-GCCcore-12.3.0'}, {'full_module_name': 'Java/11.0.27', 'module_name': 'Java', 'module_version': '11.0.27'}, {'full_module_name': 'Java/11', 'module_name': 'Java', 'module_version': '11'}, {'full_module_name': 'PCRE/8.45-GCCcore-12.3.0', 'module_name': 'PCRE', 'module_version': '8.45-GCCcore-12.3.0'}, {'full_module_name': 'libgit2/1.7.1-GCCcore-12.3.0', 'module_name': 'libgit2', 'module_version': '1.7.1-GCCcore-12.3.0'}, {'full_module_name': 'cURL/8.0.1-GCCcore-12.3.0', 'module_name': 'cURL', 'module_version': '8.0.1-GCCcore-12.3.0'}, {'full_module_name': 'Tk/8.6.13-GCCcore-12.3.0', 'module_name': 'Tk', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'ICU/73.2-GCCcore-12.3.0', 'module_name': 'ICU', 'module_version': '73.2-GCCcore-12.3.0'}, {'full_module_name': 'HarfBuzz/5.3.1-GCCcore-12.3.0', 'module_name': 'HarfBuzz', 'module_version': '5.3.1-GCCcore-12.3.0'}, {'full_module_name': 'FriBidi/1.0.12-GCCcore-12.3.0', 'module_name': 'FriBidi', 'module_version': '1.0.12-GCCcore-12.3.0'}, {'full_module_name': 'R/4.3.2-gfbf-2023a', 'module_name': 'R', 'module_version': '4.3.2-gfbf-2023a'}, {'full_module_name': 'Boost/1.82.0-GCC-12.3.0', 'module_name': 'Boost', 'module_version': '1.82.0-GCC-12.3.0'}, {'full_module_name': 'GSL/2.7-GCC-12.3.0', 'module_name': 'GSL', 'module_version': '2.7-GCC-12.3.0'}, {'full_module_name': 'GMP/6.2.1-GCCcore-12.3.0', 'module_name': 'GMP', 'module_version': '6.2.1-GCCcore-12.3.0'}, {'full_module_name': 'NLopt/2.7.1-GCCcore-12.3.0', 'module_name': 'NLopt', 'module_version': '2.7.1-GCCcore-12.3.0'}, {'full_module_name': 'libogg/1.3.5-GCCcore-12.3.0', 'module_name': 'libogg', 'module_version': '1.3.5-GCCcore-12.3.0'}, {'full_module_name': 'FLAC/1.4.2-GCCcore-12.3.0', 'module_name': 'FLAC', 'module_version': '1.4.2-GCCcore-12.3.0'}, {'full_module_name': 'libvorbis/1.3.7-GCCcore-12.3.0', 'module_name': 'libvorbis', 'module_version': '1.3.7-GCCcore-12.3.0'}, {'full_module_name': 'libopus/1.4-GCCcore-12.3.0', 'module_name': 'libopus', 'module_version': '1.4-GCCcore-12.3.0'}, {'full_module_name': 'LAME/3.100-GCCcore-12.3.0', 'module_name': 'LAME', 'module_version': '3.100-GCCcore-12.3.0'}, {'full_module_name': 'libsndfile/1.2.2-GCCcore-12.3.0', 'module_name': 'libsndfile', 'module_version': '1.2.2-GCCcore-12.3.0'}, {'full_module_name': 'Szip/2.1.1-GCCcore-12.3.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-12.3.0'}, {'full_module_name': 'HDF5/1.14.0-gompi-2023a', 'module_name': 'HDF5', 'module_version': '1.14.0-gompi-2023a'}, {'full_module_name': 'UDUNITS/2.2.28-GCCcore-12.3.0', 'module_name': 'UDUNITS', 'module_version': '2.2.28-GCCcore-12.3.0'}, {'full_module_name': 'ATK/2.38.0-GCCcore-12.3.0', 'module_name': 'ATK', 'module_version': '2.38.0-GCCcore-12.3.0'}, {'full_module_name': 'at-spi2-core/2.49.91-GCCcore-12.3.0', 'module_name': 'at-spi2-core', 'module_version': '2.49.91-GCCcore-12.3.0'}, {'full_module_name': 'at-spi2-atk/2.38.0-GCCcore-12.3.0', 'module_name': 'at-spi2-atk', 'module_version': '2.38.0-GCCcore-12.3.0'}, {'full_module_name': 'Gdk-Pixbuf/2.42.10-GCCcore-12.3.0', 'module_name': 'Gdk-Pixbuf', 'module_version': '2.42.10-GCCcore-12.3.0'}, {'full_module_name': 'Pango/1.50.14-GCCcore-12.3.0', 'module_name': 'Pango', 'module_version': '1.50.14-GCCcore-12.3.0'}, {'full_module_name': 'libepoxy/1.5.10-GCCcore-12.3.0', 'module_name': 'libepoxy', 'module_version': '1.5.10-GCCcore-12.3.0'}, {'full_module_name': 'Wayland/1.22.0-GCCcore-12.3.0', 'module_name': 'Wayland', 'module_version': '1.22.0-GCCcore-12.3.0'}, {'full_module_name': 'GTK3/3.24.37-GCCcore-12.3.0', 'module_name': 'GTK3', 'module_version': '3.24.37-GCCcore-12.3.0'}, {'full_module_name': 'Ghostscript/10.01.2-GCCcore-12.3.0', 'module_name': 'Ghostscript', 'module_version': '10.01.2-GCCcore-12.3.0'}, {'full_module_name': 'JasPer/4.0.0-GCCcore-12.3.0', 'module_name': 'JasPer', 'module_version': '4.0.0-GCCcore-12.3.0'}, {'full_module_name': 'LittleCMS/2.15-GCCcore-12.3.0', 'module_name': 'LittleCMS', 'module_version': '2.15-GCCcore-12.3.0'}, {'full_module_name': 'ImageMagick/7.1.1-15-GCCcore-12.3.0', 'module_name': 'ImageMagick', 'module_version': '7.1.1-15-GCCcore-12.3.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-12.3.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-12.3.0'}, {'full_module_name': 'nodejs/18.17.1-GCCcore-12.3.0', 'module_name': 'nodejs', 'module_version': '18.17.1-GCCcore-12.3.0'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'netCDF/4.9.2-gompi-2023a', 'module_name': 'netCDF', 'module_version': '4.9.2-gompi-2023a'}, {'full_module_name': 'GEOS/3.12.0-GCC-12.3.0', 'module_name': 'GEOS', 'module_version': '3.12.0-GCC-12.3.0'}, {'full_module_name': 'libarchive/3.6.2-GCCcore-12.3.0', 'module_name': 'libarchive', 'module_version': '3.6.2-GCCcore-12.3.0'}, {'full_module_name': 'nlohmann_json/3.11.2-GCCcore-12.3.0', 'module_name': 'nlohmann_json', 'module_version': '3.11.2-GCCcore-12.3.0'}, {'full_module_name': 'PROJ/9.2.0-GCCcore-12.3.0', 'module_name': 'PROJ', 'module_version': '9.2.0-GCCcore-12.3.0'}, {'full_module_name': 'libgeotiff/1.7.1-GCCcore-12.3.0', 'module_name': 'libgeotiff', 'module_version': '1.7.1-GCCcore-12.3.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-12.3.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-12.3.0'}, {'full_module_name': 'SciPy-bundle/2023.07-gfbf-2023a', 'module_name': 'SciPy-bundle', 'module_version': '2023.07-gfbf-2023a'}, {'full_module_name': 'libtirpc/1.3.3-GCCcore-12.3.0', 'module_name': 'libtirpc', 'module_version': '1.3.3-GCCcore-12.3.0'}, {'full_module_name': 'HDF/4.2.16-2-GCCcore-12.3.0', 'module_name': 'HDF', 'module_version': '4.2.16-2-GCCcore-12.3.0'}, {'full_module_name': 'arpack-ng/3.9.0-foss-2023a', 'module_name': 'arpack-ng', 'module_version': '3.9.0-foss-2023a'}, {'full_module_name': 'Armadillo/12.6.2-foss-2023a', 'module_name': 'Armadillo', 'module_version': '12.6.2-foss-2023a'}, {'full_module_name': 'CFITSIO/4.3.0-GCCcore-12.3.0', 'module_name': 'CFITSIO', 'module_version': '4.3.0-GCCcore-12.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-12.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-12.3.0'}, {'full_module_name': 'json-c/0.16-GCCcore-12.3.0', 'module_name': 'json-c', 'module_version': '0.16-GCCcore-12.3.0'}, {'full_module_name': 'Xerces-C++/3.2.4-GCCcore-12.3.0', 'module_name': 'Xerces-C++', 'module_version': '3.2.4-GCCcore-12.3.0'}, {'full_module_name': 'Imath/3.1.7-GCCcore-12.3.0', 'module_name': 'Imath', 'module_version': '3.1.7-GCCcore-12.3.0'}, {'full_module_name': 'OpenEXR/3.1.7-GCCcore-12.3.0', 'module_name': 'OpenEXR', 'module_version': '3.1.7-GCCcore-12.3.0'}, {'full_module_name': 'Highway/1.0.4-GCCcore-12.3.0', 'module_name': 'Highway', 'module_version': '1.0.4-GCCcore-12.3.0'}, {'full_module_name': 'Brunsli/0.1-GCCcore-12.3.0', 'module_name': 'Brunsli', 'module_version': '0.1-GCCcore-12.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-12.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-12.3.0'}, {'full_module_name': 'LERC/4.0.0-GCCcore-12.3.0', 'module_name': 'LERC', 'module_version': '4.0.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-12.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'SWIG/4.1.1-GCCcore-12.3.0', 'module_name': 'SWIG', 'module_version': '4.1.1-GCCcore-12.3.0'}, {'full_module_name': 'GDAL/3.7.1-foss-2023a', 'module_name': 'GDAL', 'module_version': '3.7.1-foss-2023a'}, {'full_module_name': 'MPFR/4.2.0-GCCcore-12.3.0', 'module_name': 'MPFR', 'module_version': '4.2.0-GCCcore-12.3.0'}, {'full_module_name': 'PostgreSQL/16.1-GCCcore-12.3.0', 'module_name': 'PostgreSQL', 'module_version': '16.1-GCCcore-12.3.0'}, {'full_module_name': 'R-bundle-CRAN/2023.12-foss-2023a', 'module_name': 'R-bundle-CRAN', 'module_version': '2023.12-foss-2023a'}, {'full_module_name': 'snappy/1.1.10-GCCcore-12.3.0', 'module_name': 'snappy', 'module_version': '1.1.10-GCCcore-12.3.0'}, {'full_module_name': 'RapidJSON/1.1.0-20230928-GCCcore-12.3.0', 'module_name': 'RapidJSON', 'module_version': '1.1.0-20230928-GCCcore-12.3.0'}, {'full_module_name': 'Abseil/20230125.3-GCCcore-12.3.0', 'module_name': 'Abseil', 'module_version': '20230125.3-GCCcore-12.3.0'}, {'full_module_name': 'RE2/2023-08-01-GCCcore-12.3.0', 'module_name': 'RE2', 'module_version': '2023-08-01-GCCcore-12.3.0'}, {'full_module_name': 'utf8proc/2.8.0-GCCcore-12.3.0', 'module_name': 'utf8proc', 'module_version': '2.8.0-GCCcore-12.3.0'}, {'full_module_name': 'Arrow/14.0.1-gfbf-2023a', 'module_name': 'Arrow', 'module_version': '14.0.1-gfbf-2023a'}, {'full_module_name': 'arrow-R/14.0.1-foss-2023a-R-4.3.2', 'module_name': 'arrow-R', 'module_version': '14.0.1-foss-2023a-R-4.3.2'}, {'full_module_name': 'R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2', 'module_name': 'R-bundle-Bioconductor', 'module_version': '3.18-foss-2023a-R-4.3.2'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Bioconductor provides tools for the analysis and coprehension\n of high-throughput genomic data.', 'version': '3.18', 'versionsuffix': '-R-4.3.2', 'extensions': [{'type': 'r', 'name': 'BiocGenerics', 'version': '0.48.0'}, {'type': 'r', 'name': 'Biobase', 'version': '2.62.0'}, {'type': 'r', 'name': 'S4Vectors', 'version': '0.40.2'}, {'type': 'r', 'name': 'IRanges', 'version': '2.36.0'}, {'type': 'r', 'name': 'GenomeInfoDbData', 'version': '1.2.11'}, {'type': 'r', 'name': 'GenomeInfoDb', 'version': '1.38.5'}, {'type': 'r', 'name': 'zlibbioc', 'version': '1.48.0'}, {'type': 'r', 'name': 'XVector', 'version': '0.42.0'}, {'type': 'r', 'name': 'Biostrings', 'version': '2.70.0'}, {'type': 'r', 'name': 'KEGGREST', 'version': '1.42.0'}, {'type': 'r', 'name': 'AnnotationDbi', 'version': '1.64.1'}, {'type': 'r', 'name': 'GenomicRanges', 'version': '1.54.1'}, {'type': 'r', 'name': 'BiocParallel', 'version': '1.36.0'}, {'type': 'r', 'name': 'Rhtslib', 'version': '2.4.1'}, {'type': 'r', 'name': 'Rsamtools', 'version': '2.18.0'}, {'type': 'r', 'name': 'MatrixGenerics', 'version': '1.14.0'}, {'type': 'r', 'name': 'S4Arrays', 'version': '1.2.0'}, {'type': 'r', 'name': 'SparseArray', 'version': '1.2.3'}, {'type': 'r', 'name': 'DelayedArray', 'version': '0.28.0'}, {'type': 'r', 'name': 'SummarizedExperiment', 'version': '1.32.0'}, {'type': 'r', 'name': 'GenomicAlignments', 'version': '1.38.2'}, {'type': 'r', 'name': 'ShortRead', 'version': '1.60.0'}, {'type': 'r', 'name': 'graph', 'version': '1.80.0'}, {'type': 'r', 'name': 'affyio', 'version': '1.72.0'}, {'type': 'r', 'name': 'preprocessCore', 'version': '1.64.0'}, {'type': 'r', 'name': 'BiocManager', 'version': '1.30.22'}, {'type': 'r', 'name': 'affy', 'version': '1.80.0'}, {'type': 'r', 'name': 'GO.db', 'version': '3.18.0'}, {'type': 'r', 'name': 'limma', 'version': '3.58.1'}, {'type': 'r', 'name': 'RBGL', 'version': '1.78.0'}, {'type': 'r', 'name': 'org.Hs.eg.db', 'version': '3.18.0'}, {'type': 'r', 'name': 'AnnotationForge', 'version': '1.44.0'}, {'type': 'r', 'name': 'annaffy', 'version': '1.74.0'}, {'type': 'r', 'name': 'gcrma', 'version': '2.74.0'}, {'type': 'r', 'name': 'oligoClasses', 'version': '1.64.0'}, {'type': 'r', 'name': 'edgeR', 'version': '4.0.12'}, {'type': 'r', 'name': 'PFAM.db', 'version': '3.18.0'}, {'type': 'r', 'name': 'perm', 'version': '1.0-0.4'}, {'type': 'r', 'name': 'baySeq', 'version': '2.36.0'}, {'type': 'r', 'name': 'qvalue', 'version': '2.34.0'}, {'type': 'r', 'name': 'impute', 'version': '1.76.0'}, {'type': 'r', 'name': 'shinyFiles', 'version': '0.9.3'}, {'type': 'r', 'name': 'samr', 'version': '3.0'}, {'type': 'r', 'name': 'DEGseq', 'version': '1.56.1'}, {'type': 'r', 'name': 'hgu133plus2.db', 'version': '3.13.0'}, {'type': 'r', 'name': 'illuminaio', 'version': '0.44.0'}, {'type': 'r', 'name': 'BiocIO', 'version': '1.12.0'}, {'type': 'r', 'name': 'restfulr', 'version': '0.0.15'}, {'type': 'r', 'name': 'rtracklayer', 'version': '1.62.0'}, {'type': 'r', 'name': 'filelock', 'version': '1.0.3'}, {'type': 'r', 'name': 'BiocFileCache', 'version': '2.10.1'}, {'type': 'r', 'name': 'biomaRt', 'version': '2.58.0'}, {'type': 'r', 'name': 'GenomicFeatures', 'version': '1.54.1'}, {'type': 'r', 'name': 'bumphunter', 'version': '1.44.0'}, {'type': 'r', 'name': 'multtest', 'version': '2.58.0'}, {'type': 'r', 'name': 'scrime', 'version': '1.3.5'}, {'type': 'r', 'name': 'siggenes', 'version': '1.76.0'}, {'type': 'r', 'name': 'DynDoc', 'version': '1.80.0'}, {'type': 'r', 'name': 'NOISeq', 'version': '2.46.0'}, {'type': 'r', 'name': 'Rgraphviz', 'version': '2.46.0'}, {'type': 'r', 'name': 'RNASeqPower', 'version': '1.42.0'}, {'type': 'r', 'name': 'annotate', 'version': '1.80.0'}, {'type': 'r', 'name': 'GSEABase', 'version': '1.64.0'}, {'type': 'r', 'name': 'genefilter', 'version': '1.84.0'}, {'type': 'r', 'name': 'Category', 'version': '2.68.0'}, {'type': 'r', 'name': 'GOstats', 'version': '2.68.0'}, {'type': 'r', 'name': 'BSgenome', 'version': '1.70.1'}, {'type': 'r', 'name': 'VariantAnnotation', 'version': '1.48.1'}, {'type': 'r', 'name': 'interactiveDisplayBase', 'version': '1.40.0'}, {'type': 'r', 'name': 'BiocVersion', 'version': '3.18.1'}, {'type': 'r', 'name': 'AnnotationHub', 'version': '3.10.0'}, {'type': 'r', 'name': 'AnnotationFilter', 'version': '1.26.0'}, {'type': 'r', 'name': 'ProtGenerics', 'version': '1.34.0'}, {'type': 'r', 'name': 'ensembldb', 'version': '2.26.0'}, {'type': 'r', 'name': 'biovizBase', 'version': '1.50.0'}, {'type': 'r', 'name': 'OrganismDbi', 'version': '1.44.0'}, {'type': 'r', 'name': 'ggbio', 'version': '1.50.0'}, {'type': 'r', 'name': 'geneplotter', 'version': '1.80.0'}, {'type': 'r', 'name': 'DESeq2', 'version': '1.42.0'}, {'type': 'r', 'name': 'ReportingTools', 'version': '2.42.3'}, {'type': 'r', 'name': 'Glimma', 'version': '2.12.0'}, {'type': 'r', 'name': 'affycoretools', 'version': '1.74.0'}, {'type': 'r', 'name': 'TxDb.Hsapiens.UCSC.hg19.knownGene', 'version': '3.2.2'}, {'type': 'r', 'name': 'Homo.sapiens', 'version': '1.3.1'}, {'type': 'r', 'name': 'BSgenome.Hsapiens.UCSC.hg19', 'version': '1.4.3'}, {'type': 'r', 'name': 'AgiMicroRna', 'version': '2.52.0'}, {'type': 'r', 'name': 'geneLenDataBase', 'version': '1.38.0'}, {'type': 'r', 'name': 'goseq', 'version': '1.54.0'}, {'type': 'r', 'name': 'KEGGgraph', 'version': '1.62.0'}, {'type': 'r', 'name': 'GEOquery', 'version': '2.70.0'}, {'type': 'r', 'name': 'rARPACK', 'version': '0.11-0'}, {'type': 'r', 'name': 'mixOmics', 'version': '6.26.0'}, {'type': 'r', 'name': 'Rhdf5lib', 'version': '1.24.1'}, {'type': 'r', 'name': 'rhdf5filters', 'version': '1.14.1'}, {'type': 'r', 'name': 'rhdf5', 'version': '2.46.1'}, {'type': 'r', 'name': 'HDF5Array', 'version': '1.30.0'}, {'type': 'r', 'name': 'sparseMatrixStats', 'version': '1.14.0'}, {'type': 'r', 'name': 'DelayedMatrixStats', 'version': '1.24.0'}, {'type': 'r', 'name': 'minfi', 'version': '1.48.0'}, {'type': 'r', 'name': 'FDb.InfiniumMethylation.hg19', 'version': '2.2.0'}, {'type': 'r', 'name': 'methylumi', 'version': '2.48.0'}, {'type': 'r', 'name': 'lumi', 'version': '2.54.0'}, {'type': 'r', 'name': 'widgetTools', 'version': '1.80.0'}, {'type': 'r', 'name': 'tkWidgets', 'version': '1.80.0'}, {'type': 'r', 'name': 'Mfuzz', 'version': '2.62.0'}, {'type': 'r', 'name': 'venn', 'version': '1.12'}, {'type': 'r', 'name': 'maSigPro', 'version': '1.74.0'}, {'type': 'r', 'name': 'SPIA', 'version': '2.54.0'}, {'type': 'r', 'name': 'Gviz', 'version': '1.46.1'}, {'type': 'r', 'name': 'cummeRbund', 'version': '2.44.0'}, {'type': 'r', 'name': 'GenomicFiles', 'version': '1.38.0'}, {'type': 'r', 'name': 'derfinderHelper', 'version': '1.36.0'}, {'type': 'r', 'name': 'derfinder', 'version': '1.36.0'}, {'type': 'r', 'name': 'polyester', 'version': '1.38.0'}, {'type': 'r', 'name': 'Rsubread', 'version': '2.16.1'}, {'type': 'r', 'name': 'pcaMethods', 'version': '1.94.0'}, {'type': 'r', 'name': 'marray', 'version': '1.80.0'}, {'type': 'r', 'name': 'CGHbase', 'version': '1.62.0'}, {'type': 'r', 'name': 'Wrench', 'version': '1.20.0'}, {'type': 'r', 'name': 'lpsymphony', 'version': '1.30.0'}, {'type': 'r', 'name': 'IHW', 'version': '1.30.0'}, {'type': 'r', 'name': 'metagenomeSeq', 'version': '1.43.0'}, {'type': 'r', 'name': 'gdsfmt', 'version': '1.38.0'}, {'type': 'r', 'name': 'SNPRelate', 'version': '1.36.0'}, {'type': 'r', 'name': 'biomformat', 'version': '1.30.0'}, {'type': 'r', 'name': 'phyloseq', 'version': '1.46.0'}, {'type': 'r', 'name': 'NADA', 'version': '1.6-1.1'}, {'type': 'r', 'name': 'zCompositions', 'version': '1.5.0-1'}, {'type': 'r', 'name': 'RcppZiggurat', 'version': '0.1.6'}, {'type': 'r', 'name': 'Rfast', 'version': '2.1.0'}, {'type': 'r', 'name': 'directlabels', 'version': '2024.1.21'}, {'type': 'r', 'name': 'ALDEx2', 'version': '1.34.0'}, {'type': 'r', 'name': 'dada2', 'version': '1.30.0'}, {'type': 'r', 'name': 'LEA', 'version': '3.14.0'}, {'type': 'r', 'name': 'tximport', 'version': '1.30.0'}, {'type': 'r', 'name': 'SingleCellExperiment', 'version': '1.24.0'}, {'type': 'r', 'name': 'beachmat', 'version': '2.18.0'}, {'type': 'r', 'name': 'RcppAnnoy', 'version': '0.0.22'}, {'type': 'r', 'name': 'RcppHNSW', 'version': '0.5.0'}, {'type': 'r', 'name': 'BiocNeighbors', 'version': '1.20.2'}, {'type': 'r', 'name': 'rsvd', 'version': '1.0.5'}, {'type': 'r', 'name': 'ScaledMatrix', 'version': '1.10.0'}, {'type': 'r', 'name': 'BiocSingular', 'version': '1.18.0'}, {'type': 'r', 'name': 'scuttle', 'version': '1.12.0'}, {'type': 'r', 'name': 'RcppML', 'version': '0.3.7'}, {'type': 'r', 'name': 'sitmo', 'version': '2.0.2'}, {'type': 'r', 'name': 'dqrng', 'version': '0.3.2'}, {'type': 'r', 'name': 'uwot', 'version': '0.1.16'}, {'type': 'r', 'name': 'ggrastr', 'version': '1.0.2'}, {'type': 'r', 'name': 'scater', 'version': '1.30.1'}, {'type': 'r', 'name': 'bluster', 'version': '1.12.0'}, {'type': 'r', 'name': 'metapod', 'version': '1.10.1'}, {'type': 'r', 'name': 'scran', 'version': '1.30.2'}, {'type': 'r', 'name': 'SC3', 'version': '1.30.0'}, {'type': 'r', 'name': 'ComplexHeatmap', 'version': '2.18.0'}, {'type': 'r', 'name': 'GENIE3', 'version': '1.24.0'}, {'type': 'r', 'name': 'dupRadar', 'version': '1.32.0'}, {'type': 'r', 'name': 'DNAcopy', 'version': '1.76.0'}, {'type': 'r', 'name': 'sva', 'version': '3.50.0'}, {'type': 'r', 'name': 'ballgown', 'version': '2.34.0'}, {'type': 'r', 'name': 'DropletUtils', 'version': '1.22.0'}, {'type': 'r', 'name': 'DeconRNASeq', 'version': '1.44.0'}, {'type': 'r', 'name': 'GSVA', 'version': '1.50.0'}, {'type': 'r', 'name': 'PureCN', 'version': '2.8.1'}, {'type': 'r', 'name': 'globaltest', 'version': '5.56.0'}, {'type': 'r', 'name': 'GlobalAncova', 'version': '4.20.0'}, {'type': 'r', 'name': 'vsn', 'version': '3.70.0'}, {'type': 'r', 'name': 'mzID', 'version': '1.40.0'}, {'type': 'r', 'name': 'mzR', 'version': '2.36.0'}, {'type': 'r', 'name': 'MsCoreUtils', 'version': '1.14.1'}, {'type': 'r', 'name': 'MSnbase', 'version': '2.28.1'}, {'type': 'r', 'name': 'MassSpecWavelet', 'version': '1.68.0'}, {'type': 'r', 'name': 'MsFeatures', 'version': '1.10.0'}, {'type': 'r', 'name': 'MetaboCoreUtils', 'version': '1.10.0'}, {'type': 'r', 'name': 'Spectra', 'version': '1.12.0'}, {'type': 'r', 'name': 'BiocBaseUtils', 'version': '1.4.0'}, {'type': 'r', 'name': 'MultiAssayExperiment', 'version': '1.28.0'}, {'type': 'r', 'name': 'QFeatures', 'version': '1.12.0'}, {'type': 'r', 'name': 'MsExperiment', 'version': '1.4.0'}, {'type': 'r', 'name': 'xcms', 'version': '4.0.2'}, {'type': 'r', 'name': 'CAMERA', 'version': '1.58.0'}, {'type': 'r', 'name': 'fgsea', 'version': '1.28.0'}, {'type': 'r', 'name': 'GWASExactHW', 'version': '1.01'}, {'type': 'r', 'name': 'quantsmooth', 'version': '1.68.0'}, {'type': 'r', 'name': 'GWASTools', 'version': '1.48.0'}, {'type': 'r', 'name': 'SeqArray', 'version': '1.42.0'}, {'type': 'r', 'name': 'SeqVarTools', 'version': '1.40.0'}, {'type': 'r', 'name': 'GENESIS', 'version': '2.32.0'}, {'type': 'r', 'name': 'MLInterfaces', 'version': '1.82.0'}, {'type': 'r', 'name': 'pRoloc', 'version': '1.42.0'}, {'type': 'r', 'name': 'pRolocdata', 'version': '1.40.0'}, {'type': 'r', 'name': 'fresh', 'version': '0.2.0'}, {'type': 'r', 'name': 'waiter', 'version': '0.2.5'}, {'type': 'r', 'name': 'shinydashboardPlus', 'version': '2.0.3'}, {'type': 'r', 'name': 'shinyhelper', 'version': '0.3.2'}, {'type': 'r', 'name': 'anytime', 'version': '0.3.9'}, {'type': 'r', 'name': 'shinyWidgets', 'version': '0.8.1'}, {'type': 'r', 'name': 'pRolocGUI', 'version': '2.12.0'}, {'type': 'r', 'name': 'EBImage', 'version': '4.44.0'}, {'type': 'r', 'name': 'GenomicScores', 'version': '2.14.3'}, {'type': 'r', 'name': 'BSgenome.Mmusculus.UCSC.mm10', 'version': '1.4.3'}, {'type': 'r', 'name': 'TxDb.Mmusculus.UCSC.mm10.knownGene', 'version': '3.10.0'}, {'type': 'r', 'name': 'regioneR', 'version': '1.34.0'}, {'type': 'r', 'name': 'InteractionSet', 'version': '1.30.0'}, {'type': 'r', 'name': 'ChIPpeakAnno', 'version': '3.36.0'}, {'type': 'r', 'name': 'seqLogo', 'version': '1.68.0'}, {'type': 'r', 'name': 'rGADEM', 'version': '2.50.0'}, {'type': 'r', 'name': 'MotifDb', 'version': '1.44.0'}, {'type': 'r', 'name': 'poweRlaw', 'version': '0.70.6'}, {'type': 'r', 'name': 'CNEr', 'version': '1.38.0'}, {'type': 'r', 'name': 'DirichletMultinomial', 'version': '1.44.0'}, {'type': 'r', 'name': 'TFMPvalue', 'version': '0.0.9'}, {'type': 'r', 'name': 'TFBSTools', 'version': '1.40.0'}, {'type': 'r', 'name': 'motifStack', 'version': '1.46.0'}, {'type': 'r', 'name': 'ATACseqQC', 'version': '1.26.0'}, {'type': 'r', 'name': 'ResidualMatrix', 'version': '1.12.0'}, {'type': 'r', 'name': 'batchelor', 'version': '1.18.1'}, {'type': 'r', 'name': 'gsmoothr', 'version': '0.1.7'}, {'type': 'r', 'name': 'Ringo', 'version': '1.66.0'}, {'type': 'r', 'name': 'R.devices', 'version': '2.17.1'}, {'type': 'r', 'name': 'R.filesets', 'version': '2.15.0'}, {'type': 'r', 'name': 'aroma.light', 'version': '3.32.0'}, {'type': 'r', 'name': 'PSCBS', 'version': '0.66.0'}, {'type': 'r', 'name': 'aroma.core', 'version': '3.3.0'}, {'type': 'r', 'name': 'R.huge', 'version': '0.10.1'}, {'type': 'r', 'name': 'aroma.apd', 'version': '0.7.0'}, {'type': 'r', 'name': 'aroma.affymetrix', 'version': '3.2.1'}, {'type': 'r', 'name': 'Repitools', 'version': '1.48.0'}, {'type': 'r', 'name': 'BSgenome.Hsapiens.UCSC.hg38', 'version': '1.4.5'}, {'type': 'r', 'name': 'MEDIPS', 'version': '1.54.0'}, {'type': 'r', 'name': 'RProtoBufLib', 'version': '2.14.0'}, {'type': 'r', 'name': 'BH', 'version': '1.84.0-0'}, {'type': 'r', 'name': 'cytolib', 'version': '2.14.1'}, {'type': 'r', 'name': 'flowCore', 'version': '2.14.0'}, {'type': 'r', 'name': 'mutoss', 'version': '0.1-13'}, {'type': 'r', 'name': 'qqconf', 'version': '1.3.2'}, {'type': 'r', 'name': 'metap', 'version': '1.9'}, {'type': 'r', 'name': 'scattermore', 'version': '1.2'}, {'type': 'r', 'name': 'SeuratObject', 'version': '5.0.1'}, {'type': 'r', 'name': 'Seurat', 'version': '5.0.1'}, {'type': 'r', 'name': 'ALL', 'version': '1.44.0'}, {'type': 'r', 'name': 'ConsensusClusterPlus', 'version': '1.66.0'}, {'type': 'r', 'name': 'flowViz', 'version': '1.66.0'}, {'type': 'r', 'name': 'ncdfFlow', 'version': '2.48.0'}, {'type': 'r', 'name': 'aws.signature', 'version': '0.6.0'}, {'type': 'r', 'name': 'aws.s3', 'version': '0.3.21'}, {'type': 'r', 'name': 'flowWorkspace', 'version': '4.14.2'}, {'type': 'r', 'name': 'ash', 'version': '1.0-15'}, {'type': 'r', 'name': 'hdrcde', 'version': '3.4'}, {'type': 'r', 'name': 'rainbow', 'version': '3.8'}, {'type': 'r', 'name': 'fds', 'version': '1.8'}, {'type': 'r', 'name': 'fda', 'version': '6.1.4'}, {'type': 'r', 'name': 'flowStats', 'version': '4.14.1'}, {'type': 'r', 'name': 'flowClust', 'version': '3.40.0'}, {'type': 'r', 'name': 'openCyto', 'version': '2.14.0'}, {'type': 'r', 'name': 'ggcyto', 'version': '1.30.0'}, {'type': 'r', 'name': 'CytoML', 'version': '2.14.0'}, {'type': 'r', 'name': 'colorRamps', 'version': '2.3.1'}, {'type': 'r', 'name': 'ggnewscale', 'version': '0.4.9'}, {'type': 'r', 'name': 'ggpointdensity', 'version': '0.1.0'}, {'type': 'r', 'name': 'FlowSOM', 'version': '2.10.0'}, {'type': 'r', 'name': 'HMMcopy', 'version': '1.44.0'}, {'type': 'r', 'name': 'diffcyt', 'version': '1.22.0'}, {'type': 'r', 'name': 'blme', 'version': '1.0-5'}, {'type': 'r', 'name': 'remaCor', 'version': '0.0.16'}, {'type': 'r', 'name': 'fANCOVA', 'version': '0.6-1'}, {'type': 'r', 'name': 'variancePartition', 'version': '1.32.2'}, {'type': 'r', 'name': 'muscat', 'version': '1.16.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylation450kmanifest', 'version': '0.4.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICmanifest', 'version': '0.3.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylation450kanno.ilmn12.hg19', 'version': '0.6.1'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICanno.ilm10b2.hg19', 'version': '0.6.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICanno.ilm10b4.hg19', 'version': '0.6.0'}, {'type': 'r', 'name': 'conumee', 'version': '1.36.0'}, {'type': 'r', 'name': 'BSgenome.Cfamiliaris.UCSC.canFam3', 'version': '1.4.0'}, {'type': 'r', 'name': 'ExperimentHub', 'version': '2.10.0'}, {'type': 'r', 'name': 'SingleR', 'version': '2.4.1'}, {'type': 'r', 'name': 'FlowSorted.Blood.EPIC', 'version': '2.6.0'}, {'type': 'r', 'name': 'FlowSorted.CordBloodCombined.450k', 'version': '1.18.0'}, {'type': 'r', 'name': 'DRIMSeq', 'version': '1.30.0'}, {'type': 'r', 'name': 'stageR', 'version': '1.24.0'}, {'type': 'r', 'name': 'isva', 'version': '1.9'}, {'type': 'r', 'name': 'org.Mm.eg.db', 'version': '3.18.0'}, {'type': 'r', 'name': 'org.Rn.eg.db', 'version': '3.18.0'}, {'type': 'r', 'name': 'ROC', 'version': '1.78.0'}, {'type': 'r', 'name': 'wateRmelon', 'version': '2.8.0'}, {'type': 'r', 'name': 'GLAD', 'version': '2.66.0'}, {'type': 'r', 'name': 'missMethyl', 'version': '1.36.0'}, {'type': 'r', 'name': 'MethylSeekR', 'version': '1.42.0'}, {'type': 'r', 'name': 'affxparser', 'version': '1.74.0'}, {'type': 'r', 'name': 'ccdata', 'version': '1.28.0'}, {'type': 'r', 'name': 'lsa', 'version': '0.73.3'}, {'type': 'r', 'name': 'ccmap', 'version': '1.28.0'}, {'type': 'r', 'name': 'oligo', 'version': '1.66.0'}, {'type': 'r', 'name': 'SMVar', 'version': '1.3.4'}, {'type': 'r', 'name': 'metaMA', 'version': '3.1.3'}, {'type': 'r', 'name': 'randomcoloR', 'version': '1.1.0.1'}, {'type': 'r', 'name': 'shinyBS', 'version': '0.61.1'}, {'type': 'r', 'name': 'shinypanel', 'version': '0.1.5'}, {'type': 'r', 'name': 'crossmeta', 'version': '1.28.0'}, {'type': 'r', 'name': 'snpStats', 'version': '1.52.0'}, {'type': 'r', 'name': 'mixsqp', 'version': '0.3-54'}, {'type': 'r', 'name': 'susieR', 'version': '0.12.35'}, {'type': 'r', 'name': 'coloc', 'version': '5.2.3'}, {'type': 'r', 'name': 'SCANVIS', 'version': '1.16.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v86', 'version': '2.99.0'}, {'type': 'r', 'name': 'agricolae', 'version': '1.3-7'}, {'type': 'r', 'name': 'bookdown', 'version': '0.37'}, {'type': 'r', 'name': 'BiocStyle', 'version': '2.30.0'}, {'type': 'r', 'name': 'estimability', 'version': '1.4.1'}, {'type': 'r', 'name': 'emmeans', 'version': '1.10.0'}, {'type': 'r', 'name': 'ggdendro', 'version': '0.1.23'}, {'type': 'r', 'name': 'pmp', 'version': '1.14.0'}, {'type': 'r', 'name': 'MultiDataSet', 'version': '1.30.0'}, {'type': 'r', 'name': 'ropls', 'version': '1.34.0'}, {'type': 'r', 'name': 'ontologyIndex', 'version': '2.11'}, {'type': 'r', 'name': 'rols', 'version': '2.30.0'}, {'type': 'r', 'name': 'struct', 'version': '1.14.0'}, {'type': 'r', 'name': 'ggthemes', 'version': '5.0.0'}, {'type': 'r', 'name': 'structToolbox', 'version': '1.14.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v75', 'version': '2.99.0'}, {'type': 'r', 'name': 'ggseqlogo', 'version': '0.1'}, {'type': 'r', 'name': 'sparsesvd', 'version': '0.2-2'}, {'type': 'r', 'name': 'docopt', 'version': '0.7.1'}, {'type': 'r', 'name': 'qlcMatrix', 'version': '0.9.7'}, {'type': 'r', 'name': 'Signac', 'version': '1.12.0'}, {'type': 'r', 'name': 'motifmatchr', 'version': '1.24.0'}, {'type': 'r', 'name': 'extraDistr', 'version': '1.10.0'}, {'type': 'r', 'name': 'PRROC', 'version': '1.3.1'}, {'type': 'r', 'name': 'TSP', 'version': '1.2-4'}, {'type': 'r', 'name': 'qap', 'version': '0.1-2'}, {'type': 'r', 'name': 'ca', 'version': '0.71.1'}, {'type': 'r', 'name': 'seriation', 'version': '1.5.4'}, {'type': 'r', 'name': 'egg', 'version': '0.4.5'}, {'type': 'r', 'name': 'heatmaply', 'version': '1.5.0'}, {'type': 'r', 'name': 'OUTRIDER', 'version': '1.20.0'}, {'type': 'r', 'name': 'FRASER', 'version': '1.14.0'}, {'type': 'r', 'name': 'JASPAR2020', 'version': '0.99.10'}, {'type': 'r', 'name': 'AUCell', 'version': '1.24.0'}, {'type': 'r', 'name': 'RcisTarget', 'version': '1.22.0'}, {'type': 'r', 'name': 'NMF', 'version': '0.26'}, {'type': 'r', 'name': 'densEstBayes', 'version': '1.0-2.2'}, {'type': 'r', 'name': 'reldist', 'version': '1.7-2'}, {'type': 'r', 'name': 'M3Drop', 'version': '1.28.0'}, {'type': 'r', 'name': 'bsseq', 'version': '1.38.0'}, {'type': 'r', 'name': 'DSS', 'version': '2.50.1'}, {'type': 'r', 'name': 'pathview', 'version': '1.42.0'}, {'type': 'r', 'name': 'chromVAR', 'version': '1.24.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v79', 'version': '2.99.0'}, {'type': 'r', 'name': 'WGCNA', 'version': '1.72-5'}, {'type': 'r', 'name': 'DNABarcodes', 'version': '1.32.0'}, {'type': 'r', 'name': 'GenomicInteractions', 'version': '1.36.0'}, {'type': 'r', 'name': 'CAGEfightR', 'version': '1.22.0'}, {'type': 'r', 'name': 'CAGEr', 'version': '2.8.0'}, {'type': 'r', 'name': 'SPOTlight', 'version': '1.6.7'}, {'type': 'r', 'name': 'CGHcall', 'version': '2.64.0'}, {'type': 'r', 'name': 'QDNAseq', 'version': '1.38.0'}, {'type': 'r', 'name': 'HiCcompare', 'version': '1.24.0'}, {'type': 'r', 'name': 'ROntoTools', 'version': '2.30.0'}, {'type': 'r', 'name': 'scDblFinder', 'version': '1.16.0'}, {'type': 'r', 'name': 'treeio', 'version': '1.26.0'}, {'type': 'r', 'name': 'ggtree', 'version': '3.10.0'}, {'type': 'r', 'name': 'scistreer', 'version': '1.2.0'}, {'type': 'r', 'name': 'numbat', 'version': '1.3.2-1'}, {'type': 'r', 'name': 'HiCBricks', 'version': '1.20.0'}, {'type': 'r', 'name': 'dir.expiry', 'version': '1.10.0'}, {'type': 'r', 'name': 'basilisk.utils', 'version': '1.14.1'}, {'type': 'r', 'name': 'basilisk', 'version': '1.14.2'}, {'type': 'r', 'name': 'zellkonverter', 'version': '1.12.1'}, {'type': 'r', 'name': 'DO.db', 'version': '2.9'}, {'type': 'r', 'name': 'GOSemSim', 'version': '2.28.1'}, {'type': 'r', 'name': 'HDO.db', 'version': '0.99.1'}, {'type': 'r', 'name': 'DOSE', 'version': '3.28.2'}, {'type': 'r', 'name': 'enrichplot', 'version': '1.22.0'}, {'type': 'r', 'name': 'gson', 'version': '0.1.0'}, {'type': 'r', 'name': 'clusterProfiler', 'version': '4.10.0'}, {'type': 'r', 'name': 'reactome.db', 'version': '1.86.2'}, {'type': 'r', 'name': 'graphite', 'version': '1.48.0'}, {'type': 'r', 'name': 'ReactomePA', 'version': '1.46.0'}, {'type': 'r', 'name': 'flowClean', 'version': '1.40.0'}, {'type': 'r', 'name': 'flowAI', 'version': '1.32.0'}, {'type': 'r', 'name': 'flowFP', 'version': '1.60.0'}, {'type': 'r', 'name': 'simplifyEnrichment', 'version': '1.12.0'}, {'type': 'r', 'name': 'RPMG', 'version': '2.2-7'}, {'type': 'r', 'name': 'Rwave', 'version': '2.6-5'}, {'type': 'r', 'name': 'RSEIS', 'version': '4.1-6'}, {'type': 'r', 'name': 'splancs', 'version': '2.01-44'}, {'type': 'r', 'name': 'MBA', 'version': '0.1-0'}, {'type': 'r', 'name': 'GEOmap', 'version': '2.5-5'}, {'type': 'r', 'name': 'RFOC', 'version': '3.4-10'}, {'type': 'r', 'name': 'flowDensity', 'version': '1.36.1'}, {'type': 'r', 'name': 'flowPeaks', 'version': '1.48.0'}, {'type': 'r', 'name': 'SamSPECTRAL', 'version': '1.56.0'}, {'type': 'r', 'name': 'ddPCRclust', 'version': '1.22.0'}, {'type': 'r', 'name': 'feature', 'version': '1.2.15'}, {'type': 'r', 'name': 'flowMerge', 'version': '2.50.0'}, {'type': 'r', 'name': 'SpatialExperiment', 'version': '1.12.0'}, {'type': 'r', 'name': 'TrajectoryUtils', 'version': '1.10.0'}, {'type': 'r', 'name': 'slingshot', 'version': '2.10.0'}, {'type': 'r', 'name': 'TreeSummarizedExperiment', 'version': '2.10.0'}, {'type': 'r', 'name': 'decontam', 'version': '1.22.0'}, {'type': 'r', 'name': 'DECIPHER', 'version': '2.30.0'}, {'type': 'r', 'name': 'mia', 'version': '1.10.0'}, {'type': 'r', 'name': 'ANCOMBC', 'version': '2.4.0'}, {'type': 'r', 'name': 'decoupleR', 'version': '2.8.0'}, {'type': 'r', 'name': 'UCell', 'version': '2.6.2'}, {'type': 'r', 'name': 'intervals', 'version': '0.15.4'}, {'type': 'r', 'name': 'oompaBase', 'version': '3.2.9'}, {'type': 'r', 'name': 'oompaData', 'version': '3.1.3'}, {'type': 'r', 'name': 'TailRank', 'version': '3.2.2'}, {'type': 'r', 'name': 'RnBeads', 'version': '2.20.0'}, {'type': 'r', 'name': 'RnBeads.hg19', 'version': '1.34.0'}, {'type': 'r', 'name': 'RnBeads.hg38', 'version': '1.34.0'}, {'type': 'r', 'name': 'RnBeads.mm9', 'version': '1.34.0'}, {'type': 'r', 'name': 'RnBeads.mm10', 'version': '2.10.0'}, {'type': 'r', 'name': 'RnBeads.rn5', 'version': '1.34.0'}, {'type': 'r', 'name': 'log4r', 'version': '0.4.3'}, {'type': 'r', 'name': 'MSstatsConvert', 'version': '1.12.0'}, {'type': 'r', 'name': 'MSstats', 'version': '4.10.0'}, {'type': 'r', 'name': 'MSstatsTMT', 'version': '2.10.0'}, {'type': 'r', 'name': 'MSstatsPTM', 'version': '2.4.2'}, {'type': 'r', 'name': 'factoextra', 'version': '1.0.7'}, {'type': 'r', 'name': 'MSstatsLiP', 'version': '1.8.1'}, {'type': 'r', 'name': 'babelgene', 'version': '22.9'}, {'type': 'r', 'name': 'msigdbr', 'version': '7.5.1'}, {'type': 'r', 'name': 'escape', 'version': '1.12.0'}, {'type': 'r', 'name': 'plyranges', 'version': '1.22.0'}, {'type': 'r', 'name': 'seqPattern', 'version': '1.34.0'}, {'type': 'r', 'name': 'genomation', 'version': '1.34.0'}, {'type': 'r', 'name': 'ChIPseeker', 'version': '1.38.0'}, {'type': 'r', 'name': 'SimBu', 'version': '1.4.3'}]}, {'homepage': 'https://bioconductor.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2024a'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2', 'module_name': 'R-bundle-Bioconductor', 'module_version': '3.20-foss-2024a-R-4.4.2'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'GCC/13.3.0', 'module_name': 'GCC', 'module_version': '13.3.0'}, {'full_module_name': 'numactl/2.0.18-GCCcore-13.3.0', 'module_name': 'numactl', 'module_version': '2.0.18-GCCcore-13.3.0'}, {'full_module_name': 'libxml2/2.12.7-GCCcore-13.3.0', 'module_name': 'libxml2', 'module_version': '2.12.7-GCCcore-13.3.0'}, {'full_module_name': 'libpciaccess/0.18.1-GCCcore-13.3.0', 'module_name': 'libpciaccess', 'module_version': '0.18.1-GCCcore-13.3.0'}, {'full_module_name': 'hwloc/2.10.0-GCCcore-13.3.0', 'module_name': 'hwloc', 'module_version': '2.10.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.3.0'}, {'full_module_name': 'UCX/1.16.0-GCCcore-13.3.0', 'module_name': 'UCX', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'libfabric/1.21.0-GCCcore-13.3.0', 'module_name': 'libfabric', 'module_version': '1.21.0-GCCcore-13.3.0'}, {'full_module_name': 'PMIx/5.0.2-GCCcore-13.3.0', 'module_name': 'PMIx', 'module_version': '5.0.2-GCCcore-13.3.0'}, {'full_module_name': 'PRRTE/3.0.5-GCCcore-13.3.0', 'module_name': 'PRRTE', 'module_version': '3.0.5-GCCcore-13.3.0'}, {'full_module_name': 'UCC/1.3.0-GCCcore-13.3.0', 'module_name': 'UCC', 'module_version': '1.3.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenMPI/5.0.3-GCC-13.3.0', 'module_name': 'OpenMPI', 'module_version': '5.0.3-GCC-13.3.0'}, {'full_module_name': 'OpenBLAS/0.3.27-GCC-13.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.27-GCC-13.3.0'}, {'full_module_name': 'FlexiBLAS/3.4.4-GCC-13.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.4.4-GCC-13.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.3.0'}, {'full_module_name': 'gompi/2024a', 'module_name': 'gompi', 'module_version': '2024a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2024a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2024a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2024a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2024a-fb'}, {'full_module_name': 'foss/2024a', 'module_name': 'foss', 'module_version': '2024a'}, {'full_module_name': 'gfbf/2024a', 'module_name': 'gfbf', 'module_version': '2024a'}, {'full_module_name': 'expat/2.6.2-GCCcore-13.3.0', 'module_name': 'expat', 'module_version': '2.6.2-GCCcore-13.3.0'}, {'full_module_name': 'libpng/1.6.43-GCCcore-13.3.0', 'module_name': 'libpng', 'module_version': '1.6.43-GCCcore-13.3.0'}, {'full_module_name': 'Brotli/1.1.0-GCCcore-13.3.0', 'module_name': 'Brotli', 'module_version': '1.1.0-GCCcore-13.3.0'}, {'full_module_name': 'freetype/2.13.2-GCCcore-13.3.0', 'module_name': 'freetype', 'module_version': '2.13.2-GCCcore-13.3.0'}, {'full_module_name': 'fontconfig/2.15.0-GCCcore-13.3.0', 'module_name': 'fontconfig', 'module_version': '2.15.0-GCCcore-13.3.0'}, {'full_module_name': 'xorg-macros/1.20.1-GCCcore-13.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.1-GCCcore-13.3.0'}, {'full_module_name': 'X11/20240607-GCCcore-13.3.0', 'module_name': 'X11', 'module_version': '20240607-GCCcore-13.3.0'}, {'full_module_name': 'gzip/1.13-GCCcore-13.3.0', 'module_name': 'gzip', 'module_version': '1.13-GCCcore-13.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-13.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-13.3.0'}, {'full_module_name': 'zstd/1.5.6-GCCcore-13.3.0', 'module_name': 'zstd', 'module_version': '1.5.6-GCCcore-13.3.0'}, {'full_module_name': 'libdrm/2.4.122-GCCcore-13.3.0', 'module_name': 'libdrm', 'module_version': '2.4.122-GCCcore-13.3.0'}, {'full_module_name': 'libglvnd/1.7.0-GCCcore-13.3.0', 'module_name': 'libglvnd', 'module_version': '1.7.0-GCCcore-13.3.0'}, {'full_module_name': 'libunwind/1.8.1-GCCcore-13.3.0', 'module_name': 'libunwind', 'module_version': '1.8.1-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'LLVM/18.1.8-GCCcore-13.3.0-minimal', 'module_name': 'LLVM', 'module_version': '18.1.8-GCCcore-13.3.0-minimal'}, {'full_module_name': 'Wayland/1.23.0-GCCcore-13.3.0', 'module_name': 'Wayland', 'module_version': '1.23.0-GCCcore-13.3.0'}, {'full_module_name': 'Mesa/24.1.3-GCCcore-13.3.0', 'module_name': 'Mesa', 'module_version': '24.1.3-GCCcore-13.3.0'}, {'full_module_name': 'libGLU/9.0.3-GCCcore-13.3.0', 'module_name': 'libGLU', 'module_version': '9.0.3-GCCcore-13.3.0'}, {'full_module_name': 'pixman/0.43.4-GCCcore-13.3.0', 'module_name': 'pixman', 'module_version': '0.43.4-GCCcore-13.3.0'}, {'full_module_name': 'PCRE2/10.43-GCCcore-13.3.0', 'module_name': 'PCRE2', 'module_version': '10.43-GCCcore-13.3.0'}, {'full_module_name': 'GLib/2.80.4-GCCcore-13.3.0', 'module_name': 'GLib', 'module_version': '2.80.4-GCCcore-13.3.0'}, {'full_module_name': 'cairo/1.18.0-GCCcore-13.3.0', 'module_name': 'cairo', 'module_version': '1.18.0-GCCcore-13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'NASM/2.16.03-GCCcore-13.3.0', 'module_name': 'NASM', 'module_version': '2.16.03-GCCcore-13.3.0'}, {'full_module_name': 'libjpeg-turbo/3.0.1-GCCcore-13.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '3.0.1-GCCcore-13.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-13.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-13.3.0'}, {'full_module_name': 'libdeflate/1.20-GCCcore-13.3.0', 'module_name': 'libdeflate', 'module_version': '1.20-GCCcore-13.3.0'}, {'full_module_name': 'LibTIFF/4.6.0-GCCcore-13.3.0', 'module_name': 'LibTIFF', 'module_version': '4.6.0-GCCcore-13.3.0'}, {'full_module_name': 'Java/17.0.15', 'module_name': 'Java', 'module_version': '17.0.15'}, {'full_module_name': 'Java/17', 'module_name': 'Java', 'module_version': '17'}, {'full_module_name': 'libgit2/1.8.1-GCCcore-13.3.0', 'module_name': 'libgit2', 'module_version': '1.8.1-GCCcore-13.3.0'}, {'full_module_name': 'cURL/8.7.1-GCCcore-13.3.0', 'module_name': 'cURL', 'module_version': '8.7.1-GCCcore-13.3.0'}, {'full_module_name': 'Tk/8.6.14-GCCcore-13.3.0', 'module_name': 'Tk', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'ICU/75.1-GCCcore-13.3.0', 'module_name': 'ICU', 'module_version': '75.1-GCCcore-13.3.0'}, {'full_module_name': 'HarfBuzz/9.0.0-GCCcore-13.3.0', 'module_name': 'HarfBuzz', 'module_version': '9.0.0-GCCcore-13.3.0'}, {'full_module_name': 'FriBidi/1.0.15-GCCcore-13.3.0', 'module_name': 'FriBidi', 'module_version': '1.0.15-GCCcore-13.3.0'}, {'full_module_name': 'R/4.4.2-gfbf-2024a', 'module_name': 'R', 'module_version': '4.4.2-gfbf-2024a'}, {'full_module_name': 'Boost/1.85.0-GCC-13.3.0', 'module_name': 'Boost', 'module_version': '1.85.0-GCC-13.3.0'}, {'full_module_name': 'GSL/2.8-GCC-13.3.0', 'module_name': 'GSL', 'module_version': '2.8-GCC-13.3.0'}, {'full_module_name': 'GMP/6.3.0-GCCcore-13.3.0', 'module_name': 'GMP', 'module_version': '6.3.0-GCCcore-13.3.0'}, {'full_module_name': 'NLopt/2.7.1-GCCcore-13.3.0', 'module_name': 'NLopt', 'module_version': '2.7.1-GCCcore-13.3.0'}, {'full_module_name': 'libogg/1.3.5-GCCcore-13.3.0', 'module_name': 'libogg', 'module_version': '1.3.5-GCCcore-13.3.0'}, {'full_module_name': 'FLAC/1.4.3-GCCcore-13.3.0', 'module_name': 'FLAC', 'module_version': '1.4.3-GCCcore-13.3.0'}, {'full_module_name': 'libvorbis/1.3.7-GCCcore-13.3.0', 'module_name': 'libvorbis', 'module_version': '1.3.7-GCCcore-13.3.0'}, {'full_module_name': 'libopus/1.5.2-GCCcore-13.3.0', 'module_name': 'libopus', 'module_version': '1.5.2-GCCcore-13.3.0'}, {'full_module_name': 'LAME/3.100-GCCcore-13.3.0', 'module_name': 'LAME', 'module_version': '3.100-GCCcore-13.3.0'}, {'full_module_name': 'libsndfile/1.2.2-GCCcore-13.3.0', 'module_name': 'libsndfile', 'module_version': '1.2.2-GCCcore-13.3.0'}, {'full_module_name': 'Szip/2.1.1-GCCcore-13.3.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-13.3.0'}, {'full_module_name': 'HDF5/1.14.5-gompi-2024a', 'module_name': 'HDF5', 'module_version': '1.14.5-gompi-2024a'}, {'full_module_name': 'UDUNITS/2.2.28-GCCcore-13.3.0', 'module_name': 'UDUNITS', 'module_version': '2.2.28-GCCcore-13.3.0'}, {'full_module_name': 'Ghostscript/10.03.1-GCCcore-13.3.0', 'module_name': 'Ghostscript', 'module_version': '10.03.1-GCCcore-13.3.0'}, {'full_module_name': 'libde265/1.0.15-GCCcore-13.3.0', 'module_name': 'libde265', 'module_version': '1.0.15-GCCcore-13.3.0'}, {'full_module_name': 'x265/3.6-GCCcore-13.3.0', 'module_name': 'x265', 'module_version': '3.6-GCCcore-13.3.0'}, {'full_module_name': 'Gdk-Pixbuf/2.42.11-GCCcore-13.3.0', 'module_name': 'Gdk-Pixbuf', 'module_version': '2.42.11-GCCcore-13.3.0'}, {'full_module_name': 'libheif/1.19.5-GCCcore-13.3.0', 'module_name': 'libheif', 'module_version': '1.19.5-GCCcore-13.3.0'}, {'full_module_name': 'JasPer/4.2.4-GCCcore-13.3.0', 'module_name': 'JasPer', 'module_version': '4.2.4-GCCcore-13.3.0'}, {'full_module_name': 'LittleCMS/2.16-GCCcore-13.3.0', 'module_name': 'LittleCMS', 'module_version': '2.16-GCCcore-13.3.0'}, {'full_module_name': 'Pango/1.54.0-GCCcore-13.3.0', 'module_name': 'Pango', 'module_version': '1.54.0-GCCcore-13.3.0'}, {'full_module_name': 'ImageMagick/7.1.1-38-GCCcore-13.3.0', 'module_name': 'ImageMagick', 'module_version': '7.1.1-38-GCCcore-13.3.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-13.3.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-13.3.0'}, {'full_module_name': 'nodejs/20.13.1-GCCcore-13.3.0', 'module_name': 'nodejs', 'module_version': '20.13.1-GCCcore-13.3.0'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'netCDF/4.9.2-gompi-2024a', 'module_name': 'netCDF', 'module_version': '4.9.2-gompi-2024a'}, {'full_module_name': 'GEOS/3.12.2-GCC-13.3.0', 'module_name': 'GEOS', 'module_version': '3.12.2-GCC-13.3.0'}, {'full_module_name': 'libarchive/3.7.4-GCCcore-13.3.0', 'module_name': 'libarchive', 'module_version': '3.7.4-GCCcore-13.3.0'}, {'full_module_name': 'PCRE/8.45-GCCcore-13.3.0', 'module_name': 'PCRE', 'module_version': '8.45-GCCcore-13.3.0'}, {'full_module_name': 'nlohmann_json/3.11.3-GCCcore-13.3.0', 'module_name': 'nlohmann_json', 'module_version': '3.11.3-GCCcore-13.3.0'}, {'full_module_name': 'PROJ/9.4.1-GCCcore-13.3.0', 'module_name': 'PROJ', 'module_version': '9.4.1-GCCcore-13.3.0'}, {'full_module_name': 'libgeotiff/1.7.3-GCCcore-13.3.0', 'module_name': 'libgeotiff', 'module_version': '1.7.3-GCCcore-13.3.0'}, {'full_module_name': 'cffi/1.16.0-GCCcore-13.3.0', 'module_name': 'cffi', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'cryptography/42.0.8-GCCcore-13.3.0', 'module_name': 'cryptography', 'module_version': '42.0.8-GCCcore-13.3.0'}, {'full_module_name': 'virtualenv/20.26.2-GCCcore-13.3.0', 'module_name': 'virtualenv', 'module_version': '20.26.2-GCCcore-13.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2024.06-GCCcore-13.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2024.06-GCCcore-13.3.0'}, {'full_module_name': 'SciPy-bundle/2024.05-gfbf-2024a', 'module_name': 'SciPy-bundle', 'module_version': '2024.05-gfbf-2024a'}, {'full_module_name': 'libtirpc/1.3.5-GCCcore-13.3.0', 'module_name': 'libtirpc', 'module_version': '1.3.5-GCCcore-13.3.0'}, {'full_module_name': 'HDF/4.3.0-GCCcore-13.3.0', 'module_name': 'HDF', 'module_version': '4.3.0-GCCcore-13.3.0'}, {'full_module_name': 'Eigen/3.4.0-GCCcore-13.3.0', 'module_name': 'Eigen', 'module_version': '3.4.0-GCCcore-13.3.0'}, {'full_module_name': 'arpack-ng/3.9.1-foss-2024a', 'module_name': 'arpack-ng', 'module_version': '3.9.1-foss-2024a'}, {'full_module_name': 'Armadillo/14.0.3-foss-2024a', 'module_name': 'Armadillo', 'module_version': '14.0.3-foss-2024a'}, {'full_module_name': 'CFITSIO/4.4.1-GCCcore-13.3.0', 'module_name': 'CFITSIO', 'module_version': '4.4.1-GCCcore-13.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-13.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-13.3.0'}, {'full_module_name': 'json-c/0.17-GCCcore-13.3.0', 'module_name': 'json-c', 'module_version': '0.17-GCCcore-13.3.0'}, {'full_module_name': 'Xerces-C++/3.2.5-GCCcore-13.3.0', 'module_name': 'Xerces-C++', 'module_version': '3.2.5-GCCcore-13.3.0'}, {'full_module_name': 'Imath/3.1.11-GCCcore-13.3.0', 'module_name': 'Imath', 'module_version': '3.1.11-GCCcore-13.3.0'}, {'full_module_name': 'OpenEXR/3.2.4-GCCcore-13.3.0', 'module_name': 'OpenEXR', 'module_version': '3.2.4-GCCcore-13.3.0'}, {'full_module_name': 'Brunsli/0.1-GCCcore-13.3.0', 'module_name': 'Brunsli', 'module_version': '0.1-GCCcore-13.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-13.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-13.3.0'}, {'full_module_name': 'LERC/4.0.0-GCCcore-13.3.0', 'module_name': 'LERC', 'module_version': '4.0.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenJPEG/2.5.2-GCCcore-13.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.2-GCCcore-13.3.0'}, {'full_module_name': 'SWIG/4.2.1-GCCcore-13.3.0', 'module_name': 'SWIG', 'module_version': '4.2.1-GCCcore-13.3.0'}, {'full_module_name': 'GDAL/3.10.0-foss-2024a', 'module_name': 'GDAL', 'module_version': '3.10.0-foss-2024a'}, {'full_module_name': 'MPFR/4.2.1-GCCcore-13.3.0', 'module_name': 'MPFR', 'module_version': '4.2.1-GCCcore-13.3.0'}, {'full_module_name': 'PostgreSQL/16.4-GCCcore-13.3.0', 'module_name': 'PostgreSQL', 'module_version': '16.4-GCCcore-13.3.0'}, {'full_module_name': 'R-bundle-CRAN/2024.11-foss-2024a', 'module_name': 'R-bundle-CRAN', 'module_version': '2024.11-foss-2024a'}, {'full_module_name': 'snappy/1.2.1-GCCcore-13.3.0', 'module_name': 'snappy', 'module_version': '1.2.1-GCCcore-13.3.0'}, {'full_module_name': 'RapidJSON/1.1.0-20240815-GCCcore-13.3.0', 'module_name': 'RapidJSON', 'module_version': '1.1.0-20240815-GCCcore-13.3.0'}, {'full_module_name': 'Abseil/20240722.0-GCCcore-13.3.0', 'module_name': 'Abseil', 'module_version': '20240722.0-GCCcore-13.3.0'}, {'full_module_name': 'RE2/2024-07-02-GCCcore-13.3.0', 'module_name': 'RE2', 'module_version': '2024-07-02-GCCcore-13.3.0'}, {'full_module_name': 'utf8proc/2.9.0-GCCcore-13.3.0', 'module_name': 'utf8proc', 'module_version': '2.9.0-GCCcore-13.3.0'}, {'full_module_name': 'Arrow/17.0.0-gfbf-2024a', 'module_name': 'Arrow', 'module_version': '17.0.0-gfbf-2024a'}, {'full_module_name': 'arrow-R/17.0.0.1-foss-2024a-R-4.4.2', 'module_name': 'arrow-R', 'module_version': '17.0.0.1-foss-2024a-R-4.4.2'}, {'full_module_name': 'R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2', 'module_name': 'R-bundle-Bioconductor', 'module_version': '3.20-foss-2024a-R-4.4.2'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Bioconductor provides tools for the analysis and coprehension\n of high-throughput genomic data.', 'version': '3.20', 'versionsuffix': '-R-4.4.2', 'extensions': [{'type': 'r', 'name': 'BiocGenerics', 'version': '0.52.0'}, {'type': 'r', 'name': 'Biobase', 'version': '2.66.0'}, {'type': 'r', 'name': 'S4Vectors', 'version': '0.44.0'}, {'type': 'r', 'name': 'IRanges', 'version': '2.40.0'}, {'type': 'r', 'name': 'GenomeInfoDbData', 'version': '1.2.13'}, {'type': 'r', 'name': 'UCSC.utils', 'version': '1.2.0'}, {'type': 'r', 'name': 'GenomeInfoDb', 'version': '1.42.0'}, {'type': 'r', 'name': 'zlibbioc', 'version': '1.52.0'}, {'type': 'r', 'name': 'XVector', 'version': '0.46.0'}, {'type': 'r', 'name': 'Biostrings', 'version': '2.74.0'}, {'type': 'r', 'name': 'KEGGREST', 'version': '1.46.0'}, {'type': 'r', 'name': 'AnnotationDbi', 'version': '1.68.0'}, {'type': 'r', 'name': 'GenomicRanges', 'version': '1.58.0'}, {'type': 'r', 'name': 'BiocParallel', 'version': '1.40.0'}, {'type': 'r', 'name': 'Rhtslib', 'version': '3.2.0'}, {'type': 'r', 'name': 'Rsamtools', 'version': '2.22.0'}, {'type': 'r', 'name': 'MatrixGenerics', 'version': '1.18.0'}, {'type': 'r', 'name': 'S4Arrays', 'version': '1.6.0'}, {'type': 'r', 'name': 'SparseArray', 'version': '1.6.0'}, {'type': 'r', 'name': 'DelayedArray', 'version': '0.32.0'}, {'type': 'r', 'name': 'SummarizedExperiment', 'version': '1.36.0'}, {'type': 'r', 'name': 'GenomicAlignments', 'version': '1.42.0'}, {'type': 'r', 'name': 'pwalign', 'version': '1.2.0'}, {'type': 'r', 'name': 'ShortRead', 'version': '1.64.0'}, {'type': 'r', 'name': 'graph', 'version': '1.84.0'}, {'type': 'r', 'name': 'affyio', 'version': '1.76.0'}, {'type': 'r', 'name': 'preprocessCore', 'version': '1.68.0'}, {'type': 'r', 'name': 'BiocManager', 'version': '1.30.25'}, {'type': 'r', 'name': 'affy', 'version': '1.84.0'}, {'type': 'r', 'name': 'GO.db', 'version': '3.20.0'}, {'type': 'r', 'name': 'limma', 'version': '3.62.1'}, {'type': 'r', 'name': 'RBGL', 'version': '1.82.0'}, {'type': 'r', 'name': 'org.Hs.eg.db', 'version': '3.20.0'}, {'type': 'r', 'name': 'AnnotationForge', 'version': '1.48.0'}, {'type': 'r', 'name': 'annaffy', 'version': '1.78.0'}, {'type': 'r', 'name': 'gcrma', 'version': '2.78.0'}, {'type': 'r', 'name': 'oligoClasses', 'version': '1.68.0'}, {'type': 'r', 'name': 'edgeR', 'version': '4.4.0'}, {'type': 'r', 'name': 'PFAM.db', 'version': '3.20.0'}, {'type': 'r', 'name': 'perm', 'version': '1.0-0.4'}, {'type': 'r', 'name': 'baySeq', 'version': '2.40.0'}, {'type': 'r', 'name': 'qvalue', 'version': '2.38.0'}, {'type': 'r', 'name': 'impute', 'version': '1.80.0'}, {'type': 'r', 'name': 'shinyFiles', 'version': '0.9.3'}, {'type': 'r', 'name': 'samr', 'version': '3.0'}, {'type': 'r', 'name': 'DEGseq', 'version': '1.60.0'}, {'type': 'r', 'name': 'hgu133plus2.db', 'version': '3.13.0'}, {'type': 'r', 'name': 'illuminaio', 'version': '0.48.0'}, {'type': 'r', 'name': 'BiocIO', 'version': '1.16.0'}, {'type': 'r', 'name': 'restfulr', 'version': '0.0.15'}, {'type': 'r', 'name': 'rtracklayer', 'version': '1.66.0'}, {'type': 'r', 'name': 'filelock', 'version': '1.0.3'}, {'type': 'r', 'name': 'BiocFileCache', 'version': '2.14.0'}, {'type': 'r', 'name': 'biomaRt', 'version': '2.62.0'}, {'type': 'r', 'name': 'GenomicFeatures', 'version': '1.58.0'}, {'type': 'r', 'name': 'bumphunter', 'version': '1.48.0'}, {'type': 'r', 'name': 'multtest', 'version': '2.62.0'}, {'type': 'r', 'name': 'scrime', 'version': '1.3.5'}, {'type': 'r', 'name': 'siggenes', 'version': '1.80.0'}, {'type': 'r', 'name': 'DynDoc', 'version': '1.84.0'}, {'type': 'r', 'name': 'NOISeq', 'version': '2.50.0'}, {'type': 'r', 'name': 'Rgraphviz', 'version': '2.50.0'}, {'type': 'r', 'name': 'RNASeqPower', 'version': '1.46.0'}, {'type': 'r', 'name': 'annotate', 'version': '1.84.0'}, {'type': 'r', 'name': 'GSEABase', 'version': '1.68.0'}, {'type': 'r', 'name': 'genefilter', 'version': '1.88.0'}, {'type': 'r', 'name': 'Category', 'version': '2.72.0'}, {'type': 'r', 'name': 'GOstats', 'version': '2.72.0'}, {'type': 'r', 'name': 'BSgenome', 'version': '1.74.0'}, {'type': 'r', 'name': 'VariantAnnotation', 'version': '1.52.0'}, {'type': 'r', 'name': 'interactiveDisplayBase', 'version': '1.44.0'}, {'type': 'r', 'name': 'BiocVersion', 'version': '3.20.0'}, {'type': 'r', 'name': 'AnnotationHub', 'version': '3.14.0'}, {'type': 'r', 'name': 'AnnotationFilter', 'version': '1.30.0'}, {'type': 'r', 'name': 'ProtGenerics', 'version': '1.38.0'}, {'type': 'r', 'name': 'ensembldb', 'version': '2.30.0'}, {'type': 'r', 'name': 'biovizBase', 'version': '1.54.0'}, {'type': 'r', 'name': 'txdbmaker', 'version': '1.2.0'}, {'type': 'r', 'name': 'OrganismDbi', 'version': '1.48.0'}, {'type': 'r', 'name': 'ggbio', 'version': '1.54.0'}, {'type': 'r', 'name': 'geneplotter', 'version': '1.84.0'}, {'type': 'r', 'name': 'DESeq2', 'version': '1.46.0'}, {'type': 'r', 'name': 'ReportingTools', 'version': '2.46.0'}, {'type': 'r', 'name': 'Glimma', 'version': '2.16.0'}, {'type': 'r', 'name': 'affycoretools', 'version': '1.78.0'}, {'type': 'r', 'name': 'TxDb.Hsapiens.UCSC.hg19.knownGene', 'version': '3.2.2'}, {'type': 'r', 'name': 'Homo.sapiens', 'version': '1.3.1'}, {'type': 'r', 'name': 'BSgenome.Hsapiens.UCSC.hg19', 'version': '1.4.3'}, {'type': 'r', 'name': 'AgiMicroRna', 'version': '2.56.0'}, {'type': 'r', 'name': 'geneLenDataBase', 'version': '1.42.0'}, {'type': 'r', 'name': 'goseq', 'version': '1.58.0'}, {'type': 'r', 'name': 'KEGGgraph', 'version': '1.66.0'}, {'type': 'r', 'name': 'GEOquery', 'version': '2.74.0'}, {'type': 'r', 'name': 'gsignal', 'version': '0.3-7'}, {'type': 'r', 'name': 'mixOmics', 'version': '6.30.0'}, {'type': 'r', 'name': 'Rhdf5lib', 'version': '1.28.0'}, {'type': 'r', 'name': 'rhdf5filters', 'version': '1.18.0'}, {'type': 'r', 'name': 'rhdf5', 'version': '2.50.0'}, {'type': 'r', 'name': 'HDF5Array', 'version': '1.34.0'}, {'type': 'r', 'name': 'sparseMatrixStats', 'version': '1.18.0'}, {'type': 'r', 'name': 'DelayedMatrixStats', 'version': '1.28.0'}, {'type': 'r', 'name': 'minfi', 'version': '1.52.1'}, {'type': 'r', 'name': 'FDb.InfiniumMethylation.hg19', 'version': '2.2.0'}, {'type': 'r', 'name': 'methylumi', 'version': '2.52.0'}, {'type': 'r', 'name': 'lumi', 'version': '2.58.0'}, {'type': 'r', 'name': 'widgetTools', 'version': '1.84.0'}, {'type': 'r', 'name': 'tkWidgets', 'version': '1.84.0'}, {'type': 'r', 'name': 'Mfuzz', 'version': '2.66.0'}, {'type': 'r', 'name': 'venn', 'version': '1.12'}, {'type': 'r', 'name': 'maSigPro', 'version': '1.78.0'}, {'type': 'r', 'name': 'SPIA', 'version': '2.58.0'}, {'type': 'r', 'name': 'Gviz', 'version': '1.50.0'}, {'type': 'r', 'name': 'cummeRbund', 'version': '2.48.0'}, {'type': 'r', 'name': 'GenomicFiles', 'version': '1.42.0'}, {'type': 'r', 'name': 'derfinderHelper', 'version': '1.40.0'}, {'type': 'r', 'name': 'derfinder', 'version': '1.40.0'}, {'type': 'r', 'name': 'Rsubread', 'version': '2.20.0'}, {'type': 'r', 'name': 'pcaMethods', 'version': '1.98.0'}, {'type': 'r', 'name': 'marray', 'version': '1.84.0'}, {'type': 'r', 'name': 'CGHbase', 'version': '1.66.0'}, {'type': 'r', 'name': 'Wrench', 'version': '1.24.0'}, {'type': 'r', 'name': 'lpsymphony', 'version': '1.34.0'}, {'type': 'r', 'name': 'IHW', 'version': '1.34.0'}, {'type': 'r', 'name': 'gdsfmt', 'version': '1.42.0'}, {'type': 'r', 'name': 'SNPRelate', 'version': '1.40.0'}, {'type': 'r', 'name': 'biomformat', 'version': '1.34.0'}, {'type': 'r', 'name': 'phyloseq', 'version': '1.50.0'}, {'type': 'r', 'name': 'NADA', 'version': '1.6-1.1'}, {'type': 'r', 'name': 'zCompositions', 'version': '1.5.0-4'}, {'type': 'r', 'name': 'RcppZiggurat', 'version': '0.1.6'}, {'type': 'r', 'name': 'Rfast', 'version': '2.1.0'}, {'type': 'r', 'name': 'directlabels', 'version': '2024.1.21'}, {'type': 'r', 'name': 'ALDEx2', 'version': '1.38.0'}, {'type': 'r', 'name': 'dada2', 'version': '1.34.0'}, {'type': 'r', 'name': 'LEA', 'version': '3.18.0'}, {'type': 'r', 'name': 'tximport', 'version': '1.34.0'}, {'type': 'r', 'name': 'SingleCellExperiment', 'version': '1.28.1'}, {'type': 'r', 'name': 'assorthead', 'version': '1.0.0'}, {'type': 'r', 'name': 'beachmat', 'version': '2.22.0'}, {'type': 'r', 'name': 'RcppAnnoy', 'version': '0.0.22'}, {'type': 'r', 'name': 'RcppHNSW', 'version': '0.6.0'}, {'type': 'r', 'name': 'BiocNeighbors', 'version': '2.0.0'}, {'type': 'r', 'name': 'rsvd', 'version': '1.0.5'}, {'type': 'r', 'name': 'ScaledMatrix', 'version': '1.14.0'}, {'type': 'r', 'name': 'BiocSingular', 'version': '1.22.0'}, {'type': 'r', 'name': 'scuttle', 'version': '1.16.0'}, {'type': 'r', 'name': 'RcppML', 'version': '0.3.7'}, {'type': 'r', 'name': 'sitmo', 'version': '2.0.2'}, {'type': 'r', 'name': 'dqrng', 'version': '0.4.1'}, {'type': 'r', 'name': 'uwot', 'version': '0.2.2'}, {'type': 'r', 'name': 'ggrastr', 'version': '1.0.2'}, {'type': 'r', 'name': 'scater', 'version': '1.34.0'}, {'type': 'r', 'name': 'bluster', 'version': '1.16.0'}, {'type': 'r', 'name': 'metapod', 'version': '1.14.0'}, {'type': 'r', 'name': 'scran', 'version': '1.34.0'}, {'type': 'r', 'name': 'SC3', 'version': '1.34.0'}, {'type': 'r', 'name': 'ComplexHeatmap', 'version': '2.22.0'}, {'type': 'r', 'name': 'GENIE3', 'version': '1.28.0'}, {'type': 'r', 'name': 'dupRadar', 'version': '1.36.0'}, {'type': 'r', 'name': 'DNAcopy', 'version': '1.80.0'}, {'type': 'r', 'name': 'sva', 'version': '3.54.0'}, {'type': 'r', 'name': 'ballgown', 'version': '2.38.0'}, {'type': 'r', 'name': 'DropletUtils', 'version': '1.26.0'}, {'type': 'r', 'name': 'DeconRNASeq', 'version': '1.48.0'}, {'type': 'r', 'name': 'SpatialExperiment', 'version': '1.16.0'}, {'type': 'r', 'name': 'GSVA', 'version': '2.0.1'}, {'type': 'r', 'name': 'PureCN', 'version': '2.12.0'}, {'type': 'r', 'name': 'globaltest', 'version': '5.60.0'}, {'type': 'r', 'name': 'GlobalAncova', 'version': '4.24.0'}, {'type': 'r', 'name': 'vsn', 'version': '3.74.0'}, {'type': 'r', 'name': 'mzID', 'version': '1.44.0'}, {'type': 'r', 'name': 'mzR', 'version': '2.40.0'}, {'type': 'r', 'name': 'MsCoreUtils', 'version': '1.18.0'}, {'type': 'r', 'name': 'BiocBaseUtils', 'version': '1.8.0'}, {'type': 'r', 'name': 'MultiAssayExperiment', 'version': '1.32.0'}, {'type': 'r', 'name': 'QFeatures', 'version': '1.16.0'}, {'type': 'r', 'name': 'PSMatch', 'version': '1.10.0'}, {'type': 'r', 'name': 'MSnbase', 'version': '2.32.0'}, {'type': 'r', 'name': 'MassSpecWavelet', 'version': '1.72.0'}, {'type': 'r', 'name': 'MsFeatures', 'version': '1.14.0'}, {'type': 'r', 'name': 'MetaboCoreUtils', 'version': '1.14.0'}, {'type': 'r', 'name': 'Spectra', 'version': '1.16.0'}, {'type': 'r', 'name': 'MsExperiment', 'version': '1.8.0'}, {'type': 'r', 'name': 'xcms', 'version': '4.4.0'}, {'type': 'r', 'name': 'CAMERA', 'version': '1.62.0'}, {'type': 'r', 'name': 'fgsea', 'version': '1.32.0'}, {'type': 'r', 'name': 'GWASExactHW', 'version': '1.2'}, {'type': 'r', 'name': 'quantsmooth', 'version': '1.72.0'}, {'type': 'r', 'name': 'GWASTools', 'version': '1.52.0'}, {'type': 'r', 'name': 'SeqArray', 'version': '1.46.0'}, {'type': 'r', 'name': 'SeqVarTools', 'version': '1.44.0'}, {'type': 'r', 'name': 'GENESIS', 'version': '2.36.0'}, {'type': 'r', 'name': 'MLInterfaces', 'version': '1.86.0'}, {'type': 'r', 'name': 'pRoloc', 'version': '1.46.0'}, {'type': 'r', 'name': 'pRolocdata', 'version': '1.44.1'}, {'type': 'r', 'name': 'fresh', 'version': '0.2.1'}, {'type': 'r', 'name': 'waiter', 'version': '0.2.5'}, {'type': 'r', 'name': 'shinydashboardPlus', 'version': '2.0.5'}, {'type': 'r', 'name': 'shinyhelper', 'version': '0.3.2'}, {'type': 'r', 'name': 'anytime', 'version': '0.3.9'}, {'type': 'r', 'name': 'shinyWidgets', 'version': '0.8.7'}, {'type': 'r', 'name': 'pRolocGUI', 'version': '2.16.0'}, {'type': 'r', 'name': 'EBImage', 'version': '4.48.0'}, {'type': 'r', 'name': 'GenomicScores', 'version': '2.18.0'}, {'type': 'r', 'name': 'BSgenome.Mmusculus.UCSC.mm10', 'version': '1.4.3'}, {'type': 'r', 'name': 'TxDb.Mmusculus.UCSC.mm10.knownGene', 'version': '3.10.0'}, {'type': 'r', 'name': 'regioneR', 'version': '1.38.0'}, {'type': 'r', 'name': 'InteractionSet', 'version': '1.34.0'}, {'type': 'r', 'name': 'universalmotif', 'version': '1.24.2'}, {'type': 'r', 'name': 'ChIPpeakAnno', 'version': '3.40.0'}, {'type': 'r', 'name': 'seqLogo', 'version': '1.72.0'}, {'type': 'r', 'name': 'rGADEM', 'version': '2.54.0'}, {'type': 'r', 'name': 'MotifDb', 'version': '1.48.0'}, {'type': 'r', 'name': 'poweRlaw', 'version': '0.80.0'}, {'type': 'r', 'name': 'CNEr', 'version': '1.42.0'}, {'type': 'r', 'name': 'DirichletMultinomial', 'version': '1.48.0'}, {'type': 'r', 'name': 'TFMPvalue', 'version': '0.0.9'}, {'type': 'r', 'name': 'TFBSTools', 'version': '1.44.0'}, {'type': 'r', 'name': 'motifStack', 'version': '1.50.0'}, {'type': 'r', 'name': 'ATACseqQC', 'version': '1.30.0'}, {'type': 'r', 'name': 'ResidualMatrix', 'version': '1.16.0'}, {'type': 'r', 'name': 'batchelor', 'version': '1.22.0'}, {'type': 'r', 'name': 'gsmoothr', 'version': '0.1.7'}, {'type': 'r', 'name': 'R.devices', 'version': '2.17.2'}, {'type': 'r', 'name': 'R.filesets', 'version': '2.15.1'}, {'type': 'r', 'name': 'aroma.light', 'version': '3.36.0'}, {'type': 'r', 'name': 'PSCBS', 'version': '0.67.0'}, {'type': 'r', 'name': 'aroma.core', 'version': '3.3.1'}, {'type': 'r', 'name': 'R.huge', 'version': '0.10.1'}, {'type': 'r', 'name': 'aroma.apd', 'version': '0.7.0'}, {'type': 'r', 'name': 'aroma.affymetrix', 'version': '3.2.2'}, {'type': 'r', 'name': 'Repitools', 'version': '1.52.0'}, {'type': 'r', 'name': 'BSgenome.Hsapiens.UCSC.hg38', 'version': '1.4.5'}, {'type': 'r', 'name': 'MEDIPS', 'version': '1.58.0'}, {'type': 'r', 'name': 'RProtoBufLib', 'version': '2.18.0'}, {'type': 'r', 'name': 'cytolib', 'version': '2.18.0'}, {'type': 'r', 'name': 'flowCore', 'version': '2.18.0'}, {'type': 'r', 'name': 'mutoss', 'version': '0.1-13'}, {'type': 'r', 'name': 'qqconf', 'version': '1.3.2'}, {'type': 'r', 'name': 'metap', 'version': '1.11'}, {'type': 'r', 'name': 'scattermore', 'version': '1.2'}, {'type': 'r', 'name': 'SeuratObject', 'version': '5.0.2'}, {'type': 'r', 'name': 'Seurat', 'version': '5.1.0'}, {'type': 'r', 'name': 'ALL', 'version': '1.48.0'}, {'type': 'r', 'name': 'ConsensusClusterPlus', 'version': '1.70.0'}, {'type': 'r', 'name': 'flowViz', 'version': '1.70.0'}, {'type': 'r', 'name': 'ncdfFlow', 'version': '2.52.0'}, {'type': 'r', 'name': 'aws.signature', 'version': '0.6.0'}, {'type': 'r', 'name': 'aws.s3', 'version': '0.3.21'}, {'type': 'r', 'name': 'flowWorkspace', 'version': '4.18.0'}, {'type': 'r', 'name': 'ash', 'version': '1.0-15'}, {'type': 'r', 'name': 'hdrcde', 'version': '3.4'}, {'type': 'r', 'name': 'rainbow', 'version': '3.8'}, {'type': 'r', 'name': 'fds', 'version': '1.8'}, {'type': 'r', 'name': 'fda', 'version': '6.2.0'}, {'type': 'r', 'name': 'flowStats', 'version': '4.18.0'}, {'type': 'r', 'name': 'flowClust', 'version': '3.44.0'}, {'type': 'r', 'name': 'openCyto', 'version': '2.18.0'}, {'type': 'r', 'name': 'ggcyto', 'version': '1.34.0'}, {'type': 'r', 'name': 'CytoML', 'version': '2.18.0'}, {'type': 'r', 'name': 'colorRamps', 'version': '2.3.4'}, {'type': 'r', 'name': 'ggnewscale', 'version': '0.5.0'}, {'type': 'r', 'name': 'ggpointdensity', 'version': '0.1.0'}, {'type': 'r', 'name': 'FlowSOM', 'version': '2.14.0'}, {'type': 'r', 'name': 'HMMcopy', 'version': '1.48.0'}, {'type': 'r', 'name': 'diffcyt', 'version': '1.26.0'}, {'type': 'r', 'name': 'blme', 'version': '1.0-6'}, {'type': 'r', 'name': 'remaCor', 'version': '0.0.18'}, {'type': 'r', 'name': 'fANCOVA', 'version': '0.6-1'}, {'type': 'r', 'name': 'variancePartition', 'version': '1.36.2'}, {'type': 'r', 'name': 'muscat', 'version': '1.20.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylation450kmanifest', 'version': '0.4.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICmanifest', 'version': '0.3.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylation450kanno.ilmn12.hg19', 'version': '0.6.1'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICanno.ilm10b2.hg19', 'version': '0.6.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICanno.ilm10b4.hg19', 'version': '0.6.0'}, {'type': 'r', 'name': 'conumee', 'version': '1.40.0'}, {'type': 'r', 'name': 'BSgenome.Cfamiliaris.UCSC.canFam3', 'version': '1.4.0'}, {'type': 'r', 'name': 'ExperimentHub', 'version': '2.14.0'}, {'type': 'r', 'name': 'SingleR', 'version': '2.8.0'}, {'type': 'r', 'name': 'FlowSorted.Blood.EPIC', 'version': '2.10.0'}, {'type': 'r', 'name': 'FlowSorted.CordBloodCombined.450k', 'version': '1.22.0'}, {'type': 'r', 'name': 'DRIMSeq', 'version': '1.34.0'}, {'type': 'r', 'name': 'stageR', 'version': '1.28.0'}, {'type': 'r', 'name': 'isva', 'version': '1.9'}, {'type': 'r', 'name': 'org.Mm.eg.db', 'version': '3.20.0'}, {'type': 'r', 'name': 'org.Rn.eg.db', 'version': '3.20.0'}, {'type': 'r', 'name': 'ROC', 'version': '1.82.0'}, {'type': 'r', 'name': 'wateRmelon', 'version': '2.12.0'}, {'type': 'r', 'name': 'GLAD', 'version': '2.70.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICv2manifest', 'version': '1.0.0'}, {'type': 'r', 'name': 'IlluminaHumanMethylationEPICv2anno.20a1.hg38', 'version': '1.0.0'}, {'type': 'r', 'name': 'missMethyl', 'version': '1.40.0'}, {'type': 'r', 'name': 'MethylSeekR', 'version': '1.46.0'}, {'type': 'r', 'name': 'affxparser', 'version': '1.78.0'}, {'type': 'r', 'name': 'ccdata', 'version': '1.32.0'}, {'type': 'r', 'name': 'lsa', 'version': '0.73.3'}, {'type': 'r', 'name': 'ccmap', 'version': '1.32.0'}, {'type': 'r', 'name': 'oligo', 'version': '1.70.0'}, {'type': 'r', 'name': 'SMVar', 'version': '1.3.4'}, {'type': 'r', 'name': 'metaMA', 'version': '3.1.3'}, {'type': 'r', 'name': 'randomcoloR', 'version': '1.1.0.1'}, {'type': 'r', 'name': 'shinyBS', 'version': '0.61.1'}, {'type': 'r', 'name': 'shinypanel', 'version': '0.1.5'}, {'type': 'r', 'name': 'snpStats', 'version': '1.56.0'}, {'type': 'r', 'name': 'mixsqp', 'version': '0.3-54'}, {'type': 'r', 'name': 'susieR', 'version': '0.12.35'}, {'type': 'r', 'name': 'coloc', 'version': '5.2.3'}, {'type': 'r', 'name': 'SCANVIS', 'version': '1.20.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v86', 'version': '2.99.0'}, {'type': 'r', 'name': 'agricolae', 'version': '1.3-7'}, {'type': 'r', 'name': 'bookdown', 'version': '0.41'}, {'type': 'r', 'name': 'BiocStyle', 'version': '2.34.0'}, {'type': 'r', 'name': 'ggdendro', 'version': '0.2.0'}, {'type': 'r', 'name': 'pmp', 'version': '1.18.0'}, {'type': 'r', 'name': 'MultiDataSet', 'version': '1.34.0'}, {'type': 'r', 'name': 'ropls', 'version': '1.38.0'}, {'type': 'r', 'name': 'ontologyIndex', 'version': '2.12'}, {'type': 'r', 'name': 'rols', 'version': '3.2.0'}, {'type': 'r', 'name': 'struct', 'version': '1.18.0'}, {'type': 'r', 'name': 'ggthemes', 'version': '5.1.0'}, {'type': 'r', 'name': 'structToolbox', 'version': '1.18.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v75', 'version': '2.99.0'}, {'type': 'r', 'name': 'ggseqlogo', 'version': '0.2'}, {'type': 'r', 'name': 'sparsesvd', 'version': '0.2-2'}, {'type': 'r', 'name': 'docopt', 'version': '0.7.1'}, {'type': 'r', 'name': 'qlcMatrix', 'version': '0.9.8'}, {'type': 'r', 'name': 'Signac', 'version': '1.14.0'}, {'type': 'r', 'name': 'motifmatchr', 'version': '1.28.0'}, {'type': 'r', 'name': 'extraDistr', 'version': '1.10.0'}, {'type': 'r', 'name': 'PRROC', 'version': '1.3.1'}, {'type': 'r', 'name': 'TSP', 'version': '1.2-4'}, {'type': 'r', 'name': 'qap', 'version': '0.1-2'}, {'type': 'r', 'name': 'ca', 'version': '0.71.1'}, {'type': 'r', 'name': 'seriation', 'version': '1.5.6'}, {'type': 'r', 'name': 'egg', 'version': '0.4.5'}, {'type': 'r', 'name': 'heatmaply', 'version': '1.5.0'}, {'type': 'r', 'name': 'OUTRIDER', 'version': '1.24.0'}, {'type': 'r', 'name': 'FRASER', 'version': '2.2.0'}, {'type': 'r', 'name': 'JASPAR2020', 'version': '0.99.10'}, {'type': 'r', 'name': 'AUCell', 'version': '1.28.0'}, {'type': 'r', 'name': 'RcisTarget', 'version': '1.26.0'}, {'type': 'r', 'name': 'NMF', 'version': '0.28'}, {'type': 'r', 'name': 'densEstBayes', 'version': '1.0-2.2'}, {'type': 'r', 'name': 'reldist', 'version': '1.7-2'}, {'type': 'r', 'name': 'M3Drop', 'version': '1.32.0'}, {'type': 'r', 'name': 'bsseq', 'version': '1.42.0'}, {'type': 'r', 'name': 'DSS', 'version': '2.54.0'}, {'type': 'r', 'name': 'pathview', 'version': '1.46.0'}, {'type': 'r', 'name': 'chromVAR', 'version': '1.28.0'}, {'type': 'r', 'name': 'EnsDb.Hsapiens.v79', 'version': '2.99.0'}, {'type': 'r', 'name': 'WGCNA', 'version': '1.73'}, {'type': 'r', 'name': 'DNABarcodes', 'version': '1.36.0'}, {'type': 'r', 'name': 'GenomicInteractions', 'version': '1.40.0'}, {'type': 'r', 'name': 'CAGEfightR', 'version': '1.26.0'}, {'type': 'r', 'name': 'CAGEr', 'version': '2.12.0'}, {'type': 'r', 'name': 'SPOTlight', 'version': '1.10.0'}, {'type': 'r', 'name': 'CGHcall', 'version': '2.68.0'}, {'type': 'r', 'name': 'QDNAseq', 'version': '1.42.0'}, {'type': 'r', 'name': 'HiCcompare', 'version': '1.28.0'}, {'type': 'r', 'name': 'ROntoTools', 'version': '2.34.0'}, {'type': 'r', 'name': 'scDblFinder', 'version': '1.20.0'}, {'type': 'r', 'name': 'treeio', 'version': '1.30.0'}, {'type': 'r', 'name': 'ggtree', 'version': '3.14.0'}, {'type': 'r', 'name': 'scistreer', 'version': '1.2.0'}, {'type': 'r', 'name': 'hahmmr', 'version': '1.0.0'}, {'type': 'r', 'name': 'numbat', 'version': '1.4.2'}, {'type': 'r', 'name': 'HiCBricks', 'version': '1.24.0'}, {'type': 'r', 'name': 'dir.expiry', 'version': '1.14.0'}, {'type': 'r', 'name': 'basilisk.utils', 'version': '1.18.0'}, {'type': 'r', 'name': 'basilisk', 'version': '1.18.0'}, {'type': 'r', 'name': 'zellkonverter', 'version': '1.16.0'}, {'type': 'r', 'name': 'DO.db', 'version': '2.9'}, {'type': 'r', 'name': 'GOSemSim', 'version': '2.32.0'}, {'type': 'r', 'name': 'HDO.db', 'version': '1.0.0'}, {'type': 'r', 'name': 'DOSE', 'version': '4.0.0'}, {'type': 'r', 'name': 'ggtangle', 'version': '0.0.4'}, {'type': 'r', 'name': 'enrichplot', 'version': '1.26.2'}, {'type': 'r', 'name': 'gson', 'version': '0.1.0'}, {'type': 'r', 'name': 'clusterProfiler', 'version': '4.14.3'}, {'type': 'r', 'name': 'reactome.db', 'version': '1.89.0'}, {'type': 'r', 'name': 'graphite', 'version': '1.52.0'}, {'type': 'r', 'name': 'ReactomePA', 'version': '1.50.0'}, {'type': 'r', 'name': 'flowClean', 'version': '1.44.0'}, {'type': 'r', 'name': 'flowAI', 'version': '1.36.0'}, {'type': 'r', 'name': 'flowFP', 'version': '1.64.0'}, {'type': 'r', 'name': 'simona', 'version': '1.4.0'}, {'type': 'r', 'name': 'simplifyEnrichment', 'version': '2.0.0'}, {'type': 'r', 'name': 'RPMG', 'version': '2.2-7'}, {'type': 'r', 'name': 'Rwave', 'version': '2.6-5'}, {'type': 'r', 'name': 'RSEIS', 'version': '4.2-4'}, {'type': 'r', 'name': 'splancs', 'version': '2.01-45'}, {'type': 'r', 'name': 'MBA', 'version': '0.1-2'}, {'type': 'r', 'name': 'GEOmap', 'version': '2.5-11'}, {'type': 'r', 'name': 'RFOC', 'version': '3.4-10'}, {'type': 'r', 'name': 'flowDensity', 'version': '1.40.0'}, {'type': 'r', 'name': 'flowPeaks', 'version': '1.52.0'}, {'type': 'r', 'name': 'SamSPECTRAL', 'version': '1.60.0'}, {'type': 'r', 'name': 'ddPCRclust', 'version': '1.26.0'}, {'type': 'r', 'name': 'feature', 'version': '1.2.15'}, {'type': 'r', 'name': 'flowMerge', 'version': '2.54.0'}, {'type': 'r', 'name': 'TrajectoryUtils', 'version': '1.14.0'}, {'type': 'r', 'name': 'slingshot', 'version': '2.14.0'}, {'type': 'r', 'name': 'TreeSummarizedExperiment', 'version': '2.14.0'}, {'type': 'r', 'name': 'decontam', 'version': '1.26.0'}, {'type': 'r', 'name': 'DECIPHER', 'version': '3.2.0'}, {'type': 'r', 'name': 'rbiom', 'version': '1.0.3'}, {'type': 'r', 'name': 'mia', 'version': '1.14.0'}, {'type': 'r', 'name': 'ANCOMBC', 'version': '2.8.0'}, {'type': 'r', 'name': 'decoupleR', 'version': '2.12.0'}, {'type': 'r', 'name': 'UCell', 'version': '2.10.1'}, {'type': 'r', 'name': 'intervals', 'version': '0.15.5'}, {'type': 'r', 'name': 'oompaBase', 'version': '3.2.9'}, {'type': 'r', 'name': 'oompaData', 'version': '3.1.4'}, {'type': 'r', 'name': 'TailRank', 'version': '3.2.2'}, {'type': 'r', 'name': 'RnBeads', 'version': '2.24.0'}, {'type': 'r', 'name': 'RnBeads.hg19', 'version': '1.38.0'}, {'type': 'r', 'name': 'RnBeads.hg38', 'version': '1.38.1'}, {'type': 'r', 'name': 'RnBeads.mm9', 'version': '1.38.0'}, {'type': 'r', 'name': 'RnBeads.mm10', 'version': '2.14.0'}, {'type': 'r', 'name': 'RnBeads.rn5', 'version': '1.38.0'}, {'type': 'r', 'name': 'log4r', 'version': '0.4.4'}, {'type': 'r', 'name': 'MSstatsConvert', 'version': '1.16.0'}, {'type': 'r', 'name': 'MSstats', 'version': '4.14.0'}, {'type': 'r', 'name': 'MSstatsTMT', 'version': '2.14.1'}, {'type': 'r', 'name': 'MSstatsPTM', 'version': '2.8.1'}, {'type': 'r', 'name': 'factoextra', 'version': '1.0.7'}, {'type': 'r', 'name': 'MSstatsLiP', 'version': '1.12.0'}, {'type': 'r', 'name': 'babelgene', 'version': '22.9'}, {'type': 'r', 'name': 'msigdbr', 'version': '7.5.1'}, {'type': 'r', 'name': 'escape', 'version': '2.2.1'}, {'type': 'r', 'name': 'plyranges', 'version': '1.26.0'}, {'type': 'r', 'name': 'seqPattern', 'version': '1.38.0'}, {'type': 'r', 'name': 'genomation', 'version': '1.38.0'}, {'type': 'r', 'name': 'ChIPseeker', 'version': '1.42.0'}, {'type': 'r', 'name': 'SimBu', 'version': '1.8.0'}, {'type': 'r', 'name': 'hiAnnotator', 'version': '1.40.0'}, {'type': 'r', 'name': 'lefser', 'version': '1.16.2'}, {'type': 'r', 'name': 'metagenomeSeq', 'version': '1.48.1'}, {'type': 'r', 'name': 'Maaslin2', 'version': '1.20.0'}, {'type': 'r', 'name': 'ggpicrust2', 'version': '2.1.2'}]}], 'homepage': 'https://bioconductor.org', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'Bioconductor provides tools for the analysis and coprehension\n of high-throughput genomic data.'} installations


### affxparser


|`affxparser` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.70.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.74.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.78.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### affy


|`affy` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### affycoretools


|`affycoretools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.70.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.74.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.78.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### affyio


|`affyio` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.68.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.72.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.76.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### AgiMicroRna


|`AgiMicroRna` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.48.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.52.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.56.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### agricolae


|`agricolae` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.3-5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.3-7|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ALDEx2


|`ALDEx2` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ALL


|`ALL` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ANCOMBC


|`ANCOMBC` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.4.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.8.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### annaffy


|`annaffy` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.70.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.74.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.78.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### annotate


|`annotate` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### AnnotationDbi


|`AnnotationDbi` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.60.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.64.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.68.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### AnnotationFilter


|`AnnotationFilter` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.22.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.26.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.30.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### AnnotationForge


|`AnnotationForge` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### AnnotationHub


|`AnnotationHub` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|3.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### anytime


|`anytime` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### aroma.affymetrix


|`aroma.affymetrix` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.2.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.2.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### aroma.apd


|`aroma.apd` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.6.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.7.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### aroma.core


|`aroma.core` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.3.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.3.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### aroma.light


|`aroma.light` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.28.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.32.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.36.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ash


|`ash` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0-15|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### assorthead


|`assorthead` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ATACseqQC


|`ATACseqQC` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.22.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.26.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.30.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### AUCell


|`AUCell` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### aws.s3


|`aws.s3` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3.21|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### aws.signature


|`aws.signature` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### babelgene


|`babelgene` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|22.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ballgown


|`ballgown` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### basilisk


|`basilisk` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### basilisk.utils


|`basilisk.utils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### batchelor


|`batchelor` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.14.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.18.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.22.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### baySeq


|`baySeq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.31.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### beachmat


|`beachmat` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.14.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.22.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BH


|`BH` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.84.0-0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### Biobase


|`Biobase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.58.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.62.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.66.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocBaseUtils


|`BiocBaseUtils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.4.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.8.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocFileCache


|`BiocFileCache` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### BiocGenerics


|`BiocGenerics` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocIO


|`BiocIO` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### BiocManager


|`BiocManager` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.20|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.22|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.30.25|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocNeighbors


|`BiocNeighbors` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.20.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocParallel


|`BiocParallel` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocSingular


|`BiocSingular` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.14.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.22.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocStyle


|`BiocStyle` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BiocVersion


|`BiocVersion` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### biomaRt


|`biomaRt` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.54.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.58.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.62.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### biomformat


|`biomformat` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Biostrings


|`Biostrings` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.66.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.70.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.74.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### biovizBase


|`biovizBase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.50.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.54.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### blme


|`blme` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0-5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.0-6|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### bluster


|`bluster` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### bookdown


|`bookdown` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.33|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.37|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.41|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BSgenome


|`BSgenome` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.66.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.70.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.74.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### BSgenome.Cfamiliaris.UCSC.canFam3


|`BSgenome.Cfamiliaris.UCSC.canFam3` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### BSgenome.Hsapiens.UCSC.hg19


|`BSgenome.Hsapiens.UCSC.hg19` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### BSgenome.Hsapiens.UCSC.hg38


|`BSgenome.Hsapiens.UCSC.hg38` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### BSgenome.Mmusculus.UCSC.mm10


|`BSgenome.Mmusculus.UCSC.mm10` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### bsseq


|`bsseq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### bumphunter


|`bumphunter` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ca


|`ca` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.71.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### CAGEfightR


|`CAGEfightR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### CAGEr


|`CAGEr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.4.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.8.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### CAMERA


|`CAMERA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.54.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.58.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.62.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Category


|`Category` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.64.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.68.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.72.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ccdata


|`ccdata` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ccmap


|`ccmap` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### CGHbase


|`CGHbase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.58.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.62.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.66.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### CGHcall


|`CGHcall` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.60.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.64.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.68.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ChIPpeakAnno


|`ChIPpeakAnno` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ChIPseeker


|`ChIPseeker` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### chromVAR


|`chromVAR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### clusterProfiler


|`clusterProfiler` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.14.3|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|4.6.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### CNEr


|`CNEr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### coloc


|`coloc` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|5.1.0.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|5.2.3|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### colorRamps


|`colorRamps` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.3.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.3.4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ComplexHeatmap


|`ComplexHeatmap` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.14.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.22.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ConsensusClusterPlus


|`ConsensusClusterPlus` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.62.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.66.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.70.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### conumee


|`conumee` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### crossmeta


|`crossmeta` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### cummeRbund


|`cummeRbund` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### cytolib


|`cytolib` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.14.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### CytoML


|`CytoML` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### dada2


|`dada2` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ddPCRclust


|`ddPCRclust` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.18.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DECIPHER


|`DECIPHER` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DeconRNASeq


|`DeconRNASeq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### decontam


|`decontam` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.18.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### decoupleR


|`decoupleR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.4.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.8.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### DEGseq


|`DEGseq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.52.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.56.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.60.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DelayedArray


|`DelayedArray` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DelayedMatrixStats


|`DelayedMatrixStats` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### densEstBayes


|`densEstBayes` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0-2.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.0-2.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### derfinder


|`derfinder` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### derfinderHelper


|`derfinderHelper` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DESeq2


|`DESeq2` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### diffcyt


|`diffcyt` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.18.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### dir.expiry


|`dir.expiry` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### directlabels


|`directlabels` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2024.1.21|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### DirichletMultinomial


|`DirichletMultinomial` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DNABarcodes


|`DNABarcodes` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.28.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.32.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.36.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DNAcopy


|`DNAcopy` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.72.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.76.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.80.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DO.db


|`DO.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### docopt


|`docopt` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.7.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### DOSE


|`DOSE` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.24.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.28.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### dqrng


|`dqrng` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.3.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.4.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DRIMSeq


|`DRIMSeq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DropletUtils


|`DropletUtils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.18.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DSS


|`DSS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.50.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.54.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### dupRadar


|`dupRadar` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.28.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.32.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.36.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### DynDoc


|`DynDoc` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### EBImage


|`EBImage` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### edgeR


|`edgeR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.40.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.0.12|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.4.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### egg


|`egg` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.4.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### emmeans


|`emmeans` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.8.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### enrichplot


|`enrichplot` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.18.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### EnsDb.Hsapiens.v75


|`EnsDb.Hsapiens.v75` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.99.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### EnsDb.Hsapiens.v79


|`EnsDb.Hsapiens.v79` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.99.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### EnsDb.Hsapiens.v86


|`EnsDb.Hsapiens.v86` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.99.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ensembldb


|`ensembldb` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.22.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.26.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.30.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### escape


|`escape` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.2.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### estimability


|`estimability` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ExperimentHub


|`ExperimentHub` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### extraDistr


|`extraDistr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.9.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### factoextra


|`factoextra` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### fANCOVA


|`fANCOVA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.6-1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### fda


|`fda` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|6.0.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|6.1.4|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|6.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### FDb.InfiniumMethylation.hg19


|`FDb.InfiniumMethylation.hg19` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.2.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### fds


|`fds` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.8|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### feature


|`feature` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.15|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### fgsea


|`fgsea` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### filelock


|`filelock` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.0.3|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### flowAI


|`flowAI` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.28.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.32.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.36.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowClean


|`flowClean` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowClust


|`flowClust` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowCore


|`flowCore` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowDensity


|`flowDensity` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowFP


|`flowFP` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.56.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.60.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.64.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowMerge


|`flowMerge` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.50.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.54.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowPeaks


|`flowPeaks` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### FlowSOM


|`FlowSOM` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### FlowSorted.Blood.EPIC


|`FlowSorted.Blood.EPIC` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.2.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.6.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### FlowSorted.CordBloodCombined.450k


|`FlowSorted.CordBloodCombined.450k` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.14.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.22.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowStats


|`flowStats` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.14.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowViz


|`flowViz` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.62.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.66.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.70.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### flowWorkspace


|`flowWorkspace` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.10.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.14.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### FRASER


|`FRASER` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### fresh


|`fresh` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.2.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.2.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### gcrma


|`gcrma` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.70.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.74.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.78.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### gdsfmt


|`gdsfmt` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### genefilter


|`genefilter` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.80.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.84.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.88.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### geneLenDataBase


|`geneLenDataBase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### geneplotter


|`geneplotter` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GENESIS


|`GENESIS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.28.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.32.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.36.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GENIE3


|`GENIE3` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### genomation


|`genomation` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomeInfoDb


|`GenomeInfoDb` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.5|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomeInfoDbData


|`GenomeInfoDbData` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.11|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.2.13|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.2.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### GenomicAlignments


|`GenomicAlignments` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomicFeatures


|`GenomicFeatures` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.50.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.54.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.58.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomicFiles


|`GenomicFiles` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomicInteractions


|`GenomicInteractions` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomicRanges


|`GenomicRanges` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.50.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.54.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.58.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GenomicScores


|`GenomicScores` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.14.3|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GEOmap


|`GEOmap` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.5-0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.5-11|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.5-5|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### GEOquery


|`GEOquery` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.66.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.70.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.74.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggbio


|`ggbio` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.50.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.54.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggcyto


|`ggcyto` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggdendro


|`ggdendro` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.23|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggnewscale


|`ggnewscale` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.4.8|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.4.9|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.5.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggpicrust2


|`ggpicrust2` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.1.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggpointdensity


|`ggpointdensity` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ggrastr


|`ggrastr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.0.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ggseqlogo


|`ggseqlogo` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggtangle


|`ggtangle` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.0.4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggthemes


|`ggthemes` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.2.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|5.0.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|5.1.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ggtree


|`ggtree` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|3.6.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### GLAD


|`GLAD` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.62.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.66.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.70.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Glimma


|`Glimma` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### GlobalAncova


|`GlobalAncova` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.20.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.24.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### globaltest


|`globaltest` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|5.52.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|5.56.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|5.60.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GO.db


|`GO.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GOSemSim


|`GOSemSim` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.28.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### goseq


|`goseq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.50.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.54.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.58.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GOstats


|`GOstats` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.64.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.68.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.72.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### graph


|`graph` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### graphite


|`graphite` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GSEABase


|`GSEABase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.60.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.64.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.68.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### gsignal


|`gsignal` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3-7|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### gsmoothr


|`gsmoothr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### gson


|`gson` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### GSVA


|`GSVA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.50.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.0.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Gviz


|`Gviz` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.42.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.46.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GWASExactHW


|`GWASExactHW` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.01|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### GWASTools


|`GWASTools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### hahmmr


|`hahmmr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### HDF5Array


|`HDF5Array` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### HDO.db


|`HDO.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.99.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### hdrcde


|`hdrcde` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### heatmaply


|`heatmaply` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.5.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### hgu133plus2.db


|`hgu133plus2.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.13.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### hiAnnotator


|`hiAnnotator` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### HiCBricks


|`HiCBricks` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.20.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.24.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### HiCcompare


|`HiCcompare` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### HMMcopy


|`HMMcopy` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Homo.sapiens


|`Homo.sapiens` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.3.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### IHW


|`IHW` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### IlluminaHumanMethylation450kanno.ilmn12.hg19


|`IlluminaHumanMethylation450kanno.ilmn12.hg19` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.6.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### IlluminaHumanMethylation450kmanifest


|`IlluminaHumanMethylation450kmanifest` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.4.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### IlluminaHumanMethylationEPICanno.ilm10b2.hg19


|`IlluminaHumanMethylationEPICanno.ilm10b2.hg19` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### IlluminaHumanMethylationEPICanno.ilm10b4.hg19


|`IlluminaHumanMethylationEPICanno.ilm10b4.hg19` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### IlluminaHumanMethylationEPICmanifest


|`IlluminaHumanMethylationEPICmanifest` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### IlluminaHumanMethylationEPICv2anno.20a1.hg38


|`IlluminaHumanMethylationEPICv2anno.20a1.hg38` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### IlluminaHumanMethylationEPICv2manifest


|`IlluminaHumanMethylationEPICv2manifest` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### illuminaio


|`illuminaio` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### impute


|`impute` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.72.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.76.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.80.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### InteractionSet


|`InteractionSet` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### interactiveDisplayBase


|`interactiveDisplayBase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### intervals


|`intervals` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.15.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.15.5|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### IRanges


|`IRanges` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### isva


|`isva` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### JASPAR2020


|`JASPAR2020` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.99.10|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### KEGGgraph


|`KEGGgraph` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.58.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.62.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.66.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### KEGGREST


|`KEGGREST` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### LEA


|`LEA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.10.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### lefser


|`lefser` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.16.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### limma


|`limma` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.54.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.58.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.62.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### log4r


|`log4r` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.4.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.4.4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### lpsymphony


|`lpsymphony` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### lsa


|`lsa` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.73.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### lumi


|`lumi` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.50.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.54.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.58.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### M3Drop


|`M3Drop` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Maaslin2


|`Maaslin2` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### marray


|`marray` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### maSigPro


|`maSigPro` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.70.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.74.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.78.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MassSpecWavelet


|`MassSpecWavelet` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.64.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.68.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.72.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MatrixGenerics


|`MatrixGenerics` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MBA


|`MBA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1-0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.1-2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MEDIPS


|`MEDIPS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.50.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.54.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.58.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MetaboCoreUtils


|`MetaboCoreUtils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### metagenomeSeq


|`metagenomeSeq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.43.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### metaMA


|`metaMA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.1.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### metap


|`metap` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.11|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.9|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### metapod


|`metapod` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### MethylSeekR


|`MethylSeekR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### methylumi


|`methylumi` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Mfuzz


|`Mfuzz` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.58.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.62.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.66.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### mia


|`mia` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### minfi


|`minfi` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### missMethyl


|`missMethyl` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### mixOmics


|`mixOmics` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|6.22.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|6.26.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|6.30.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### mixsqp


|`mixsqp` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3-48|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.3-54|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### MLInterfaces


|`MLInterfaces` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.78.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.82.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.86.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MotifDb


|`MotifDb` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### motifmatchr


|`motifmatchr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### motifStack


|`motifStack` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.42.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.46.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MsCoreUtils


|`MsCoreUtils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MsExperiment


|`MsExperiment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.8.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MsFeatures


|`MsFeatures` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### msigdbr


|`msigdbr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|7.5.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### MSnbase


|`MSnbase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.24.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.28.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MSstats


|`MSstats` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|4.6.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### MSstatsConvert


|`MSstatsConvert` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### MSstatsLiP


|`MSstatsLiP` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.4.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.8.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### MSstatsPTM


|`MSstatsPTM` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.4.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.8.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MSstatsTMT


|`MSstatsTMT` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### MultiAssayExperiment


|`MultiAssayExperiment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.28.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.32.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### MultiDataSet


|`MultiDataSet` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### multtest


|`multtest` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.54.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.58.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.62.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### muscat


|`muscat` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.16.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### mutoss


|`mutoss` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1-13|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### mzID


|`mzID` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### mzR


|`mzR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.32.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### NADA


|`NADA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.6-1.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### ncdfFlow


|`ncdfFlow` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### NMF


|`NMF` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.25|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.26|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.28|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### NOISeq


|`NOISeq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.42.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.46.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### numbat


|`numbat` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.3.2-1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.4.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### oligo


|`oligo` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.62.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.66.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.70.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### oligoClasses


|`oligoClasses` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.60.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.64.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.68.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ontologyIndex


|`ontologyIndex` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.11|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.12|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### oompaBase


|`oompaBase` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.2.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### oompaData


|`oompaData` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.1.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.1.4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### openCyto


|`openCyto` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### org.Hs.eg.db


|`org.Hs.eg.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### org.Mm.eg.db


|`org.Mm.eg.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### org.Rn.eg.db


|`org.Rn.eg.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### OrganismDbi


|`OrganismDbi` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.40.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.44.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.48.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### OUTRIDER


|`OUTRIDER` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.16.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.20.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.24.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### pathview


|`pathview` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### pcaMethods


|`pcaMethods` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.90.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.94.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.98.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### perm


|`perm` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0-0.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.0-0.4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### PFAM.db


|`PFAM.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### phyloseq


|`phyloseq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.42.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.46.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### plyranges


|`plyranges` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### pmp


|`pmp` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### polyester


|`polyester` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### poweRlaw


|`poweRlaw` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.70.6|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.80.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### preprocessCore


|`preprocessCore` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.60.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.64.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.68.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### pRoloc


|`pRoloc` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### pRolocdata


|`pRolocdata` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.44.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### pRolocGUI


|`pRolocGUI` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### ProtGenerics


|`ProtGenerics` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### PRROC


|`PRROC` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.3.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### PSCBS


|`PSCBS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.66.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.67.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### PSMatch


|`PSMatch` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### PureCN


|`PureCN` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.4.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.8.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### pwalign


|`pwalign` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### qap


|`qap` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1-2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### QDNAseq


|`QDNAseq` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.38.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.42.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### QFeatures


|`QFeatures` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### qlcMatrix


|`qlcMatrix` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.9.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.9.8|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### qqconf


|`qqconf` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.3.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.3.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### quantsmooth


|`quantsmooth` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.64.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.68.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.72.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### qvalue


|`qvalue` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### R.devices


|`R.devices` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.17.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.17.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### R.filesets


|`R.filesets` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.15.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.15.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### R.huge


|`R.huge` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.10.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.9.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### rainbow


|`rainbow` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.8|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### randomcoloR


|`randomcoloR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.1.0.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### rARPACK


|`rARPACK` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.11-0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### RBGL


|`RBGL` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.74.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.78.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.82.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### rbiom


|`rbiom` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.3|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RcisTarget


|`RcisTarget` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.18.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.22.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.26.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RcppAnnoy


|`RcppAnnoy` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.0.20|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.0.22|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### RcppHNSW


|`RcppHNSW` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.4.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.5.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.6.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RcppML


|`RcppML` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### RcppZiggurat


|`RcppZiggurat` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.6|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### reactome.db


|`reactome.db` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.82.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.86.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.89.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ReactomePA


|`ReactomePA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.42.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.46.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### regioneR


|`regioneR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### reldist


|`reldist` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.7-2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### remaCor


|`remaCor` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.0.11|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.0.16|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.0.18|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Repitools


|`Repitools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ReportingTools


|`ReportingTools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.42.3|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ResidualMatrix


|`ResidualMatrix` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### restfulr


|`restfulr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.0.15|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### Rfast


|`Rfast` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.1.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### RFOC


|`RFOC` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.4-10|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.4-6|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### rGADEM


|`rGADEM` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.50.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.54.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Rgraphviz


|`Rgraphviz` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.42.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.46.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### rhdf5


|`rhdf5` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.42.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.46.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.50.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### rhdf5filters


|`rhdf5filters` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Rhdf5lib


|`Rhdf5lib` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Rhtslib


|`Rhtslib` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.4.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Ringo


|`Ringo` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.62.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.66.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### RNASeqPower


|`RNASeqPower` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RnBeads


|`RnBeads` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.20.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.24.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RnBeads.hg19


|`RnBeads.hg19` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RnBeads.hg38


|`RnBeads.hg38` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RnBeads.mm10


|`RnBeads.mm10` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### RnBeads.mm9


|`RnBeads.mm9` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RnBeads.rn5


|`RnBeads.rn5` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ROC


|`ROC` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.74.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.78.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.82.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### rols


|`rols` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ROntoTools


|`ROntoTools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.26.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ropls


|`ropls` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.30.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RPMG


|`RPMG` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.2-3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.2-7|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### RProtoBufLib


|`RProtoBufLib` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Rsamtools


|`Rsamtools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.14.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.18.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.22.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### RSEIS


|`RSEIS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.1-4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.1-6|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.2-4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Rsubread


|`Rsubread` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.16.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### rsvd


|`rsvd` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.0.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### rtracklayer


|`rtracklayer` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.58.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.62.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.66.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Rwave


|`Rwave` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.6-5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### S4Arrays


|`S4Arrays` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.6.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### S4Vectors


|`S4Vectors` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.36.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.40.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### samr


|`samr` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### SamSPECTRAL


|`SamSPECTRAL` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.52.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.56.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.60.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SC3


|`SC3` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ScaledMatrix


|`ScaledMatrix` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### SCANVIS


|`SCANVIS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.16.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### scater


|`scater` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### scattermore


|`scattermore` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.8|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### scDblFinder


|`scDblFinder` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.16.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.20.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### scistreer


|`scistreer` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.1.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### scran


|`scran` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### scrime


|`scrime` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.3.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### scuttle


|`scuttle` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### SeqArray


|`SeqArray` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### seqLogo


|`seqLogo` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.64.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.68.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.72.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### seqPattern


|`seqPattern` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.34.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.38.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SeqVarTools


|`SeqVarTools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### seriation


|`seriation` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.5.4|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.5.6|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Seurat


|`Seurat` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.3.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|5.0.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|5.1.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SeuratObject


|`SeuratObject` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|4.1.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|5.0.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|5.0.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### shinyBS


|`shinyBS` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.61.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### shinydashboardPlus


|`shinydashboardPlus` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.0.5|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### shinyFiles


|`shinyFiles` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.9.3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### shinyhelper


|`shinyhelper` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.3.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### shinypanel


|`shinypanel` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### shinyWidgets


|`shinyWidgets` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.7.6|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.8.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.8.7|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### ShortRead


|`ShortRead` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.56.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.60.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.64.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### siggenes


|`siggenes` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.72.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.76.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.80.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Signac


|`Signac` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.9.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### SimBu


|`SimBu` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.3|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.8.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### simona


|`simona` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### simplifyEnrichment


|`simplifyEnrichment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.0.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SingleCellExperiment


|`SingleCellExperiment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SingleR


|`SingleR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.4.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.8.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### sitmo


|`sitmo` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.0.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### slingshot


|`slingshot` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### SMVar


|`SMVar` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.3.4|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### SNPRelate


|`SNPRelate` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.32.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.36.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.40.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### snpStats


|`snpStats` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.48.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.52.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.56.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SparseArray


|`SparseArray` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.3|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.6.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### sparseMatrixStats


|`sparseMatrixStats` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### sparsesvd


|`sparsesvd` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.2-2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### SpatialExperiment


|`SpatialExperiment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### Spectra


|`Spectra` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SPIA


|`SPIA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.50.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.54.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.58.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### splancs


|`splancs` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.01-43|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.01-44|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.01-45|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SPOTlight


|`SPOTlight` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.2.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.6.7|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### stageR


|`stageR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.24.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.28.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### struct


|`struct` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### structToolbox


|`structToolbox` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.14.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.18.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### SummarizedExperiment


|`SummarizedExperiment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.28.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.32.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.36.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### susieR


|`susieR` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.12.35|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### sva


|`sva` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.46.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.50.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.54.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### TailRank


|`TailRank` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.2.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### TFBSTools


|`TFBSTools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.36.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.40.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.44.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### TFMPvalue


|`TFMPvalue` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.0.9|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### tkWidgets


|`tkWidgets` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### TrajectoryUtils


|`TrajectoryUtils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### treeio


|`treeio` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.22.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.26.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.30.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### TreeSummarizedExperiment


|`TreeSummarizedExperiment` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|2.14.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.6.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### TSP


|`TSP` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2-3|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.2-4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### TxDb.Hsapiens.UCSC.hg19.knownGene


|`TxDb.Hsapiens.UCSC.hg19.knownGene` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.2.2|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### TxDb.Mmusculus.UCSC.mm10.knownGene


|`TxDb.Mmusculus.UCSC.mm10.knownGene` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.10.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### txdbmaker


|`txdbmaker` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### tximport


|`tximport` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.26.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.30.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.34.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### UCell


|`UCell` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.10.1|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.2.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.6.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### UCSC.utils


|`UCSC.utils` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.2.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### universalmotif


|`universalmotif` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.24.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### uwot


|`uwot` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.1.14|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.1.16|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.2.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### variancePartition


|`variancePartition` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.28.7|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.32.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.36.2|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### VariantAnnotation


|`VariantAnnotation` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### venn


|`venn` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.11|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.12|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### vsn


|`vsn` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.66.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|3.70.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|3.74.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### waiter


|`waiter` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.2.5|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`<br/>`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`<br/>`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### wateRmelon


|`wateRmelon` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|2.12.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|2.4.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|2.8.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|

### WGCNA


|`WGCNA` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.72-1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.72-5|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.73|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### widgetTools


|`widgetTools` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.76.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.80.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.84.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### Wrench


|`Wrench` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.16.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.20.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.24.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### xcms


|`xcms` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|3.20.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|4.0.2|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|4.4.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### XVector


|`XVector` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|0.38.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|0.42.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|0.46.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### zCompositions


|`zCompositions` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.4.0-1|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.5.0-1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.5.0-4|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|

### zellkonverter


|`zellkonverter` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.12.1|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.16.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|
|1.8.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|

### zlibbioc


|`zlibbioc` version|R-bundle-Bioconductor modules that include it|
| --- | --- |
|1.44.0|`R-bundle-Bioconductor/3.16-foss-2022b-R-4.2.2`|
|1.48.0|`R-bundle-Bioconductor/3.18-foss-2023a-R-4.3.2`|
|1.52.0|`R-bundle-Bioconductor/3.20-foss-2024a-R-4.4.2`|