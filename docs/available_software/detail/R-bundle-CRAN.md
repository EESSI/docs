# R-bundle-CRAN


Bundle of R packages from CRAN

<small>homepage: </small><span class="software-link">[https://www.r-project.org/](https://www.r-project.org/)</span>

## Available installations


|Version|Supported CPU targets|Supported GPU targets|Module|
| --- | --- | --- | --- |
|2023.12|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`R-bundle-CRAN/2023.12-foss-2023a`|
|2024.06|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`R-bundle-CRAN/2024.06-foss-2023b`|
|2024.11|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|`R-bundle-CRAN/2024.11-foss-2024a`|

## Extensions

Overview of extensions included in {'versions': [{'homepage': 'https://www.r-project.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023a'}, 'toolchain_families_compatibility': ['2023a_foss'], 'module': {'full_module_name': 'R-bundle-CRAN/2023.12-foss-2023a', 'module_name': 'R-bundle-CRAN', 'module_version': '2023.12-foss-2023a'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/12.3.0', 'module_name': 'GCCcore', 'module_version': '12.3.0'}, {'full_module_name': 'GCC/12.3.0', 'module_name': 'GCC', 'module_version': '12.3.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-12.3.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-12.3.0'}, {'full_module_name': 'libxml2/2.11.4-GCCcore-12.3.0', 'module_name': 'libxml2', 'module_version': '2.11.4-GCCcore-12.3.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-12.3.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-12.3.0'}, {'full_module_name': 'hwloc/2.9.1-GCCcore-12.3.0', 'module_name': 'hwloc', 'module_version': '2.9.1-GCCcore-12.3.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-12.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-12.3.0'}, {'full_module_name': 'UCX/1.14.1-GCCcore-12.3.0', 'module_name': 'UCX', 'module_version': '1.14.1-GCCcore-12.3.0'}, {'full_module_name': 'libfabric/1.18.0-GCCcore-12.3.0', 'module_name': 'libfabric', 'module_version': '1.18.0-GCCcore-12.3.0'}, {'full_module_name': 'PMIx/4.2.4-GCCcore-12.3.0', 'module_name': 'PMIx', 'module_version': '4.2.4-GCCcore-12.3.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-12.3.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenMPI/4.1.5-GCC-12.3.0', 'module_name': 'OpenMPI', 'module_version': '4.1.5-GCC-12.3.0'}, {'full_module_name': 'OpenBLAS/0.3.23-GCC-12.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.23-GCC-12.3.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-12.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-12.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-12.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-12.3.0'}, {'full_module_name': 'gompi/2023a', 'module_name': 'gompi', 'module_version': '2023a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023a-fb'}, {'full_module_name': 'foss/2023a', 'module_name': 'foss', 'module_version': '2023a'}, {'full_module_name': 'gfbf/2023a', 'module_name': 'gfbf', 'module_version': '2023a'}, {'full_module_name': 'expat/2.5.0-GCCcore-12.3.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'libpng/1.6.39-GCCcore-12.3.0', 'module_name': 'libpng', 'module_version': '1.6.39-GCCcore-12.3.0'}, {'full_module_name': 'Brotli/1.0.9-GCCcore-12.3.0', 'module_name': 'Brotli', 'module_version': '1.0.9-GCCcore-12.3.0'}, {'full_module_name': 'freetype/2.13.0-GCCcore-12.3.0', 'module_name': 'freetype', 'module_version': '2.13.0-GCCcore-12.3.0'}, {'full_module_name': 'fontconfig/2.14.2-GCCcore-12.3.0', 'module_name': 'fontconfig', 'module_version': '2.14.2-GCCcore-12.3.0'}, {'full_module_name': 'xorg-macros/1.20.0-GCCcore-12.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.0-GCCcore-12.3.0'}, {'full_module_name': 'X11/20230603-GCCcore-12.3.0', 'module_name': 'X11', 'module_version': '20230603-GCCcore-12.3.0'}, {'full_module_name': 'gzip/1.12-GCCcore-12.3.0', 'module_name': 'gzip', 'module_version': '1.12-GCCcore-12.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-12.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-12.3.0'}, {'full_module_name': 'zstd/1.5.5-GCCcore-12.3.0', 'module_name': 'zstd', 'module_version': '1.5.5-GCCcore-12.3.0'}, {'full_module_name': 'libdrm/2.4.115-GCCcore-12.3.0', 'module_name': 'libdrm', 'module_version': '2.4.115-GCCcore-12.3.0'}, {'full_module_name': 'libglvnd/1.6.0-GCCcore-12.3.0', 'module_name': 'libglvnd', 'module_version': '1.6.0-GCCcore-12.3.0'}, {'full_module_name': 'libunwind/1.6.2-GCCcore-12.3.0', 'module_name': 'libunwind', 'module_version': '1.6.2-GCCcore-12.3.0'}, {'full_module_name': 'LLVM/16.0.6-GCCcore-12.3.0', 'module_name': 'LLVM', 'module_version': '16.0.6-GCCcore-12.3.0'}, {'full_module_name': 'Mesa/23.1.4-GCCcore-12.3.0', 'module_name': 'Mesa', 'module_version': '23.1.4-GCCcore-12.3.0'}, {'full_module_name': 'libGLU/9.0.3-GCCcore-12.3.0', 'module_name': 'libGLU', 'module_version': '9.0.3-GCCcore-12.3.0'}, {'full_module_name': 'pixman/0.42.2-GCCcore-12.3.0', 'module_name': 'pixman', 'module_version': '0.42.2-GCCcore-12.3.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-12.3.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-12.3.0'}, {'full_module_name': 'PCRE2/10.42-GCCcore-12.3.0', 'module_name': 'PCRE2', 'module_version': '10.42-GCCcore-12.3.0'}, {'full_module_name': 'GLib/2.77.1-GCCcore-12.3.0', 'module_name': 'GLib', 'module_version': '2.77.1-GCCcore-12.3.0'}, {'full_module_name': 'cairo/1.17.8-GCCcore-12.3.0', 'module_name': 'cairo', 'module_version': '1.17.8-GCCcore-12.3.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-12.3.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'SQLite/3.42.0-GCCcore-12.3.0', 'module_name': 'SQLite', 'module_version': '3.42.0-GCCcore-12.3.0'}, {'full_module_name': 'NASM/2.16.01-GCCcore-12.3.0', 'module_name': 'NASM', 'module_version': '2.16.01-GCCcore-12.3.0'}, {'full_module_name': 'libjpeg-turbo/2.1.5.1-GCCcore-12.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '2.1.5.1-GCCcore-12.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-12.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-12.3.0'}, {'full_module_name': 'libdeflate/1.18-GCCcore-12.3.0', 'module_name': 'libdeflate', 'module_version': '1.18-GCCcore-12.3.0'}, {'full_module_name': 'LibTIFF/4.5.0-GCCcore-12.3.0', 'module_name': 'LibTIFF', 'module_version': '4.5.0-GCCcore-12.3.0'}, {'full_module_name': 'Java/11.0.27', 'module_name': 'Java', 'module_version': '11.0.27'}, {'full_module_name': 'Java/11', 'module_name': 'Java', 'module_version': '11'}, {'full_module_name': 'PCRE/8.45-GCCcore-12.3.0', 'module_name': 'PCRE', 'module_version': '8.45-GCCcore-12.3.0'}, {'full_module_name': 'libgit2/1.7.1-GCCcore-12.3.0', 'module_name': 'libgit2', 'module_version': '1.7.1-GCCcore-12.3.0'}, {'full_module_name': 'cURL/8.0.1-GCCcore-12.3.0', 'module_name': 'cURL', 'module_version': '8.0.1-GCCcore-12.3.0'}, {'full_module_name': 'Tk/8.6.13-GCCcore-12.3.0', 'module_name': 'Tk', 'module_version': '8.6.13-GCCcore-12.3.0'}, {'full_module_name': 'ICU/73.2-GCCcore-12.3.0', 'module_name': 'ICU', 'module_version': '73.2-GCCcore-12.3.0'}, {'full_module_name': 'HarfBuzz/5.3.1-GCCcore-12.3.0', 'module_name': 'HarfBuzz', 'module_version': '5.3.1-GCCcore-12.3.0'}, {'full_module_name': 'FriBidi/1.0.12-GCCcore-12.3.0', 'module_name': 'FriBidi', 'module_version': '1.0.12-GCCcore-12.3.0'}, {'full_module_name': 'R/4.3.2-gfbf-2023a', 'module_name': 'R', 'module_version': '4.3.2-gfbf-2023a'}, {'full_module_name': 'GMP/6.2.1-GCCcore-12.3.0', 'module_name': 'GMP', 'module_version': '6.2.1-GCCcore-12.3.0'}, {'full_module_name': 'NLopt/2.7.1-GCCcore-12.3.0', 'module_name': 'NLopt', 'module_version': '2.7.1-GCCcore-12.3.0'}, {'full_module_name': 'libogg/1.3.5-GCCcore-12.3.0', 'module_name': 'libogg', 'module_version': '1.3.5-GCCcore-12.3.0'}, {'full_module_name': 'FLAC/1.4.2-GCCcore-12.3.0', 'module_name': 'FLAC', 'module_version': '1.4.2-GCCcore-12.3.0'}, {'full_module_name': 'libvorbis/1.3.7-GCCcore-12.3.0', 'module_name': 'libvorbis', 'module_version': '1.3.7-GCCcore-12.3.0'}, {'full_module_name': 'libopus/1.4-GCCcore-12.3.0', 'module_name': 'libopus', 'module_version': '1.4-GCCcore-12.3.0'}, {'full_module_name': 'LAME/3.100-GCCcore-12.3.0', 'module_name': 'LAME', 'module_version': '3.100-GCCcore-12.3.0'}, {'full_module_name': 'libsndfile/1.2.2-GCCcore-12.3.0', 'module_name': 'libsndfile', 'module_version': '1.2.2-GCCcore-12.3.0'}, {'full_module_name': 'Szip/2.1.1-GCCcore-12.3.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-12.3.0'}, {'full_module_name': 'HDF5/1.14.0-gompi-2023a', 'module_name': 'HDF5', 'module_version': '1.14.0-gompi-2023a'}, {'full_module_name': 'UDUNITS/2.2.28-GCCcore-12.3.0', 'module_name': 'UDUNITS', 'module_version': '2.2.28-GCCcore-12.3.0'}, {'full_module_name': 'GSL/2.7-GCC-12.3.0', 'module_name': 'GSL', 'module_version': '2.7-GCC-12.3.0'}, {'full_module_name': 'ATK/2.38.0-GCCcore-12.3.0', 'module_name': 'ATK', 'module_version': '2.38.0-GCCcore-12.3.0'}, {'full_module_name': 'at-spi2-core/2.49.91-GCCcore-12.3.0', 'module_name': 'at-spi2-core', 'module_version': '2.49.91-GCCcore-12.3.0'}, {'full_module_name': 'at-spi2-atk/2.38.0-GCCcore-12.3.0', 'module_name': 'at-spi2-atk', 'module_version': '2.38.0-GCCcore-12.3.0'}, {'full_module_name': 'Gdk-Pixbuf/2.42.10-GCCcore-12.3.0', 'module_name': 'Gdk-Pixbuf', 'module_version': '2.42.10-GCCcore-12.3.0'}, {'full_module_name': 'Pango/1.50.14-GCCcore-12.3.0', 'module_name': 'Pango', 'module_version': '1.50.14-GCCcore-12.3.0'}, {'full_module_name': 'libepoxy/1.5.10-GCCcore-12.3.0', 'module_name': 'libepoxy', 'module_version': '1.5.10-GCCcore-12.3.0'}, {'full_module_name': 'Wayland/1.22.0-GCCcore-12.3.0', 'module_name': 'Wayland', 'module_version': '1.22.0-GCCcore-12.3.0'}, {'full_module_name': 'GTK3/3.24.37-GCCcore-12.3.0', 'module_name': 'GTK3', 'module_version': '3.24.37-GCCcore-12.3.0'}, {'full_module_name': 'Ghostscript/10.01.2-GCCcore-12.3.0', 'module_name': 'Ghostscript', 'module_version': '10.01.2-GCCcore-12.3.0'}, {'full_module_name': 'JasPer/4.0.0-GCCcore-12.3.0', 'module_name': 'JasPer', 'module_version': '4.0.0-GCCcore-12.3.0'}, {'full_module_name': 'LittleCMS/2.15-GCCcore-12.3.0', 'module_name': 'LittleCMS', 'module_version': '2.15-GCCcore-12.3.0'}, {'full_module_name': 'ImageMagick/7.1.1-15-GCCcore-12.3.0', 'module_name': 'ImageMagick', 'module_version': '7.1.1-15-GCCcore-12.3.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-12.3.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-12.3.0'}, {'full_module_name': 'nodejs/18.17.1-GCCcore-12.3.0', 'module_name': 'nodejs', 'module_version': '18.17.1-GCCcore-12.3.0'}, {'full_module_name': 'Python/3.11.3-GCCcore-12.3.0', 'module_name': 'Python', 'module_version': '3.11.3-GCCcore-12.3.0'}, {'full_module_name': 'netCDF/4.9.2-gompi-2023a', 'module_name': 'netCDF', 'module_version': '4.9.2-gompi-2023a'}, {'full_module_name': 'GEOS/3.12.0-GCC-12.3.0', 'module_name': 'GEOS', 'module_version': '3.12.0-GCC-12.3.0'}, {'full_module_name': 'libarchive/3.6.2-GCCcore-12.3.0', 'module_name': 'libarchive', 'module_version': '3.6.2-GCCcore-12.3.0'}, {'full_module_name': 'nlohmann_json/3.11.2-GCCcore-12.3.0', 'module_name': 'nlohmann_json', 'module_version': '3.11.2-GCCcore-12.3.0'}, {'full_module_name': 'PROJ/9.2.0-GCCcore-12.3.0', 'module_name': 'PROJ', 'module_version': '9.2.0-GCCcore-12.3.0'}, {'full_module_name': 'libgeotiff/1.7.1-GCCcore-12.3.0', 'module_name': 'libgeotiff', 'module_version': '1.7.1-GCCcore-12.3.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-12.3.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-12.3.0'}, {'full_module_name': 'cryptography/41.0.1-GCCcore-12.3.0', 'module_name': 'cryptography', 'module_version': '41.0.1-GCCcore-12.3.0'}, {'full_module_name': 'virtualenv/20.23.1-GCCcore-12.3.0', 'module_name': 'virtualenv', 'module_version': '20.23.1-GCCcore-12.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.06-GCCcore-12.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.06-GCCcore-12.3.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-12.3.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-12.3.0'}, {'full_module_name': 'SciPy-bundle/2023.07-gfbf-2023a', 'module_name': 'SciPy-bundle', 'module_version': '2023.07-gfbf-2023a'}, {'full_module_name': 'libtirpc/1.3.3-GCCcore-12.3.0', 'module_name': 'libtirpc', 'module_version': '1.3.3-GCCcore-12.3.0'}, {'full_module_name': 'HDF/4.2.16-2-GCCcore-12.3.0', 'module_name': 'HDF', 'module_version': '4.2.16-2-GCCcore-12.3.0'}, {'full_module_name': 'Boost/1.82.0-GCC-12.3.0', 'module_name': 'Boost', 'module_version': '1.82.0-GCC-12.3.0'}, {'full_module_name': 'arpack-ng/3.9.0-foss-2023a', 'module_name': 'arpack-ng', 'module_version': '3.9.0-foss-2023a'}, {'full_module_name': 'Armadillo/12.6.2-foss-2023a', 'module_name': 'Armadillo', 'module_version': '12.6.2-foss-2023a'}, {'full_module_name': 'CFITSIO/4.3.0-GCCcore-12.3.0', 'module_name': 'CFITSIO', 'module_version': '4.3.0-GCCcore-12.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-12.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-12.3.0'}, {'full_module_name': 'json-c/0.16-GCCcore-12.3.0', 'module_name': 'json-c', 'module_version': '0.16-GCCcore-12.3.0'}, {'full_module_name': 'Xerces-C++/3.2.4-GCCcore-12.3.0', 'module_name': 'Xerces-C++', 'module_version': '3.2.4-GCCcore-12.3.0'}, {'full_module_name': 'Imath/3.1.7-GCCcore-12.3.0', 'module_name': 'Imath', 'module_version': '3.1.7-GCCcore-12.3.0'}, {'full_module_name': 'OpenEXR/3.1.7-GCCcore-12.3.0', 'module_name': 'OpenEXR', 'module_version': '3.1.7-GCCcore-12.3.0'}, {'full_module_name': 'Highway/1.0.4-GCCcore-12.3.0', 'module_name': 'Highway', 'module_version': '1.0.4-GCCcore-12.3.0'}, {'full_module_name': 'Brunsli/0.1-GCCcore-12.3.0', 'module_name': 'Brunsli', 'module_version': '0.1-GCCcore-12.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-12.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-12.3.0'}, {'full_module_name': 'LERC/4.0.0-GCCcore-12.3.0', 'module_name': 'LERC', 'module_version': '4.0.0-GCCcore-12.3.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-12.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-12.3.0'}, {'full_module_name': 'SWIG/4.1.1-GCCcore-12.3.0', 'module_name': 'SWIG', 'module_version': '4.1.1-GCCcore-12.3.0'}, {'full_module_name': 'GDAL/3.7.1-foss-2023a', 'module_name': 'GDAL', 'module_version': '3.7.1-foss-2023a'}, {'full_module_name': 'MPFR/4.2.0-GCCcore-12.3.0', 'module_name': 'MPFR', 'module_version': '4.2.0-GCCcore-12.3.0'}, {'full_module_name': 'PostgreSQL/16.1-GCCcore-12.3.0', 'module_name': 'PostgreSQL', 'module_version': '16.1-GCCcore-12.3.0'}, {'full_module_name': 'R-bundle-CRAN/2023.12-foss-2023a', 'module_name': 'R-bundle-CRAN', 'module_version': '2023.12-foss-2023a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Bundle of R packages from CRAN', 'version': '2023.12', 'versionsuffix': '', 'extensions': [{'type': 'r', 'name': 'abind', 'version': '1.4-5'}, {'type': 'r', 'name': 'magic', 'version': '1.6-1'}, {'type': 'r', 'name': 'RcppProgress', 'version': '0.4.2'}, {'type': 'r', 'name': 'lpSolve', 'version': '5.6.19'}, {'type': 'r', 'name': 'linprog', 'version': '0.9-4'}, {'type': 'r', 'name': 'geometry', 'version': '0.4.7'}, {'type': 'r', 'name': 'bit', 'version': '4.0.5'}, {'type': 'r', 'name': 'filehash', 'version': '2.4-5'}, {'type': 'r', 'name': 'ff', 'version': '4.0.9'}, {'type': 'r', 'name': 'bnlearn', 'version': '4.9.1'}, {'type': 'r', 'name': 'bootstrap', 'version': '2019.6'}, {'type': 'r', 'name': 'combinat', 'version': '0.0-8'}, {'type': 'r', 'name': 'deal', 'version': '1.2-42'}, {'type': 'r', 'name': 'fdrtool', 'version': '1.2.17'}, {'type': 'r', 'name': 'formatR', 'version': '1.14'}, {'type': 'r', 'name': 'gtools', 'version': '3.9.5'}, {'type': 'r', 'name': 'gdata', 'version': '3.0.0'}, {'type': 'r', 'name': 'GSA', 'version': '1.03.2'}, {'type': 'r', 'name': 'infotheo', 'version': '1.2.0.1'}, {'type': 'r', 'name': 'lars', 'version': '1.3'}, {'type': 'r', 'name': 'lazy', 'version': '1.2-18'}, {'type': 'r', 'name': 'kernlab', 'version': '0.9-32'}, {'type': 'r', 'name': 'markdown', 'version': '1.12'}, {'type': 'r', 'name': 'mlbench', 'version': '2.1-3.1'}, {'type': 'r', 'name': 'NLP', 'version': '0.2-1'}, {'type': 'r', 'name': 'mclust', 'version': '6.0.1'}, {'type': 'r', 'name': 'RANN', 'version': '2.6.1'}, {'type': 'r', 'name': 'rmeta', 'version': '3.0'}, {'type': 'r', 'name': 'MASS', 'version': '7.3-60'}, {'type': 'r', 'name': 'lattice', 'version': '0.22-5'}, {'type': 'r', 'name': 'nlme', 'version': '3.1-164'}, {'type': 'r', 'name': 'segmented', 'version': '2.0-0'}, {'type': 'r', 'name': 'som', 'version': '0.3-5.1'}, {'type': 'r', 'name': 'SuppDists', 'version': '1.1-9.7'}, {'type': 'r', 'name': 'stabledist', 'version': '0.7-1'}, {'type': 'r', 'name': 'survivalROC', 'version': '1.0.3.1'}, {'type': 'r', 'name': 'pspline', 'version': '1.0-19'}, {'type': 'r', 'name': 'timeDate', 'version': '4022.108'}, {'type': 'r', 'name': 'longmemo', 'version': '1.1-2'}, {'type': 'r', 'name': 'ADGofTest', 'version': '0.3'}, {'type': 'r', 'name': 'pixmap', 'version': '0.4-12'}, {'type': 'r', 'name': 'sp', 'version': '2.1-2'}, {'type': 'r', 'name': 'hms', 'version': '1.1.3'}, {'type': 'r', 'name': 'progress', 'version': '1.2.3'}, {'type': 'r', 'name': 'RcppArmadillo', 'version': '0.12.6.6.1'}, {'type': 'r', 'name': 'ade4', 'version': '1.7-22'}, {'type': 'r', 'name': 'AlgDesign', 'version': '1.2.1'}, {'type': 'r', 'name': 'BH', 'version': '1.81.0-1'}, {'type': 'r', 'name': 'Matrix', 'version': '1.6-4'}, {'type': 'r', 'name': 'Brobdingnag', 'version': '1.2-9'}, {'type': 'r', 'name': 'corpcor', 'version': '1.6.10'}, {'type': 'r', 'name': 'longitudinal', 'version': '1.1.13'}, {'type': 'r', 'name': 'backports', 'version': '1.4.1'}, {'type': 'r', 'name': 'checkmate', 'version': '2.3.1'}, {'type': 'r', 'name': 'cubature', 'version': '2.1.0'}, {'type': 'r', 'name': 'DEoptimR', 'version': '1.1-3'}, {'type': 'r', 'name': 'fastmatch', 'version': '1.1-4'}, {'type': 'r', 'name': 'iterators', 'version': '1.0.14'}, {'type': 'r', 'name': 'maps', 'version': '3.4.1.1'}, {'type': 'r', 'name': 'nnls', 'version': '1.5'}, {'type': 'r', 'name': 'sendmailR', 'version': '1.4-0'}, {'type': 'r', 'name': 'dotCall64', 'version': '1.1-1'}, {'type': 'r', 'name': 'spam', 'version': '2.10-0'}, {'type': 'r', 'name': 'subplex', 'version': '1.8'}, {'type': 'r', 'name': 'logspline', 'version': '2.1.21'}, {'type': 'r', 'name': 'ncbit', 'version': '2013.03.29.1'}, {'type': 'r', 'name': 'permute', 'version': '0.9-7'}, {'type': 'r', 'name': 'plotrix', 'version': '3.8-4'}, {'type': 'r', 'name': 'randomForest', 'version': '4.7-1.1'}, {'type': 'r', 'name': 'scatterplot3d', 'version': '0.3-44'}, {'type': 'r', 'name': 'SparseM', 'version': '1.81'}, {'type': 'r', 'name': 'tripack', 'version': '1.3-9.1'}, {'type': 'r', 'name': 'irace', 'version': '3.5'}, {'type': 'r', 'name': 'rJava', 'version': '1.0-10'}, {'type': 'r', 'name': 'RColorBrewer', 'version': '1.1-3'}, {'type': 'r', 'name': 'png', 'version': '0.1-8'}, {'type': 'r', 'name': 'jpeg', 'version': '0.1-10'}, {'type': 'r', 'name': 'deldir', 'version': '2.0-2'}, {'type': 'r', 'name': 'RcppEigen', 'version': '0.3.3.9.4'}, {'type': 'r', 'name': 'interp', 'version': '1.1-5'}, {'type': 'r', 'name': 'latticeExtra', 'version': '0.6-30'}, {'type': 'r', 'name': 'plyr', 'version': '1.8.9'}, {'type': 'r', 'name': 'gtable', 'version': '0.3.4'}, {'type': 'r', 'name': 'reshape2', 'version': '1.4.4'}, {'type': 'r', 'name': 'dichromat', 'version': '2.0-0.1'}, {'type': 'r', 'name': 'colorspace', 'version': '2.1-0'}, {'type': 'r', 'name': 'munsell', 'version': '0.5.0'}, {'type': 'r', 'name': 'labeling', 'version': '0.4.3'}, {'type': 'r', 'name': 'viridisLite', 'version': '0.4.2'}, {'type': 'r', 'name': 'farver', 'version': '2.1.1'}, {'type': 'r', 'name': 'scales', 'version': '1.3.0'}, {'type': 'r', 'name': 'zeallot', 'version': '0.1.0'}, {'type': 'r', 'name': 'assertthat', 'version': '0.2.1'}, {'type': 'r', 'name': 'lazyeval', 'version': '0.2.2'}, {'type': 'r', 'name': 'mgcv', 'version': '1.9-0'}, {'type': 'r', 'name': 'isoband', 'version': '0.2.7'}, {'type': 'r', 'name': 'ggplot2', 'version': '3.4.4'}, {'type': 'r', 'name': 'pROC', 'version': '1.18.5'}, {'type': 'r', 'name': 'quadprog', 'version': '1.5-8'}, {'type': 'r', 'name': 'BB', 'version': '2019.10-1'}, {'type': 'r', 'name': 'data.table', 'version': '1.14.10'}, {'type': 'r', 'name': 'BBmisc', 'version': '1.13'}, {'type': 'r', 'name': 'fail', 'version': '1.3'}, {'type': 'r', 'name': 'rlecuyer', 'version': '0.3-8'}, {'type': 'r', 'name': 'snow', 'version': '0.4-4'}, {'type': 'r', 'name': 'tree', 'version': '1.0-43'}, {'type': 'r', 'name': 'pls', 'version': '2.8-3'}, {'type': 'r', 'name': 'class', 'version': '7.3-22'}, {'type': 'r', 'name': 'proxy', 'version': '0.4-27'}, {'type': 'r', 'name': 'e1071', 'version': '1.7-14'}, {'type': 'r', 'name': 'nnet', 'version': '7.3-19'}, {'type': 'r', 'name': 'minqa', 'version': '1.2.6'}, {'type': 'r', 'name': 'MatrixModels', 'version': '0.5-3'}, {'type': 'r', 'name': 'matrixStats', 'version': '1.1.0'}, {'type': 'r', 'name': 'codetools', 'version': '0.2-19'}, {'type': 'r', 'name': 'foreach', 'version': '1.5.2'}, {'type': 'r', 'name': 'ModelMetrics', 'version': '1.2.2.2'}, {'type': 'r', 'name': 'generics', 'version': '0.1.3'}, {'type': 'r', 'name': 'tidyselect', 'version': '1.2.0'}, {'type': 'r', 'name': 'dplyr', 'version': '1.1.4'}, {'type': 'r', 'name': 'gower', 'version': '1.0.1'}, {'type': 'r', 'name': 'rpart', 'version': '4.1.23'}, {'type': 'r', 'name': 'survival', 'version': '3.5-7'}, {'type': 'r', 'name': 'KernSmooth', 'version': '2.23-22'}, {'type': 'r', 'name': 'globals', 'version': '0.16.2'}, {'type': 'r', 'name': 'listenv', 'version': '0.9.0'}, {'type': 'r', 'name': 'parallelly', 'version': '1.36.0'}, {'type': 'r', 'name': 'future', 'version': '1.33.0'}, {'type': 'r', 'name': 'future.apply', 'version': '1.11.0'}, {'type': 'r', 'name': 'progressr', 'version': '0.14.0'}, {'type': 'r', 'name': 'numDeriv', 'version': '2016.8-1.1'}, {'type': 'r', 'name': 'SQUAREM', 'version': '2021.1'}, {'type': 'r', 'name': 'lava', 'version': '1.7.3'}, {'type': 'r', 'name': 'shape', 'version': '1.4.6'}, {'type': 'r', 'name': 'diagram', 'version': '1.6.5'}, {'type': 'r', 'name': 'prodlim', 'version': '2023.08.28'}, {'type': 'r', 'name': 'ipred', 'version': '0.9-14'}, {'type': 'r', 'name': 'timechange', 'version': '0.2.0'}, {'type': 'r', 'name': 'lubridate', 'version': '1.9.3'}, {'type': 'r', 'name': 'tidyr', 'version': '1.3.0'}, {'type': 'r', 'name': 'hardhat', 'version': '1.3.0'}, {'type': 'r', 'name': 'tzdb', 'version': '0.4.0'}, {'type': 'r', 'name': 'clock', 'version': '0.7.0'}, {'type': 'r', 'name': 'recipes', 'version': '1.0.8'}, {'type': 'r', 'name': 'caret', 'version': '6.0-94'}, {'type': 'r', 'name': 'conquer', 'version': '1.3.3'}, {'type': 'r', 'name': 'quantreg', 'version': '5.97'}, {'type': 'r', 'name': 'robustbase', 'version': '0.99-1'}, {'type': 'r', 'name': 'zoo', 'version': '1.8-12'}, {'type': 'r', 'name': 'lmtest', 'version': '0.9-40'}, {'type': 'r', 'name': 'vcd', 'version': '1.4-11'}, {'type': 'r', 'name': 'snowfall', 'version': '1.84-6.3'}, {'type': 'r', 'name': 'bindr', 'version': '0.1.1'}, {'type': 'r', 'name': 'plogr', 'version': '0.2.0'}, {'type': 'r', 'name': 'bindrcpp', 'version': '0.2.2'}, {'type': 'r', 'name': 'tmvnsim', 'version': '1.0-2'}, {'type': 'r', 'name': 'mnormt', 'version': '2.1.1'}, {'type': 'r', 'name': 'foreign', 'version': '0.8-86'}, {'type': 'r', 'name': 'psych', 'version': '2.3.9'}, {'type': 'r', 'name': 'broom', 'version': '1.0.5'}, {'type': 'r', 'name': 'nloptr', 'version': '2.0.3'}, {'type': 'r', 'name': 'boot', 'version': '1.3-28.1'}, {'type': 'r', 'name': 'statmod', 'version': '1.5.0'}, {'type': 'r', 'name': 'lme4', 'version': '1.1-35.1'}, {'type': 'r', 'name': 'ucminf', 'version': '1.2.0'}, {'type': 'r', 'name': 'ordinal', 'version': '2023.12-4'}, {'type': 'r', 'name': 'jomo', 'version': '2.7-6'}, {'type': 'r', 'name': 'bit64', 'version': '4.0.5'}, {'type': 'r', 'name': 'vroom', 'version': '1.6.5'}, {'type': 'r', 'name': 'readr', 'version': '2.1.4'}, {'type': 'r', 'name': 'forcats', 'version': '1.0.0'}, {'type': 'r', 'name': 'haven', 'version': '2.5.4'}, {'type': 'r', 'name': 'pan', 'version': '1.9'}, {'type': 'r', 'name': 'mitml', 'version': '0.4-5'}, {'type': 'r', 'name': 'glmnet', 'version': '4.1-8'}, {'type': 'r', 'name': 'mice', 'version': '3.16.0'}, {'type': 'r', 'name': 'urca', 'version': '1.3-3'}, {'type': 'r', 'name': 'fracdiff', 'version': '1.5-2'}, {'type': 'r', 'name': 'operator.tools', 'version': '1.6.3'}, {'type': 'r', 'name': 'formula.tools', 'version': '1.7.1'}, {'type': 'r', 'name': 'logistf', 'version': '1.26.0'}, {'type': 'r', 'name': 'akima', 'version': '0.6-3.4'}, {'type': 'r', 'name': 'bitops', 'version': '1.0-7'}, {'type': 'r', 'name': 'crosstalk', 'version': '1.2.1'}, {'type': 'r', 'name': 'plotly', 'version': '4.10.3'}, {'type': 'r', 'name': 'mixtools', 'version': '2.0.0'}, {'type': 'r', 'name': 'cluster', 'version': '2.1.6'}, {'type': 'r', 'name': 'gclus', 'version': '1.3.2'}, {'type': 'r', 'name': 'coda', 'version': '0.19-4'}, {'type': 'r', 'name': 'doMC', 'version': '1.3.8'}, {'type': 'r', 'name': 'DBI', 'version': '1.1.3'}, {'type': 'r', 'name': 'gam', 'version': '1.22-3'}, {'type': 'r', 'name': 'gamlss.data', 'version': '6.0-2'}, {'type': 'r', 'name': 'gamlss.dist', 'version': '6.1-1'}, {'type': 'r', 'name': 'gamlss', 'version': '5.4-20'}, {'type': 'r', 'name': 'gamlss.tr', 'version': '5.1-7'}, {'type': 'r', 'name': 'hwriter', 'version': '1.3.2.1'}, {'type': 'r', 'name': 'xts', 'version': '0.13.1'}, {'type': 'r', 'name': 'TTR', 'version': '0.24.4'}, {'type': 'r', 'name': 'quantmod', 'version': '0.4.25'}, {'type': 'r', 'name': 'mvtnorm', 'version': '1.2-4'}, {'type': 'r', 'name': 'pcaPP', 'version': '2.0-4'}, {'type': 'r', 'name': 'pscl', 'version': '1.5.5.1'}, {'type': 'r', 'name': 'blob', 'version': '1.2.4'}, {'type': 'r', 'name': 'RSQLite', 'version': '2.3.4'}, {'type': 'r', 'name': 'BatchJobs', 'version': '1.9'}, {'type': 'r', 'name': 'sandwich', 'version': '3.0-2'}, {'type': 'r', 'name': 'sfsmisc', 'version': '1.1-16'}, {'type': 'r', 'name': 'spatial', 'version': '7.3-17'}, {'type': 'r', 'name': 'VGAM', 'version': '1.1-9'}, {'type': 'r', 'name': 'waveslim', 'version': '1.8.4'}, {'type': 'r', 'name': 'profileModel', 'version': '0.6.1'}, {'type': 'r', 'name': 'brglm', 'version': '0.7.2'}, {'type': 'r', 'name': 'deSolve', 'version': '1.40'}, {'type': 'r', 'name': 'tseriesChaos', 'version': '0.1-13.1'}, {'type': 'r', 'name': 'tseries', 'version': '0.10-55'}, {'type': 'r', 'name': 'fastICA', 'version': '1.2-4'}, {'type': 'r', 'name': 'R.methodsS3', 'version': '1.8.2'}, {'type': 'r', 'name': 'R.oo', 'version': '1.25.0'}, {'type': 'r', 'name': 'cgdsr', 'version': '1.3.0'}, {'type': 'r', 'name': 'R.utils', 'version': '2.12.3'}, {'type': 'r', 'name': 'R.matlab', 'version': '3.7.0'}, {'type': 'r', 'name': 'gridExtra', 'version': '2.3'}, {'type': 'r', 'name': 'gbm', 'version': '2.1.8.1'}, {'type': 'r', 'name': 'Formula', 'version': '1.2-5'}, {'type': 'r', 'name': 'acepack', 'version': '1.4.2'}, {'type': 'r', 'name': 'proto', 'version': '1.0.0'}, {'type': 'r', 'name': 'chron', 'version': '2.3-61'}, {'type': 'r', 'name': 'viridis', 'version': '0.6.4'}, {'type': 'r', 'name': 'htmlTable', 'version': '2.4.2'}, {'type': 'r', 'name': 'Hmisc', 'version': '5.1-1'}, {'type': 'r', 'name': 'fastcluster', 'version': '1.2.3'}, {'type': 'r', 'name': 'registry', 'version': '0.5-1'}, {'type': 'r', 'name': 'bibtex', 'version': '0.5.1'}, {'type': 'r', 'name': 'pkgmaker', 'version': '0.32.10'}, {'type': 'r', 'name': 'rngtools', 'version': '1.5.2'}, {'type': 'r', 'name': 'doParallel', 'version': '1.0.17'}, {'type': 'r', 'name': 'gridBase', 'version': '0.4-7'}, {'type': 'r', 'name': 'irlba', 'version': '2.3.5.1'}, {'type': 'r', 'name': 'igraph', 'version': '1.5.1'}, {'type': 'r', 'name': 'GeneNet', 'version': '1.2.16'}, {'type': 'r', 'name': 'ape', 'version': '5.7-1'}, {'type': 'r', 'name': 'RJSONIO', 'version': '1.3-1.9'}, {'type': 'r', 'name': 'caTools', 'version': '1.18.2'}, {'type': 'r', 'name': 'gplots', 'version': '3.1.3'}, {'type': 'r', 'name': 'ROCR', 'version': '1.0-11'}, {'type': 'r', 'name': 'rjson', 'version': '0.2.21'}, {'type': 'r', 'name': 'seqinr', 'version': '4.2-36'}, {'type': 'r', 'name': 'LearnBayes', 'version': '2.15.1'}, {'type': 'r', 'name': 'gmodels', 'version': '2.18.1.1'}, {'type': 'r', 'name': 'expm', 'version': '0.999-8'}, {'type': 'r', 'name': 'terra', 'version': '1.7-55'}, {'type': 'r', 'name': 'raster', 'version': '3.6-26'}, {'type': 'r', 'name': 'spData', 'version': '2.3.0'}, {'type': 'r', 'name': 'units', 'version': '0.8-5'}, {'type': 'r', 'name': 'classInt', 'version': '0.4-10'}, {'type': 'r', 'name': 'vegan', 'version': '2.6-4'}, {'type': 'r', 'name': 'rncl', 'version': '0.8.7'}, {'type': 'r', 'name': 'XML', 'version': '3.99-0.16'}, {'type': 'r', 'name': 'reshape', 'version': '0.8.9'}, {'type': 'r', 'name': 'triebeard', 'version': '0.4.1'}, {'type': 'r', 'name': 'urltools', 'version': '1.7.3'}, {'type': 'r', 'name': 'httpcode', 'version': '0.3.0'}, {'type': 'r', 'name': 'crul', 'version': '1.4.0'}, {'type': 'r', 'name': 'bold', 'version': '1.3.0'}, {'type': 'r', 'name': 'rredlist', 'version': '0.7.1'}, {'type': 'r', 'name': 'rentrez', 'version': '1.2.3'}, {'type': 'r', 'name': 'rotl', 'version': '3.1.0'}, {'type': 'r', 'name': 'solrium', 'version': '1.2.0'}, {'type': 'r', 'name': 'ritis', 'version': '1.0.0'}, {'type': 'r', 'name': 'worrms', 'version': '0.4.3'}, {'type': 'r', 'name': 'natserv', 'version': '1.0.0'}, {'type': 'r', 'name': 'WikipediR', 'version': '1.5.0'}, {'type': 'r', 'name': 'ratelimitr', 'version': '0.4.1'}, {'type': 'r', 'name': 'rex', 'version': '1.2.1'}, {'type': 'r', 'name': 'WikidataQueryServiceR', 'version': '1.0.0'}, {'type': 'r', 'name': 'pbapply', 'version': '1.7-2'}, {'type': 'r', 'name': 'WikidataR', 'version': '2.3.3'}, {'type': 'r', 'name': 'wikitaxa', 'version': '0.4.0'}, {'type': 'r', 'name': 'phangorn', 'version': '2.11.1'}, {'type': 'r', 'name': 'uuid', 'version': '1.1-1'}, {'type': 'r', 'name': 'conditionz', 'version': '0.1.0'}, {'type': 'r', 'name': 'taxize', 'version': '0.9.100'}, {'type': 'r', 'name': 'RNeXML', 'version': '2.4.11'}, {'type': 'r', 'name': 'phylobase', 'version': '0.8.10'}, {'type': 'r', 'name': 'magick', 'version': '2.8.1'}, {'type': 'r', 'name': 'animation', 'version': '2.7'}, {'type': 'r', 'name': 'bigmemory.sri', 'version': '0.1.6'}, {'type': 'r', 'name': 'bigmemory', 'version': '4.6.1'}, {'type': 'r', 'name': 'calibrate', 'version': '1.7.7'}, {'type': 'r', 'name': 'clusterGeneration', 'version': '1.3.8'}, {'type': 'r', 'name': 'dismo', 'version': '1.3-14'}, {'type': 'r', 'name': 'extrafontdb', 'version': '1.0'}, {'type': 'r', 'name': 'Rttf2pt1', 'version': '1.3.12'}, {'type': 'r', 'name': 'extrafont', 'version': '0.19'}, {'type': 'r', 'name': 'fields', 'version': '15.2'}, {'type': 'r', 'name': 'shapefiles', 'version': '0.7.2'}, {'type': 'r', 'name': 'fossil', 'version': '0.4.0'}, {'type': 'r', 'name': 'optimParallel', 'version': '1.0-2'}, {'type': 'r', 'name': 'phytools', 'version': '2.0-3'}, {'type': 'r', 'name': 'geiger', 'version': '2.0.11'}, {'type': 'r', 'name': 'webshot', 'version': '0.5.5'}, {'type': 'r', 'name': 'shinyjs', 'version': '2.1.0'}, {'type': 'r', 'name': 'manipulateWidget', 'version': '0.11.1'}, {'type': 'r', 'name': 'rgl', 'version': '1.2.8'}, {'type': 'r', 'name': 'Rtsne', 'version': '0.17'}, {'type': 'r', 'name': 'labdsv', 'version': '2.1-0'}, {'type': 'r', 'name': 'stabs', 'version': '0.6-4'}, {'type': 'r', 'name': 'modeltools', 'version': '0.2-23'}, {'type': 'r', 'name': 'strucchange', 'version': '1.5-3'}, {'type': 'r', 'name': 'TH.data', 'version': '1.1-2'}, {'type': 'r', 'name': 'multcomp', 'version': '1.4-25'}, {'type': 'r', 'name': 'libcoin', 'version': '1.0-10'}, {'type': 'r', 'name': 'coin', 'version': '1.4-3'}, {'type': 'r', 'name': 'party', 'version': '1.3-14'}, {'type': 'r', 'name': 'inum', 'version': '1.0-5'}, {'type': 'r', 'name': 'partykit', 'version': '1.2-20'}, {'type': 'r', 'name': 'mboost', 'version': '2.9-9'}, {'type': 'r', 'name': 'msm', 'version': '1.7.1'}, {'type': 'r', 'name': 'nor1mix', 'version': '1.3-2'}, {'type': 'r', 'name': 'np', 'version': '0.60-17'}, {'type': 'r', 'name': 'polynom', 'version': '1.4-1'}, {'type': 'r', 'name': 'polspline', 'version': '1.1.24'}, {'type': 'r', 'name': 'rms', 'version': '6.7-1'}, {'type': 'r', 'name': 'RWekajars', 'version': '3.9.3-2'}, {'type': 'r', 'name': 'RWeka', 'version': '0.4-46'}, {'type': 'r', 'name': 'slam', 'version': '0.1-50'}, {'type': 'r', 'name': 'tm', 'version': '0.7-11'}, {'type': 'r', 'name': 'leaps', 'version': '3.1'}, {'type': 'r', 'name': 'cNORM', 'version': '3.0.4'}, {'type': 'r', 'name': 'weights', 'version': '1.0.4'}, {'type': 'r', 'name': 'TraMineR', 'version': '2.2-8'}, {'type': 'r', 'name': 'chemometrics', 'version': '1.4.4'}, {'type': 'r', 'name': 'FNN', 'version': '1.1.3.2'}, {'type': 'r', 'name': 'miscTools', 'version': '0.6-28'}, {'type': 'r', 'name': 'maxLik', 'version': '1.5-2'}, {'type': 'r', 'name': 'gbRd', 'version': '0.4-11'}, {'type': 'r', 'name': 'rbibutils', 'version': '2.2.16'}, {'type': 'r', 'name': 'Rdpack', 'version': '2.6'}, {'type': 'r', 'name': 'dfidx', 'version': '0.0-5'}, {'type': 'r', 'name': 'mlogit', 'version': '1.1-1'}, {'type': 'r', 'name': 'getopt', 'version': '1.20.4'}, {'type': 'r', 'name': 'gsalib', 'version': '2.2.1'}, {'type': 'r', 'name': 'optparse', 'version': '1.7.3'}, {'type': 'r', 'name': 'labelled', 'version': '2.12.0'}, {'type': 'r', 'name': 'R.cache', 'version': '0.16.0'}, {'type': 'r', 'name': 'styler', 'version': '1.10.2'}, {'type': 'r', 'name': 'questionr', 'version': '0.7.8'}, {'type': 'r', 'name': 'klaR', 'version': '1.7-2'}, {'type': 'r', 'name': 'neuRosim', 'version': '0.2-14'}, {'type': 'r', 'name': 'locfit', 'version': '1.5-9.8'}, {'type': 'r', 'name': 'patchwork', 'version': '1.1.3'}, {'type': 'r', 'name': 'broom.helpers', 'version': '1.14.0'}, {'type': 'r', 'name': 'ggstats', 'version': '0.5.1'}, {'type': 'r', 'name': 'GGally', 'version': '2.2.0'}, {'type': 'r', 'name': 'beanplot', 'version': '1.3.1'}, {'type': 'r', 'name': 'clValid', 'version': '0.7'}, {'type': 'r', 'name': 'DiscriMiner', 'version': '0.1-29'}, {'type': 'r', 'name': 'ellipse', 'version': '0.5.0'}, {'type': 'r', 'name': 'pbkrtest', 'version': '0.5.2'}, {'type': 'r', 'name': 'carData', 'version': '3.0-5'}, {'type': 'r', 'name': 'maptools', 'version': '1.1-8'}, {'type': 'r', 'name': 'openxlsx', 'version': '4.2.5.2'}, {'type': 'r', 'name': 'rematch', 'version': '2.0.0'}, {'type': 'r', 'name': 'cellranger', 'version': '1.1.0'}, {'type': 'r', 'name': 'readxl', 'version': '1.4.3'}, {'type': 'r', 'name': 'writexl', 'version': '1.4.2'}, {'type': 'r', 'name': 'rio', 'version': '1.0.1'}, {'type': 'r', 'name': 'car', 'version': '3.1-2'}, {'type': 'r', 'name': 'flashClust', 'version': '1.01-2'}, {'type': 'r', 'name': 'ggrepel', 'version': '0.9.4'}, {'type': 'r', 'name': 'DT', 'version': '0.31'}, {'type': 'r', 'name': 'estimability', 'version': '1.4.1'}, {'type': 'r', 'name': 'emmeans', 'version': '1.8.9'}, {'type': 'r', 'name': 'multcompView', 'version': '0.1-9'}, {'type': 'r', 'name': 'FactoMineR', 'version': '2.9'}, {'type': 'r', 'name': 'flexclust', 'version': '1.4-1'}, {'type': 'r', 'name': 'flexmix', 'version': '2.3-19'}, {'type': 'r', 'name': 'prabclus', 'version': '2.3-3'}, {'type': 'r', 'name': 'diptest', 'version': '0.77-0'}, {'type': 'r', 'name': 'trimcluster', 'version': '0.1-5'}, {'type': 'r', 'name': 'fpc', 'version': '2.2-10'}, {'type': 'r', 'name': 'BiasedUrn', 'version': '2.0.11'}, {'type': 'r', 'name': 'TeachingDemos', 'version': '2.12'}, {'type': 'r', 'name': 'kohonen', 'version': '3.0.12'}, {'type': 'r', 'name': 'base64', 'version': '2.0.1'}, {'type': 'r', 'name': 'doRNG', 'version': '1.8.6'}, {'type': 'r', 'name': 'nleqslv', 'version': '3.3.5'}, {'type': 'r', 'name': 'Deriv', 'version': '4.1.3'}, {'type': 'r', 'name': 'RGCCA', 'version': '3.0.2'}, {'type': 'r', 'name': 'pheatmap', 'version': '1.0.12'}, {'type': 'r', 'name': 'pvclust', 'version': '2.2-0'}, {'type': 'r', 'name': 'RCircos', 'version': '1.2.2'}, {'type': 'r', 'name': 'lambda.r', 'version': '1.2.4'}, {'type': 'r', 'name': 'futile.options', 'version': '1.0.1'}, {'type': 'r', 'name': 'futile.logger', 'version': '1.4.3'}, {'type': 'r', 'name': 'VennDiagram', 'version': '1.7.3'}, {'type': 'r', 'name': 'xlsxjars', 'version': '0.6.1'}, {'type': 'r', 'name': 'xlsx', 'version': '0.6.5'}, {'type': 'r', 'name': 'uroot', 'version': '2.1-2'}, {'type': 'r', 'name': 'forecast', 'version': '8.21.1'}, {'type': 'r', 'name': 'fma', 'version': '2.5'}, {'type': 'r', 'name': 'expsmooth', 'version': '2.3'}, {'type': 'r', 'name': 'fpp', 'version': '0.5'}, {'type': 'r', 'name': 'tensor', 'version': '1.5'}, {'type': 'r', 'name': 'polyclip', 'version': '1.10-6'}, {'type': 'r', 'name': 'goftest', 'version': '1.2-3'}, {'type': 'r', 'name': 'spatstat.utils', 'version': '3.0-4'}, {'type': 'r', 'name': 'spatstat.data', 'version': '3.0-3'}, {'type': 'r', 'name': 'spatstat.geom', 'version': '3.2-7'}, {'type': 'r', 'name': 'spatstat.sparse', 'version': '3.0-3'}, {'type': 'r', 'name': 'spatstat.random', 'version': '3.2-2'}, {'type': 'r', 'name': 'spatstat.core', 'version': '2.4-4'}, {'type': 'r', 'name': 'spatstat.explore', 'version': '3.2-5'}, {'type': 'r', 'name': 'spatstat.model', 'version': '3.2-8'}, {'type': 'r', 'name': 'spatstat.linnet', 'version': '3.1-3'}, {'type': 'r', 'name': 'spatstat', 'version': '3.0-7'}, {'type': 'r', 'name': 'pracma', 'version': '2.4.4'}, {'type': 'r', 'name': 'RCurl', 'version': '1.98-1.13'}, {'type': 'r', 'name': 'bio3d', 'version': '2.4-4'}, {'type': 'r', 'name': 'AUC', 'version': '0.3.2'}, {'type': 'r', 'name': 'interpretR', 'version': '0.2.5'}, {'type': 'r', 'name': 'cvAUC', 'version': '1.1.4'}, {'type': 'r', 'name': 'SuperLearner', 'version': '2.0-28.1'}, {'type': 'r', 'name': 'mediation', 'version': '4.5.0'}, {'type': 'r', 'name': 'CVST', 'version': '0.2-3'}, {'type': 'r', 'name': 'DRR', 'version': '0.0.4'}, {'type': 'r', 'name': 'dimRed', 'version': '0.2.6'}, {'type': 'r', 'name': 'ddalpha', 'version': '1.3.13'}, {'type': 'r', 'name': 'RcppRoll', 'version': '0.3.0'}, {'type': 'r', 'name': 'rlist', 'version': '0.4.6.2'}, {'type': 'r', 'name': 'ConsRank', 'version': '2.1.3'}, {'type': 'r', 'name': 'adabag', 'version': '5.0'}, {'type': 'r', 'name': 'parallelMap', 'version': '1.5.1'}, {'type': 'r', 'name': 'ParamHelpers', 'version': '1.14.1'}, {'type': 'r', 'name': 'ggvis', 'version': '0.4.8'}, {'type': 'r', 'name': 'mlr', 'version': '2.19.1'}, {'type': 'r', 'name': 'unbalanced', 'version': '2.0'}, {'type': 'r', 'name': 'RSNNS', 'version': '0.4-17'}, {'type': 'r', 'name': 'abc.data', 'version': '1.0'}, {'type': 'r', 'name': 'abc', 'version': '2.2.1'}, {'type': 'r', 'name': 'lhs', 'version': '1.1.6'}, {'type': 'r', 'name': 'tensorA', 'version': '0.36.2'}, {'type': 'r', 'name': 'EasyABC', 'version': '1.5.2'}, {'type': 'r', 'name': 'git2r', 'version': '0.33.0'}, {'type': 'r', 'name': 'clisymbols', 'version': '1.2.0'}, {'type': 'r', 'name': 'covr', 'version': '3.6.4'}, {'type': 'r', 'name': 'Rook', 'version': '1.2'}, {'type': 'r', 'name': 'Cairo', 'version': '1.6-2'}, {'type': 'r', 'name': 'RMTstat', 'version': '0.3.1'}, {'type': 'r', 'name': 'Lmoments', 'version': '1.3-1'}, {'type': 'r', 'name': 'distillery', 'version': '1.2-1'}, {'type': 'r', 'name': 'extRemes', 'version': '2.1-3'}, {'type': 'r', 'name': 'tkrplot', 'version': '0.0-27'}, {'type': 'r', 'name': 'misc3d', 'version': '0.9-1'}, {'type': 'r', 'name': 'multicool', 'version': '1.0.0'}, {'type': 'r', 'name': 'plot3D', 'version': '1.4'}, {'type': 'r', 'name': 'plot3Drgl', 'version': '1.0.4'}, {'type': 'r', 'name': 'OceanView', 'version': '1.0.6'}, {'type': 'r', 'name': 'ks', 'version': '1.14.1'}, {'type': 'r', 'name': 'logcondens', 'version': '2.1.8'}, {'type': 'r', 'name': 'Iso', 'version': '0.0-21'}, {'type': 'r', 'name': 'penalized', 'version': '0.9-52'}, {'type': 'r', 'name': 'clusterRepro', 'version': '0.9'}, {'type': 'r', 'name': 'data.tree', 'version': '1.1.0'}, {'type': 'r', 'name': 'influenceR', 'version': '0.1.5'}, {'type': 'r', 'name': 'visNetwork', 'version': '2.1.2'}, {'type': 'r', 'name': 'downloader', 'version': '0.4'}, {'type': 'r', 'name': 'DiagrammeR', 'version': '1.0.10'}, {'type': 'r', 'name': 'randomForestSRC', 'version': '3.2.3'}, {'type': 'r', 'name': 'sm', 'version': '2.2-5.7.1'}, {'type': 'r', 'name': 'pbivnorm', 'version': '0.6.0'}, {'type': 'r', 'name': 'lavaan', 'version': '0.6-16'}, {'type': 'r', 'name': 'matrixcalc', 'version': '1.0-6'}, {'type': 'r', 'name': 'arm', 'version': '1.13-1'}, {'type': 'r', 'name': 'mi', 'version': '1.1'}, {'type': 'r', 'name': 'servr', 'version': '0.27'}, {'type': 'r', 'name': 'rgexf', 'version': '0.16.2'}, {'type': 'r', 'name': 'sem', 'version': '3.1-15'}, {'type': 'r', 'name': 'statnet.common', 'version': '4.9.0'}, {'type': 'r', 'name': 'network', 'version': '1.18.2'}, {'type': 'r', 'name': 'rle', 'version': '0.9.2'}, {'type': 'r', 'name': 'sna', 'version': '2.7-2'}, {'type': 'r', 'name': 'glasso', 'version': '1.11'}, {'type': 'r', 'name': 'huge', 'version': '1.3.5'}, {'type': 'r', 'name': 'd3Network', 'version': '0.5.2.1'}, {'type': 'r', 'name': 'BDgraph', 'version': '2.72'}, {'type': 'r', 'name': 'graphlayouts', 'version': '1.0.2'}, {'type': 'r', 'name': 'tweenr', 'version': '2.0.2'}, {'type': 'r', 'name': 'ggforce', 'version': '0.4.1'}, {'type': 'r', 'name': 'tidygraph', 'version': '1.2.3'}, {'type': 'r', 'name': 'ggraph', 'version': '2.1.0'}, {'type': 'r', 'name': 'qgraph', 'version': '1.9.8'}, {'type': 'r', 'name': 'HWxtest', 'version': '1.1.9'}, {'type': 'r', 'name': 'diveRsity', 'version': '1.9.90'}, {'type': 'r', 'name': 'doSNOW', 'version': '1.0.20'}, {'type': 'r', 'name': 'geepack', 'version': '1.3.9'}, {'type': 'r', 'name': 'biom', 'version': '0.3.12'}, {'type': 'r', 'name': 'pim', 'version': '2.0.2'}, {'type': 'r', 'name': 'minpack.lm', 'version': '1.2-4'}, {'type': 'r', 'name': 'rootSolve', 'version': '1.8.2.4'}, {'type': 'r', 'name': 'FME', 'version': '1.3.6.3'}, {'type': 'r', 'name': 'bmp', 'version': '0.3'}, {'type': 'r', 'name': 'tiff', 'version': '0.1-12'}, {'type': 'r', 'name': 'readbitmap', 'version': '0.1.5'}, {'type': 'r', 'name': 'imager', 'version': '0.45.2'}, {'type': 'r', 'name': 'signal', 'version': '1.8-0'}, {'type': 'r', 'name': 'tuneR', 'version': '1.4.6'}, {'type': 'r', 'name': 'pastecs', 'version': '1.3.21'}, {'type': 'r', 'name': 'audio', 'version': '0.1-11'}, {'type': 'r', 'name': 'fftw', 'version': '1.0-7'}, {'type': 'r', 'name': 'seewave', 'version': '2.2.3'}, {'type': 'r', 'name': 'gsw', 'version': '1.1-1'}, {'type': 'r', 'name': 'wk', 'version': '0.9.1'}, {'type': 'r', 'name': 's2', 'version': '1.1.4'}, {'type': 'r', 'name': 'sf', 'version': '1.0-14'}, {'type': 'r', 'name': 'oce', 'version': '1.8-2'}, {'type': 'r', 'name': 'ineq', 'version': '0.2-13'}, {'type': 'r', 'name': 'soundecology', 'version': '1.3.3'}, {'type': 'r', 'name': 'memuse', 'version': '4.2-3'}, {'type': 'r', 'name': 'pinfsc50', 'version': '1.3.0'}, {'type': 'r', 'name': 'vcfR', 'version': '1.15.0'}, {'type': 'r', 'name': 'glmmML', 'version': '1.1.6'}, {'type': 'r', 'name': 'cowplot', 'version': '1.1.1'}, {'type': 'r', 'name': 'tsne', 'version': '0.1-3.1'}, {'type': 'r', 'name': 'sn', 'version': '2.1.1'}, {'type': 'r', 'name': 'tclust', 'version': '1.5-5'}, {'type': 'r', 'name': 'ranger', 'version': '0.16.0'}, {'type': 'r', 'name': 'hexbin', 'version': '1.28.3'}, {'type': 'r', 'name': 'lobstr', 'version': '1.1.2'}, {'type': 'r', 'name': 'pryr', 'version': '0.1.6'}, {'type': 'r', 'name': 'moments', 'version': '0.14.1'}, {'type': 'r', 'name': 'laeken', 'version': '0.5.2'}, {'type': 'r', 'name': 'VIM', 'version': '6.2.2'}, {'type': 'r', 'name': 'smoother', 'version': '1.1'}, {'type': 'r', 'name': 'dynamicTreeCut', 'version': '1.63-1'}, {'type': 'r', 'name': 'beeswarm', 'version': '0.4.0'}, {'type': 'r', 'name': 'vipor', 'version': '0.4.5'}, {'type': 'r', 'name': 'ggbeeswarm', 'version': '0.7.2'}, {'type': 'r', 'name': 'shinydashboard', 'version': '0.7.2'}, {'type': 'r', 'name': 'rrcov', 'version': '1.7-4'}, {'type': 'r', 'name': 'WriteXLS', 'version': '6.4.0'}, {'type': 'r', 'name': 'bst', 'version': '0.3-24'}, {'type': 'r', 'name': 'pamr', 'version': '1.56.1'}, {'type': 'r', 'name': 'WeightSVM', 'version': '1.7-13'}, {'type': 'r', 'name': 'mpath', 'version': '0.4-2.23'}, {'type': 'r', 'name': 'timereg', 'version': '2.0.5'}, {'type': 'r', 'name': 'peperr', 'version': '1.5'}, {'type': 'r', 'name': 'heatmap3', 'version': '1.1.9'}, {'type': 'r', 'name': 'GlobalOptions', 'version': '0.1.2'}, {'type': 'r', 'name': 'circlize', 'version': '0.4.15'}, {'type': 'r', 'name': 'GetoptLong', 'version': '1.0.5'}, {'type': 'r', 'name': 'dendextend', 'version': '1.17.1'}, {'type': 'r', 'name': 'RInside', 'version': '0.2.18'}, {'type': 'r', 'name': 'limSolve', 'version': '1.5.7'}, {'type': 'r', 'name': 'dbplyr', 'version': '2.4.0'}, {'type': 'r', 'name': 'modelr', 'version': '0.1.11'}, {'type': 'r', 'name': 'debugme', 'version': '1.1.0'}, {'type': 'r', 'name': 'reprex', 'version': '2.0.2'}, {'type': 'r', 'name': 'selectr', 'version': '0.4-2'}, {'type': 'r', 'name': 'rvest', 'version': '1.0.3'}, {'type': 'r', 'name': 'dtplyr', 'version': '1.3.1'}, {'type': 'r', 'name': 'gargle', 'version': '1.5.2'}, {'type': 'r', 'name': 'googledrive', 'version': '2.1.1'}, {'type': 'r', 'name': 'ids', 'version': '1.0.1'}, {'type': 'r', 'name': 'googlesheets4', 'version': '1.1.1'}, {'type': 'r', 'name': 'conflicted', 'version': '1.2.0'}, {'type': 'r', 'name': 'tidyverse', 'version': '2.0.0'}, {'type': 'r', 'name': 'R.rsp', 'version': '0.45.0'}, {'type': 'r', 'name': 'gdistance', 'version': '1.6.4'}, {'type': 'r', 'name': 'vioplot', 'version': '0.4.0'}, {'type': 'r', 'name': 'emulator', 'version': '1.2-21'}, {'type': 'r', 'name': 'gmm', 'version': '1.8'}, {'type': 'r', 'name': 'tmvtnorm', 'version': '1.6'}, {'type': 'r', 'name': 'IDPmisc', 'version': '1.1.20'}, {'type': 'r', 'name': 'gap.datasets', 'version': '0.0.6'}, {'type': 'r', 'name': 'gap', 'version': '1.5-3'}, {'type': 'r', 'name': 'qrnn', 'version': '2.1'}, {'type': 'r', 'name': 'TMB', 'version': '1.9.9'}, {'type': 'r', 'name': 'glmmTMB', 'version': '1.1.8'}, {'type': 'r', 'name': 'gmp', 'version': '0.7-3'}, {'type': 'r', 'name': 'ROI', 'version': '1.0-1'}, {'type': 'r', 'name': 'Rglpk', 'version': '0.6-5'}, {'type': 'r', 'name': 'ROI.plugin.glpk', 'version': '1.0-0'}, {'type': 'r', 'name': 'spaMM', 'version': '4.4.0'}, {'type': 'r', 'name': 'qgam', 'version': '1.3.4'}, {'type': 'r', 'name': 'DHARMa', 'version': '0.4.6'}, {'type': 'r', 'name': 'mvnfast', 'version': '0.2.8'}, {'type': 'r', 'name': 'bridgesampling', 'version': '1.1-2'}, {'type': 'r', 'name': 'BayesianTools', 'version': '0.1.8'}, {'type': 'r', 'name': 'gomms', 'version': '1.0'}, {'type': 'r', 'name': 'feather', 'version': '0.3.5'}, {'type': 'r', 'name': 'dummies', 'version': '1.5.6'}, {'type': 'r', 'name': 'SimSeq', 'version': '1.4.0'}, {'type': 'r', 'name': 'uniqueAtomMat', 'version': '0.1-3-2'}, {'type': 'r', 'name': 'PoissonSeq', 'version': '1.1.2'}, {'type': 'r', 'name': 'aod', 'version': '1.3.2'}, {'type': 'r', 'name': 'cghFLasso', 'version': '0.2-1'}, {'type': 'r', 'name': 'svd', 'version': '0.5.5'}, {'type': 'r', 'name': 'Rssa', 'version': '1.0.5'}, {'type': 'r', 'name': 'JBTools', 'version': '0.7.2.9'}, {'type': 'r', 'name': 'RUnit', 'version': '0.4.32'}, {'type': 'r', 'name': 'DistributionUtils', 'version': '0.6-1'}, {'type': 'r', 'name': 'gapfill', 'version': '0.9.6-1'}, {'type': 'r', 'name': 'gee', 'version': '4.13-26'}, {'type': 'r', 'name': 'Matching', 'version': '4.10-14'}, {'type': 'r', 'name': 'chk', 'version': '0.9.1'}, {'type': 'r', 'name': 'MatchIt', 'version': '4.5.5'}, {'type': 'r', 'name': 'RItools', 'version': '0.3-3'}, {'type': 'r', 'name': 'mitools', 'version': '2.4'}, {'type': 'r', 'name': 'survey', 'version': '4.2-1'}, {'type': 'r', 'name': 'rlemon', 'version': '0.2.1'}, {'type': 'r', 'name': 'optmatch', 'version': '0.10.7'}, {'type': 'r', 'name': 'SPAtest', 'version': '3.1.2'}, {'type': 'r', 'name': 'RSpectra', 'version': '0.16-1'}, {'type': 'r', 'name': 'SKAT', 'version': '2.2.5'}, {'type': 'r', 'name': 'GillespieSSA', 'version': '0.6.2'}, {'type': 'r', 'name': 'startupmsg', 'version': '0.9.6'}, {'type': 'r', 'name': 'distr', 'version': '2.9.2'}, {'type': 'r', 'name': 'distrEx', 'version': '2.9.0'}, {'type': 'r', 'name': 'minerva', 'version': '1.5.10'}, {'type': 'r', 'name': 'RcppTOML', 'version': '0.2.2'}, {'type': 'r', 'name': 'here', 'version': '1.0.1'}, {'type': 'r', 'name': 'reticulate', 'version': '1.34.0'}, {'type': 'r', 'name': 'umap', 'version': '0.2.10.0'}, {'type': 'r', 'name': 'KODAMA', 'version': '2.4'}, {'type': 'r', 'name': 'locfdr', 'version': '1.1-8'}, {'type': 'r', 'name': 'ica', 'version': '1.0-3'}, {'type': 'r', 'name': 'dtw', 'version': '1.23-1'}, {'type': 'r', 'name': 'SDMTools', 'version': '1.1-221.2'}, {'type': 'r', 'name': 'ggridges', 'version': '0.5.4'}, {'type': 'r', 'name': 'TFisher', 'version': '0.2.0'}, {'type': 'r', 'name': 'lsei', 'version': '1.3-0'}, {'type': 'r', 'name': 'npsurv', 'version': '0.5-0'}, {'type': 'r', 'name': 'fitdistrplus', 'version': '1.1-11'}, {'type': 'r', 'name': 'hdf5r', 'version': '1.3.8'}, {'type': 'r', 'name': 'DTRreg', 'version': '2.0'}, {'type': 'r', 'name': 'pulsar', 'version': '0.3.11'}, {'type': 'r', 'name': 'bayesm', 'version': '3.1-6'}, {'type': 'r', 'name': 'gsl', 'version': '2.1-8'}, {'type': 'r', 'name': 'energy', 'version': '1.7-11'}, {'type': 'r', 'name': 'compositions', 'version': '2.0-6'}, {'type': 'r', 'name': 'clustree', 'version': '0.5.1'}, {'type': 'r', 'name': 'tweedie', 'version': '2.3.5'}, {'type': 'r', 'name': 'RcppGSL', 'version': '0.3.13'}, {'type': 'r', 'name': 'mvabund', 'version': '4.2.1'}, {'type': 'r', 'name': 'fishMod', 'version': '0.29'}, {'type': 'r', 'name': 'alabama', 'version': '2023.1.0'}, {'type': 'r', 'name': 'gllvm', 'version': '1.4.3'}, {'type': 'r', 'name': 'grpreg', 'version': '3.4.0'}, {'type': 'r', 'name': 'trust', 'version': '0.1-8'}, {'type': 'r', 'name': 'lpSolveAPI', 'version': '5.5.2.0-17.11'}, {'type': 'r', 'name': 'ergm', 'version': '4.5.0'}, {'type': 'r', 'name': 'networkLite', 'version': '1.0.5'}, {'type': 'r', 'name': 'networkDynamic', 'version': '0.11.3'}, {'type': 'r', 'name': 'ergm.multi', 'version': '0.2.0'}, {'type': 'r', 'name': 'tergm', 'version': '4.2.0'}, {'type': 'r', 'name': 'ergm.count', 'version': '4.1.1'}, {'type': 'r', 'name': 'tsna', 'version': '0.3.5'}, {'type': 'r', 'name': 'statnet', 'version': '2019.6'}, {'type': 'r', 'name': 'aggregation', 'version': '1.0.1'}, {'type': 'r', 'name': 'ComICS', 'version': '1.0.4'}, {'type': 'r', 'name': 'dtangle', 'version': '2.0.9'}, {'type': 'r', 'name': 'mcmc', 'version': '0.9-8'}, {'type': 'r', 'name': 'MCMCpack', 'version': '1.6-3'}, {'type': 'r', 'name': 'shinythemes', 'version': '1.2.0'}, {'type': 'r', 'name': 'csSAM', 'version': '1.2.4'}, {'type': 'r', 'name': 'bridgedist', 'version': '0.1.2'}, {'type': 'r', 'name': 'asnipe', 'version': '1.1.17'}, {'type': 'r', 'name': 'liquidSVM', 'version': '1.2.4'}, {'type': 'r', 'name': 'oddsratio', 'version': '2.0.1'}, {'type': 'r', 'name': 'mltools', 'version': '0.3.5'}, {'type': 'r', 'name': 'h2o', 'version': '3.42.0.2'}, {'type': 'r', 'name': 'mlegp', 'version': '3.1.9'}, {'type': 'r', 'name': 'itertools', 'version': '0.1-3'}, {'type': 'r', 'name': 'missForest', 'version': '1.5'}, {'type': 'r', 'name': 'bartMachineJARs', 'version': '1.2.1'}, {'type': 'r', 'name': 'bartMachine', 'version': '1.3.4.1'}, {'type': 'r', 'name': 'lqa', 'version': '1.0-3'}, {'type': 'r', 'name': 'PresenceAbsence', 'version': '1.1.11'}, {'type': 'r', 'name': 'GUTS', 'version': '1.2.5'}, {'type': 'r', 'name': 'GenSA', 'version': '1.1.10.1'}, {'type': 'r', 'name': 'parsedate', 'version': '1.3.1'}, {'type': 'r', 'name': 'circular', 'version': '0.5-0'}, {'type': 'r', 'name': 'cobs', 'version': '1.3-5'}, {'type': 'r', 'name': 'resample', 'version': '0.6'}, {'type': 'r', 'name': 'MIIVsem', 'version': '0.5.8'}, {'type': 'r', 'name': 'medflex', 'version': '0.6-10'}, {'type': 'r', 'name': 'Rserve', 'version': '1.8-13'}, {'type': 'r', 'name': 'spls', 'version': '2.2-3'}, {'type': 'r', 'name': 'Boruta', 'version': '8.0.0'}, {'type': 'r', 'name': 'dr', 'version': '3.0.10'}, {'type': 'r', 'name': 'CovSel', 'version': '1.2.1'}, {'type': 'r', 'name': 'tmle', 'version': '2.0.0'}, {'type': 'r', 'name': 'ctmle', 'version': '0.1.2'}, {'type': 'r', 'name': 'BayesPen', 'version': '1.0'}, {'type': 'r', 'name': 'inline', 'version': '0.3.19'}, {'type': 'r', 'name': 'BMA', 'version': '3.18.17'}, {'type': 'r', 'name': 'BCEE', 'version': '1.3.2'}, {'type': 'r', 'name': 'bacr', 'version': '1.0.1'}, {'type': 'r', 'name': 'clue', 'version': '0.3-65'}, {'type': 'r', 'name': 'bdsmatrix', 'version': '1.3-6'}, {'type': 'r', 'name': 'fftwtools', 'version': '0.9-11'}, {'type': 'r', 'name': 'imagerExtra', 'version': '1.3.2'}, {'type': 'r', 'name': 'MALDIquant', 'version': '1.22.1'}, {'type': 'r', 'name': 'threejs', 'version': '0.3.3'}, {'type': 'r', 'name': 'LaplacesDemon', 'version': '16.1.6'}, {'type': 'r', 'name': 'rda', 'version': '1.2-1'}, {'type': 'r', 'name': 'sampling', 'version': '2.10'}, {'type': 'r', 'name': 'lda', 'version': '1.4.2'}, {'type': 'r', 'name': 'jiebaRD', 'version': '0.1'}, {'type': 'r', 'name': 'jiebaR', 'version': '0.11'}, {'type': 'r', 'name': 'hdm', 'version': '0.3.1'}, {'type': 'r', 'name': 'abe', 'version': '3.0.1'}, {'type': 'r', 'name': 'SignifReg', 'version': '4.3'}, {'type': 'r', 'name': 'bbmle', 'version': '1.0.25.1'}, {'type': 'r', 'name': 'emdbook', 'version': '1.3.13'}, {'type': 'r', 'name': 'SOAR', 'version': '0.99-11'}, {'type': 'r', 'name': 'rasterVis', 'version': '0.51.6'}, {'type': 'r', 'name': 'tictoc', 'version': '1.2'}, {'type': 'r', 'name': 'ISOcodes', 'version': '2023.12.07'}, {'type': 'r', 'name': 'stopwords', 'version': '2.3'}, {'type': 'r', 'name': 'janeaustenr', 'version': '1.0.0'}, {'type': 'r', 'name': 'SnowballC', 'version': '0.7.1'}, {'type': 'r', 'name': 'tokenizers', 'version': '0.3.0'}, {'type': 'r', 'name': 'hunspell', 'version': '3.0.3'}, {'type': 'r', 'name': 'topicmodels', 'version': '0.2-15'}, {'type': 'r', 'name': 'tidytext', 'version': '0.4.1'}, {'type': 'r', 'name': 'splitstackshape', 'version': '1.4.8'}, {'type': 'r', 'name': 'grImport2', 'version': '0.3-1'}, {'type': 'r', 'name': 'preseqR', 'version': '4.0.0'}, {'type': 'r', 'name': 'idr', 'version': '1.3'}, {'type': 'r', 'name': 'entropy', 'version': '1.3.1'}, {'type': 'r', 'name': 'kedd', 'version': '1.0.3'}, {'type': 'r', 'name': 'HiddenMarkov', 'version': '1.8-13'}, {'type': 'r', 'name': 'lmerTest', 'version': '3.1-3'}, {'type': 'r', 'name': 'loo', 'version': '2.6.0'}, {'type': 'r', 'name': 'RcppParallel', 'version': '5.1.7'}, {'type': 'r', 'name': 'StanHeaders', 'version': '2.26.28'}, {'type': 'r', 'name': 'V8', 'version': '4.4.1'}, {'type': 'r', 'name': 'QuickJSR', 'version': '1.0.8'}, {'type': 'r', 'name': 'rstan', 'version': '2.32.3'}, {'type': 'r', 'name': 'Rborist', 'version': '0.3-5'}, {'type': 'r', 'name': 'VSURF', 'version': '1.2.0'}, {'type': 'r', 'name': 'mRMRe', 'version': '2.1.2.1'}, {'type': 'r', 'name': 'dHSIC', 'version': '2.1'}, {'type': 'r', 'name': 'ggsci', 'version': '3.0.0'}, {'type': 'r', 'name': 'ggsignif', 'version': '0.6.4'}, {'type': 'r', 'name': 'corrplot', 'version': '0.92'}, {'type': 'r', 'name': 'rstatix', 'version': '0.7.2'}, {'type': 'r', 'name': 'ggfan', 'version': '0.1.3'}, {'type': 'r', 'name': 'ggpubr', 'version': '0.6.0'}, {'type': 'r', 'name': 'yaImpute', 'version': '1.0-33'}, {'type': 'r', 'name': 'intrinsicDimension', 'version': '1.2.0'}, {'type': 'r', 'name': 'leiden', 'version': '0.4.3.1'}, {'type': 'r', 'name': 'sctransform', 'version': '0.4.1'}, {'type': 'r', 'name': 'packrat', 'version': '0.9.2'}, {'type': 'r', 'name': 'colourpicker', 'version': '1.3.0'}, {'type': 'r', 'name': 'ggExtra', 'version': '0.10.1'}, {'type': 'r', 'name': 'findpython', 'version': '1.0.8'}, {'type': 'r', 'name': 'argparse', 'version': '2.2.2'}, {'type': 'r', 'name': 'intergraph', 'version': '2.0-3'}, {'type': 'r', 'name': 'ggnetwork', 'version': '0.5.12'}, {'type': 'r', 'name': 'qqman', 'version': '0.1.9'}, {'type': 'r', 'name': 'rstantools', 'version': '2.3.1.1'}, {'type': 'r', 'name': 'distributional', 'version': '0.3.2'}, {'type': 'r', 'name': 'posterior', 'version': '1.5.0'}, {'type': 'r', 'name': 'bayesplot', 'version': '1.10.0'}, {'type': 'r', 'name': 'dygraphs', 'version': '1.1.1.6'}, {'type': 'r', 'name': 'renv', 'version': '1.0.3'}, {'type': 'r', 'name': 'rsconnect', 'version': '1.1.1'}, {'type': 'r', 'name': 'shinystan', 'version': '2.6.0'}, {'type': 'r', 'name': 'optimx', 'version': '2023-10.21'}, {'type': 'r', 'name': 'gamm4', 'version': '0.2-6'}, {'type': 'r', 'name': 'memisc', 'version': '0.99.31.6'}, {'type': 'r', 'name': 'mclogit', 'version': '0.9.6'}, {'type': 'r', 'name': 'projpred', 'version': '2.7.0'}, {'type': 'r', 'name': 'brms', 'version': '2.20.4'}, {'type': 'r', 'name': 'drgee', 'version': '1.1.10'}, {'type': 'r', 'name': 'stdReg', 'version': '3.4.1'}, {'type': 'r', 'name': 'mcmcse', 'version': '1.5-0'}, {'type': 'r', 'name': 'copCAR', 'version': '2.0-4'}, {'type': 'r', 'name': 'batchmeans', 'version': '1.0-4'}, {'type': 'r', 'name': 'ngspatial', 'version': '1.2-2'}, {'type': 'r', 'name': 'BIGL', 'version': '1.8.0'}, {'type': 'r', 'name': 'drugCombo', 'version': '1.2.1'}, {'type': 'r', 'name': 'betareg', 'version': '3.1-4'}, {'type': 'r', 'name': 'unmarked', 'version': '1.3.2'}, {'type': 'r', 'name': 'maxlike', 'version': '0.1-10'}, {'type': 'r', 'name': 'coxme', 'version': '2.2-18.1'}, {'type': 'r', 'name': 'AICcmodavg', 'version': '2.3-3'}, {'type': 'r', 'name': 'pacman', 'version': '0.5.1'}, {'type': 'r', 'name': 'spaa', 'version': '0.2.2'}, {'type': 'r', 'name': 'maxnet', 'version': '0.1.4'}, {'type': 'r', 'name': 'oai', 'version': '0.4.0'}, {'type': 'r', 'name': 'wellknown', 'version': '0.7.4'}, {'type': 'r', 'name': 'rgbif', 'version': '3.7.8'}, {'type': 'r', 'name': 'rgdal', 'version': '1.6-7'}, {'type': 'r', 'name': 'rgeos', 'version': '0.6-4'}, {'type': 'r', 'name': 'mapproj', 'version': '1.2.11'}, {'type': 'r', 'name': 'rbison', 'version': '1.0.0'}, {'type': 'r', 'name': 'rebird', 'version': '1.3.0'}, {'type': 'r', 'name': 'rvertnet', 'version': '0.8.2'}, {'type': 'r', 'name': 'ridigbio', 'version': '0.3.7'}, {'type': 'r', 'name': 'spocc', 'version': '1.2.2'}, {'type': 'r', 'name': 'spThin', 'version': '0.2.0'}, {'type': 'r', 'name': 'RPostgreSQL', 'version': '0.7-5'}, {'type': 'r', 'name': 'fasterize', 'version': '1.0.5'}, {'type': 'r', 'name': 'BIEN', 'version': '1.2.6'}, {'type': 'r', 'name': 'rangeModelMetadata', 'version': '0.1.5'}, {'type': 'r', 'name': 'ENMeval', 'version': '2.0.4'}, {'type': 'r', 'name': 'plotmo', 'version': '3.6.2'}, {'type': 'r', 'name': 'earth', 'version': '5.3.2'}, {'type': 'r', 'name': 'mda', 'version': '0.5-4'}, {'type': 'r', 'name': 'xgboost', 'version': '1.7.6.1'}, {'type': 'r', 'name': 'biomod2', 'version': '4.2-4'}, {'type': 'r', 'name': 'poLCA', 'version': '1.6.0.1'}, {'type': 'r', 'name': 'PermAlgo', 'version': '1.2'}, {'type': 'r', 'name': 'coxed', 'version': '0.3.3'}, {'type': 'r', 'name': 'testit', 'version': '0.13'}, {'type': 'r', 'name': 'NISTunits', 'version': '1.0.1'}, {'type': 'r', 'name': 'celestial', 'version': '1.4.6'}, {'type': 'r', 'name': 'RPMM', 'version': '1.25'}, {'type': 'r', 'name': 'RefFreeEWAS', 'version': '2.2'}, {'type': 'r', 'name': 'wordcloud', 'version': '2.6'}, {'type': 'r', 'name': 'JADE', 'version': '2.0-4'}, {'type': 'r', 'name': 'awsMethods', 'version': '1.1-1'}, {'type': 'r', 'name': 'aws', 'version': '2.5-3'}, {'type': 'r', 'name': 'ruv', 'version': '0.9.7.1'}, {'type': 'r', 'name': 'mhsmm', 'version': '0.4.21'}, {'type': 'r', 'name': 'dbarts', 'version': '0.9-25'}, {'type': 'r', 'name': 'proftools', 'version': '0.99-3'}, {'type': 'r', 'name': 'NCmisc', 'version': '1.2.0'}, {'type': 'r', 'name': 'reader', 'version': '1.0.6'}, {'type': 'r', 'name': 'gnumeric', 'version': '0.7-10'}, {'type': 'r', 'name': 'tcltk2', 'version': '1.2-11'}, {'type': 'r', 'name': 'readODS', 'version': '2.1.0'}, {'type': 'r', 'name': 'nortest', 'version': '1.0-4'}, {'type': 'r', 'name': 'EnvStats', 'version': '2.8.1'}, {'type': 'r', 'name': 'outliers', 'version': '0.15'}, {'type': 'r', 'name': 'gWidgets2', 'version': '1.0-9'}, {'type': 'r', 'name': 'gWidgets2tcltk', 'version': '1.0-8'}, {'type': 'r', 'name': 'mgsub', 'version': '1.7.3'}, {'type': 'r', 'name': 'ie2misc', 'version': '0.9.1'}, {'type': 'r', 'name': 'assertive.base', 'version': '0.0-9'}, {'type': 'r', 'name': 'assertive.properties', 'version': '0.0-5'}, {'type': 'r', 'name': 'assertive.types', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.numbers', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.strings', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.datetimes', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.files', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.sets', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.matrices', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.models', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.data', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.data.uk', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.data.us', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.reflection', 'version': '0.0-5'}, {'type': 'r', 'name': 'assertive.code', 'version': '0.0-4'}, {'type': 'r', 'name': 'assertive', 'version': '0.3-6'}, {'type': 'r', 'name': 'rdrop2', 'version': '0.8.2.1'}, {'type': 'r', 'name': 'Exact', 'version': '3.2'}, {'type': 'r', 'name': 'lmom', 'version': '3.0'}, {'type': 'r', 'name': 'gld', 'version': '2.6.6'}, {'type': 'r', 'name': 'DescTools', 'version': '0.99.52'}, {'type': 'r', 'name': 'orthopolynom', 'version': '1.0-6.1'}, {'type': 'r', 'name': 'gaussquad', 'version': '1.0-3'}, {'type': 'r', 'name': 'nlsem', 'version': '0.8-1'}, {'type': 'r', 'name': 'tableone', 'version': '0.13.2'}, {'type': 'r', 'name': 'jstable', 'version': '1.1.3'}, {'type': 'r', 'name': 'RCAL', 'version': '2.0'}, {'type': 'r', 'name': 'stargazer', 'version': '5.2.3'}, {'type': 'r', 'name': 'sensemakr', 'version': '0.1.4'}, {'type': 'r', 'name': 'CompQuadForm', 'version': '1.4.3'}, {'type': 'r', 'name': 'nonnest2', 'version': '0.5-6'}, {'type': 'r', 'name': 'blavaan', 'version': '0.5-2'}, {'type': 'r', 'name': 'mathjaxr', 'version': '1.6-0'}, {'type': 'r', 'name': 'metadat', 'version': '1.2-0'}, {'type': 'r', 'name': 'metafor', 'version': '4.4-0'}, {'type': 'r', 'name': 'RNifti', 'version': '1.5.1'}, {'type': 'r', 'name': 'oro.nifti', 'version': '0.11.4'}, {'type': 'r', 'name': 'fmri', 'version': '1.9.12'}, {'type': 'r', 'name': 'linkcomm', 'version': '1.0-14'}, {'type': 'r', 'name': 'rnetcarto', 'version': '0.2.6'}, {'type': 'r', 'name': 'DEoptim', 'version': '2.2-8'}, {'type': 'r', 'name': 'optextras', 'version': '2019-12.4'}, {'type': 'r', 'name': 'setRNG', 'version': '2022.4-1'}, {'type': 'r', 'name': 'Rvmmin', 'version': '2018-4.17.1'}, {'type': 'r', 'name': 'Rcgmin', 'version': '2022-4.30'}, {'type': 'r', 'name': 'optimr', 'version': '2019-12.16'}, {'type': 'r', 'name': 'DMCfun', 'version': '2.0.2'}, {'type': 'r', 'name': 'miceadds', 'version': '3.16-18'}, {'type': 'r', 'name': 'visdat', 'version': '0.6.0'}, {'type': 'r', 'name': 'UpSetR', 'version': '1.4.0'}, {'type': 'r', 'name': 'norm', 'version': '1.0-11.1'}, {'type': 'r', 'name': 'naniar', 'version': '1.0.0'}, {'type': 'r', 'name': 'stringdist', 'version': '0.9.12'}, {'type': 'r', 'name': 'image.binarization', 'version': '0.1.3'}, {'type': 'r', 'name': 'lassosum', 'version': '0.4.5'}, {'type': 'r', 'name': 'lslx', 'version': '0.6.11'}, {'type': 'r', 'name': 'truncnorm', 'version': '1.0-9'}, {'type': 'r', 'name': 'Rsolnp', 'version': '1.16'}, {'type': 'r', 'name': 'regsem', 'version': '1.9.5'}, {'type': 'r', 'name': 'semPLS', 'version': '1.0-10'}, {'type': 'r', 'name': 'GxEScanR', 'version': '2.0.2'}, {'type': 'r', 'name': 'admisc', 'version': '0.34'}, {'type': 'r', 'name': 'polycor', 'version': '0.8-1'}, {'type': 'r', 'name': 'multipol', 'version': '1.0-9'}, {'type': 'r', 'name': 'symmoments', 'version': '1.2.1'}, {'type': 'r', 'name': 'rngWELL', 'version': '0.10-9'}, {'type': 'r', 'name': 'randtoolbox', 'version': '2.0.4'}, {'type': 'r', 'name': 'TruncatedNormal', 'version': '2.2.2'}, {'type': 'r', 'name': 'cSEM', 'version': '0.5.0'}, {'type': 'r', 'name': 'cubelyr', 'version': '1.0.2'}, {'type': 'r', 'name': 'furrr', 'version': '0.3.1'}, {'type': 'r', 'name': 'broom.mixed', 'version': '0.2.9.4'}, {'type': 'r', 'name': 'DiceKriging', 'version': '1.6.0'}, {'type': 'r', 'name': 'grf', 'version': '2.3.1'}, {'type': 'r', 'name': 'twang', 'version': '2.6'}, {'type': 'r', 'name': 'neuralnet', 'version': '1.44.2'}, {'type': 'r', 'name': 'PCAmatchR', 'version': '0.3.3'}, {'type': 'r', 'name': 'origami', 'version': '1.0.7'}, {'type': 'r', 'name': 'hal9001', 'version': '0.4.6'}, {'type': 'r', 'name': 'cobalt', 'version': '4.5.2'}, {'type': 'r', 'name': 'CBPS', 'version': '0.23'}, {'type': 'r', 'name': 'SBdecomp', 'version': '1.2'}, {'type': 'r', 'name': 'naturalsort', 'version': '0.1.3'}, {'type': 'r', 'name': 'lwgeom', 'version': '0.2-13'}, {'type': 'r', 'name': 'finalfit', 'version': '1.0.7'}, {'type': 'r', 'name': 'bigD', 'version': '0.2.0'}, {'type': 'r', 'name': 'juicyjuice', 'version': '0.1.0'}, {'type': 'r', 'name': 'reactR', 'version': '0.5.0'}, {'type': 'r', 'name': 'reactable', 'version': '0.4.4'}, {'type': 'r', 'name': 'gt', 'version': '0.10.0'}, {'type': 'r', 'name': 'gtsummary', 'version': '1.7.2'}, {'type': 'r', 'name': 'ncdf4', 'version': '1.22'}, {'type': 'r', 'name': 'geex', 'version': '1.1.1'}, {'type': 'r', 'name': 'momentfit', 'version': '0.5'}, {'type': 'r', 'name': 'StatMatch', 'version': '1.4.1'}, {'type': 'r', 'name': 'stars', 'version': '0.6-4'}, {'type': 'r', 'name': 'rapidjsonr', 'version': '1.2.0'}, {'type': 'r', 'name': 'jsonify', 'version': '1.2.2'}, {'type': 'r', 'name': 'geometries', 'version': '0.2.3'}, {'type': 'r', 'name': 'sfheaders', 'version': '0.4.3'}, {'type': 'r', 'name': 'geojsonsf', 'version': '2.0.3'}, {'type': 'r', 'name': 'leaflet.providers', 'version': '2.0.0'}, {'type': 'r', 'name': 'leaflet', 'version': '2.2.1'}, {'type': 'r', 'name': 'leafsync', 'version': '0.1.0'}, {'type': 'r', 'name': 'leafem', 'version': '0.2.3'}, {'type': 'r', 'name': 'widgetframe', 'version': '0.3.1'}, {'type': 'r', 'name': 'tmaptools', 'version': '3.1-1'}, {'type': 'r', 'name': 'tmap', 'version': '3.3-4'}, {'type': 'r', 'name': 'collapse', 'version': '2.0.7'}, {'type': 'r', 'name': 'genoPlotR', 'version': '0.8.11'}, {'type': 'r', 'name': 'VineCopula', 'version': '2.5.0'}, {'type': 'r', 'name': 'Rmpfr', 'version': '0.9-4'}, {'type': 'r', 'name': 'scam', 'version': '1.2-14'}, {'type': 'r', 'name': 'copula', 'version': '1.1-3'}, {'type': 'r', 'name': 'evd', 'version': '2.3-6.1'}, {'type': 'r', 'name': 'ismev', 'version': '1.42'}, {'type': 'r', 'name': 'GJRM', 'version': '0.2-6.4'}, {'type': 'r', 'name': 'penfa', 'version': '0.1.1'}, {'type': 'r', 'name': 'kde1d', 'version': '1.0.5'}, {'type': 'r', 'name': 'RcppThread', 'version': '2.1.6'}, {'type': 'r', 'name': 'wdm', 'version': '0.2.4'}, {'type': 'r', 'name': 'rvinecopulib', 'version': '0.6.3.1.1'}, {'type': 'r', 'name': 'PearsonDS', 'version': '1.3.0'}, {'type': 'r', 'name': 'covsim', 'version': '1.0.0'}, {'type': 'r', 'name': 'semTools', 'version': '0.5-6'}, {'type': 'r', 'name': 'GPArotation', 'version': '2023.11-1'}, {'type': 'r', 'name': 'dcurver', 'version': '0.9.2'}, {'type': 'r', 'name': 'mirt', 'version': '1.41'}, {'type': 'r', 'name': 'rpf', 'version': '1.0.14'}, {'type': 'r', 'name': 'OpenMx', 'version': '2.21.11'}, {'type': 'r', 'name': 'matlab', 'version': '1.0.4'}, {'type': 'r', 'name': 'FactorCopula', 'version': '0.9.3'}, {'type': 'r', 'name': 'rpact', 'version': '3.4.0'}, {'type': 'r', 'name': 'ldbounds', 'version': '2.0.2'}, {'type': 'r', 'name': 'catlearn', 'version': '1.0'}, {'type': 'r', 'name': 'MetaUtility', 'version': '2.1.2'}, {'type': 'r', 'name': 'EValue', 'version': '4.1.3'}, {'type': 'r', 'name': 'dagitty', 'version': '0.3-4'}, {'type': 'r', 'name': 'ggdag', 'version': '0.2.10'}, {'type': 'r', 'name': 'simex', 'version': '1.8'}, {'type': 'r', 'name': 'hash', 'version': '2.2.6.3'}, {'type': 'r', 'name': 'nabor', 'version': '0.5.0'}, {'type': 'r', 'name': 'RhpcBLASctl', 'version': '0.23-42'}, {'type': 'r', 'name': 'harmony', 'version': '1.2.0'}, {'type': 'r', 'name': 'apcluster', 'version': '1.4.11'}, {'type': 'r', 'name': 'DataCombine', 'version': '0.2.21'}, {'type': 'r', 'name': 'docstring', 'version': '1.0.0'}, {'type': 'r', 'name': 'gdalUtils', 'version': '2.0.3.2'}, {'type': 'r', 'name': 'openair', 'version': '2.18-0'}, {'type': 'r', 'name': 'pdp', 'version': '0.8.1'}, {'type': 'r', 'name': 'date', 'version': '1.2-42'}, {'type': 'r', 'name': 'cmprsk', 'version': '2.2-11'}, {'type': 'r', 'name': 'mets', 'version': '1.3.3'}, {'type': 'r', 'name': 'Publish', 'version': '2023.01.17'}, {'type': 'r', 'name': 'riskRegression', 'version': '2023.09.08'}, {'type': 'r', 'name': 'pec', 'version': '2023.04.12'}, {'type': 'r', 'name': 'pammtools', 'version': '0.5.92'}, {'type': 'r', 'name': 'relsurv', 'version': '2.2-9'}, {'type': 'r', 'name': 'mstate', 'version': '0.3.2'}, {'type': 'r', 'name': 'microbenchmark', 'version': '1.4.10'}, {'type': 'r', 'name': 'prettyGraphs', 'version': '2.1.6'}, {'type': 'r', 'name': 'ExPosition', 'version': '2.8.23'}, {'type': 'r', 'name': 'alluvial', 'version': '0.1-2'}, {'type': 'r', 'name': 'SNFtool', 'version': '2.3.1'}, {'type': 'r', 'name': 'BayesLogit', 'version': '2.1'}, {'type': 'r', 'name': 'Hmsc', 'version': '3.0-13'}, {'type': 'r', 'name': 'MonteCarlo', 'version': '1.0.6'}, {'type': 'r', 'name': 'chkptstanr', 'version': '0.1.1'}, {'type': 'r', 'name': 'MLmetrics', 'version': '1.1.1'}, {'type': 'r', 'name': 'elliptic', 'version': '1.4-0'}, {'type': 'r', 'name': 'contfrac', 'version': '1.1-12'}, {'type': 'r', 'name': 'hypergeo', 'version': '1.2-13'}, {'type': 'r', 'name': 'rtdists', 'version': '0.11-5'}, {'type': 'r', 'name': 'AMAPVox', 'version': '1.0.1'}, {'type': 'r', 'name': 'LCFdata', 'version': '2.0'}, {'type': 'r', 'name': 'LMERConvenienceFunctions', 'version': '3.0'}, {'type': 'r', 'name': 'HGNChelper', 'version': '0.8.1'}, {'type': 'r', 'name': 'logger', 'version': '0.2.2'}, {'type': 'r', 'name': 'parallelDist', 'version': '0.2.6'}, {'type': 'r', 'name': 'roptim', 'version': '0.1.6'}, {'type': 'r', 'name': 'yulab.utils', 'version': '0.1.0'}, {'type': 'r', 'name': 'ggfun', 'version': '0.1.3'}, {'type': 'r', 'name': 'gridGraphics', 'version': '0.5-1'}, {'type': 'r', 'name': 'ggplotify', 'version': '0.1.2'}, {'type': 'r', 'name': 'aplot', 'version': '0.2.2'}, {'type': 'r', 'name': 'tidytree', 'version': '0.4.5'}, {'type': 'r', 'name': 'ggvenn', 'version': '0.1.10'}, {'type': 'r', 'name': 'scatterpie', 'version': '0.2.1'}, {'type': 'r', 'name': 'shadowtext', 'version': '0.1.2'}, {'type': 'r', 'name': 'random', 'version': '0.2.6'}, {'type': 'r', 'name': 'R2WinBUGS', 'version': '2.1-21'}, {'type': 'r', 'name': 'aricode', 'version': '1.0.3'}, {'type': 'r', 'name': 'DepthProc', 'version': '2.1.5'}, {'type': 'r', 'name': 'dbscan', 'version': '1.1-12'}, {'type': 'r', 'name': 'ggh4x', 'version': '0.2.6'}, {'type': 'r', 'name': 'ComplexUpset', 'version': '1.3.3'}, {'type': 'r', 'name': 'proxyC', 'version': '0.3.4'}, {'type': 'r', 'name': 'changepoint', 'version': '2.2.4'}, {'type': 'r', 'name': 'geeM', 'version': '0.10.1'}, {'type': 'r', 'name': 'ggstance', 'version': '0.3.6'}, {'type': 'r', 'name': 'mosaicCore', 'version': '0.9.4.0'}, {'type': 'r', 'name': 'ggformula', 'version': '0.12.0'}, {'type': 'r', 'name': 'kinship2', 'version': '1.9.6'}, {'type': 'r', 'name': 'MESS', 'version': '0.5.12'}, {'type': 'r', 'name': 'smoof', 'version': '1.6.0.3'}, {'type': 'r', 'name': 'mlrMBO', 'version': '1.1.5.1'}, {'type': 'r', 'name': 'emoa', 'version': '0.5-0.2'}, {'type': 'r', 'name': 'webutils', 'version': '1.2.0'}, {'type': 'r', 'name': 'swagger', 'version': '3.33.1'}, {'type': 'r', 'name': 'varhandle', 'version': '2.0.6'}, {'type': 'r', 'name': 'dlm', 'version': '1.1-6'}, {'type': 'r', 'name': 'PMA', 'version': '1.2-2'}, {'type': 'r', 'name': 'unikn', 'version': '0.9.0'}, {'type': 'r', 'name': 'ppcor', 'version': '1.1'}, {'type': 'r', 'name': 'berryFunctions', 'version': '1.22.0'}, {'type': 'r', 'name': 'cld2', 'version': '1.2.4'}, {'type': 'r', 'name': 'crfsuite', 'version': '0.4.2'}, {'type': 'r', 'name': 'doc2vec', 'version': '0.2.0'}, {'type': 'r', 'name': 'fastDummies', 'version': '1.7.3'}, {'type': 'r', 'name': 'quanteda', 'version': '3.3.1'}, {'type': 'r', 'name': 'ISOweek', 'version': '0.6-2'}, {'type': 'r', 'name': 'sentometrics', 'version': '1.0.0'}, {'type': 'r', 'name': 'tau', 'version': '0.0-25'}, {'type': 'r', 'name': 'textcat', 'version': '1.0-8'}, {'type': 'r', 'name': 'textplot', 'version': '0.2.2'}, {'type': 'r', 'name': 'udpipe', 'version': '0.8.11'}, {'type': 'r', 'name': 'word2vec', 'version': '0.4.0'}, {'type': 'r', 'name': 'epitools', 'version': '0.5-10.1'}, {'type': 'r', 'name': 'RBesT', 'version': '1.7-2'}, {'type': 'r', 'name': 'svglite', 'version': '2.1.3'}, {'type': 'r', 'name': 'rARPACK', 'version': '0.11-0'}, {'type': 'r', 'name': 'FKSUM', 'version': '1.0.1'}, {'type': 'r', 'name': 'warp', 'version': '0.2.1'}, {'type': 'r', 'name': 'slider', 'version': '0.3.1'}, {'type': 'r', 'name': 'rsample', 'version': '1.2.0'}, {'type': 'r', 'name': 'haldensify', 'version': '0.2.3'}, {'type': 'r', 'name': 'Polychrome', 'version': '1.5.1'}, {'type': 'r', 'name': 'shinycssloaders', 'version': '1.0.0'}, {'type': 'r', 'name': 'princurve', 'version': '2.1.6'}, {'type': 'r', 'name': 'ECOSolveR', 'version': '0.5.5'}, {'type': 'r', 'name': 'scs', 'version': '3.2.4'}, {'type': 'r', 'name': 'osqp', 'version': '0.6.3.2'}, {'type': 'r', 'name': 'CVXR', 'version': '1.0-11'}, {'type': 'r', 'name': 'tabletools', 'version': '0.1.0'}, {'type': 'r', 'name': 'officer', 'version': '0.6.3'}, {'type': 'r', 'name': 'gfonts', 'version': '0.2.0'}, {'type': 'r', 'name': 'fontBitstreamVera', 'version': '0.1.1'}, {'type': 'r', 'name': 'fontLiberation', 'version': '0.1.0'}, {'type': 'r', 'name': 'fontquiver', 'version': '0.2.1'}, {'type': 'r', 'name': 'gdtools', 'version': '0.3.5'}, {'type': 'r', 'name': 'flextable', 'version': '0.9.4'}, {'type': 'r', 'name': 'ridge', 'version': '3.3'}, {'type': 'r', 'name': 'ggdist', 'version': '3.3.1'}, {'type': 'r', 'name': 'svUnit', 'version': '1.0.6'}, {'type': 'r', 'name': 'arrayhelpers', 'version': '1.1-0'}, {'type': 'r', 'name': 'tidybayes', 'version': '3.0.6'}, {'type': 'r', 'name': 'spdep', 'version': '1.3-1'}, {'type': 'r', 'name': 'stringmagic', 'version': '1.0.0'}, {'type': 'r', 'name': 'dreamerr', 'version': '1.4.0'}, {'type': 'r', 'name': 'fixest', 'version': '0.11.2'}, {'type': 'r', 'name': 'cmna', 'version': '1.0.5'}, {'type': 'r', 'name': 'XBRL', 'version': '0.99.19.1'}, {'type': 'r', 'name': 'rhandsontable', 'version': '0.3.8'}, {'type': 'r', 'name': 'missMDA', 'version': '1.19'}]}, {'homepage': 'https://www.r-project.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2023b'}, 'toolchain_families_compatibility': ['2023b_foss'], 'module': {'full_module_name': 'R-bundle-CRAN/2024.06-foss-2023b', 'module_name': 'R-bundle-CRAN', 'module_version': '2024.06-foss-2023b'}, 'required_modules': [{'full_module_name': 'EESSI/2023.06', 'module_name': 'EESSI', 'module_version': '2023.06'}, {'full_module_name': 'GCCcore/13.2.0', 'module_name': 'GCCcore', 'module_version': '13.2.0'}, {'full_module_name': 'GCC/13.2.0', 'module_name': 'GCC', 'module_version': '13.2.0'}, {'full_module_name': 'numactl/2.0.16-GCCcore-13.2.0', 'module_name': 'numactl', 'module_version': '2.0.16-GCCcore-13.2.0'}, {'full_module_name': 'libxml2/2.11.5-GCCcore-13.2.0', 'module_name': 'libxml2', 'module_version': '2.11.5-GCCcore-13.2.0'}, {'full_module_name': 'libpciaccess/0.17-GCCcore-13.2.0', 'module_name': 'libpciaccess', 'module_version': '0.17-GCCcore-13.2.0'}, {'full_module_name': 'hwloc/2.9.2-GCCcore-13.2.0', 'module_name': 'hwloc', 'module_version': '2.9.2-GCCcore-13.2.0'}, {'full_module_name': 'OpenSSL/1.1', 'module_name': 'OpenSSL', 'module_version': '1.1'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.2.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.2.0'}, {'full_module_name': 'UCX/1.15.0-GCCcore-13.2.0', 'module_name': 'UCX', 'module_version': '1.15.0-GCCcore-13.2.0'}, {'full_module_name': 'libfabric/1.19.0-GCCcore-13.2.0', 'module_name': 'libfabric', 'module_version': '1.19.0-GCCcore-13.2.0'}, {'full_module_name': 'PMIx/4.2.6-GCCcore-13.2.0', 'module_name': 'PMIx', 'module_version': '4.2.6-GCCcore-13.2.0'}, {'full_module_name': 'UCC/1.2.0-GCCcore-13.2.0', 'module_name': 'UCC', 'module_version': '1.2.0-GCCcore-13.2.0'}, {'full_module_name': 'OpenMPI/4.1.6-GCC-13.2.0', 'module_name': 'OpenMPI', 'module_version': '4.1.6-GCC-13.2.0'}, {'full_module_name': 'OpenBLAS/0.3.24-GCC-13.2.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.24-GCC-13.2.0'}, {'full_module_name': 'FlexiBLAS/3.3.1-GCC-13.2.0', 'module_name': 'FlexiBLAS', 'module_version': '3.3.1-GCC-13.2.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.2.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.2.0'}, {'full_module_name': 'gompi/2023b', 'module_name': 'gompi', 'module_version': '2023b'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2023b', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2023b'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2023b-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2023b-fb'}, {'full_module_name': 'foss/2023b', 'module_name': 'foss', 'module_version': '2023b'}, {'full_module_name': 'gfbf/2023b', 'module_name': 'gfbf', 'module_version': '2023b'}, {'full_module_name': 'expat/2.5.0-GCCcore-13.2.0', 'module_name': 'expat', 'module_version': '2.5.0-GCCcore-13.2.0'}, {'full_module_name': 'libpng/1.6.40-GCCcore-13.2.0', 'module_name': 'libpng', 'module_version': '1.6.40-GCCcore-13.2.0'}, {'full_module_name': 'Brotli/1.1.0-GCCcore-13.2.0', 'module_name': 'Brotli', 'module_version': '1.1.0-GCCcore-13.2.0'}, {'full_module_name': 'freetype/2.13.2-GCCcore-13.2.0', 'module_name': 'freetype', 'module_version': '2.13.2-GCCcore-13.2.0'}, {'full_module_name': 'fontconfig/2.14.2-GCCcore-13.2.0', 'module_name': 'fontconfig', 'module_version': '2.14.2-GCCcore-13.2.0'}, {'full_module_name': 'xorg-macros/1.20.0-GCCcore-13.2.0', 'module_name': 'xorg-macros', 'module_version': '1.20.0-GCCcore-13.2.0'}, {'full_module_name': 'X11/20231019-GCCcore-13.2.0', 'module_name': 'X11', 'module_version': '20231019-GCCcore-13.2.0'}, {'full_module_name': 'gzip/1.13-GCCcore-13.2.0', 'module_name': 'gzip', 'module_version': '1.13-GCCcore-13.2.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-13.2.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-13.2.0'}, {'full_module_name': 'zstd/1.5.5-GCCcore-13.2.0', 'module_name': 'zstd', 'module_version': '1.5.5-GCCcore-13.2.0'}, {'full_module_name': 'libdrm/2.4.117-GCCcore-13.2.0', 'module_name': 'libdrm', 'module_version': '2.4.117-GCCcore-13.2.0'}, {'full_module_name': 'libglvnd/1.7.0-GCCcore-13.2.0', 'module_name': 'libglvnd', 'module_version': '1.7.0-GCCcore-13.2.0'}, {'full_module_name': 'libunwind/1.6.2-GCCcore-13.2.0', 'module_name': 'libunwind', 'module_version': '1.6.2-GCCcore-13.2.0'}, {'full_module_name': 'LLVM/16.0.6-GCCcore-13.2.0', 'module_name': 'LLVM', 'module_version': '16.0.6-GCCcore-13.2.0'}, {'full_module_name': 'Mesa/23.1.9-GCCcore-13.2.0', 'module_name': 'Mesa', 'module_version': '23.1.9-GCCcore-13.2.0'}, {'full_module_name': 'libGLU/9.0.3-GCCcore-13.2.0', 'module_name': 'libGLU', 'module_version': '9.0.3-GCCcore-13.2.0'}, {'full_module_name': 'pixman/0.42.2-GCCcore-13.2.0', 'module_name': 'pixman', 'module_version': '0.42.2-GCCcore-13.2.0'}, {'full_module_name': 'libffi/3.4.4-GCCcore-13.2.0', 'module_name': 'libffi', 'module_version': '3.4.4-GCCcore-13.2.0'}, {'full_module_name': 'PCRE2/10.42-GCCcore-13.2.0', 'module_name': 'PCRE2', 'module_version': '10.42-GCCcore-13.2.0'}, {'full_module_name': 'GLib/2.78.1-GCCcore-13.2.0', 'module_name': 'GLib', 'module_version': '2.78.1-GCCcore-13.2.0'}, {'full_module_name': 'cairo/1.18.0-GCCcore-13.2.0', 'module_name': 'cairo', 'module_version': '1.18.0-GCCcore-13.2.0'}, {'full_module_name': 'Tcl/8.6.13-GCCcore-13.2.0', 'module_name': 'Tcl', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'SQLite/3.43.1-GCCcore-13.2.0', 'module_name': 'SQLite', 'module_version': '3.43.1-GCCcore-13.2.0'}, {'full_module_name': 'NASM/2.16.01-GCCcore-13.2.0', 'module_name': 'NASM', 'module_version': '2.16.01-GCCcore-13.2.0'}, {'full_module_name': 'libjpeg-turbo/3.0.1-GCCcore-13.2.0', 'module_name': 'libjpeg-turbo', 'module_version': '3.0.1-GCCcore-13.2.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-13.2.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-13.2.0'}, {'full_module_name': 'libdeflate/1.19-GCCcore-13.2.0', 'module_name': 'libdeflate', 'module_version': '1.19-GCCcore-13.2.0'}, {'full_module_name': 'LibTIFF/4.6.0-GCCcore-13.2.0', 'module_name': 'LibTIFF', 'module_version': '4.6.0-GCCcore-13.2.0'}, {'full_module_name': 'Java/11.0.27', 'module_name': 'Java', 'module_version': '11.0.27'}, {'full_module_name': 'Java/11', 'module_name': 'Java', 'module_version': '11'}, {'full_module_name': 'libgit2/1.7.2-GCCcore-13.2.0', 'module_name': 'libgit2', 'module_version': '1.7.2-GCCcore-13.2.0'}, {'full_module_name': 'cURL/8.3.0-GCCcore-13.2.0', 'module_name': 'cURL', 'module_version': '8.3.0-GCCcore-13.2.0'}, {'full_module_name': 'Tk/8.6.13-GCCcore-13.2.0', 'module_name': 'Tk', 'module_version': '8.6.13-GCCcore-13.2.0'}, {'full_module_name': 'ICU/74.1-GCCcore-13.2.0', 'module_name': 'ICU', 'module_version': '74.1-GCCcore-13.2.0'}, {'full_module_name': 'HarfBuzz/8.2.2-GCCcore-13.2.0', 'module_name': 'HarfBuzz', 'module_version': '8.2.2-GCCcore-13.2.0'}, {'full_module_name': 'FriBidi/1.0.13-GCCcore-13.2.0', 'module_name': 'FriBidi', 'module_version': '1.0.13-GCCcore-13.2.0'}, {'full_module_name': 'R/4.4.1-gfbf-2023b', 'module_name': 'R', 'module_version': '4.4.1-gfbf-2023b'}, {'full_module_name': 'GMP/6.3.0-GCCcore-13.2.0', 'module_name': 'GMP', 'module_version': '6.3.0-GCCcore-13.2.0'}, {'full_module_name': 'NLopt/2.7.1-GCCcore-13.2.0', 'module_name': 'NLopt', 'module_version': '2.7.1-GCCcore-13.2.0'}, {'full_module_name': 'libogg/1.3.5-GCCcore-13.2.0', 'module_name': 'libogg', 'module_version': '1.3.5-GCCcore-13.2.0'}, {'full_module_name': 'FLAC/1.4.3-GCCcore-13.2.0', 'module_name': 'FLAC', 'module_version': '1.4.3-GCCcore-13.2.0'}, {'full_module_name': 'libvorbis/1.3.7-GCCcore-13.2.0', 'module_name': 'libvorbis', 'module_version': '1.3.7-GCCcore-13.2.0'}, {'full_module_name': 'libopus/1.5.2-GCCcore-13.2.0', 'module_name': 'libopus', 'module_version': '1.5.2-GCCcore-13.2.0'}, {'full_module_name': 'LAME/3.100-GCCcore-13.2.0', 'module_name': 'LAME', 'module_version': '3.100-GCCcore-13.2.0'}, {'full_module_name': 'libsndfile/1.2.2-GCCcore-13.2.0', 'module_name': 'libsndfile', 'module_version': '1.2.2-GCCcore-13.2.0'}, {'full_module_name': 'Szip/2.1.1-GCCcore-13.2.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-13.2.0'}, {'full_module_name': 'HDF5/1.14.3-gompi-2023b', 'module_name': 'HDF5', 'module_version': '1.14.3-gompi-2023b'}, {'full_module_name': 'UDUNITS/2.2.28-GCCcore-13.2.0', 'module_name': 'UDUNITS', 'module_version': '2.2.28-GCCcore-13.2.0'}, {'full_module_name': 'GSL/2.7-GCC-13.2.0', 'module_name': 'GSL', 'module_version': '2.7-GCC-13.2.0'}, {'full_module_name': 'ATK/2.38.0-GCCcore-13.2.0', 'module_name': 'ATK', 'module_version': '2.38.0-GCCcore-13.2.0'}, {'full_module_name': 'at-spi2-core/2.50.0-GCCcore-13.2.0', 'module_name': 'at-spi2-core', 'module_version': '2.50.0-GCCcore-13.2.0'}, {'full_module_name': 'at-spi2-atk/2.38.0-GCCcore-13.2.0', 'module_name': 'at-spi2-atk', 'module_version': '2.38.0-GCCcore-13.2.0'}, {'full_module_name': 'Gdk-Pixbuf/2.42.10-GCCcore-13.2.0', 'module_name': 'Gdk-Pixbuf', 'module_version': '2.42.10-GCCcore-13.2.0'}, {'full_module_name': 'Pango/1.51.0-GCCcore-13.2.0', 'module_name': 'Pango', 'module_version': '1.51.0-GCCcore-13.2.0'}, {'full_module_name': 'libepoxy/1.5.10-GCCcore-13.2.0', 'module_name': 'libepoxy', 'module_version': '1.5.10-GCCcore-13.2.0'}, {'full_module_name': 'Wayland/1.22.0-GCCcore-13.2.0', 'module_name': 'Wayland', 'module_version': '1.22.0-GCCcore-13.2.0'}, {'full_module_name': 'GTK3/3.24.39-GCCcore-13.2.0', 'module_name': 'GTK3', 'module_version': '3.24.39-GCCcore-13.2.0'}, {'full_module_name': 'Ghostscript/10.02.1-GCCcore-13.2.0', 'module_name': 'Ghostscript', 'module_version': '10.02.1-GCCcore-13.2.0'}, {'full_module_name': 'JasPer/4.0.0-GCCcore-13.2.0', 'module_name': 'JasPer', 'module_version': '4.0.0-GCCcore-13.2.0'}, {'full_module_name': 'LittleCMS/2.15-GCCcore-13.2.0', 'module_name': 'LittleCMS', 'module_version': '2.15-GCCcore-13.2.0'}, {'full_module_name': 'ImageMagick/7.1.1-34-GCCcore-13.2.0', 'module_name': 'ImageMagick', 'module_version': '7.1.1-34-GCCcore-13.2.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-13.2.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-13.2.0'}, {'full_module_name': 'nodejs/20.9.0-GCCcore-13.2.0', 'module_name': 'nodejs', 'module_version': '20.9.0-GCCcore-13.2.0'}, {'full_module_name': 'Python/3.11.5-GCCcore-13.2.0', 'module_name': 'Python', 'module_version': '3.11.5-GCCcore-13.2.0'}, {'full_module_name': 'netCDF/4.9.2-gompi-2023b', 'module_name': 'netCDF', 'module_version': '4.9.2-gompi-2023b'}, {'full_module_name': 'GEOS/3.12.1-GCC-13.2.0', 'module_name': 'GEOS', 'module_version': '3.12.1-GCC-13.2.0'}, {'full_module_name': 'libarchive/3.7.2-GCCcore-13.2.0', 'module_name': 'libarchive', 'module_version': '3.7.2-GCCcore-13.2.0'}, {'full_module_name': 'PCRE/8.45-GCCcore-13.2.0', 'module_name': 'PCRE', 'module_version': '8.45-GCCcore-13.2.0'}, {'full_module_name': 'nlohmann_json/3.11.3-GCCcore-13.2.0', 'module_name': 'nlohmann_json', 'module_version': '3.11.3-GCCcore-13.2.0'}, {'full_module_name': 'PROJ/9.3.1-GCCcore-13.2.0', 'module_name': 'PROJ', 'module_version': '9.3.1-GCCcore-13.2.0'}, {'full_module_name': 'libgeotiff/1.7.3-GCCcore-13.2.0', 'module_name': 'libgeotiff', 'module_version': '1.7.3-GCCcore-13.2.0'}, {'full_module_name': 'cffi/1.15.1-GCCcore-13.2.0', 'module_name': 'cffi', 'module_version': '1.15.1-GCCcore-13.2.0'}, {'full_module_name': 'cryptography/41.0.5-GCCcore-13.2.0', 'module_name': 'cryptography', 'module_version': '41.0.5-GCCcore-13.2.0'}, {'full_module_name': 'virtualenv/20.24.6-GCCcore-13.2.0', 'module_name': 'virtualenv', 'module_version': '20.24.6-GCCcore-13.2.0'}, {'full_module_name': 'Python-bundle-PyPI/2023.10-GCCcore-13.2.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2023.10-GCCcore-13.2.0'}, {'full_module_name': 'pybind11/2.11.1-GCCcore-13.2.0', 'module_name': 'pybind11', 'module_version': '2.11.1-GCCcore-13.2.0'}, {'full_module_name': 'SciPy-bundle/2023.11-gfbf-2023b', 'module_name': 'SciPy-bundle', 'module_version': '2023.11-gfbf-2023b'}, {'full_module_name': 'libtirpc/1.3.4-GCCcore-13.2.0', 'module_name': 'libtirpc', 'module_version': '1.3.4-GCCcore-13.2.0'}, {'full_module_name': 'HDF/4.2.16-2-GCCcore-13.2.0', 'module_name': 'HDF', 'module_version': '4.2.16-2-GCCcore-13.2.0'}, {'full_module_name': 'Boost/1.83.0-GCC-13.2.0', 'module_name': 'Boost', 'module_version': '1.83.0-GCC-13.2.0'}, {'full_module_name': 'Eigen/3.4.0-GCCcore-13.2.0', 'module_name': 'Eigen', 'module_version': '3.4.0-GCCcore-13.2.0'}, {'full_module_name': 'arpack-ng/3.9.0-foss-2023b', 'module_name': 'arpack-ng', 'module_version': '3.9.0-foss-2023b'}, {'full_module_name': 'Armadillo/12.8.0-foss-2023b', 'module_name': 'Armadillo', 'module_version': '12.8.0-foss-2023b'}, {'full_module_name': 'CFITSIO/4.3.1-GCCcore-13.2.0', 'module_name': 'CFITSIO', 'module_version': '4.3.1-GCCcore-13.2.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-13.2.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-13.2.0'}, {'full_module_name': 'json-c/0.17-GCCcore-13.2.0', 'module_name': 'json-c', 'module_version': '0.17-GCCcore-13.2.0'}, {'full_module_name': 'Xerces-C++/3.2.5-GCCcore-13.2.0', 'module_name': 'Xerces-C++', 'module_version': '3.2.5-GCCcore-13.2.0'}, {'full_module_name': 'Imath/3.1.9-GCCcore-13.2.0', 'module_name': 'Imath', 'module_version': '3.1.9-GCCcore-13.2.0'}, {'full_module_name': 'OpenEXR/3.2.0-GCCcore-13.2.0', 'module_name': 'OpenEXR', 'module_version': '3.2.0-GCCcore-13.2.0'}, {'full_module_name': 'Brunsli/0.1-GCCcore-13.2.0', 'module_name': 'Brunsli', 'module_version': '0.1-GCCcore-13.2.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-13.2.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-13.2.0'}, {'full_module_name': 'LERC/4.0.0-GCCcore-13.2.0', 'module_name': 'LERC', 'module_version': '4.0.0-GCCcore-13.2.0'}, {'full_module_name': 'OpenJPEG/2.5.0-GCCcore-13.2.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.0-GCCcore-13.2.0'}, {'full_module_name': 'SWIG/4.1.1-GCCcore-13.2.0', 'module_name': 'SWIG', 'module_version': '4.1.1-GCCcore-13.2.0'}, {'full_module_name': 'GDAL/3.9.0-foss-2023b', 'module_name': 'GDAL', 'module_version': '3.9.0-foss-2023b'}, {'full_module_name': 'MPFR/4.2.1-GCCcore-13.2.0', 'module_name': 'MPFR', 'module_version': '4.2.1-GCCcore-13.2.0'}, {'full_module_name': 'PostgreSQL/16.1-GCCcore-13.2.0', 'module_name': 'PostgreSQL', 'module_version': '16.1-GCCcore-13.2.0'}, {'full_module_name': 'R-bundle-CRAN/2024.06-foss-2023b', 'module_name': 'R-bundle-CRAN', 'module_version': '2024.06-foss-2023b'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Bundle of R packages from CRAN', 'version': '2024.06', 'versionsuffix': '', 'extensions': [{'type': 'r', 'name': 'abind', 'version': '1.4-5'}, {'type': 'r', 'name': 'magic', 'version': '1.6-1'}, {'type': 'r', 'name': 'RcppProgress', 'version': '0.4.2'}, {'type': 'r', 'name': 'lpSolve', 'version': '5.6.20'}, {'type': 'r', 'name': 'linprog', 'version': '0.9-4'}, {'type': 'r', 'name': 'geometry', 'version': '0.4.7'}, {'type': 'r', 'name': 'bit', 'version': '4.0.5'}, {'type': 'r', 'name': 'filehash', 'version': '2.4-5'}, {'type': 'r', 'name': 'ff', 'version': '4.0.12'}, {'type': 'r', 'name': 'bnlearn', 'version': '4.9.4'}, {'type': 'r', 'name': 'bootstrap', 'version': '2019.6'}, {'type': 'r', 'name': 'combinat', 'version': '0.0-8'}, {'type': 'r', 'name': 'deal', 'version': '1.2-42'}, {'type': 'r', 'name': 'fdrtool', 'version': '1.2.17'}, {'type': 'r', 'name': 'formatR', 'version': '1.14'}, {'type': 'r', 'name': 'gtools', 'version': '3.9.5'}, {'type': 'r', 'name': 'gdata', 'version': '3.0.0'}, {'type': 'r', 'name': 'GSA', 'version': '1.03.3'}, {'type': 'r', 'name': 'infotheo', 'version': '1.2.0.1'}, {'type': 'r', 'name': 'lars', 'version': '1.3'}, {'type': 'r', 'name': 'lazy', 'version': '1.2-18'}, {'type': 'r', 'name': 'kernlab', 'version': '0.9-32'}, {'type': 'r', 'name': 'markdown', 'version': '1.13'}, {'type': 'r', 'name': 'mlbench', 'version': '2.1-5'}, {'type': 'r', 'name': 'NLP', 'version': '0.2-1'}, {'type': 'r', 'name': 'mclust', 'version': '6.1.1'}, {'type': 'r', 'name': 'RANN', 'version': '2.6.1'}, {'type': 'r', 'name': 'rmeta', 'version': '3.0'}, {'type': 'r', 'name': 'MASS', 'version': '7.3-61'}, {'type': 'r', 'name': 'lattice', 'version': '0.22-6'}, {'type': 'r', 'name': 'nlme', 'version': '3.1-165'}, {'type': 'r', 'name': 'segmented', 'version': '2.1-0'}, {'type': 'r', 'name': 'som', 'version': '0.3-5.1'}, {'type': 'r', 'name': 'SuppDists', 'version': '1.1-9.7'}, {'type': 'r', 'name': 'stabledist', 'version': '0.7-1'}, {'type': 'r', 'name': 'survivalROC', 'version': '1.0.3.1'}, {'type': 'r', 'name': 'pspline', 'version': '1.0-20'}, {'type': 'r', 'name': 'timeDate', 'version': '4032.109'}, {'type': 'r', 'name': 'longmemo', 'version': '1.1-2'}, {'type': 'r', 'name': 'ADGofTest', 'version': '0.3'}, {'type': 'r', 'name': 'pixmap', 'version': '0.4-13'}, {'type': 'r', 'name': 'sp', 'version': '2.1-4'}, {'type': 'r', 'name': 'hms', 'version': '1.1.3'}, {'type': 'r', 'name': 'progress', 'version': '1.2.3'}, {'type': 'r', 'name': 'RcppArmadillo', 'version': '0.12.8.4.0'}, {'type': 'r', 'name': 'ade4', 'version': '1.7-22'}, {'type': 'r', 'name': 'AlgDesign', 'version': '1.2.1'}, {'type': 'r', 'name': 'BH', 'version': '1.84.0-0'}, {'type': 'r', 'name': 'Matrix', 'version': '1.7-0'}, {'type': 'r', 'name': 'Brobdingnag', 'version': '1.2-9'}, {'type': 'r', 'name': 'corpcor', 'version': '1.6.10'}, {'type': 'r', 'name': 'longitudinal', 'version': '1.1.13'}, {'type': 'r', 'name': 'backports', 'version': '1.5.0'}, {'type': 'r', 'name': 'checkmate', 'version': '2.3.1'}, {'type': 'r', 'name': 'cubature', 'version': '2.1.0'}, {'type': 'r', 'name': 'DEoptimR', 'version': '1.1-3'}, {'type': 'r', 'name': 'fastmatch', 'version': '1.1-4'}, {'type': 'r', 'name': 'iterators', 'version': '1.0.14'}, {'type': 'r', 'name': 'maps', 'version': '3.4.2'}, {'type': 'r', 'name': 'nnls', 'version': '1.5'}, {'type': 'r', 'name': 'sendmailR', 'version': '1.4-0'}, {'type': 'r', 'name': 'dotCall64', 'version': '1.1-1'}, {'type': 'r', 'name': 'spam', 'version': '2.10-0'}, {'type': 'r', 'name': 'subplex', 'version': '1.8'}, {'type': 'r', 'name': 'logspline', 'version': '2.1.22'}, {'type': 'r', 'name': 'ncbit', 'version': '2013.03.29.1'}, {'type': 'r', 'name': 'permute', 'version': '0.9-7'}, {'type': 'r', 'name': 'plotrix', 'version': '3.8-4'}, {'type': 'r', 'name': 'randomForest', 'version': '4.7-1.1'}, {'type': 'r', 'name': 'scatterplot3d', 'version': '0.3-44'}, {'type': 'r', 'name': 'SparseM', 'version': '1.83'}, {'type': 'r', 'name': 'tripack', 'version': '1.3-9.1'}, {'type': 'r', 'name': 'irace', 'version': '3.5'}, {'type': 'r', 'name': 'rJava', 'version': '1.0-11'}, {'type': 'r', 'name': 'RColorBrewer', 'version': '1.1-3'}, {'type': 'r', 'name': 'png', 'version': '0.1-8'}, {'type': 'r', 'name': 'jpeg', 'version': '0.1-10'}, {'type': 'r', 'name': 'deldir', 'version': '2.0-4'}, {'type': 'r', 'name': 'RcppEigen', 'version': '0.3.4.0.0'}, {'type': 'r', 'name': 'interp', 'version': '1.1-6'}, {'type': 'r', 'name': 'latticeExtra', 'version': '0.6-30'}, {'type': 'r', 'name': 'plyr', 'version': '1.8.9'}, {'type': 'r', 'name': 'gtable', 'version': '0.3.5'}, {'type': 'r', 'name': 'reshape2', 'version': '1.4.4'}, {'type': 'r', 'name': 'dichromat', 'version': '2.0-0.1'}, {'type': 'r', 'name': 'colorspace', 'version': '2.1-0'}, {'type': 'r', 'name': 'munsell', 'version': '0.5.1'}, {'type': 'r', 'name': 'labeling', 'version': '0.4.3'}, {'type': 'r', 'name': 'viridisLite', 'version': '0.4.2'}, {'type': 'r', 'name': 'farver', 'version': '2.1.2'}, {'type': 'r', 'name': 'scales', 'version': '1.3.0'}, {'type': 'r', 'name': 'zeallot', 'version': '0.1.0'}, {'type': 'r', 'name': 'assertthat', 'version': '0.2.1'}, {'type': 'r', 'name': 'lazyeval', 'version': '0.2.2'}, {'type': 'r', 'name': 'mgcv', 'version': '1.9-1'}, {'type': 'r', 'name': 'isoband', 'version': '0.2.7'}, {'type': 'r', 'name': 'ggplot2', 'version': '3.5.1'}, {'type': 'r', 'name': 'pROC', 'version': '1.18.5'}, {'type': 'r', 'name': 'quadprog', 'version': '1.5-8'}, {'type': 'r', 'name': 'BB', 'version': '2019.10-1'}, {'type': 'r', 'name': 'data.table', 'version': '1.15.4'}, {'type': 'r', 'name': 'BBmisc', 'version': '1.13'}, {'type': 'r', 'name': 'fail', 'version': '1.3'}, {'type': 'r', 'name': 'rlecuyer', 'version': '0.3-8'}, {'type': 'r', 'name': 'snow', 'version': '0.4-4'}, {'type': 'r', 'name': 'tree', 'version': '1.0-43'}, {'type': 'r', 'name': 'pls', 'version': '2.8-3'}, {'type': 'r', 'name': 'class', 'version': '7.3-22'}, {'type': 'r', 'name': 'proxy', 'version': '0.4-27'}, {'type': 'r', 'name': 'e1071', 'version': '1.7-14'}, {'type': 'r', 'name': 'nnet', 'version': '7.3-19'}, {'type': 'r', 'name': 'minqa', 'version': '1.2.7'}, {'type': 'r', 'name': 'MatrixModels', 'version': '0.5-3'}, {'type': 'r', 'name': 'matrixStats', 'version': '1.3.0'}, {'type': 'r', 'name': 'codetools', 'version': '0.2-20'}, {'type': 'r', 'name': 'foreach', 'version': '1.5.2'}, {'type': 'r', 'name': 'ModelMetrics', 'version': '1.2.2.2'}, {'type': 'r', 'name': 'generics', 'version': '0.1.3'}, {'type': 'r', 'name': 'tidyselect', 'version': '1.2.1'}, {'type': 'r', 'name': 'dplyr', 'version': '1.1.4'}, {'type': 'r', 'name': 'gower', 'version': '1.0.1'}, {'type': 'r', 'name': 'rpart', 'version': '4.1.23'}, {'type': 'r', 'name': 'survival', 'version': '3.7-0'}, {'type': 'r', 'name': 'KernSmooth', 'version': '2.23-24'}, {'type': 'r', 'name': 'globals', 'version': '0.16.3'}, {'type': 'r', 'name': 'listenv', 'version': '0.9.1'}, {'type': 'r', 'name': 'parallelly', 'version': '1.37.1'}, {'type': 'r', 'name': 'future', 'version': '1.33.2'}, {'type': 'r', 'name': 'future.apply', 'version': '1.11.2'}, {'type': 'r', 'name': 'progressr', 'version': '0.14.0'}, {'type': 'r', 'name': 'numDeriv', 'version': '2016.8-1.1'}, {'type': 'r', 'name': 'SQUAREM', 'version': '2021.1'}, {'type': 'r', 'name': 'lava', 'version': '1.8.0'}, {'type': 'r', 'name': 'shape', 'version': '1.4.6.1'}, {'type': 'r', 'name': 'diagram', 'version': '1.6.5'}, {'type': 'r', 'name': 'prodlim', 'version': '2023.08.28'}, {'type': 'r', 'name': 'ipred', 'version': '0.9-14'}, {'type': 'r', 'name': 'timechange', 'version': '0.3.0'}, {'type': 'r', 'name': 'lubridate', 'version': '1.9.3'}, {'type': 'r', 'name': 'tidyr', 'version': '1.3.1'}, {'type': 'r', 'name': 'hardhat', 'version': '1.4.0'}, {'type': 'r', 'name': 'tzdb', 'version': '0.4.0'}, {'type': 'r', 'name': 'clock', 'version': '0.7.0'}, {'type': 'r', 'name': 'recipes', 'version': '1.0.10'}, {'type': 'r', 'name': 'caret', 'version': '6.0-94'}, {'type': 'r', 'name': 'conquer', 'version': '1.3.3'}, {'type': 'r', 'name': 'quantreg', 'version': '5.98'}, {'type': 'r', 'name': 'robustbase', 'version': '0.99-2'}, {'type': 'r', 'name': 'zoo', 'version': '1.8-12'}, {'type': 'r', 'name': 'lmtest', 'version': '0.9-40'}, {'type': 'r', 'name': 'vcd', 'version': '1.4-12'}, {'type': 'r', 'name': 'snowfall', 'version': '1.84-6.3'}, {'type': 'r', 'name': 'bindr', 'version': '0.1.1'}, {'type': 'r', 'name': 'plogr', 'version': '0.2.0'}, {'type': 'r', 'name': 'bindrcpp', 'version': '0.2.3'}, {'type': 'r', 'name': 'tmvnsim', 'version': '1.0-2'}, {'type': 'r', 'name': 'mnormt', 'version': '2.1.1'}, {'type': 'r', 'name': 'foreign', 'version': '0.8-86'}, {'type': 'r', 'name': 'psych', 'version': '2.4.3'}, {'type': 'r', 'name': 'broom', 'version': '1.0.6'}, {'type': 'r', 'name': 'nloptr', 'version': '2.1.0'}, {'type': 'r', 'name': 'boot', 'version': '1.3-30'}, {'type': 'r', 'name': 'statmod', 'version': '1.5.0'}, {'type': 'r', 'name': 'lme4', 'version': '1.1-35.4'}, {'type': 'r', 'name': 'ucminf', 'version': '1.2.1'}, {'type': 'r', 'name': 'ordinal', 'version': '2023.12-4'}, {'type': 'r', 'name': 'jomo', 'version': '2.7-6'}, {'type': 'r', 'name': 'bit64', 'version': '4.0.5'}, {'type': 'r', 'name': 'vroom', 'version': '1.6.5'}, {'type': 'r', 'name': 'readr', 'version': '2.1.5'}, {'type': 'r', 'name': 'forcats', 'version': '1.0.0'}, {'type': 'r', 'name': 'haven', 'version': '2.5.4'}, {'type': 'r', 'name': 'pan', 'version': '1.9'}, {'type': 'r', 'name': 'mitml', 'version': '0.4-5'}, {'type': 'r', 'name': 'glmnet', 'version': '4.1-8'}, {'type': 'r', 'name': 'mice', 'version': '3.16.0'}, {'type': 'r', 'name': 'urca', 'version': '1.3-4'}, {'type': 'r', 'name': 'fracdiff', 'version': '1.5-3'}, {'type': 'r', 'name': 'operator.tools', 'version': '1.6.3'}, {'type': 'r', 'name': 'formula.tools', 'version': '1.7.1'}, {'type': 'r', 'name': 'logistf', 'version': '1.26.0'}, {'type': 'r', 'name': 'akima', 'version': '0.6-3.4'}, {'type': 'r', 'name': 'bitops', 'version': '1.0-7'}, {'type': 'r', 'name': 'crosstalk', 'version': '1.2.1'}, {'type': 'r', 'name': 'plotly', 'version': '4.10.4'}, {'type': 'r', 'name': 'mixtools', 'version': '2.0.0'}, {'type': 'r', 'name': 'cluster', 'version': '2.1.6'}, {'type': 'r', 'name': 'gclus', 'version': '1.3.2'}, {'type': 'r', 'name': 'coda', 'version': '0.19-4.1'}, {'type': 'r', 'name': 'doMC', 'version': '1.3.8'}, {'type': 'r', 'name': 'DBI', 'version': '1.2.3'}, {'type': 'r', 'name': 'gam', 'version': '1.22-3'}, {'type': 'r', 'name': 'gamlss.data', 'version': '6.0-6'}, {'type': 'r', 'name': 'gamlss.dist', 'version': '6.1-1'}, {'type': 'r', 'name': 'gamlss', 'version': '5.4-22'}, {'type': 'r', 'name': 'gamlss.tr', 'version': '5.1-9'}, {'type': 'r', 'name': 'hwriter', 'version': '1.3.2.1'}, {'type': 'r', 'name': 'xts', 'version': '0.14.0'}, {'type': 'r', 'name': 'TTR', 'version': '0.24.4'}, {'type': 'r', 'name': 'quantmod', 'version': '0.4.26'}, {'type': 'r', 'name': 'mvtnorm', 'version': '1.2-5'}, {'type': 'r', 'name': 'pcaPP', 'version': '2.0-4'}, {'type': 'r', 'name': 'pscl', 'version': '1.5.9'}, {'type': 'r', 'name': 'blob', 'version': '1.2.4'}, {'type': 'r', 'name': 'RSQLite', 'version': '2.3.7'}, {'type': 'r', 'name': 'BatchJobs', 'version': '1.9'}, {'type': 'r', 'name': 'sandwich', 'version': '3.1-0'}, {'type': 'r', 'name': 'sfsmisc', 'version': '1.1-18'}, {'type': 'r', 'name': 'spatial', 'version': '7.3-17'}, {'type': 'r', 'name': 'VGAM', 'version': '1.1-11'}, {'type': 'r', 'name': 'multitaper', 'version': '1.0-17'}, {'type': 'r', 'name': 'waveslim', 'version': '1.8.5'}, {'type': 'r', 'name': 'profileModel', 'version': '0.6.1'}, {'type': 'r', 'name': 'brglm', 'version': '0.7.2'}, {'type': 'r', 'name': 'deSolve', 'version': '1.40'}, {'type': 'r', 'name': 'tseriesChaos', 'version': '0.1-13.1'}, {'type': 'r', 'name': 'tseries', 'version': '0.10-56'}, {'type': 'r', 'name': 'fastICA', 'version': '1.2-4'}, {'type': 'r', 'name': 'R.methodsS3', 'version': '1.8.2'}, {'type': 'r', 'name': 'R.oo', 'version': '1.26.0'}, {'type': 'r', 'name': 'cgdsr', 'version': '1.3.0'}, {'type': 'r', 'name': 'R.utils', 'version': '2.12.3'}, {'type': 'r', 'name': 'R.matlab', 'version': '3.7.0'}, {'type': 'r', 'name': 'gridExtra', 'version': '2.3'}, {'type': 'r', 'name': 'gbm', 'version': '2.1.9'}, {'type': 'r', 'name': 'Formula', 'version': '1.2-5'}, {'type': 'r', 'name': 'acepack', 'version': '1.4.2'}, {'type': 'r', 'name': 'proto', 'version': '1.0.0'}, {'type': 'r', 'name': 'chron', 'version': '2.3-61'}, {'type': 'r', 'name': 'viridis', 'version': '0.6.5'}, {'type': 'r', 'name': 'htmlTable', 'version': '2.4.2'}, {'type': 'r', 'name': 'Hmisc', 'version': '5.1-3'}, {'type': 'r', 'name': 'fastcluster', 'version': '1.2.6'}, {'type': 'r', 'name': 'registry', 'version': '0.5-1'}, {'type': 'r', 'name': 'bibtex', 'version': '0.5.1'}, {'type': 'r', 'name': 'pkgmaker', 'version': '0.32.10'}, {'type': 'r', 'name': 'rngtools', 'version': '1.5.2'}, {'type': 'r', 'name': 'doParallel', 'version': '1.0.17'}, {'type': 'r', 'name': 'gridBase', 'version': '0.4-7'}, {'type': 'r', 'name': 'irlba', 'version': '2.3.5.1'}, {'type': 'r', 'name': 'igraph', 'version': '2.0.3'}, {'type': 'r', 'name': 'GeneNet', 'version': '1.2.16'}, {'type': 'r', 'name': 'ape', 'version': '5.8'}, {'type': 'r', 'name': 'RJSONIO', 'version': '1.3-1.9'}, {'type': 'r', 'name': 'caTools', 'version': '1.18.2'}, {'type': 'r', 'name': 'gplots', 'version': '3.1.3.1'}, {'type': 'r', 'name': 'ROCR', 'version': '1.0-11'}, {'type': 'r', 'name': 'rjson', 'version': '0.2.21'}, {'type': 'r', 'name': 'seqinr', 'version': '4.2-36'}, {'type': 'r', 'name': 'LearnBayes', 'version': '2.15.1'}, {'type': 'r', 'name': 'gmodels', 'version': '2.19.1'}, {'type': 'r', 'name': 'expm', 'version': '0.999-9'}, {'type': 'r', 'name': 'terra', 'version': '1.7-78'}, {'type': 'r', 'name': 'raster', 'version': '3.6-26'}, {'type': 'r', 'name': 'spData', 'version': '2.3.1'}, {'type': 'r', 'name': 'units', 'version': '0.8-5'}, {'type': 'r', 'name': 'classInt', 'version': '0.4-10'}, {'type': 'r', 'name': 'vegan', 'version': '2.6-6.1'}, {'type': 'r', 'name': 'rncl', 'version': '0.8.7'}, {'type': 'r', 'name': 'XML', 'version': '3.99-0.16.1'}, {'type': 'r', 'name': 'reshape', 'version': '0.8.9'}, {'type': 'r', 'name': 'triebeard', 'version': '0.4.1'}, {'type': 'r', 'name': 'urltools', 'version': '1.7.3'}, {'type': 'r', 'name': 'httpcode', 'version': '0.3.0'}, {'type': 'r', 'name': 'crul', 'version': '1.4.2'}, {'type': 'r', 'name': 'bold', 'version': '1.3.0'}, {'type': 'r', 'name': 'rredlist', 'version': '0.7.1'}, {'type': 'r', 'name': 'rentrez', 'version': '1.2.3'}, {'type': 'r', 'name': 'rotl', 'version': '3.1.0'}, {'type': 'r', 'name': 'solrium', 'version': '1.2.0'}, {'type': 'r', 'name': 'ritis', 'version': '1.0.0'}, {'type': 'r', 'name': 'worrms', 'version': '0.4.3'}, {'type': 'r', 'name': 'natserv', 'version': '1.0.0'}, {'type': 'r', 'name': 'WikipediR', 'version': '1.7.1'}, {'type': 'r', 'name': 'ratelimitr', 'version': '0.4.1'}, {'type': 'r', 'name': 'rex', 'version': '1.2.1'}, {'type': 'r', 'name': 'WikidataQueryServiceR', 'version': '1.0.0'}, {'type': 'r', 'name': 'pbapply', 'version': '1.7-2'}, {'type': 'r', 'name': 'WikidataR', 'version': '2.3.3'}, {'type': 'r', 'name': 'wikitaxa', 'version': '0.4.0'}, {'type': 'r', 'name': 'phangorn', 'version': '2.11.1'}, {'type': 'r', 'name': 'uuid', 'version': '1.2-0'}, {'type': 'r', 'name': 'conditionz', 'version': '0.1.0'}, {'type': 'r', 'name': 'taxize', 'version': '0.9.100'}, {'type': 'r', 'name': 'RNeXML', 'version': '2.4.11'}, {'type': 'r', 'name': 'phylobase', 'version': '0.8.12'}, {'type': 'r', 'name': 'magick', 'version': '2.8.3'}, {'type': 'r', 'name': 'animation', 'version': '2.7'}, {'type': 'r', 'name': 'bigmemory.sri', 'version': '0.1.8'}, {'type': 'r', 'name': 'bigmemory', 'version': '4.6.4'}, {'type': 'r', 'name': 'calibrate', 'version': '1.7.7'}, {'type': 'r', 'name': 'clusterGeneration', 'version': '1.3.8'}, {'type': 'r', 'name': 'dismo', 'version': '1.3-14'}, {'type': 'r', 'name': 'extrafontdb', 'version': '1.0'}, {'type': 'r', 'name': 'Rttf2pt1', 'version': '1.3.12'}, {'type': 'r', 'name': 'extrafont', 'version': '0.19'}, {'type': 'r', 'name': 'fields', 'version': '15.2'}, {'type': 'r', 'name': 'shapefiles', 'version': '0.7.2'}, {'type': 'r', 'name': 'fossil', 'version': '0.4.0'}, {'type': 'r', 'name': 'optimParallel', 'version': '1.0-2'}, {'type': 'r', 'name': 'DEoptim', 'version': '2.2-8'}, {'type': 'r', 'name': 'phytools', 'version': '2.3-0'}, {'type': 'r', 'name': 'geiger', 'version': '2.0.11'}, {'type': 'r', 'name': 'webshot', 'version': '0.5.5'}, {'type': 'r', 'name': 'shinyjs', 'version': '2.1.0'}, {'type': 'r', 'name': 'manipulateWidget', 'version': '0.11.1'}, {'type': 'r', 'name': 'rgl', 'version': '1.3.1'}, {'type': 'r', 'name': 'Rtsne', 'version': '0.17'}, {'type': 'r', 'name': 'labdsv', 'version': '2.1-0'}, {'type': 'r', 'name': 'stabs', 'version': '0.6-4'}, {'type': 'r', 'name': 'modeltools', 'version': '0.2-23'}, {'type': 'r', 'name': 'strucchange', 'version': '1.5-3'}, {'type': 'r', 'name': 'TH.data', 'version': '1.1-2'}, {'type': 'r', 'name': 'multcomp', 'version': '1.4-25'}, {'type': 'r', 'name': 'libcoin', 'version': '1.0-10'}, {'type': 'r', 'name': 'coin', 'version': '1.4-3'}, {'type': 'r', 'name': 'party', 'version': '1.3-15'}, {'type': 'r', 'name': 'inum', 'version': '1.0-5'}, {'type': 'r', 'name': 'partykit', 'version': '1.2-20'}, {'type': 'r', 'name': 'mboost', 'version': '2.9-10'}, {'type': 'r', 'name': 'msm', 'version': '1.7.1'}, {'type': 'r', 'name': 'nor1mix', 'version': '1.3-3'}, {'type': 'r', 'name': 'np', 'version': '0.60-17'}, {'type': 'r', 'name': 'polynom', 'version': '1.4-1'}, {'type': 'r', 'name': 'polspline', 'version': '1.1.25'}, {'type': 'r', 'name': 'rms', 'version': '6.8-1'}, {'type': 'r', 'name': 'RWekajars', 'version': '3.9.3-2'}, {'type': 'r', 'name': 'RWeka', 'version': '0.4-46'}, {'type': 'r', 'name': 'slam', 'version': '0.1-50'}, {'type': 'r', 'name': 'tm', 'version': '0.7-13'}, {'type': 'r', 'name': 'leaps', 'version': '3.2'}, {'type': 'r', 'name': 'cNORM', 'version': '3.0.4'}, {'type': 'r', 'name': 'weights', 'version': '1.0.4'}, {'type': 'r', 'name': 'TraMineR', 'version': '2.2-10'}, {'type': 'r', 'name': 'chemometrics', 'version': '1.4.4'}, {'type': 'r', 'name': 'FNN', 'version': '1.1.4'}, {'type': 'r', 'name': 'miscTools', 'version': '0.6-28'}, {'type': 'r', 'name': 'maxLik', 'version': '1.5-2.1'}, {'type': 'r', 'name': 'gbRd', 'version': '0.4.12'}, {'type': 'r', 'name': 'rbibutils', 'version': '2.2.16'}, {'type': 'r', 'name': 'Rdpack', 'version': '2.6'}, {'type': 'r', 'name': 'dfidx', 'version': '0.0-5'}, {'type': 'r', 'name': 'mlogit', 'version': '1.1-1'}, {'type': 'r', 'name': 'getopt', 'version': '1.20.4'}, {'type': 'r', 'name': 'gsalib', 'version': '2.2.1'}, {'type': 'r', 'name': 'optparse', 'version': '1.7.5'}, {'type': 'r', 'name': 'labelled', 'version': '2.13.0'}, {'type': 'r', 'name': 'R.cache', 'version': '0.16.0'}, {'type': 'r', 'name': 'styler', 'version': '1.10.3'}, {'type': 'r', 'name': 'questionr', 'version': '0.7.8'}, {'type': 'r', 'name': 'klaR', 'version': '1.7-3'}, {'type': 'r', 'name': 'neuRosim', 'version': '0.2-14'}, {'type': 'r', 'name': 'locfit', 'version': '1.5-9.10'}, {'type': 'r', 'name': 'patchwork', 'version': '1.2.0'}, {'type': 'r', 'name': 'broom.helpers', 'version': '1.15.0'}, {'type': 'r', 'name': 'ggstats', 'version': '0.6.0'}, {'type': 'r', 'name': 'GGally', 'version': '2.2.1'}, {'type': 'r', 'name': 'beanplot', 'version': '1.3.1'}, {'type': 'r', 'name': 'clValid', 'version': '0.7'}, {'type': 'r', 'name': 'DiscriMiner', 'version': '0.1-29'}, {'type': 'r', 'name': 'ellipse', 'version': '0.5.0'}, {'type': 'r', 'name': 'pbkrtest', 'version': '0.5.2'}, {'type': 'r', 'name': 'carData', 'version': '3.0-5'}, {'type': 'r', 'name': 'maptools', 'version': '1.1-8'}, {'type': 'r', 'name': 'openxlsx', 'version': '4.2.5.2'}, {'type': 'r', 'name': 'rematch', 'version': '2.0.0'}, {'type': 'r', 'name': 'cellranger', 'version': '1.1.0'}, {'type': 'r', 'name': 'readxl', 'version': '1.4.3'}, {'type': 'r', 'name': 'writexl', 'version': '1.5.0'}, {'type': 'r', 'name': 'rio', 'version': '1.1.1'}, {'type': 'r', 'name': 'car', 'version': '3.1-2'}, {'type': 'r', 'name': 'flashClust', 'version': '1.01-2'}, {'type': 'r', 'name': 'ggrepel', 'version': '0.9.5'}, {'type': 'r', 'name': 'DT', 'version': '0.33'}, {'type': 'r', 'name': 'estimability', 'version': '1.5.1'}, {'type': 'r', 'name': 'emmeans', 'version': '1.10.2'}, {'type': 'r', 'name': 'multcompView', 'version': '0.1-10'}, {'type': 'r', 'name': 'FactoMineR', 'version': '2.11'}, {'type': 'r', 'name': 'flexclust', 'version': '1.4-2'}, {'type': 'r', 'name': 'flexmix', 'version': '2.3-19'}, {'type': 'r', 'name': 'prabclus', 'version': '2.3-3'}, {'type': 'r', 'name': 'diptest', 'version': '0.77-1'}, {'type': 'r', 'name': 'trimcluster', 'version': '0.1-5'}, {'type': 'r', 'name': 'fpc', 'version': '2.2-12'}, {'type': 'r', 'name': 'BiasedUrn', 'version': '2.0.12'}, {'type': 'r', 'name': 'TeachingDemos', 'version': '2.13'}, {'type': 'r', 'name': 'kohonen', 'version': '3.0.12'}, {'type': 'r', 'name': 'base64', 'version': '2.0.1'}, {'type': 'r', 'name': 'doRNG', 'version': '1.8.6'}, {'type': 'r', 'name': 'nleqslv', 'version': '3.3.5'}, {'type': 'r', 'name': 'Deriv', 'version': '4.1.3'}, {'type': 'r', 'name': 'RGCCA', 'version': '3.0.3'}, {'type': 'r', 'name': 'pheatmap', 'version': '1.0.12'}, {'type': 'r', 'name': 'pvclust', 'version': '2.2-0'}, {'type': 'r', 'name': 'RCircos', 'version': '1.2.2'}, {'type': 'r', 'name': 'lambda.r', 'version': '1.2.4'}, {'type': 'r', 'name': 'futile.options', 'version': '1.0.1'}, {'type': 'r', 'name': 'futile.logger', 'version': '1.4.3'}, {'type': 'r', 'name': 'VennDiagram', 'version': '1.7.3'}, {'type': 'r', 'name': 'xlsxjars', 'version': '0.6.1'}, {'type': 'r', 'name': 'xlsx', 'version': '0.6.5'}, {'type': 'r', 'name': 'uroot', 'version': '2.1-3'}, {'type': 'r', 'name': 'forecast', 'version': '8.23.0'}, {'type': 'r', 'name': 'fma', 'version': '2.5'}, {'type': 'r', 'name': 'expsmooth', 'version': '2.3'}, {'type': 'r', 'name': 'fpp', 'version': '0.5'}, {'type': 'r', 'name': 'tensor', 'version': '1.5'}, {'type': 'r', 'name': 'polyclip', 'version': '1.10-6'}, {'type': 'r', 'name': 'goftest', 'version': '1.2-3'}, {'type': 'r', 'name': 'spatstat.utils', 'version': '3.0-5'}, {'type': 'r', 'name': 'spatstat.data', 'version': '3.1-2'}, {'type': 'r', 'name': 'spatstat.geom', 'version': '3.2-9'}, {'type': 'r', 'name': 'spatstat.sparse', 'version': '3.1-0'}, {'type': 'r', 'name': 'spatstat.random', 'version': '3.2-3'}, {'type': 'r', 'name': 'spatstat.core', 'version': '2.4-4'}, {'type': 'r', 'name': 'spatstat.explore', 'version': '3.2-7'}, {'type': 'r', 'name': 'spatstat.model', 'version': '3.2-11'}, {'type': 'r', 'name': 'spatstat.linnet', 'version': '3.1-5'}, {'type': 'r', 'name': 'spatstat', 'version': '3.0-8'}, {'type': 'r', 'name': 'pracma', 'version': '2.4.4'}, {'type': 'r', 'name': 'RCurl', 'version': '1.98-1.14'}, {'type': 'r', 'name': 'bio3d', 'version': '2.4-4'}, {'type': 'r', 'name': 'AUC', 'version': '0.3.2'}, {'type': 'r', 'name': 'interpretR', 'version': '0.2.5'}, {'type': 'r', 'name': 'cvAUC', 'version': '1.1.4'}, {'type': 'r', 'name': 'SuperLearner', 'version': '2.0-29'}, {'type': 'r', 'name': 'mediation', 'version': '4.5.0'}, {'type': 'r', 'name': 'CVST', 'version': '0.2-3'}, {'type': 'r', 'name': 'DRR', 'version': '0.0.4'}, {'type': 'r', 'name': 'dimRed', 'version': '0.2.6'}, {'type': 'r', 'name': 'ddalpha', 'version': '1.3.15'}, {'type': 'r', 'name': 'RcppRoll', 'version': '0.3.0'}, {'type': 'r', 'name': 'rlist', 'version': '0.4.6.2'}, {'type': 'r', 'name': 'ConsRank', 'version': '2.1.4'}, {'type': 'r', 'name': 'adabag', 'version': '5.0'}, {'type': 'r', 'name': 'parallelMap', 'version': '1.5.1'}, {'type': 'r', 'name': 'ParamHelpers', 'version': '1.14.1'}, {'type': 'r', 'name': 'ggvis', 'version': '0.4.9'}, {'type': 'r', 'name': 'mlr', 'version': '2.19.2'}, {'type': 'r', 'name': 'unbalanced', 'version': '2.0'}, {'type': 'r', 'name': 'RSNNS', 'version': '0.4-17'}, {'type': 'r', 'name': 'abc.data', 'version': '1.1'}, {'type': 'r', 'name': 'abc', 'version': '2.2.1'}, {'type': 'r', 'name': 'lhs', 'version': '1.1.6'}, {'type': 'r', 'name': 'tensorA', 'version': '0.36.2.1'}, {'type': 'r', 'name': 'EasyABC', 'version': '1.5.2'}, {'type': 'r', 'name': 'git2r', 'version': '0.33.0'}, {'type': 'r', 'name': 'clisymbols', 'version': '1.2.0'}, {'type': 'r', 'name': 'covr', 'version': '3.6.4'}, {'type': 'r', 'name': 'Rook', 'version': '1.2'}, {'type': 'r', 'name': 'Cairo', 'version': '1.6-2'}, {'type': 'r', 'name': 'RMTstat', 'version': '0.3.1'}, {'type': 'r', 'name': 'Lmoments', 'version': '1.3-1'}, {'type': 'r', 'name': 'distillery', 'version': '1.2-1'}, {'type': 'r', 'name': 'extRemes', 'version': '2.1-4'}, {'type': 'r', 'name': 'tkrplot', 'version': '0.0-27'}, {'type': 'r', 'name': 'misc3d', 'version': '0.9-1'}, {'type': 'r', 'name': 'multicool', 'version': '1.0.1'}, {'type': 'r', 'name': 'plot3D', 'version': '1.4.1'}, {'type': 'r', 'name': 'plot3Drgl', 'version': '1.0.4'}, {'type': 'r', 'name': 'OceanView', 'version': '1.0.7'}, {'type': 'r', 'name': 'ks', 'version': '1.14.2'}, {'type': 'r', 'name': 'logcondens', 'version': '2.1.8'}, {'type': 'r', 'name': 'Iso', 'version': '0.0-21'}, {'type': 'r', 'name': 'penalized', 'version': '0.9-52'}, {'type': 'r', 'name': 'clusterRepro', 'version': '0.9'}, {'type': 'r', 'name': 'data.tree', 'version': '1.1.0'}, {'type': 'r', 'name': 'influenceR', 'version': '0.1.5'}, {'type': 'r', 'name': 'visNetwork', 'version': '2.1.2'}, {'type': 'r', 'name': 'downloader', 'version': '0.4'}, {'type': 'r', 'name': 'DiagrammeR', 'version': '1.0.11'}, {'type': 'r', 'name': 'randomForestSRC', 'version': '3.2.3'}, {'type': 'r', 'name': 'sm', 'version': '2.2-6.0'}, {'type': 'r', 'name': 'pbivnorm', 'version': '0.6.0'}, {'type': 'r', 'name': 'lavaan', 'version': '0.6-18'}, {'type': 'r', 'name': 'matrixcalc', 'version': '1.0-6'}, {'type': 'r', 'name': 'arm', 'version': '1.14-4'}, {'type': 'r', 'name': 'mi', 'version': '1.1'}, {'type': 'r', 'name': 'servr', 'version': '0.30'}, {'type': 'r', 'name': 'rgexf', 'version': '0.16.2'}, {'type': 'r', 'name': 'sem', 'version': '3.1-15'}, {'type': 'r', 'name': 'statnet.common', 'version': '4.9.0'}, {'type': 'r', 'name': 'network', 'version': '1.18.2'}, {'type': 'r', 'name': 'rle', 'version': '0.9.2'}, {'type': 'r', 'name': 'sna', 'version': '2.7-2'}, {'type': 'r', 'name': 'glasso', 'version': '1.11'}, {'type': 'r', 'name': 'huge', 'version': '1.3.5'}, {'type': 'r', 'name': 'd3Network', 'version': '0.5.2.1'}, {'type': 'r', 'name': 'BDgraph', 'version': '2.72'}, {'type': 'r', 'name': 'graphlayouts', 'version': '1.1.1'}, {'type': 'r', 'name': 'tweenr', 'version': '2.0.3'}, {'type': 'r', 'name': 'ggforce', 'version': '0.4.2'}, {'type': 'r', 'name': 'tidygraph', 'version': '1.3.1'}, {'type': 'r', 'name': 'ggraph', 'version': '2.2.1'}, {'type': 'r', 'name': 'qgraph', 'version': '1.9.8'}, {'type': 'r', 'name': 'HWxtest', 'version': '1.1.9'}, {'type': 'r', 'name': 'diveRsity', 'version': '1.9.90'}, {'type': 'r', 'name': 'doSNOW', 'version': '1.0.20'}, {'type': 'r', 'name': 'geepack', 'version': '1.3.11'}, {'type': 'r', 'name': 'biom', 'version': '0.3.12'}, {'type': 'r', 'name': 'pim', 'version': '2.0.2'}, {'type': 'r', 'name': 'minpack.lm', 'version': '1.2-4'}, {'type': 'r', 'name': 'rootSolve', 'version': '1.8.2.4'}, {'type': 'r', 'name': 'FME', 'version': '1.3.6.3'}, {'type': 'r', 'name': 'bmp', 'version': '0.3'}, {'type': 'r', 'name': 'tiff', 'version': '0.1-12'}, {'type': 'r', 'name': 'readbitmap', 'version': '0.1.5'}, {'type': 'r', 'name': 'imager', 'version': '1.0.2'}, {'type': 'r', 'name': 'signal', 'version': '1.8-0'}, {'type': 'r', 'name': 'tuneR', 'version': '1.4.7'}, {'type': 'r', 'name': 'pastecs', 'version': '1.4.2'}, {'type': 'r', 'name': 'audio', 'version': '0.1-11'}, {'type': 'r', 'name': 'fftw', 'version': '1.0-8'}, {'type': 'r', 'name': 'seewave', 'version': '2.2.3'}, {'type': 'r', 'name': 'gsw', 'version': '1.1-1'}, {'type': 'r', 'name': 'wk', 'version': '0.9.1'}, {'type': 'r', 'name': 's2', 'version': '1.1.6'}, {'type': 'r', 'name': 'sf', 'version': '1.0-16'}, {'type': 'r', 'name': 'oce', 'version': '1.8-2'}, {'type': 'r', 'name': 'ineq', 'version': '0.2-13'}, {'type': 'r', 'name': 'soundecology', 'version': '1.3.3'}, {'type': 'r', 'name': 'memuse', 'version': '4.2-3'}, {'type': 'r', 'name': 'pinfsc50', 'version': '1.3.0'}, {'type': 'r', 'name': 'vcfR', 'version': '1.15.0'}, {'type': 'r', 'name': 'glmmML', 'version': '1.1.6'}, {'type': 'r', 'name': 'cowplot', 'version': '1.1.3'}, {'type': 'r', 'name': 'tsne', 'version': '0.1-3.1'}, {'type': 'r', 'name': 'sn', 'version': '2.1.1'}, {'type': 'r', 'name': 'tclust', 'version': '2.0-4'}, {'type': 'r', 'name': 'ranger', 'version': '0.16.0'}, {'type': 'r', 'name': 'hexbin', 'version': '1.28.3'}, {'type': 'r', 'name': 'lobstr', 'version': '1.1.2'}, {'type': 'r', 'name': 'pryr', 'version': '0.1.6'}, {'type': 'r', 'name': 'moments', 'version': '0.14.1'}, {'type': 'r', 'name': 'laeken', 'version': '0.5.3'}, {'type': 'r', 'name': 'VIM', 'version': '6.2.2'}, {'type': 'r', 'name': 'smoother', 'version': '1.3'}, {'type': 'r', 'name': 'dynamicTreeCut', 'version': '1.63-1'}, {'type': 'r', 'name': 'beeswarm', 'version': '0.4.0'}, {'type': 'r', 'name': 'vipor', 'version': '0.4.7'}, {'type': 'r', 'name': 'ggbeeswarm', 'version': '0.7.2'}, {'type': 'r', 'name': 'shinydashboard', 'version': '0.7.2'}, {'type': 'r', 'name': 'rrcov', 'version': '1.7-5'}, {'type': 'r', 'name': 'WriteXLS', 'version': '6.6.0'}, {'type': 'r', 'name': 'bst', 'version': '0.3-24'}, {'type': 'r', 'name': 'pamr', 'version': '1.56.2'}, {'type': 'r', 'name': 'WeightSVM', 'version': '1.7-13'}, {'type': 'r', 'name': 'mpath', 'version': '0.4-2.25'}, {'type': 'r', 'name': 'timereg', 'version': '2.0.5'}, {'type': 'r', 'name': 'peperr', 'version': '1.5'}, {'type': 'r', 'name': 'heatmap3', 'version': '1.1.9'}, {'type': 'r', 'name': 'GlobalOptions', 'version': '0.1.2'}, {'type': 'r', 'name': 'circlize', 'version': '0.4.16'}, {'type': 'r', 'name': 'GetoptLong', 'version': '1.0.5'}, {'type': 'r', 'name': 'dendextend', 'version': '1.17.1'}, {'type': 'r', 'name': 'RInside', 'version': '0.2.18'}, {'type': 'r', 'name': 'limSolve', 'version': '1.5.7.1'}, {'type': 'r', 'name': 'dbplyr', 'version': '2.5.0'}, {'type': 'r', 'name': 'modelr', 'version': '0.1.11'}, {'type': 'r', 'name': 'debugme', 'version': '1.2.0'}, {'type': 'r', 'name': 'reprex', 'version': '2.1.0'}, {'type': 'r', 'name': 'selectr', 'version': '0.4-2'}, {'type': 'r', 'name': 'rvest', 'version': '1.0.4'}, {'type': 'r', 'name': 'dtplyr', 'version': '1.3.1'}, {'type': 'r', 'name': 'gargle', 'version': '1.5.2'}, {'type': 'r', 'name': 'googledrive', 'version': '2.1.1'}, {'type': 'r', 'name': 'ids', 'version': '1.0.1'}, {'type': 'r', 'name': 'googlesheets4', 'version': '1.1.1'}, {'type': 'r', 'name': 'conflicted', 'version': '1.2.0'}, {'type': 'r', 'name': 'tidyverse', 'version': '2.0.0'}, {'type': 'r', 'name': 'R.rsp', 'version': '0.46.0'}, {'type': 'r', 'name': 'gdistance', 'version': '1.6.4'}, {'type': 'r', 'name': 'vioplot', 'version': '0.4.0'}, {'type': 'r', 'name': 'emulator', 'version': '1.2-24'}, {'type': 'r', 'name': 'gmm', 'version': '1.8'}, {'type': 'r', 'name': 'tmvtnorm', 'version': '1.6'}, {'type': 'r', 'name': 'IDPmisc', 'version': '1.1.21'}, {'type': 'r', 'name': 'gap.datasets', 'version': '0.0.6'}, {'type': 'r', 'name': 'gap', 'version': '1.5-3'}, {'type': 'r', 'name': 'qrnn', 'version': '2.1.1'}, {'type': 'r', 'name': 'TMB', 'version': '1.9.12'}, {'type': 'r', 'name': 'glmmTMB', 'version': '1.1.9'}, {'type': 'r', 'name': 'gmp', 'version': '0.7-4'}, {'type': 'r', 'name': 'ROI', 'version': '1.0-1'}, {'type': 'r', 'name': 'Rglpk', 'version': '0.6-5.1'}, {'type': 'r', 'name': 'ROI.plugin.glpk', 'version': '1.0-0'}, {'type': 'r', 'name': 'spaMM', 'version': '4.5.0'}, {'type': 'r', 'name': 'qgam', 'version': '1.3.4'}, {'type': 'r', 'name': 'DHARMa', 'version': '0.4.6'}, {'type': 'r', 'name': 'mvnfast', 'version': '0.2.8'}, {'type': 'r', 'name': 'bridgesampling', 'version': '1.1-2'}, {'type': 'r', 'name': 'BayesianTools', 'version': '0.1.8'}, {'type': 'r', 'name': 'gomms', 'version': '1.0'}, {'type': 'r', 'name': 'feather', 'version': '0.3.5'}, {'type': 'r', 'name': 'dummies', 'version': '1.5.6'}, {'type': 'r', 'name': 'SimSeq', 'version': '1.4.0'}, {'type': 'r', 'name': 'uniqueAtomMat', 'version': '0.1-3-2'}, {'type': 'r', 'name': 'PoissonSeq', 'version': '1.1.2'}, {'type': 'r', 'name': 'aod', 'version': '1.3.3'}, {'type': 'r', 'name': 'cghFLasso', 'version': '0.2-1'}, {'type': 'r', 'name': 'svd', 'version': '0.5.5'}, {'type': 'r', 'name': 'Rssa', 'version': '1.0.5'}, {'type': 'r', 'name': 'JBTools', 'version': '0.7.2.9'}, {'type': 'r', 'name': 'RUnit', 'version': '0.4.33'}, {'type': 'r', 'name': 'DistributionUtils', 'version': '0.6-1'}, {'type': 'r', 'name': 'gapfill', 'version': '0.9.6-1'}, {'type': 'r', 'name': 'gee', 'version': '4.13-27'}, {'type': 'r', 'name': 'Matching', 'version': '4.10-14'}, {'type': 'r', 'name': 'chk', 'version': '0.9.1'}, {'type': 'r', 'name': 'MatchIt', 'version': '4.5.5'}, {'type': 'r', 'name': 'RItools', 'version': '0.3-4'}, {'type': 'r', 'name': 'mitools', 'version': '2.4'}, {'type': 'r', 'name': 'survey', 'version': '4.4-2'}, {'type': 'r', 'name': 'rlemon', 'version': '0.2.1'}, {'type': 'r', 'name': 'optmatch', 'version': '0.10.7'}, {'type': 'r', 'name': 'SPAtest', 'version': '3.1.2'}, {'type': 'r', 'name': 'RSpectra', 'version': '0.16-1'}, {'type': 'r', 'name': 'SKAT', 'version': '2.2.5'}, {'type': 'r', 'name': 'GillespieSSA', 'version': '0.6.2'}, {'type': 'r', 'name': 'startupmsg', 'version': '0.9.6.1'}, {'type': 'r', 'name': 'distr', 'version': '2.9.3'}, {'type': 'r', 'name': 'distrEx', 'version': '2.9.2'}, {'type': 'r', 'name': 'minerva', 'version': '1.5.10'}, {'type': 'r', 'name': 'RcppTOML', 'version': '0.2.2'}, {'type': 'r', 'name': 'here', 'version': '1.0.1'}, {'type': 'r', 'name': 'reticulate', 'version': '1.38.0'}, {'type': 'r', 'name': 'umap', 'version': '0.2.10.0'}, {'type': 'r', 'name': 'KODAMA', 'version': '2.4'}, {'type': 'r', 'name': 'locfdr', 'version': '1.1-8'}, {'type': 'r', 'name': 'ica', 'version': '1.0-3'}, {'type': 'r', 'name': 'dtw', 'version': '1.23-1'}, {'type': 'r', 'name': 'SDMTools', 'version': '1.1-221.2'}, {'type': 'r', 'name': 'ggridges', 'version': '0.5.6'}, {'type': 'r', 'name': 'TFisher', 'version': '0.2.0'}, {'type': 'r', 'name': 'lsei', 'version': '1.3-0'}, {'type': 'r', 'name': 'npsurv', 'version': '0.5-0'}, {'type': 'r', 'name': 'fitdistrplus', 'version': '1.1-11'}, {'type': 'r', 'name': 'hdf5r', 'version': '1.3.10'}, {'type': 'r', 'name': 'DTRreg', 'version': '2.2'}, {'type': 'r', 'name': 'pulsar', 'version': '0.3.11'}, {'type': 'r', 'name': 'bayesm', 'version': '3.1-6'}, {'type': 'r', 'name': 'gsl', 'version': '2.1-8'}, {'type': 'r', 'name': 'energy', 'version': '1.7-11'}, {'type': 'r', 'name': 'compositions', 'version': '2.0-8'}, {'type': 'r', 'name': 'clustree', 'version': '0.5.1'}, {'type': 'r', 'name': 'tweedie', 'version': '2.3.5'}, {'type': 'r', 'name': 'RcppGSL', 'version': '0.3.13'}, {'type': 'r', 'name': 'mvabund', 'version': '4.2.1'}, {'type': 'r', 'name': 'fishMod', 'version': '0.29'}, {'type': 'r', 'name': 'alabama', 'version': '2023.1.0'}, {'type': 'r', 'name': 'gllvm', 'version': '1.4.3'}, {'type': 'r', 'name': 'grpreg', 'version': '3.4.0'}, {'type': 'r', 'name': 'trust', 'version': '0.1-8'}, {'type': 'r', 'name': 'lpSolveAPI', 'version': '5.5.2.0-17.11'}, {'type': 'r', 'name': 'ergm', 'version': '4.6.0'}, {'type': 'r', 'name': 'networkLite', 'version': '1.0.5'}, {'type': 'r', 'name': 'networkDynamic', 'version': '0.11.4'}, {'type': 'r', 'name': 'ergm.multi', 'version': '0.2.1'}, {'type': 'r', 'name': 'tergm', 'version': '4.2.0'}, {'type': 'r', 'name': 'ergm.count', 'version': '4.1.2'}, {'type': 'r', 'name': 'tsna', 'version': '0.3.5'}, {'type': 'r', 'name': 'statnet', 'version': '2019.6'}, {'type': 'r', 'name': 'aggregation', 'version': '1.0.1'}, {'type': 'r', 'name': 'ComICS', 'version': '1.0.4'}, {'type': 'r', 'name': 'dtangle', 'version': '2.0.9'}, {'type': 'r', 'name': 'mcmc', 'version': '0.9-8'}, {'type': 'r', 'name': 'MCMCpack', 'version': '1.7-0'}, {'type': 'r', 'name': 'shinythemes', 'version': '1.2.0'}, {'type': 'r', 'name': 'csSAM', 'version': '1.2.4'}, {'type': 'r', 'name': 'bridgedist', 'version': '0.1.2'}, {'type': 'r', 'name': 'asnipe', 'version': '1.1.17'}, {'type': 'r', 'name': 'liquidSVM', 'version': '1.2.4'}, {'type': 'r', 'name': 'oddsratio', 'version': '2.0.1'}, {'type': 'r', 'name': 'mltools', 'version': '0.3.5'}, {'type': 'r', 'name': 'h2o', 'version': '3.44.0.3'}, {'type': 'r', 'name': 'mlegp', 'version': '3.1.9'}, {'type': 'r', 'name': 'itertools', 'version': '0.1-3'}, {'type': 'r', 'name': 'missForest', 'version': '1.5'}, {'type': 'r', 'name': 'bartMachineJARs', 'version': '1.2.1'}, {'type': 'r', 'name': 'bartMachine', 'version': '1.3.4.1'}, {'type': 'r', 'name': 'lqa', 'version': '1.0-3'}, {'type': 'r', 'name': 'PresenceAbsence', 'version': '1.1.11'}, {'type': 'r', 'name': 'GUTS', 'version': '1.2.5'}, {'type': 'r', 'name': 'GenSA', 'version': '1.1.14'}, {'type': 'r', 'name': 'parsedate', 'version': '1.3.1'}, {'type': 'r', 'name': 'circular', 'version': '0.5-0'}, {'type': 'r', 'name': 'cobs', 'version': '1.3-8'}, {'type': 'r', 'name': 'resample', 'version': '0.6'}, {'type': 'r', 'name': 'MIIVsem', 'version': '0.5.8'}, {'type': 'r', 'name': 'medflex', 'version': '0.6-10'}, {'type': 'r', 'name': 'Rserve', 'version': '1.8-13'}, {'type': 'r', 'name': 'spls', 'version': '2.2-3'}, {'type': 'r', 'name': 'Boruta', 'version': '8.0.0'}, {'type': 'r', 'name': 'dr', 'version': '3.0.10'}, {'type': 'r', 'name': 'CovSel', 'version': '1.2.1'}, {'type': 'r', 'name': 'tmle', 'version': '2.0.1.1'}, {'type': 'r', 'name': 'ctmle', 'version': '0.1.2'}, {'type': 'r', 'name': 'BayesPen', 'version': '1.0'}, {'type': 'r', 'name': 'inline', 'version': '0.3.19'}, {'type': 'r', 'name': 'BMA', 'version': '3.18.17'}, {'type': 'r', 'name': 'BCEE', 'version': '1.3.2'}, {'type': 'r', 'name': 'bacr', 'version': '1.0.1'}, {'type': 'r', 'name': 'clue', 'version': '0.3-65'}, {'type': 'r', 'name': 'bdsmatrix', 'version': '1.3-7'}, {'type': 'r', 'name': 'fftwtools', 'version': '0.9-11'}, {'type': 'r', 'name': 'imagerExtra', 'version': '1.3.2'}, {'type': 'r', 'name': 'MALDIquant', 'version': '1.22.2'}, {'type': 'r', 'name': 'threejs', 'version': '0.3.3'}, {'type': 'r', 'name': 'LaplacesDemon', 'version': '16.1.6'}, {'type': 'r', 'name': 'rda', 'version': '1.2-1'}, {'type': 'r', 'name': 'sampling', 'version': '2.10'}, {'type': 'r', 'name': 'lda', 'version': '1.5.2'}, {'type': 'r', 'name': 'jiebaRD', 'version': '0.1'}, {'type': 'r', 'name': 'jiebaR', 'version': '0.11'}, {'type': 'r', 'name': 'hdm', 'version': '0.3.2'}, {'type': 'r', 'name': 'abe', 'version': '3.0.1'}, {'type': 'r', 'name': 'SignifReg', 'version': '4.3'}, {'type': 'r', 'name': 'bbmle', 'version': '1.0.25.1'}, {'type': 'r', 'name': 'emdbook', 'version': '1.3.13'}, {'type': 'r', 'name': 'SOAR', 'version': '0.99-11'}, {'type': 'r', 'name': 'rasterVis', 'version': '0.51.6'}, {'type': 'r', 'name': 'tictoc', 'version': '1.2.1'}, {'type': 'r', 'name': 'ISOcodes', 'version': '2024.02.12'}, {'type': 'r', 'name': 'stopwords', 'version': '2.3'}, {'type': 'r', 'name': 'janeaustenr', 'version': '1.0.0'}, {'type': 'r', 'name': 'SnowballC', 'version': '0.7.1'}, {'type': 'r', 'name': 'tokenizers', 'version': '0.3.0'}, {'type': 'r', 'name': 'hunspell', 'version': '3.0.3'}, {'type': 'r', 'name': 'topicmodels', 'version': '0.2-16'}, {'type': 'r', 'name': 'tidytext', 'version': '0.4.2'}, {'type': 'r', 'name': 'splitstackshape', 'version': '1.4.8'}, {'type': 'r', 'name': 'grImport2', 'version': '0.3-1'}, {'type': 'r', 'name': 'preseqR', 'version': '4.0.0'}, {'type': 'r', 'name': 'idr', 'version': '1.3'}, {'type': 'r', 'name': 'entropy', 'version': '1.3.1'}, {'type': 'r', 'name': 'kedd', 'version': '1.0.4'}, {'type': 'r', 'name': 'HiddenMarkov', 'version': '1.8-13'}, {'type': 'r', 'name': 'lmerTest', 'version': '3.1-3'}, {'type': 'r', 'name': 'distributional', 'version': '0.4.0'}, {'type': 'r', 'name': 'posterior', 'version': '1.5.0'}, {'type': 'r', 'name': 'loo', 'version': '2.7.0'}, {'type': 'r', 'name': 'RcppParallel', 'version': '5.1.7'}, {'type': 'r', 'name': 'StanHeaders', 'version': '2.32.9'}, {'type': 'r', 'name': 'V8', 'version': '4.4.2'}, {'type': 'r', 'name': 'QuickJSR', 'version': '1.2.2'}, {'type': 'r', 'name': 'rstan', 'version': '2.32.6'}, {'type': 'r', 'name': 'Rborist', 'version': '0.3-7'}, {'type': 'r', 'name': 'VSURF', 'version': '1.2.0'}, {'type': 'r', 'name': 'mRMRe', 'version': '2.1.2.1'}, {'type': 'r', 'name': 'dHSIC', 'version': '2.1'}, {'type': 'r', 'name': 'ggsci', 'version': '3.2.0'}, {'type': 'r', 'name': 'ggsignif', 'version': '0.6.4'}, {'type': 'r', 'name': 'corrplot', 'version': '0.92'}, {'type': 'r', 'name': 'rstatix', 'version': '0.7.2'}, {'type': 'r', 'name': 'ggfan', 'version': '0.1.3'}, {'type': 'r', 'name': 'ggpubr', 'version': '0.6.0'}, {'type': 'r', 'name': 'yaImpute', 'version': '1.0-34'}, {'type': 'r', 'name': 'intrinsicDimension', 'version': '1.2.0'}, {'type': 'r', 'name': 'leiden', 'version': '0.4.3.1'}, {'type': 'r', 'name': 'sctransform', 'version': '0.4.1'}, {'type': 'r', 'name': 'packrat', 'version': '0.9.2'}, {'type': 'r', 'name': 'colourpicker', 'version': '1.3.0'}, {'type': 'r', 'name': 'ggExtra', 'version': '0.10.1'}, {'type': 'r', 'name': 'findpython', 'version': '1.0.8'}, {'type': 'r', 'name': 'argparse', 'version': '2.2.3'}, {'type': 'r', 'name': 'intergraph', 'version': '2.0-4'}, {'type': 'r', 'name': 'ggnetwork', 'version': '0.5.13'}, {'type': 'r', 'name': 'qqman', 'version': '0.1.9'}, {'type': 'r', 'name': 'rstantools', 'version': '2.4.0'}, {'type': 'r', 'name': 'bayesplot', 'version': '1.11.1'}, {'type': 'r', 'name': 'dygraphs', 'version': '1.1.1.6'}, {'type': 'r', 'name': 'renv', 'version': '1.0.7'}, {'type': 'r', 'name': 'PKI', 'version': '0.1-14'}, {'type': 'r', 'name': 'rsconnect', 'version': '1.3.1'}, {'type': 'r', 'name': 'shinystan', 'version': '2.6.0'}, {'type': 'r', 'name': 'optimx', 'version': '2023-10.21'}, {'type': 'r', 'name': 'gamm4', 'version': '0.2-6'}, {'type': 'r', 'name': 'memisc', 'version': '0.99.31.7'}, {'type': 'r', 'name': 'mclogit', 'version': '0.9.6'}, {'type': 'r', 'name': 'projpred', 'version': '2.8.0'}, {'type': 'r', 'name': 'brms', 'version': '2.21.0'}, {'type': 'r', 'name': 'drgee', 'version': '1.1.10'}, {'type': 'r', 'name': 'stdReg', 'version': '3.4.1'}, {'type': 'r', 'name': 'mcmcse', 'version': '1.5-0'}, {'type': 'r', 'name': 'copCAR', 'version': '2.0-4'}, {'type': 'r', 'name': 'batchmeans', 'version': '1.0-4'}, {'type': 'r', 'name': 'ngspatial', 'version': '1.2-2'}, {'type': 'r', 'name': 'BIGL', 'version': '1.9.1'}, {'type': 'r', 'name': 'drugCombo', 'version': '1.2.1'}, {'type': 'r', 'name': 'betareg', 'version': '3.1-4'}, {'type': 'r', 'name': 'unmarked', 'version': '1.4.1'}, {'type': 'r', 'name': 'maxlike', 'version': '0.1-11'}, {'type': 'r', 'name': 'coxme', 'version': '2.2-20'}, {'type': 'r', 'name': 'AICcmodavg', 'version': '2.3-3'}, {'type': 'r', 'name': 'pacman', 'version': '0.5.1'}, {'type': 'r', 'name': 'spaa', 'version': '0.2.2'}, {'type': 'r', 'name': 'maxnet', 'version': '0.1.4'}, {'type': 'r', 'name': 'oai', 'version': '0.4.0'}, {'type': 'r', 'name': 'wellknown', 'version': '0.7.4'}, {'type': 'r', 'name': 'rgbif', 'version': '3.8.0'}, {'type': 'r', 'name': 'rgdal', 'version': '1.6-7'}, {'type': 'r', 'name': 'rgeos', 'version': '0.6-4'}, {'type': 'r', 'name': 'mapproj', 'version': '1.2.11'}, {'type': 'r', 'name': 'rbison', 'version': '1.0.0'}, {'type': 'r', 'name': 'rebird', 'version': '1.3.0'}, {'type': 'r', 'name': 'rvertnet', 'version': '0.8.4'}, {'type': 'r', 'name': 'ridigbio', 'version': '0.3.8'}, {'type': 'r', 'name': 'spocc', 'version': '1.2.3'}, {'type': 'r', 'name': 'spThin', 'version': '0.2.0'}, {'type': 'r', 'name': 'RPostgreSQL', 'version': '0.7-6'}, {'type': 'r', 'name': 'fasterize', 'version': '1.0.5'}, {'type': 'r', 'name': 'BIEN', 'version': '1.2.6'}, {'type': 'r', 'name': 'rangeModelMetadata', 'version': '0.1.5'}, {'type': 'r', 'name': 'ENMeval', 'version': '2.0.4'}, {'type': 'r', 'name': 'plotmo', 'version': '3.6.3'}, {'type': 'r', 'name': 'earth', 'version': '5.3.3'}, {'type': 'r', 'name': 'mda', 'version': '0.5-4'}, {'type': 'r', 'name': 'xgboost', 'version': '1.7.7.1'}, {'type': 'r', 'name': 'biomod2', 'version': '4.2-5-2'}, {'type': 'r', 'name': 'poLCA', 'version': '1.6.0.1'}, {'type': 'r', 'name': 'PermAlgo', 'version': '1.2'}, {'type': 'r', 'name': 'coxed', 'version': '0.3.3'}, {'type': 'r', 'name': 'testit', 'version': '0.13'}, {'type': 'r', 'name': 'NISTunits', 'version': '1.0.1'}, {'type': 'r', 'name': 'celestial', 'version': '1.4.6'}, {'type': 'r', 'name': 'RPMM', 'version': '1.25'}, {'type': 'r', 'name': 'RefFreeEWAS', 'version': '2.2'}, {'type': 'r', 'name': 'wordcloud', 'version': '2.6'}, {'type': 'r', 'name': 'JADE', 'version': '2.0-4'}, {'type': 'r', 'name': 'awsMethods', 'version': '1.1-1'}, {'type': 'r', 'name': 'aws', 'version': '2.5-5'}, {'type': 'r', 'name': 'ruv', 'version': '0.9.7.1'}, {'type': 'r', 'name': 'mhsmm', 'version': '0.4.21'}, {'type': 'r', 'name': 'dbarts', 'version': '0.9-28'}, {'type': 'r', 'name': 'proftools', 'version': '0.99-3'}, {'type': 'r', 'name': 'NCmisc', 'version': '1.2.0'}, {'type': 'r', 'name': 'reader', 'version': '1.0.6'}, {'type': 'r', 'name': 'gnumeric', 'version': '0.7-10'}, {'type': 'r', 'name': 'tcltk2', 'version': '1.2-11'}, {'type': 'r', 'name': 'minty', 'version': '0.0.1'}, {'type': 'r', 'name': 'readODS', 'version': '2.3.0'}, {'type': 'r', 'name': 'nortest', 'version': '1.0-4'}, {'type': 'r', 'name': 'EnvStats', 'version': '2.8.1'}, {'type': 'r', 'name': 'outliers', 'version': '0.15'}, {'type': 'r', 'name': 'gWidgets2', 'version': '1.0-9'}, {'type': 'r', 'name': 'gWidgets2tcltk', 'version': '1.0-8'}, {'type': 'r', 'name': 'mgsub', 'version': '1.7.3'}, {'type': 'r', 'name': 'ie2misc', 'version': '0.9.1'}, {'type': 'r', 'name': 'assertive.base', 'version': '0.0-9'}, {'type': 'r', 'name': 'assertive.properties', 'version': '0.0-5'}, {'type': 'r', 'name': 'assertive.types', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.numbers', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.strings', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.datetimes', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.files', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.sets', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.matrices', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.models', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.data', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.data.uk', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.data.us', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.reflection', 'version': '0.0-5'}, {'type': 'r', 'name': 'assertive.code', 'version': '0.0-4'}, {'type': 'r', 'name': 'assertive', 'version': '0.3-6'}, {'type': 'r', 'name': 'rdrop2', 'version': '0.8.2.1'}, {'type': 'r', 'name': 'Exact', 'version': '3.2'}, {'type': 'r', 'name': 'lmom', 'version': '3.0'}, {'type': 'r', 'name': 'gld', 'version': '2.6.6'}, {'type': 'r', 'name': 'DescTools', 'version': '0.99.54'}, {'type': 'r', 'name': 'orthopolynom', 'version': '1.0-6.1'}, {'type': 'r', 'name': 'gaussquad', 'version': '1.0-3'}, {'type': 'r', 'name': 'nlsem', 'version': '0.8-1'}, {'type': 'r', 'name': 'tableone', 'version': '0.13.2'}, {'type': 'r', 'name': 'jstable', 'version': '1.2.6'}, {'type': 'r', 'name': 'RCAL', 'version': '2.0'}, {'type': 'r', 'name': 'stargazer', 'version': '5.2.3'}, {'type': 'r', 'name': 'sensemakr', 'version': '0.1.4'}, {'type': 'r', 'name': 'CompQuadForm', 'version': '1.4.3'}, {'type': 'r', 'name': 'nonnest2', 'version': '0.5-7'}, {'type': 'r', 'name': 'blavaan', 'version': '0.5-5'}, {'type': 'r', 'name': 'mathjaxr', 'version': '1.6-0'}, {'type': 'r', 'name': 'metadat', 'version': '1.2-0'}, {'type': 'r', 'name': 'metafor', 'version': '4.6-0'}, {'type': 'r', 'name': 'RNifti', 'version': '1.7.0'}, {'type': 'r', 'name': 'oro.nifti', 'version': '0.11.4'}, {'type': 'r', 'name': 'fmri', 'version': '1.9.12'}, {'type': 'r', 'name': 'linkcomm', 'version': '1.0-14'}, {'type': 'r', 'name': 'rnetcarto', 'version': '0.2.6'}, {'type': 'r', 'name': 'optextras', 'version': '2019-12.4'}, {'type': 'r', 'name': 'setRNG', 'version': '2024.2-1'}, {'type': 'r', 'name': 'Rvmmin', 'version': '2018-4.17.1'}, {'type': 'r', 'name': 'Rcgmin', 'version': '2022-4.30'}, {'type': 'r', 'name': 'optimr', 'version': '2019-12.16'}, {'type': 'r', 'name': 'DMCfun', 'version': '3.5.4'}, {'type': 'r', 'name': 'miceadds', 'version': '3.17-44'}, {'type': 'r', 'name': 'visdat', 'version': '0.6.0'}, {'type': 'r', 'name': 'UpSetR', 'version': '1.4.0'}, {'type': 'r', 'name': 'norm', 'version': '1.0-11.1'}, {'type': 'r', 'name': 'naniar', 'version': '1.1.0'}, {'type': 'r', 'name': 'stringdist', 'version': '0.9.12'}, {'type': 'r', 'name': 'image.binarization', 'version': '0.1.3'}, {'type': 'r', 'name': 'lassosum', 'version': '0.4.5'}, {'type': 'r', 'name': 'lslx', 'version': '0.6.11'}, {'type': 'r', 'name': 'truncnorm', 'version': '1.0-9'}, {'type': 'r', 'name': 'Rsolnp', 'version': '1.16'}, {'type': 'r', 'name': 'regsem', 'version': '1.9.5'}, {'type': 'r', 'name': 'semPLS', 'version': '1.0-10'}, {'type': 'r', 'name': 'GxEScanR', 'version': '2.0.2'}, {'type': 'r', 'name': 'admisc', 'version': '0.35'}, {'type': 'r', 'name': 'polycor', 'version': '0.8-1'}, {'type': 'r', 'name': 'multipol', 'version': '1.0-9'}, {'type': 'r', 'name': 'symmoments', 'version': '1.2.1'}, {'type': 'r', 'name': 'rngWELL', 'version': '0.10-9'}, {'type': 'r', 'name': 'randtoolbox', 'version': '2.0.4'}, {'type': 'r', 'name': 'TruncatedNormal', 'version': '2.2.2'}, {'type': 'r', 'name': 'cSEM', 'version': '0.5.0'}, {'type': 'r', 'name': 'cubelyr', 'version': '1.0.2'}, {'type': 'r', 'name': 'furrr', 'version': '0.3.1'}, {'type': 'r', 'name': 'broom.mixed', 'version': '0.2.9.5'}, {'type': 'r', 'name': 'DiceKriging', 'version': '1.6.0'}, {'type': 'r', 'name': 'grf', 'version': '2.3.2'}, {'type': 'r', 'name': 'twang', 'version': '2.6'}, {'type': 'r', 'name': 'neuralnet', 'version': '1.44.2'}, {'type': 'r', 'name': 'PCAmatchR', 'version': '0.3.3'}, {'type': 'r', 'name': 'origami', 'version': '1.0.7'}, {'type': 'r', 'name': 'hal9001', 'version': '0.4.6'}, {'type': 'r', 'name': 'cobalt', 'version': '4.5.5'}, {'type': 'r', 'name': 'CBPS', 'version': '0.23'}, {'type': 'r', 'name': 'SBdecomp', 'version': '1.2'}, {'type': 'r', 'name': 'naturalsort', 'version': '0.1.3'}, {'type': 'r', 'name': 'lwgeom', 'version': '0.2-14'}, {'type': 'r', 'name': 'finalfit', 'version': '1.0.7'}, {'type': 'r', 'name': 'bigD', 'version': '0.2.0'}, {'type': 'r', 'name': 'juicyjuice', 'version': '0.1.0'}, {'type': 'r', 'name': 'reactR', 'version': '0.5.0'}, {'type': 'r', 'name': 'reactable', 'version': '0.4.4'}, {'type': 'r', 'name': 'gt', 'version': '0.10.1'}, {'type': 'r', 'name': 'gtsummary', 'version': '1.7.2'}, {'type': 'r', 'name': 'ncdf4', 'version': '1.22'}, {'type': 'r', 'name': 'geex', 'version': '1.1.1'}, {'type': 'r', 'name': 'momentfit', 'version': '0.5'}, {'type': 'r', 'name': 'StatMatch', 'version': '1.4.2'}, {'type': 'r', 'name': 'stars', 'version': '0.6-5'}, {'type': 'r', 'name': 'rapidjsonr', 'version': '1.2.0'}, {'type': 'r', 'name': 'jsonify', 'version': '1.2.2'}, {'type': 'r', 'name': 'geometries', 'version': '0.2.4'}, {'type': 'r', 'name': 'sfheaders', 'version': '0.4.4'}, {'type': 'r', 'name': 'geojsonsf', 'version': '2.0.3'}, {'type': 'r', 'name': 'leaflet.providers', 'version': '2.0.0'}, {'type': 'r', 'name': 'leaflet', 'version': '2.2.2'}, {'type': 'r', 'name': 'leafsync', 'version': '0.1.0'}, {'type': 'r', 'name': 'leafem', 'version': '0.2.3'}, {'type': 'r', 'name': 'widgetframe', 'version': '0.3.1'}, {'type': 'r', 'name': 'tmaptools', 'version': '3.1-1'}, {'type': 'r', 'name': 'tmap', 'version': '3.3-4'}, {'type': 'r', 'name': 'collapse', 'version': '2.0.14'}, {'type': 'r', 'name': 'genoPlotR', 'version': '0.8.11'}, {'type': 'r', 'name': 'VineCopula', 'version': '2.5.0'}, {'type': 'r', 'name': 'Rmpfr', 'version': '0.9-5'}, {'type': 'r', 'name': 'scam', 'version': '1.2-17'}, {'type': 'r', 'name': 'copula', 'version': '1.1-3'}, {'type': 'r', 'name': 'evd', 'version': '2.3-7'}, {'type': 'r', 'name': 'ismev', 'version': '1.42'}, {'type': 'r', 'name': 'GJRM', 'version': '0.2-6.5'}, {'type': 'r', 'name': 'penfa', 'version': '0.1.1'}, {'type': 'r', 'name': 'kde1d', 'version': '1.0.7'}, {'type': 'r', 'name': 'RcppThread', 'version': '2.1.7'}, {'type': 'r', 'name': 'wdm', 'version': '0.2.4'}, {'type': 'r', 'name': 'rvinecopulib', 'version': '0.6.3.1.1'}, {'type': 'r', 'name': 'PearsonDS', 'version': '1.3.1'}, {'type': 'r', 'name': 'covsim', 'version': '1.1.0'}, {'type': 'r', 'name': 'semTools', 'version': '0.5-6'}, {'type': 'r', 'name': 'GPArotation', 'version': '2024.3-1'}, {'type': 'r', 'name': 'dcurver', 'version': '0.9.2'}, {'type': 'r', 'name': 'mirt', 'version': '1.41'}, {'type': 'r', 'name': 'rpf', 'version': '1.0.14'}, {'type': 'r', 'name': 'OpenMx', 'version': '2.21.11'}, {'type': 'r', 'name': 'matlab', 'version': '1.0.4'}, {'type': 'r', 'name': 'FactorCopula', 'version': '0.9.3'}, {'type': 'r', 'name': 'rpact', 'version': '4.0.0'}, {'type': 'r', 'name': 'ldbounds', 'version': '2.0.2'}, {'type': 'r', 'name': 'catlearn', 'version': '1.0'}, {'type': 'r', 'name': 'MetaUtility', 'version': '2.1.2'}, {'type': 'r', 'name': 'EValue', 'version': '4.1.3'}, {'type': 'r', 'name': 'dagitty', 'version': '0.3-4'}, {'type': 'r', 'name': 'ggdag', 'version': '0.2.12'}, {'type': 'r', 'name': 'simex', 'version': '1.8'}, {'type': 'r', 'name': 'hash', 'version': '2.2.6.3'}, {'type': 'r', 'name': 'nabor', 'version': '0.5.0'}, {'type': 'r', 'name': 'RhpcBLASctl', 'version': '0.23-42'}, {'type': 'r', 'name': 'harmony', 'version': '1.2.0'}, {'type': 'r', 'name': 'apcluster', 'version': '1.4.13'}, {'type': 'r', 'name': 'DataCombine', 'version': '0.2.21'}, {'type': 'r', 'name': 'docstring', 'version': '1.0.0'}, {'type': 'r', 'name': 'gdalUtils', 'version': '2.0.3.2'}, {'type': 'r', 'name': 'openair', 'version': '2.18-2'}, {'type': 'r', 'name': 'pdp', 'version': '0.8.1'}, {'type': 'r', 'name': 'date', 'version': '1.2-42'}, {'type': 'r', 'name': 'cmprsk', 'version': '2.2-12'}, {'type': 'r', 'name': 'mets', 'version': '1.3.4'}, {'type': 'r', 'name': 'Publish', 'version': '2023.01.17'}, {'type': 'r', 'name': 'riskRegression', 'version': '2023.12.21'}, {'type': 'r', 'name': 'pec', 'version': '2023.04.12'}, {'type': 'r', 'name': 'pammtools', 'version': '0.5.93'}, {'type': 'r', 'name': 'relsurv', 'version': '2.2-9'}, {'type': 'r', 'name': 'mstate', 'version': '0.3.2'}, {'type': 'r', 'name': 'microbenchmark', 'version': '1.4.10'}, {'type': 'r', 'name': 'prettyGraphs', 'version': '2.1.6'}, {'type': 'r', 'name': 'ExPosition', 'version': '2.8.23'}, {'type': 'r', 'name': 'alluvial', 'version': '0.1-2'}, {'type': 'r', 'name': 'SNFtool', 'version': '2.3.1'}, {'type': 'r', 'name': 'BayesLogit', 'version': '2.1'}, {'type': 'r', 'name': 'Hmsc', 'version': '3.0-13'}, {'type': 'r', 'name': 'MonteCarlo', 'version': '1.0.6'}, {'type': 'r', 'name': 'chkptstanr', 'version': '0.1.1'}, {'type': 'r', 'name': 'MLmetrics', 'version': '1.1.3'}, {'type': 'r', 'name': 'elliptic', 'version': '1.4-0'}, {'type': 'r', 'name': 'contfrac', 'version': '1.1-12'}, {'type': 'r', 'name': 'hypergeo', 'version': '1.2-13'}, {'type': 'r', 'name': 'rtdists', 'version': '0.11-5'}, {'type': 'r', 'name': 'AMAPVox', 'version': '2.2.1'}, {'type': 'r', 'name': 'LCFdata', 'version': '2.0'}, {'type': 'r', 'name': 'LMERConvenienceFunctions', 'version': '3.0'}, {'type': 'r', 'name': 'HGNChelper', 'version': '0.8.14'}, {'type': 'r', 'name': 'logger', 'version': '0.3.0'}, {'type': 'r', 'name': 'parallelDist', 'version': '0.2.6'}, {'type': 'r', 'name': 'roptim', 'version': '0.1.6'}, {'type': 'r', 'name': 'yulab.utils', 'version': '0.1.4'}, {'type': 'r', 'name': 'ggfun', 'version': '0.1.5'}, {'type': 'r', 'name': 'gridGraphics', 'version': '0.5-1'}, {'type': 'r', 'name': 'ggplotify', 'version': '0.1.2'}, {'type': 'r', 'name': 'aplot', 'version': '0.2.3'}, {'type': 'r', 'name': 'tidytree', 'version': '0.4.6'}, {'type': 'r', 'name': 'ggvenn', 'version': '0.1.10'}, {'type': 'r', 'name': 'scatterpie', 'version': '0.2.3'}, {'type': 'r', 'name': 'shadowtext', 'version': '0.1.3'}, {'type': 'r', 'name': 'random', 'version': '0.2.6'}, {'type': 'r', 'name': 'R2WinBUGS', 'version': '2.1-22.1'}, {'type': 'r', 'name': 'aricode', 'version': '1.0.3'}, {'type': 'r', 'name': 'DepthProc', 'version': '2.1.5'}, {'type': 'r', 'name': 'dbscan', 'version': '1.1-12'}, {'type': 'r', 'name': 'ggh4x', 'version': '0.2.8'}, {'type': 'r', 'name': 'ComplexUpset', 'version': '1.3.3'}, {'type': 'r', 'name': 'proxyC', 'version': '0.4.1'}, {'type': 'r', 'name': 'changepoint', 'version': '2.2.4'}, {'type': 'r', 'name': 'geeM', 'version': '0.10.1'}, {'type': 'r', 'name': 'ggstance', 'version': '0.3.7'}, {'type': 'r', 'name': 'mosaicCore', 'version': '0.9.4.0'}, {'type': 'r', 'name': 'ggformula', 'version': '0.12.0'}, {'type': 'r', 'name': 'kinship2', 'version': '1.9.6.1'}, {'type': 'r', 'name': 'MESS', 'version': '0.5.12'}, {'type': 'r', 'name': 'smoof', 'version': '1.6.0.3'}, {'type': 'r', 'name': 'mlrMBO', 'version': '1.1.5.1'}, {'type': 'r', 'name': 'emoa', 'version': '0.5-2'}, {'type': 'r', 'name': 'webutils', 'version': '1.2.0'}, {'type': 'r', 'name': 'swagger', 'version': '5.17.14'}, {'type': 'r', 'name': 'varhandle', 'version': '2.0.6'}, {'type': 'r', 'name': 'dlm', 'version': '1.1-6'}, {'type': 'r', 'name': 'PMA', 'version': '1.2-3'}, {'type': 'r', 'name': 'unikn', 'version': '1.0.0'}, {'type': 'r', 'name': 'ppcor', 'version': '1.1'}, {'type': 'r', 'name': 'berryFunctions', 'version': '1.22.5'}, {'type': 'r', 'name': 'cld2', 'version': '1.2.4'}, {'type': 'r', 'name': 'crfsuite', 'version': '0.4.2'}, {'type': 'r', 'name': 'doc2vec', 'version': '0.2.0'}, {'type': 'r', 'name': 'fastDummies', 'version': '1.7.3'}, {'type': 'r', 'name': 'quanteda', 'version': '4.0.2'}, {'type': 'r', 'name': 'ISOweek', 'version': '0.6-2'}, {'type': 'r', 'name': 'sentometrics', 'version': '1.0.0'}, {'type': 'r', 'name': 'tau', 'version': '0.0-25'}, {'type': 'r', 'name': 'textcat', 'version': '1.0-8'}, {'type': 'r', 'name': 'textplot', 'version': '0.2.2'}, {'type': 'r', 'name': 'udpipe', 'version': '0.8.11'}, {'type': 'r', 'name': 'word2vec', 'version': '0.4.0'}, {'type': 'r', 'name': 'epitools', 'version': '0.5-10.1'}, {'type': 'r', 'name': 'RBesT', 'version': '1.7-3'}, {'type': 'r', 'name': 'svglite', 'version': '2.1.3'}, {'type': 'r', 'name': 'rARPACK', 'version': '0.11-0'}, {'type': 'r', 'name': 'FKSUM', 'version': '1.0.1'}, {'type': 'r', 'name': 'warp', 'version': '0.2.1'}, {'type': 'r', 'name': 'slider', 'version': '0.3.1'}, {'type': 'r', 'name': 'rsample', 'version': '1.2.1'}, {'type': 'r', 'name': 'haldensify', 'version': '0.2.3'}, {'type': 'r', 'name': 'Polychrome', 'version': '1.5.1'}, {'type': 'r', 'name': 'shinycssloaders', 'version': '1.0.0'}, {'type': 'r', 'name': 'princurve', 'version': '2.1.6'}, {'type': 'r', 'name': 'ECOSolveR', 'version': '0.5.5'}, {'type': 'r', 'name': 'scs', 'version': '3.2.4'}, {'type': 'r', 'name': 'osqp', 'version': '0.6.3.3'}, {'type': 'r', 'name': 'CVXR', 'version': '1.0-13'}, {'type': 'r', 'name': 'tabletools', 'version': '0.1.0'}, {'type': 'r', 'name': 'officer', 'version': '0.6.6'}, {'type': 'r', 'name': 'gfonts', 'version': '0.2.0'}, {'type': 'r', 'name': 'fontBitstreamVera', 'version': '0.1.1'}, {'type': 'r', 'name': 'fontLiberation', 'version': '0.1.0'}, {'type': 'r', 'name': 'fontquiver', 'version': '0.2.1'}, {'type': 'r', 'name': 'gdtools', 'version': '0.3.7'}, {'type': 'r', 'name': 'flextable', 'version': '0.9.6'}, {'type': 'r', 'name': 'ridge', 'version': '3.3'}, {'type': 'r', 'name': 'ggdist', 'version': '3.3.2'}, {'type': 'r', 'name': 'svUnit', 'version': '1.0.6'}, {'type': 'r', 'name': 'arrayhelpers', 'version': '1.1-0'}, {'type': 'r', 'name': 'tidybayes', 'version': '3.0.6'}, {'type': 'r', 'name': 'spdep', 'version': '1.3-5'}, {'type': 'r', 'name': 'stringmagic', 'version': '1.1.2'}, {'type': 'r', 'name': 'dreamerr', 'version': '1.4.0'}, {'type': 'r', 'name': 'fixest', 'version': '0.12.1'}, {'type': 'r', 'name': 'cmna', 'version': '1.0.5'}, {'type': 'r', 'name': 'XBRL', 'version': '0.99.19.1'}, {'type': 'r', 'name': 'rhandsontable', 'version': '0.3.8'}, {'type': 'r', 'name': 'missMDA', 'version': '1.19'}, {'type': 'r', 'name': 'insight', 'version': '0.20.3'}, {'type': 'r', 'name': 'datawizard', 'version': '0.12.2'}, {'type': 'r', 'name': 'bayestestR', 'version': '0.14.0'}, {'type': 'r', 'name': 'performance', 'version': '0.12.2'}]}, {'homepage': 'https://www.r-project.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'toolchain': {'name': 'foss', 'version': '2024a'}, 'toolchain_families_compatibility': ['2024a_foss'], 'module': {'full_module_name': 'R-bundle-CRAN/2024.11-foss-2024a', 'module_name': 'R-bundle-CRAN', 'module_version': '2024.11-foss-2024a'}, 'required_modules': [{'full_module_name': 'EESSI/2025.06', 'module_name': 'EESSI', 'module_version': '2025.06'}, {'full_module_name': 'GCCcore/13.3.0', 'module_name': 'GCCcore', 'module_version': '13.3.0'}, {'full_module_name': 'GCC/13.3.0', 'module_name': 'GCC', 'module_version': '13.3.0'}, {'full_module_name': 'numactl/2.0.18-GCCcore-13.3.0', 'module_name': 'numactl', 'module_version': '2.0.18-GCCcore-13.3.0'}, {'full_module_name': 'libxml2/2.12.7-GCCcore-13.3.0', 'module_name': 'libxml2', 'module_version': '2.12.7-GCCcore-13.3.0'}, {'full_module_name': 'libpciaccess/0.18.1-GCCcore-13.3.0', 'module_name': 'libpciaccess', 'module_version': '0.18.1-GCCcore-13.3.0'}, {'full_module_name': 'hwloc/2.10.0-GCCcore-13.3.0', 'module_name': 'hwloc', 'module_version': '2.10.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenSSL/3', 'module_name': 'OpenSSL', 'module_version': '3'}, {'full_module_name': 'libevent/2.1.12-GCCcore-13.3.0', 'module_name': 'libevent', 'module_version': '2.1.12-GCCcore-13.3.0'}, {'full_module_name': 'UCX/1.16.0-GCCcore-13.3.0', 'module_name': 'UCX', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'libfabric/1.21.0-GCCcore-13.3.0', 'module_name': 'libfabric', 'module_version': '1.21.0-GCCcore-13.3.0'}, {'full_module_name': 'PMIx/5.0.2-GCCcore-13.3.0', 'module_name': 'PMIx', 'module_version': '5.0.2-GCCcore-13.3.0'}, {'full_module_name': 'PRRTE/3.0.5-GCCcore-13.3.0', 'module_name': 'PRRTE', 'module_version': '3.0.5-GCCcore-13.3.0'}, {'full_module_name': 'UCC/1.3.0-GCCcore-13.3.0', 'module_name': 'UCC', 'module_version': '1.3.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenMPI/5.0.3-GCC-13.3.0', 'module_name': 'OpenMPI', 'module_version': '5.0.3-GCC-13.3.0'}, {'full_module_name': 'OpenBLAS/0.3.27-GCC-13.3.0', 'module_name': 'OpenBLAS', 'module_version': '0.3.27-GCC-13.3.0'}, {'full_module_name': 'FlexiBLAS/3.4.4-GCC-13.3.0', 'module_name': 'FlexiBLAS', 'module_version': '3.4.4-GCC-13.3.0'}, {'full_module_name': 'FFTW/3.3.10-GCC-13.3.0', 'module_name': 'FFTW', 'module_version': '3.3.10-GCC-13.3.0'}, {'full_module_name': 'gompi/2024a', 'module_name': 'gompi', 'module_version': '2024a'}, {'full_module_name': 'FFTW.MPI/3.3.10-gompi-2024a', 'module_name': 'FFTW.MPI', 'module_version': '3.3.10-gompi-2024a'}, {'full_module_name': 'ScaLAPACK/2.2.0-gompi-2024a-fb', 'module_name': 'ScaLAPACK', 'module_version': '2.2.0-gompi-2024a-fb'}, {'full_module_name': 'foss/2024a', 'module_name': 'foss', 'module_version': '2024a'}, {'full_module_name': 'gfbf/2024a', 'module_name': 'gfbf', 'module_version': '2024a'}, {'full_module_name': 'expat/2.6.2-GCCcore-13.3.0', 'module_name': 'expat', 'module_version': '2.6.2-GCCcore-13.3.0'}, {'full_module_name': 'libpng/1.6.43-GCCcore-13.3.0', 'module_name': 'libpng', 'module_version': '1.6.43-GCCcore-13.3.0'}, {'full_module_name': 'Brotli/1.1.0-GCCcore-13.3.0', 'module_name': 'Brotli', 'module_version': '1.1.0-GCCcore-13.3.0'}, {'full_module_name': 'freetype/2.13.2-GCCcore-13.3.0', 'module_name': 'freetype', 'module_version': '2.13.2-GCCcore-13.3.0'}, {'full_module_name': 'fontconfig/2.15.0-GCCcore-13.3.0', 'module_name': 'fontconfig', 'module_version': '2.15.0-GCCcore-13.3.0'}, {'full_module_name': 'xorg-macros/1.20.1-GCCcore-13.3.0', 'module_name': 'xorg-macros', 'module_version': '1.20.1-GCCcore-13.3.0'}, {'full_module_name': 'X11/20240607-GCCcore-13.3.0', 'module_name': 'X11', 'module_version': '20240607-GCCcore-13.3.0'}, {'full_module_name': 'gzip/1.13-GCCcore-13.3.0', 'module_name': 'gzip', 'module_version': '1.13-GCCcore-13.3.0'}, {'full_module_name': 'lz4/1.9.4-GCCcore-13.3.0', 'module_name': 'lz4', 'module_version': '1.9.4-GCCcore-13.3.0'}, {'full_module_name': 'zstd/1.5.6-GCCcore-13.3.0', 'module_name': 'zstd', 'module_version': '1.5.6-GCCcore-13.3.0'}, {'full_module_name': 'libdrm/2.4.122-GCCcore-13.3.0', 'module_name': 'libdrm', 'module_version': '2.4.122-GCCcore-13.3.0'}, {'full_module_name': 'libglvnd/1.7.0-GCCcore-13.3.0', 'module_name': 'libglvnd', 'module_version': '1.7.0-GCCcore-13.3.0'}, {'full_module_name': 'libunwind/1.8.1-GCCcore-13.3.0', 'module_name': 'libunwind', 'module_version': '1.8.1-GCCcore-13.3.0'}, {'full_module_name': 'libffi/3.4.5-GCCcore-13.3.0', 'module_name': 'libffi', 'module_version': '3.4.5-GCCcore-13.3.0'}, {'full_module_name': 'LLVM/18.1.8-GCCcore-13.3.0-minimal', 'module_name': 'LLVM', 'module_version': '18.1.8-GCCcore-13.3.0-minimal'}, {'full_module_name': 'Wayland/1.23.0-GCCcore-13.3.0', 'module_name': 'Wayland', 'module_version': '1.23.0-GCCcore-13.3.0'}, {'full_module_name': 'Mesa/24.1.3-GCCcore-13.3.0', 'module_name': 'Mesa', 'module_version': '24.1.3-GCCcore-13.3.0'}, {'full_module_name': 'libGLU/9.0.3-GCCcore-13.3.0', 'module_name': 'libGLU', 'module_version': '9.0.3-GCCcore-13.3.0'}, {'full_module_name': 'pixman/0.43.4-GCCcore-13.3.0', 'module_name': 'pixman', 'module_version': '0.43.4-GCCcore-13.3.0'}, {'full_module_name': 'PCRE2/10.43-GCCcore-13.3.0', 'module_name': 'PCRE2', 'module_version': '10.43-GCCcore-13.3.0'}, {'full_module_name': 'GLib/2.80.4-GCCcore-13.3.0', 'module_name': 'GLib', 'module_version': '2.80.4-GCCcore-13.3.0'}, {'full_module_name': 'cairo/1.18.0-GCCcore-13.3.0', 'module_name': 'cairo', 'module_version': '1.18.0-GCCcore-13.3.0'}, {'full_module_name': 'Tcl/8.6.14-GCCcore-13.3.0', 'module_name': 'Tcl', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'SQLite/3.45.3-GCCcore-13.3.0', 'module_name': 'SQLite', 'module_version': '3.45.3-GCCcore-13.3.0'}, {'full_module_name': 'NASM/2.16.03-GCCcore-13.3.0', 'module_name': 'NASM', 'module_version': '2.16.03-GCCcore-13.3.0'}, {'full_module_name': 'libjpeg-turbo/3.0.1-GCCcore-13.3.0', 'module_name': 'libjpeg-turbo', 'module_version': '3.0.1-GCCcore-13.3.0'}, {'full_module_name': 'jbigkit/2.1-GCCcore-13.3.0', 'module_name': 'jbigkit', 'module_version': '2.1-GCCcore-13.3.0'}, {'full_module_name': 'libdeflate/1.20-GCCcore-13.3.0', 'module_name': 'libdeflate', 'module_version': '1.20-GCCcore-13.3.0'}, {'full_module_name': 'LibTIFF/4.6.0-GCCcore-13.3.0', 'module_name': 'LibTIFF', 'module_version': '4.6.0-GCCcore-13.3.0'}, {'full_module_name': 'Java/17.0.15', 'module_name': 'Java', 'module_version': '17.0.15'}, {'full_module_name': 'Java/17', 'module_name': 'Java', 'module_version': '17'}, {'full_module_name': 'libgit2/1.8.1-GCCcore-13.3.0', 'module_name': 'libgit2', 'module_version': '1.8.1-GCCcore-13.3.0'}, {'full_module_name': 'cURL/8.7.1-GCCcore-13.3.0', 'module_name': 'cURL', 'module_version': '8.7.1-GCCcore-13.3.0'}, {'full_module_name': 'Tk/8.6.14-GCCcore-13.3.0', 'module_name': 'Tk', 'module_version': '8.6.14-GCCcore-13.3.0'}, {'full_module_name': 'ICU/75.1-GCCcore-13.3.0', 'module_name': 'ICU', 'module_version': '75.1-GCCcore-13.3.0'}, {'full_module_name': 'HarfBuzz/9.0.0-GCCcore-13.3.0', 'module_name': 'HarfBuzz', 'module_version': '9.0.0-GCCcore-13.3.0'}, {'full_module_name': 'FriBidi/1.0.15-GCCcore-13.3.0', 'module_name': 'FriBidi', 'module_version': '1.0.15-GCCcore-13.3.0'}, {'full_module_name': 'R/4.4.2-gfbf-2024a', 'module_name': 'R', 'module_version': '4.4.2-gfbf-2024a'}, {'full_module_name': 'GMP/6.3.0-GCCcore-13.3.0', 'module_name': 'GMP', 'module_version': '6.3.0-GCCcore-13.3.0'}, {'full_module_name': 'NLopt/2.7.1-GCCcore-13.3.0', 'module_name': 'NLopt', 'module_version': '2.7.1-GCCcore-13.3.0'}, {'full_module_name': 'libogg/1.3.5-GCCcore-13.3.0', 'module_name': 'libogg', 'module_version': '1.3.5-GCCcore-13.3.0'}, {'full_module_name': 'FLAC/1.4.3-GCCcore-13.3.0', 'module_name': 'FLAC', 'module_version': '1.4.3-GCCcore-13.3.0'}, {'full_module_name': 'libvorbis/1.3.7-GCCcore-13.3.0', 'module_name': 'libvorbis', 'module_version': '1.3.7-GCCcore-13.3.0'}, {'full_module_name': 'libopus/1.5.2-GCCcore-13.3.0', 'module_name': 'libopus', 'module_version': '1.5.2-GCCcore-13.3.0'}, {'full_module_name': 'LAME/3.100-GCCcore-13.3.0', 'module_name': 'LAME', 'module_version': '3.100-GCCcore-13.3.0'}, {'full_module_name': 'libsndfile/1.2.2-GCCcore-13.3.0', 'module_name': 'libsndfile', 'module_version': '1.2.2-GCCcore-13.3.0'}, {'full_module_name': 'Szip/2.1.1-GCCcore-13.3.0', 'module_name': 'Szip', 'module_version': '2.1.1-GCCcore-13.3.0'}, {'full_module_name': 'HDF5/1.14.5-gompi-2024a', 'module_name': 'HDF5', 'module_version': '1.14.5-gompi-2024a'}, {'full_module_name': 'UDUNITS/2.2.28-GCCcore-13.3.0', 'module_name': 'UDUNITS', 'module_version': '2.2.28-GCCcore-13.3.0'}, {'full_module_name': 'GSL/2.8-GCC-13.3.0', 'module_name': 'GSL', 'module_version': '2.8-GCC-13.3.0'}, {'full_module_name': 'Ghostscript/10.03.1-GCCcore-13.3.0', 'module_name': 'Ghostscript', 'module_version': '10.03.1-GCCcore-13.3.0'}, {'full_module_name': 'libde265/1.0.15-GCCcore-13.3.0', 'module_name': 'libde265', 'module_version': '1.0.15-GCCcore-13.3.0'}, {'full_module_name': 'x265/3.6-GCCcore-13.3.0', 'module_name': 'x265', 'module_version': '3.6-GCCcore-13.3.0'}, {'full_module_name': 'Gdk-Pixbuf/2.42.11-GCCcore-13.3.0', 'module_name': 'Gdk-Pixbuf', 'module_version': '2.42.11-GCCcore-13.3.0'}, {'full_module_name': 'libheif/1.19.5-GCCcore-13.3.0', 'module_name': 'libheif', 'module_version': '1.19.5-GCCcore-13.3.0'}, {'full_module_name': 'JasPer/4.2.4-GCCcore-13.3.0', 'module_name': 'JasPer', 'module_version': '4.2.4-GCCcore-13.3.0'}, {'full_module_name': 'LittleCMS/2.16-GCCcore-13.3.0', 'module_name': 'LittleCMS', 'module_version': '2.16-GCCcore-13.3.0'}, {'full_module_name': 'Pango/1.54.0-GCCcore-13.3.0', 'module_name': 'Pango', 'module_version': '1.54.0-GCCcore-13.3.0'}, {'full_module_name': 'ImageMagick/7.1.1-38-GCCcore-13.3.0', 'module_name': 'ImageMagick', 'module_version': '7.1.1-38-GCCcore-13.3.0'}, {'full_module_name': 'GLPK/5.0-GCCcore-13.3.0', 'module_name': 'GLPK', 'module_version': '5.0-GCCcore-13.3.0'}, {'full_module_name': 'nodejs/20.13.1-GCCcore-13.3.0', 'module_name': 'nodejs', 'module_version': '20.13.1-GCCcore-13.3.0'}, {'full_module_name': 'Python/3.12.3-GCCcore-13.3.0', 'module_name': 'Python', 'module_version': '3.12.3-GCCcore-13.3.0'}, {'full_module_name': 'netCDF/4.9.2-gompi-2024a', 'module_name': 'netCDF', 'module_version': '4.9.2-gompi-2024a'}, {'full_module_name': 'GEOS/3.12.2-GCC-13.3.0', 'module_name': 'GEOS', 'module_version': '3.12.2-GCC-13.3.0'}, {'full_module_name': 'libarchive/3.7.4-GCCcore-13.3.0', 'module_name': 'libarchive', 'module_version': '3.7.4-GCCcore-13.3.0'}, {'full_module_name': 'PCRE/8.45-GCCcore-13.3.0', 'module_name': 'PCRE', 'module_version': '8.45-GCCcore-13.3.0'}, {'full_module_name': 'nlohmann_json/3.11.3-GCCcore-13.3.0', 'module_name': 'nlohmann_json', 'module_version': '3.11.3-GCCcore-13.3.0'}, {'full_module_name': 'PROJ/9.4.1-GCCcore-13.3.0', 'module_name': 'PROJ', 'module_version': '9.4.1-GCCcore-13.3.0'}, {'full_module_name': 'libgeotiff/1.7.3-GCCcore-13.3.0', 'module_name': 'libgeotiff', 'module_version': '1.7.3-GCCcore-13.3.0'}, {'full_module_name': 'cffi/1.16.0-GCCcore-13.3.0', 'module_name': 'cffi', 'module_version': '1.16.0-GCCcore-13.3.0'}, {'full_module_name': 'cryptography/42.0.8-GCCcore-13.3.0', 'module_name': 'cryptography', 'module_version': '42.0.8-GCCcore-13.3.0'}, {'full_module_name': 'virtualenv/20.26.2-GCCcore-13.3.0', 'module_name': 'virtualenv', 'module_version': '20.26.2-GCCcore-13.3.0'}, {'full_module_name': 'Python-bundle-PyPI/2024.06-GCCcore-13.3.0', 'module_name': 'Python-bundle-PyPI', 'module_version': '2024.06-GCCcore-13.3.0'}, {'full_module_name': 'SciPy-bundle/2024.05-gfbf-2024a', 'module_name': 'SciPy-bundle', 'module_version': '2024.05-gfbf-2024a'}, {'full_module_name': 'libtirpc/1.3.5-GCCcore-13.3.0', 'module_name': 'libtirpc', 'module_version': '1.3.5-GCCcore-13.3.0'}, {'full_module_name': 'HDF/4.3.0-GCCcore-13.3.0', 'module_name': 'HDF', 'module_version': '4.3.0-GCCcore-13.3.0'}, {'full_module_name': 'Eigen/3.4.0-GCCcore-13.3.0', 'module_name': 'Eigen', 'module_version': '3.4.0-GCCcore-13.3.0'}, {'full_module_name': 'arpack-ng/3.9.1-foss-2024a', 'module_name': 'arpack-ng', 'module_version': '3.9.1-foss-2024a'}, {'full_module_name': 'Armadillo/14.0.3-foss-2024a', 'module_name': 'Armadillo', 'module_version': '14.0.3-foss-2024a'}, {'full_module_name': 'CFITSIO/4.4.1-GCCcore-13.3.0', 'module_name': 'CFITSIO', 'module_version': '4.4.1-GCCcore-13.3.0'}, {'full_module_name': 'giflib/5.2.1-GCCcore-13.3.0', 'module_name': 'giflib', 'module_version': '5.2.1-GCCcore-13.3.0'}, {'full_module_name': 'json-c/0.17-GCCcore-13.3.0', 'module_name': 'json-c', 'module_version': '0.17-GCCcore-13.3.0'}, {'full_module_name': 'Xerces-C++/3.2.5-GCCcore-13.3.0', 'module_name': 'Xerces-C++', 'module_version': '3.2.5-GCCcore-13.3.0'}, {'full_module_name': 'Imath/3.1.11-GCCcore-13.3.0', 'module_name': 'Imath', 'module_version': '3.1.11-GCCcore-13.3.0'}, {'full_module_name': 'OpenEXR/3.2.4-GCCcore-13.3.0', 'module_name': 'OpenEXR', 'module_version': '3.2.4-GCCcore-13.3.0'}, {'full_module_name': 'Brunsli/0.1-GCCcore-13.3.0', 'module_name': 'Brunsli', 'module_version': '0.1-GCCcore-13.3.0'}, {'full_module_name': 'Qhull/2020.2-GCCcore-13.3.0', 'module_name': 'Qhull', 'module_version': '2020.2-GCCcore-13.3.0'}, {'full_module_name': 'LERC/4.0.0-GCCcore-13.3.0', 'module_name': 'LERC', 'module_version': '4.0.0-GCCcore-13.3.0'}, {'full_module_name': 'OpenJPEG/2.5.2-GCCcore-13.3.0', 'module_name': 'OpenJPEG', 'module_version': '2.5.2-GCCcore-13.3.0'}, {'full_module_name': 'SWIG/4.2.1-GCCcore-13.3.0', 'module_name': 'SWIG', 'module_version': '4.2.1-GCCcore-13.3.0'}, {'full_module_name': 'GDAL/3.10.0-foss-2024a', 'module_name': 'GDAL', 'module_version': '3.10.0-foss-2024a'}, {'full_module_name': 'MPFR/4.2.1-GCCcore-13.3.0', 'module_name': 'MPFR', 'module_version': '4.2.1-GCCcore-13.3.0'}, {'full_module_name': 'PostgreSQL/16.4-GCCcore-13.3.0', 'module_name': 'PostgreSQL', 'module_version': '16.4-GCCcore-13.3.0'}, {'full_module_name': 'R-bundle-CRAN/2024.11-foss-2024a', 'module_name': 'R-bundle-CRAN', 'module_version': '2024.11-foss-2024a'}], 'cpu_arch': ['aarch64/generic', 'aarch64/a64fx', 'aarch64/neoverse_n1', 'aarch64/neoverse_v1', 'aarch64/nvidia/grace', 'x86_64/generic', 'x86_64/amd/zen2', 'x86_64/amd/zen3', 'x86_64/amd/zen4', 'x86_64/intel/haswell', 'x86_64/intel/skylake_avx512', 'x86_64/intel/sapphirerapids', 'x86_64/intel/icelake', 'x86_64/intel/cascadelake'], 'gpu_arch': {}, 'description': 'Bundle of R packages from CRAN', 'version': '2024.11', 'versionsuffix': '', 'extensions': [{'type': 'r', 'name': 'abind', 'version': '1.4-8'}, {'type': 'r', 'name': 'magic', 'version': '1.6-1'}, {'type': 'r', 'name': 'RcppProgress', 'version': '0.4.2'}, {'type': 'r', 'name': 'lpSolve', 'version': '5.6.22'}, {'type': 'r', 'name': 'linprog', 'version': '0.9-4'}, {'type': 'r', 'name': 'geometry', 'version': '0.5.0'}, {'type': 'r', 'name': 'bit', 'version': '4.5.0'}, {'type': 'r', 'name': 'filehash', 'version': '2.4-6'}, {'type': 'r', 'name': 'ff', 'version': '4.5.0'}, {'type': 'r', 'name': 'bnlearn', 'version': '5.0.1'}, {'type': 'r', 'name': 'bootstrap', 'version': '2019.6'}, {'type': 'r', 'name': 'combinat', 'version': '0.0-8'}, {'type': 'r', 'name': 'deal', 'version': '1.2-42'}, {'type': 'r', 'name': 'fdrtool', 'version': '1.2.18'}, {'type': 'r', 'name': 'formatR', 'version': '1.14'}, {'type': 'r', 'name': 'gtools', 'version': '3.9.5'}, {'type': 'r', 'name': 'gdata', 'version': '3.0.1'}, {'type': 'r', 'name': 'GSA', 'version': '1.03.3'}, {'type': 'r', 'name': 'infotheo', 'version': '1.2.0.1'}, {'type': 'r', 'name': 'lars', 'version': '1.3'}, {'type': 'r', 'name': 'lazy', 'version': '1.2-18'}, {'type': 'r', 'name': 'kernlab', 'version': '0.9-33'}, {'type': 'r', 'name': 'markdown', 'version': '1.13'}, {'type': 'r', 'name': 'mlbench', 'version': '2.1-5'}, {'type': 'r', 'name': 'NLP', 'version': '0.3-2'}, {'type': 'r', 'name': 'mclust', 'version': '6.1.1'}, {'type': 'r', 'name': 'RANN', 'version': '2.6.2'}, {'type': 'r', 'name': 'rmeta', 'version': '3.0'}, {'type': 'r', 'name': 'MASS', 'version': '7.3-61'}, {'type': 'r', 'name': 'lattice', 'version': '0.22-6'}, {'type': 'r', 'name': 'nlme', 'version': '3.1-166'}, {'type': 'r', 'name': 'segmented', 'version': '2.1-3'}, {'type': 'r', 'name': 'som', 'version': '0.3-5.2'}, {'type': 'r', 'name': 'SuppDists', 'version': '1.1-9.8'}, {'type': 'r', 'name': 'stabledist', 'version': '0.7-2'}, {'type': 'r', 'name': 'survivalROC', 'version': '1.0.3.1'}, {'type': 'r', 'name': 'pspline', 'version': '1.0-20'}, {'type': 'r', 'name': 'timeDate', 'version': '4041.110'}, {'type': 'r', 'name': 'longmemo', 'version': '1.1-3'}, {'type': 'r', 'name': 'ADGofTest', 'version': '0.3'}, {'type': 'r', 'name': 'pixmap', 'version': '0.4-13'}, {'type': 'r', 'name': 'sp', 'version': '2.1-4'}, {'type': 'r', 'name': 'hms', 'version': '1.1.3'}, {'type': 'r', 'name': 'progress', 'version': '1.2.3'}, {'type': 'r', 'name': 'RcppArmadillo', 'version': '14.2.0-1'}, {'type': 'r', 'name': 'ade4', 'version': '1.7-22'}, {'type': 'r', 'name': 'AlgDesign', 'version': '1.2.1.1'}, {'type': 'r', 'name': 'BH', 'version': '1.84.0-0'}, {'type': 'r', 'name': 'Matrix', 'version': '1.7-1'}, {'type': 'r', 'name': 'Brobdingnag', 'version': '1.2-9'}, {'type': 'r', 'name': 'corpcor', 'version': '1.6.10'}, {'type': 'r', 'name': 'longitudinal', 'version': '1.1.13'}, {'type': 'r', 'name': 'backports', 'version': '1.5.0'}, {'type': 'r', 'name': 'checkmate', 'version': '2.3.2'}, {'type': 'r', 'name': 'cubature', 'version': '2.1.1'}, {'type': 'r', 'name': 'DEoptimR', 'version': '1.1-3-1'}, {'type': 'r', 'name': 'fastmatch', 'version': '1.1-4'}, {'type': 'r', 'name': 'iterators', 'version': '1.0.14'}, {'type': 'r', 'name': 'maps', 'version': '3.4.2.1'}, {'type': 'r', 'name': 'nnls', 'version': '1.6'}, {'type': 'r', 'name': 'sendmailR', 'version': '1.4-0'}, {'type': 'r', 'name': 'dotCall64', 'version': '1.2'}, {'type': 'r', 'name': 'spam', 'version': '2.11-0'}, {'type': 'r', 'name': 'subplex', 'version': '1.9'}, {'type': 'r', 'name': 'logspline', 'version': '2.1.22'}, {'type': 'r', 'name': 'ncbit', 'version': '2013.03.29.1'}, {'type': 'r', 'name': 'permute', 'version': '0.9-7'}, {'type': 'r', 'name': 'plotrix', 'version': '3.8-4'}, {'type': 'r', 'name': 'randomForest', 'version': '4.7-1.2'}, {'type': 'r', 'name': 'scatterplot3d', 'version': '0.3-44'}, {'type': 'r', 'name': 'SparseM', 'version': '1.84-2'}, {'type': 'r', 'name': 'tripack', 'version': '1.3-9.2'}, {'type': 'r', 'name': 'irace', 'version': '3.5'}, {'type': 'r', 'name': 'rJava', 'version': '1.0-11'}, {'type': 'r', 'name': 'RColorBrewer', 'version': '1.1-3'}, {'type': 'r', 'name': 'png', 'version': '0.1-8'}, {'type': 'r', 'name': 'jpeg', 'version': '0.1-10'}, {'type': 'r', 'name': 'deldir', 'version': '2.0-4'}, {'type': 'r', 'name': 'RcppEigen', 'version': '0.3.4.0.2'}, {'type': 'r', 'name': 'interp', 'version': '1.1-6'}, {'type': 'r', 'name': 'latticeExtra', 'version': '0.6-30'}, {'type': 'r', 'name': 'plyr', 'version': '1.8.9'}, {'type': 'r', 'name': 'gtable', 'version': '0.3.6'}, {'type': 'r', 'name': 'reshape2', 'version': '1.4.4'}, {'type': 'r', 'name': 'dichromat', 'version': '2.0-0.1'}, {'type': 'r', 'name': 'colorspace', 'version': '2.1-1'}, {'type': 'r', 'name': 'munsell', 'version': '0.5.1'}, {'type': 'r', 'name': 'labeling', 'version': '0.4.3'}, {'type': 'r', 'name': 'viridisLite', 'version': '0.4.2'}, {'type': 'r', 'name': 'farver', 'version': '2.1.2'}, {'type': 'r', 'name': 'scales', 'version': '1.3.0'}, {'type': 'r', 'name': 'zeallot', 'version': '0.1.0'}, {'type': 'r', 'name': 'assertthat', 'version': '0.2.1'}, {'type': 'r', 'name': 'lazyeval', 'version': '0.2.2'}, {'type': 'r', 'name': 'mgcv', 'version': '1.9-1'}, {'type': 'r', 'name': 'isoband', 'version': '0.2.7'}, {'type': 'r', 'name': 'ggplot2', 'version': '3.5.1'}, {'type': 'r', 'name': 'pROC', 'version': '1.18.5'}, {'type': 'r', 'name': 'quadprog', 'version': '1.5-8'}, {'type': 'r', 'name': 'BB', 'version': '2019.10-1'}, {'type': 'r', 'name': 'data.table', 'version': '1.16.2'}, {'type': 'r', 'name': 'BBmisc', 'version': '1.13'}, {'type': 'r', 'name': 'fail', 'version': '1.3'}, {'type': 'r', 'name': 'rlecuyer', 'version': '0.3-8'}, {'type': 'r', 'name': 'snow', 'version': '0.4-4'}, {'type': 'r', 'name': 'tree', 'version': '1.0-43'}, {'type': 'r', 'name': 'pls', 'version': '2.8-5'}, {'type': 'r', 'name': 'class', 'version': '7.3-22'}, {'type': 'r', 'name': 'proxy', 'version': '0.4-27'}, {'type': 'r', 'name': 'e1071', 'version': '1.7-16'}, {'type': 'r', 'name': 'nnet', 'version': '7.3-19'}, {'type': 'r', 'name': 'minqa', 'version': '1.2.8'}, {'type': 'r', 'name': 'MatrixModels', 'version': '0.5-3'}, {'type': 'r', 'name': 'matrixStats', 'version': '1.4.1'}, {'type': 'r', 'name': 'codetools', 'version': '0.2-20'}, {'type': 'r', 'name': 'foreach', 'version': '1.5.2'}, {'type': 'r', 'name': 'ModelMetrics', 'version': '1.2.2.2'}, {'type': 'r', 'name': 'generics', 'version': '0.1.3'}, {'type': 'r', 'name': 'tidyselect', 'version': '1.2.1'}, {'type': 'r', 'name': 'dplyr', 'version': '1.1.4'}, {'type': 'r', 'name': 'gower', 'version': '1.0.1'}, {'type': 'r', 'name': 'rpart', 'version': '4.1.23'}, {'type': 'r', 'name': 'survival', 'version': '3.7-0'}, {'type': 'r', 'name': 'KernSmooth', 'version': '2.23-24'}, {'type': 'r', 'name': 'globals', 'version': '0.16.3'}, {'type': 'r', 'name': 'listenv', 'version': '0.9.1'}, {'type': 'r', 'name': 'parallelly', 'version': '1.39.0'}, {'type': 'r', 'name': 'future', 'version': '1.34.0'}, {'type': 'r', 'name': 'future.apply', 'version': '1.11.3'}, {'type': 'r', 'name': 'progressr', 'version': '0.15.1'}, {'type': 'r', 'name': 'numDeriv', 'version': '2016.8-1.1'}, {'type': 'r', 'name': 'SQUAREM', 'version': '2021.1'}, {'type': 'r', 'name': 'lava', 'version': '1.8.0'}, {'type': 'r', 'name': 'shape', 'version': '1.4.6.1'}, {'type': 'r', 'name': 'diagram', 'version': '1.6.5'}, {'type': 'r', 'name': 'prodlim', 'version': '2024.06.25'}, {'type': 'r', 'name': 'ipred', 'version': '0.9-15'}, {'type': 'r', 'name': 'timechange', 'version': '0.3.0'}, {'type': 'r', 'name': 'lubridate', 'version': '1.9.3'}, {'type': 'r', 'name': 'tidyr', 'version': '1.3.1'}, {'type': 'r', 'name': 'hardhat', 'version': '1.4.0'}, {'type': 'r', 'name': 'tzdb', 'version': '0.4.0'}, {'type': 'r', 'name': 'clock', 'version': '0.7.1'}, {'type': 'r', 'name': 'recipes', 'version': '1.1.0'}, {'type': 'r', 'name': 'caret', 'version': '6.0-94'}, {'type': 'r', 'name': 'conquer', 'version': '1.3.3'}, {'type': 'r', 'name': 'quantreg', 'version': '5.99.1'}, {'type': 'r', 'name': 'robustbase', 'version': '0.99-4-1'}, {'type': 'r', 'name': 'zoo', 'version': '1.8-12'}, {'type': 'r', 'name': 'lmtest', 'version': '0.9-40'}, {'type': 'r', 'name': 'vcd', 'version': '1.4-13'}, {'type': 'r', 'name': 'snowfall', 'version': '1.84-6.3'}, {'type': 'r', 'name': 'bindr', 'version': '0.1.2'}, {'type': 'r', 'name': 'plogr', 'version': '0.2.0'}, {'type': 'r', 'name': 'bindrcpp', 'version': '0.2.3'}, {'type': 'r', 'name': 'tmvnsim', 'version': '1.0-2'}, {'type': 'r', 'name': 'mnormt', 'version': '2.1.1'}, {'type': 'r', 'name': 'foreign', 'version': '0.8-87'}, {'type': 'r', 'name': 'GPArotation', 'version': '2024.3-1'}, {'type': 'r', 'name': 'psych', 'version': '2.4.6.26'}, {'type': 'r', 'name': 'broom', 'version': '1.0.7'}, {'type': 'r', 'name': 'nloptr', 'version': '2.1.1'}, {'type': 'r', 'name': 'boot', 'version': '1.3-31'}, {'type': 'r', 'name': 'statmod', 'version': '1.5.0'}, {'type': 'r', 'name': 'lme4', 'version': '1.1-35.5'}, {'type': 'r', 'name': 'ucminf', 'version': '1.2.2'}, {'type': 'r', 'name': 'ordinal', 'version': '2023.12-4.1'}, {'type': 'r', 'name': 'jomo', 'version': '2.7-6'}, {'type': 'r', 'name': 'bit64', 'version': '4.5.2'}, {'type': 'r', 'name': 'vroom', 'version': '1.6.5'}, {'type': 'r', 'name': 'readr', 'version': '2.1.5'}, {'type': 'r', 'name': 'forcats', 'version': '1.0.0'}, {'type': 'r', 'name': 'haven', 'version': '2.5.4'}, {'type': 'r', 'name': 'pan', 'version': '1.9'}, {'type': 'r', 'name': 'mitml', 'version': '0.4-5'}, {'type': 'r', 'name': 'glmnet', 'version': '4.1-8'}, {'type': 'r', 'name': 'mice', 'version': '3.16.0'}, {'type': 'r', 'name': 'urca', 'version': '1.3-4'}, {'type': 'r', 'name': 'fracdiff', 'version': '1.5-3'}, {'type': 'r', 'name': 'operator.tools', 'version': '1.6.3'}, {'type': 'r', 'name': 'formula.tools', 'version': '1.7.1'}, {'type': 'r', 'name': 'logistf', 'version': '1.26.0'}, {'type': 'r', 'name': 'akima', 'version': '0.6-3.4'}, {'type': 'r', 'name': 'bitops', 'version': '1.0-9'}, {'type': 'r', 'name': 'crosstalk', 'version': '1.2.1'}, {'type': 'r', 'name': 'plotly', 'version': '4.10.4'}, {'type': 'r', 'name': 'mixtools', 'version': '2.0.0'}, {'type': 'r', 'name': 'cluster', 'version': '2.1.6'}, {'type': 'r', 'name': 'gclus', 'version': '1.3.2'}, {'type': 'r', 'name': 'coda', 'version': '0.19-4.1'}, {'type': 'r', 'name': 'doMC', 'version': '1.3.8'}, {'type': 'r', 'name': 'DBI', 'version': '1.2.3'}, {'type': 'r', 'name': 'gam', 'version': '1.22-5'}, {'type': 'r', 'name': 'gamlss.data', 'version': '6.0-6'}, {'type': 'r', 'name': 'gamlss.dist', 'version': '6.1-1'}, {'type': 'r', 'name': 'gamlss', 'version': '5.4-22'}, {'type': 'r', 'name': 'gamlss.tr', 'version': '5.1-9'}, {'type': 'r', 'name': 'hwriter', 'version': '1.3.2.1'}, {'type': 'r', 'name': 'xts', 'version': '0.14.1'}, {'type': 'r', 'name': 'TTR', 'version': '0.24.4'}, {'type': 'r', 'name': 'quantmod', 'version': '0.4.26'}, {'type': 'r', 'name': 'mvtnorm', 'version': '1.3-2'}, {'type': 'r', 'name': 'pcaPP', 'version': '2.0-5'}, {'type': 'r', 'name': 'pscl', 'version': '1.5.9'}, {'type': 'r', 'name': 'blob', 'version': '1.2.4'}, {'type': 'r', 'name': 'RSQLite', 'version': '2.3.8'}, {'type': 'r', 'name': 'BatchJobs', 'version': '1.9'}, {'type': 'r', 'name': 'sandwich', 'version': '3.1-1'}, {'type': 'r', 'name': 'sfsmisc', 'version': '1.1-20'}, {'type': 'r', 'name': 'spatial', 'version': '7.3-17'}, {'type': 'r', 'name': 'VGAM', 'version': '1.1-12'}, {'type': 'r', 'name': 'multitaper', 'version': '1.0-17'}, {'type': 'r', 'name': 'waveslim', 'version': '1.8.5'}, {'type': 'r', 'name': 'profileModel', 'version': '0.6.1'}, {'type': 'r', 'name': 'brglm', 'version': '0.7.2'}, {'type': 'r', 'name': 'deSolve', 'version': '1.40'}, {'type': 'r', 'name': 'tseriesChaos', 'version': '0.1-13.1'}, {'type': 'r', 'name': 'tseries', 'version': '0.10-58'}, {'type': 'r', 'name': 'fastICA', 'version': '1.2-5.1'}, {'type': 'r', 'name': 'R.methodsS3', 'version': '1.8.2'}, {'type': 'r', 'name': 'R.oo', 'version': '1.27.0'}, {'type': 'r', 'name': 'cgdsr', 'version': '1.3.0'}, {'type': 'r', 'name': 'R.utils', 'version': '2.12.3'}, {'type': 'r', 'name': 'R.matlab', 'version': '3.7.0'}, {'type': 'r', 'name': 'gridExtra', 'version': '2.3'}, {'type': 'r', 'name': 'gbm', 'version': '2.2.2'}, {'type': 'r', 'name': 'Formula', 'version': '1.2-5'}, {'type': 'r', 'name': 'acepack', 'version': '1.4.2'}, {'type': 'r', 'name': 'proto', 'version': '1.0.0'}, {'type': 'r', 'name': 'chron', 'version': '2.3-61'}, {'type': 'r', 'name': 'viridis', 'version': '0.6.5'}, {'type': 'r', 'name': 'htmlTable', 'version': '2.4.3'}, {'type': 'r', 'name': 'Hmisc', 'version': '5.2-0'}, {'type': 'r', 'name': 'fastcluster', 'version': '1.2.6'}, {'type': 'r', 'name': 'registry', 'version': '0.5-1'}, {'type': 'r', 'name': 'bibtex', 'version': '0.5.1'}, {'type': 'r', 'name': 'pkgmaker', 'version': '0.32.10'}, {'type': 'r', 'name': 'rngtools', 'version': '1.5.2'}, {'type': 'r', 'name': 'doParallel', 'version': '1.0.17'}, {'type': 'r', 'name': 'gridBase', 'version': '0.4-7'}, {'type': 'r', 'name': 'irlba', 'version': '2.3.5.1'}, {'type': 'r', 'name': 'igraph', 'version': '2.1.1'}, {'type': 'r', 'name': 'GeneNet', 'version': '1.2.16'}, {'type': 'r', 'name': 'ape', 'version': '5.8'}, {'type': 'r', 'name': 'RJSONIO', 'version': '1.3-1.9'}, {'type': 'r', 'name': 'caTools', 'version': '1.18.3'}, {'type': 'r', 'name': 'gplots', 'version': '3.2.0'}, {'type': 'r', 'name': 'ROCR', 'version': '1.0-11'}, {'type': 'r', 'name': 'rjson', 'version': '0.2.23'}, {'type': 'r', 'name': 'seqinr', 'version': '4.2-36'}, {'type': 'r', 'name': 'LearnBayes', 'version': '2.15.1'}, {'type': 'r', 'name': 'gmodels', 'version': '2.19.1'}, {'type': 'r', 'name': 'expm', 'version': '1.0-0'}, {'type': 'r', 'name': 'terra', 'version': '1.7-83'}, {'type': 'r', 'name': 'raster', 'version': '3.6-30'}, {'type': 'r', 'name': 'spData', 'version': '2.3.3'}, {'type': 'r', 'name': 'units', 'version': '0.8-5'}, {'type': 'r', 'name': 'classInt', 'version': '0.4-10'}, {'type': 'r', 'name': 'vegan', 'version': '2.6-8'}, {'type': 'r', 'name': 'rncl', 'version': '0.8.7'}, {'type': 'r', 'name': 'XML', 'version': '3.99-0.17'}, {'type': 'r', 'name': 'reshape', 'version': '0.8.9'}, {'type': 'r', 'name': 'triebeard', 'version': '0.4.1'}, {'type': 'r', 'name': 'urltools', 'version': '1.7.3'}, {'type': 'r', 'name': 'httpcode', 'version': '0.3.0'}, {'type': 'r', 'name': 'crul', 'version': '1.5.0'}, {'type': 'r', 'name': 'bold', 'version': '1.3.0'}, {'type': 'r', 'name': 'rredlist', 'version': '0.7.1'}, {'type': 'r', 'name': 'rentrez', 'version': '1.2.3'}, {'type': 'r', 'name': 'rotl', 'version': '3.1.0'}, {'type': 'r', 'name': 'solrium', 'version': '1.2.0'}, {'type': 'r', 'name': 'ritis', 'version': '1.0.0'}, {'type': 'r', 'name': 'worrms', 'version': '0.4.3'}, {'type': 'r', 'name': 'natserv', 'version': '1.0.0'}, {'type': 'r', 'name': 'WikipediR', 'version': '1.7.1'}, {'type': 'r', 'name': 'ratelimitr', 'version': '0.4.1'}, {'type': 'r', 'name': 'rex', 'version': '1.2.1'}, {'type': 'r', 'name': 'WikidataQueryServiceR', 'version': '1.0.0'}, {'type': 'r', 'name': 'pbapply', 'version': '1.7-2'}, {'type': 'r', 'name': 'WikidataR', 'version': '2.3.3'}, {'type': 'r', 'name': 'wikitaxa', 'version': '0.4.0'}, {'type': 'r', 'name': 'phangorn', 'version': '2.12.1'}, {'type': 'r', 'name': 'uuid', 'version': '1.2-1'}, {'type': 'r', 'name': 'conditionz', 'version': '0.1.0'}, {'type': 'r', 'name': 'taxize', 'version': '0.9.100.1'}, {'type': 'r', 'name': 'RNeXML', 'version': '2.4.11'}, {'type': 'r', 'name': 'phylobase', 'version': '0.8.12'}, {'type': 'r', 'name': 'magick', 'version': '2.8.5'}, {'type': 'r', 'name': 'animation', 'version': '2.7'}, {'type': 'r', 'name': 'bigmemory.sri', 'version': '0.1.8'}, {'type': 'r', 'name': 'bigmemory', 'version': '4.6.4'}, {'type': 'r', 'name': 'calibrate', 'version': '1.7.7'}, {'type': 'r', 'name': 'clusterGeneration', 'version': '1.3.8'}, {'type': 'r', 'name': 'dismo', 'version': '1.3-14'}, {'type': 'r', 'name': 'extrafontdb', 'version': '1.0'}, {'type': 'r', 'name': 'Rttf2pt1', 'version': '1.3.12'}, {'type': 'r', 'name': 'extrafont', 'version': '0.19'}, {'type': 'r', 'name': 'fields', 'version': '16.3'}, {'type': 'r', 'name': 'shapefiles', 'version': '0.7.2'}, {'type': 'r', 'name': 'fossil', 'version': '0.4.0'}, {'type': 'r', 'name': 'optimParallel', 'version': '1.0-2'}, {'type': 'r', 'name': 'DEoptim', 'version': '2.2-8'}, {'type': 'r', 'name': 'phytools', 'version': '2.3-0'}, {'type': 'r', 'name': 'geiger', 'version': '2.0.11'}, {'type': 'r', 'name': 'webshot', 'version': '0.5.5'}, {'type': 'r', 'name': 'shinyjs', 'version': '2.1.0'}, {'type': 'r', 'name': 'manipulateWidget', 'version': '0.11.1'}, {'type': 'r', 'name': 'rgl', 'version': '1.3.14'}, {'type': 'r', 'name': 'Rtsne', 'version': '0.17'}, {'type': 'r', 'name': 'labdsv', 'version': '2.1-0'}, {'type': 'r', 'name': 'stabs', 'version': '0.6-4'}, {'type': 'r', 'name': 'modeltools', 'version': '0.2-23'}, {'type': 'r', 'name': 'strucchange', 'version': '1.5-4'}, {'type': 'r', 'name': 'TH.data', 'version': '1.1-2'}, {'type': 'r', 'name': 'multcomp', 'version': '1.4-26'}, {'type': 'r', 'name': 'libcoin', 'version': '1.0-10'}, {'type': 'r', 'name': 'coin', 'version': '1.4-3'}, {'type': 'r', 'name': 'party', 'version': '1.3-17'}, {'type': 'r', 'name': 'inum', 'version': '1.0-5'}, {'type': 'r', 'name': 'partykit', 'version': '1.2-22'}, {'type': 'r', 'name': 'mboost', 'version': '2.9-11'}, {'type': 'r', 'name': 'msm', 'version': '1.8.2'}, {'type': 'r', 'name': 'nor1mix', 'version': '1.3-3'}, {'type': 'r', 'name': 'np', 'version': '0.60-17'}, {'type': 'r', 'name': 'polynom', 'version': '1.4-1'}, {'type': 'r', 'name': 'polspline', 'version': '1.1.25'}, {'type': 'r', 'name': 'rms', 'version': '6.8-2'}, {'type': 'r', 'name': 'RWekajars', 'version': '3.9.3-2'}, {'type': 'r', 'name': 'RWeka', 'version': '0.4-46'}, {'type': 'r', 'name': 'slam', 'version': '0.1-55'}, {'type': 'r', 'name': 'tm', 'version': '0.7-15'}, {'type': 'r', 'name': 'leaps', 'version': '3.2'}, {'type': 'r', 'name': 'cNORM', 'version': '3.4.0'}, {'type': 'r', 'name': 'weights', 'version': '1.0.4'}, {'type': 'r', 'name': 'TraMineR', 'version': '2.2-10'}, {'type': 'r', 'name': 'chemometrics', 'version': '1.4.4'}, {'type': 'r', 'name': 'FNN', 'version': '1.1.4.1'}, {'type': 'r', 'name': 'miscTools', 'version': '0.6-28'}, {'type': 'r', 'name': 'maxLik', 'version': '1.5-2.1'}, {'type': 'r', 'name': 'gbRd', 'version': '0.4.12'}, {'type': 'r', 'name': 'rbibutils', 'version': '2.3'}, {'type': 'r', 'name': 'Rdpack', 'version': '2.6.2'}, {'type': 'r', 'name': 'dfidx', 'version': '0.1-0'}, {'type': 'r', 'name': 'mlogit', 'version': '1.1-1'}, {'type': 'r', 'name': 'getopt', 'version': '1.20.4'}, {'type': 'r', 'name': 'gsalib', 'version': '2.2.1'}, {'type': 'r', 'name': 'optparse', 'version': '1.7.5'}, {'type': 'r', 'name': 'labelled', 'version': '2.13.0'}, {'type': 'r', 'name': 'R.cache', 'version': '0.16.0'}, {'type': 'r', 'name': 'styler', 'version': '1.10.3'}, {'type': 'r', 'name': 'questionr', 'version': '0.7.8'}, {'type': 'r', 'name': 'klaR', 'version': '1.7-3'}, {'type': 'r', 'name': 'neuRosim', 'version': '0.2-14'}, {'type': 'r', 'name': 'locfit', 'version': '1.5-9.10'}, {'type': 'r', 'name': 'patchwork', 'version': '1.3.0'}, {'type': 'r', 'name': 'cards', 'version': '0.3.0'}, {'type': 'r', 'name': 'broom.helpers', 'version': '1.17.0'}, {'type': 'r', 'name': 'ggstats', 'version': '0.7.0'}, {'type': 'r', 'name': 'GGally', 'version': '2.2.1'}, {'type': 'r', 'name': 'beanplot', 'version': '1.3.1'}, {'type': 'r', 'name': 'clValid', 'version': '0.7'}, {'type': 'r', 'name': 'DiscriMiner', 'version': '0.1-29'}, {'type': 'r', 'name': 'ellipse', 'version': '0.5.0'}, {'type': 'r', 'name': 'cowplot', 'version': '1.1.3'}, {'type': 'r', 'name': 'Deriv', 'version': '4.1.6'}, {'type': 'r', 'name': 'modelr', 'version': '0.1.11'}, {'type': 'r', 'name': 'microbenchmark', 'version': '1.5.0'}, {'type': 'r', 'name': 'doBy', 'version': '4.6.24'}, {'type': 'r', 'name': 'pbkrtest', 'version': '0.5.3'}, {'type': 'r', 'name': 'carData', 'version': '3.0-5'}, {'type': 'r', 'name': 'maptools', 'version': '1.1-8'}, {'type': 'r', 'name': 'openxlsx', 'version': '4.2.7.1'}, {'type': 'r', 'name': 'rematch', 'version': '2.0.0'}, {'type': 'r', 'name': 'cellranger', 'version': '1.1.0'}, {'type': 'r', 'name': 'readxl', 'version': '1.4.3'}, {'type': 'r', 'name': 'writexl', 'version': '1.5.1'}, {'type': 'r', 'name': 'rio', 'version': '1.2.3'}, {'type': 'r', 'name': 'car', 'version': '3.1-3'}, {'type': 'r', 'name': 'flashClust', 'version': '1.01-2'}, {'type': 'r', 'name': 'ggrepel', 'version': '0.9.6'}, {'type': 'r', 'name': 'DT', 'version': '0.33'}, {'type': 'r', 'name': 'estimability', 'version': '1.5.1'}, {'type': 'r', 'name': 'emmeans', 'version': '1.10.5'}, {'type': 'r', 'name': 'multcompView', 'version': '0.1-10'}, {'type': 'r', 'name': 'FactoMineR', 'version': '2.11'}, {'type': 'r', 'name': 'flexclust', 'version': '1.4-2'}, {'type': 'r', 'name': 'flexmix', 'version': '2.3-19'}, {'type': 'r', 'name': 'prabclus', 'version': '2.3-4'}, {'type': 'r', 'name': 'diptest', 'version': '0.77-1'}, {'type': 'r', 'name': 'trimcluster', 'version': '0.1-5'}, {'type': 'r', 'name': 'fpc', 'version': '2.2-13'}, {'type': 'r', 'name': 'BiasedUrn', 'version': '2.0.12'}, {'type': 'r', 'name': 'TeachingDemos', 'version': '2.13'}, {'type': 'r', 'name': 'kohonen', 'version': '3.0.12'}, {'type': 'r', 'name': 'base64', 'version': '2.0.2'}, {'type': 'r', 'name': 'doRNG', 'version': '1.8.6'}, {'type': 'r', 'name': 'nleqslv', 'version': '3.3.5'}, {'type': 'r', 'name': 'RGCCA', 'version': '3.0.3'}, {'type': 'r', 'name': 'pheatmap', 'version': '1.0.12'}, {'type': 'r', 'name': 'pvclust', 'version': '2.2-0'}, {'type': 'r', 'name': 'RCircos', 'version': '1.2.2'}, {'type': 'r', 'name': 'lambda.r', 'version': '1.2.4'}, {'type': 'r', 'name': 'futile.options', 'version': '1.0.1'}, {'type': 'r', 'name': 'futile.logger', 'version': '1.4.3'}, {'type': 'r', 'name': 'VennDiagram', 'version': '1.7.3'}, {'type': 'r', 'name': 'xlsxjars', 'version': '0.6.1'}, {'type': 'r', 'name': 'xlsx', 'version': '0.6.5'}, {'type': 'r', 'name': 'uroot', 'version': '2.1-3'}, {'type': 'r', 'name': 'forecast', 'version': '8.23.0'}, {'type': 'r', 'name': 'fma', 'version': '2.5'}, {'type': 'r', 'name': 'expsmooth', 'version': '2.3'}, {'type': 'r', 'name': 'fpp', 'version': '0.5'}, {'type': 'r', 'name': 'tensor', 'version': '1.5'}, {'type': 'r', 'name': 'polyclip', 'version': '1.10-7'}, {'type': 'r', 'name': 'goftest', 'version': '1.2-3'}, {'type': 'r', 'name': 'spatstat.utils', 'version': '3.1-1'}, {'type': 'r', 'name': 'spatstat.data', 'version': '3.1-4'}, {'type': 'r', 'name': 'spatstat.univar', 'version': '3.1-1'}, {'type': 'r', 'name': 'spatstat.geom', 'version': '3.3-4'}, {'type': 'r', 'name': 'spatstat.sparse', 'version': '3.1-0'}, {'type': 'r', 'name': 'spatstat.random', 'version': '3.3-2'}, {'type': 'r', 'name': 'spatstat.core', 'version': '2.4-4'}, {'type': 'r', 'name': 'spatstat.explore', 'version': '3.3-3'}, {'type': 'r', 'name': 'spatstat.model', 'version': '3.3-3'}, {'type': 'r', 'name': 'spatstat.linnet', 'version': '3.2-3'}, {'type': 'r', 'name': 'spatstat', 'version': '3.3-0'}, {'type': 'r', 'name': 'pracma', 'version': '2.4.4'}, {'type': 'r', 'name': 'RCurl', 'version': '1.98-1.16'}, {'type': 'r', 'name': 'bio3d', 'version': '2.4-5'}, {'type': 'r', 'name': 'AUC', 'version': '0.3.2'}, {'type': 'r', 'name': 'interpretR', 'version': '0.2.5'}, {'type': 'r', 'name': 'cvAUC', 'version': '1.1.4'}, {'type': 'r', 'name': 'SuperLearner', 'version': '2.0-29'}, {'type': 'r', 'name': 'mediation', 'version': '4.5.0'}, {'type': 'r', 'name': 'CVST', 'version': '0.2-3'}, {'type': 'r', 'name': 'DRR', 'version': '0.0.4'}, {'type': 'r', 'name': 'dimRed', 'version': '0.2.6'}, {'type': 'r', 'name': 'ddalpha', 'version': '1.3.16'}, {'type': 'r', 'name': 'RcppRoll', 'version': '0.3.1'}, {'type': 'r', 'name': 'rlist', 'version': '0.4.6.2'}, {'type': 'r', 'name': 'ConsRank', 'version': '2.1.4'}, {'type': 'r', 'name': 'adabag', 'version': '5.0'}, {'type': 'r', 'name': 'parallelMap', 'version': '1.5.1'}, {'type': 'r', 'name': 'ParamHelpers', 'version': '1.14.1'}, {'type': 'r', 'name': 'ggvis', 'version': '0.4.9'}, {'type': 'r', 'name': 'mlr', 'version': '2.19.2'}, {'type': 'r', 'name': 'unbalanced', 'version': '2.0'}, {'type': 'r', 'name': 'RSNNS', 'version': '0.4-17'}, {'type': 'r', 'name': 'abc.data', 'version': '1.1'}, {'type': 'r', 'name': 'abc', 'version': '2.2.1'}, {'type': 'r', 'name': 'lhs', 'version': '1.2.0'}, {'type': 'r', 'name': 'tensorA', 'version': '0.36.2.1'}, {'type': 'r', 'name': 'EasyABC', 'version': '1.5.2'}, {'type': 'r', 'name': 'git2r', 'version': '0.35.0'}, {'type': 'r', 'name': 'clisymbols', 'version': '1.2.0'}, {'type': 'r', 'name': 'covr', 'version': '3.6.4'}, {'type': 'r', 'name': 'Rook', 'version': '1.2'}, {'type': 'r', 'name': 'Cairo', 'version': '1.6-2'}, {'type': 'r', 'name': 'RMTstat', 'version': '0.3.1'}, {'type': 'r', 'name': 'Lmoments', 'version': '1.3-1'}, {'type': 'r', 'name': 'distillery', 'version': '1.2-1'}, {'type': 'r', 'name': 'extRemes', 'version': '2.1-4'}, {'type': 'r', 'name': 'tkrplot', 'version': '0.0-27'}, {'type': 'r', 'name': 'misc3d', 'version': '0.9-1'}, {'type': 'r', 'name': 'multicool', 'version': '1.0.1'}, {'type': 'r', 'name': 'plot3D', 'version': '1.4.1'}, {'type': 'r', 'name': 'plot3Drgl', 'version': '1.0.4'}, {'type': 'r', 'name': 'OceanView', 'version': '1.0.7'}, {'type': 'r', 'name': 'ks', 'version': '1.14.3'}, {'type': 'r', 'name': 'logcondens', 'version': '2.1.8'}, {'type': 'r', 'name': 'Iso', 'version': '0.0-21'}, {'type': 'r', 'name': 'penalized', 'version': '0.9-52'}, {'type': 'r', 'name': 'clusterRepro', 'version': '0.9'}, {'type': 'r', 'name': 'data.tree', 'version': '1.1.0'}, {'type': 'r', 'name': 'influenceR', 'version': '0.1.5'}, {'type': 'r', 'name': 'visNetwork', 'version': '2.1.2'}, {'type': 'r', 'name': 'downloader', 'version': '0.4'}, {'type': 'r', 'name': 'DiagrammeR', 'version': '1.0.11'}, {'type': 'r', 'name': 'randomForestSRC', 'version': '3.3.1'}, {'type': 'r', 'name': 'sm', 'version': '2.2-6.0'}, {'type': 'r', 'name': 'pbivnorm', 'version': '0.6.0'}, {'type': 'r', 'name': 'lavaan', 'version': '0.6-19'}, {'type': 'r', 'name': 'matrixcalc', 'version': '1.0-6'}, {'type': 'r', 'name': 'arm', 'version': '1.14-4'}, {'type': 'r', 'name': 'mi', 'version': '1.1'}, {'type': 'r', 'name': 'servr', 'version': '0.32'}, {'type': 'r', 'name': 'rgexf', 'version': '0.16.3'}, {'type': 'r', 'name': 'sem', 'version': '3.1-16'}, {'type': 'r', 'name': 'statnet.common', 'version': '4.10.0'}, {'type': 'r', 'name': 'network', 'version': '1.18.2'}, {'type': 'r', 'name': 'rle', 'version': '0.9.2'}, {'type': 'r', 'name': 'sna', 'version': '2.8'}, {'type': 'r', 'name': 'glasso', 'version': '1.11'}, {'type': 'r', 'name': 'huge', 'version': '1.3.5'}, {'type': 'r', 'name': 'd3Network', 'version': '0.5.2.1'}, {'type': 'r', 'name': 'BDgraph', 'version': '2.73'}, {'type': 'r', 'name': 'graphlayouts', 'version': '1.2.1'}, {'type': 'r', 'name': 'tweenr', 'version': '2.0.3'}, {'type': 'r', 'name': 'ggforce', 'version': '0.4.2'}, {'type': 'r', 'name': 'tidygraph', 'version': '1.3.1'}, {'type': 'r', 'name': 'ggraph', 'version': '2.2.1'}, {'type': 'r', 'name': 'qgraph', 'version': '1.9.8'}, {'type': 'r', 'name': 'HWxtest', 'version': '1.1.9'}, {'type': 'r', 'name': 'diveRsity', 'version': '1.9.90'}, {'type': 'r', 'name': 'doSNOW', 'version': '1.0.20'}, {'type': 'r', 'name': 'geepack', 'version': '1.3.12'}, {'type': 'r', 'name': 'biom', 'version': '0.3.12'}, {'type': 'r', 'name': 'pim', 'version': '2.0.2'}, {'type': 'r', 'name': 'minpack.lm', 'version': '1.2-4'}, {'type': 'r', 'name': 'rootSolve', 'version': '1.8.2.4'}, {'type': 'r', 'name': 'FME', 'version': '1.3.6.3'}, {'type': 'r', 'name': 'bmp', 'version': '0.3'}, {'type': 'r', 'name': 'tiff', 'version': '0.1-12'}, {'type': 'r', 'name': 'readbitmap', 'version': '0.1.5'}, {'type': 'r', 'name': 'imager', 'version': '1.0.2'}, {'type': 'r', 'name': 'signal', 'version': '1.8-1'}, {'type': 'r', 'name': 'tuneR', 'version': '1.4.7'}, {'type': 'r', 'name': 'pastecs', 'version': '1.4.2'}, {'type': 'r', 'name': 'audio', 'version': '0.1-11'}, {'type': 'r', 'name': 'fftw', 'version': '1.0-9'}, {'type': 'r', 'name': 'seewave', 'version': '2.2.3'}, {'type': 'r', 'name': 'gsw', 'version': '1.2-0'}, {'type': 'r', 'name': 'wk', 'version': '0.9.4'}, {'type': 'r', 'name': 's2', 'version': '1.1.7'}, {'type': 'r', 'name': 'sf', 'version': '1.0-19'}, {'type': 'r', 'name': 'oce', 'version': '1.8-3'}, {'type': 'r', 'name': 'ineq', 'version': '0.2-13'}, {'type': 'r', 'name': 'soundecology', 'version': '1.3.3'}, {'type': 'r', 'name': 'memuse', 'version': '4.2-3'}, {'type': 'r', 'name': 'pinfsc50', 'version': '1.3.0'}, {'type': 'r', 'name': 'vcfR', 'version': '1.15.0'}, {'type': 'r', 'name': 'glmmML', 'version': '1.1.7'}, {'type': 'r', 'name': 'tsne', 'version': '0.1-3.1'}, {'type': 'r', 'name': 'sn', 'version': '2.1.1'}, {'type': 'r', 'name': 'tclust', 'version': '2.0-5'}, {'type': 'r', 'name': 'ranger', 'version': '0.17.0'}, {'type': 'r', 'name': 'hexbin', 'version': '1.28.5'}, {'type': 'r', 'name': 'lobstr', 'version': '1.1.2'}, {'type': 'r', 'name': 'pryr', 'version': '0.1.6'}, {'type': 'r', 'name': 'moments', 'version': '0.14.1'}, {'type': 'r', 'name': 'laeken', 'version': '0.5.3'}, {'type': 'r', 'name': 'VIM', 'version': '6.2.2'}, {'type': 'r', 'name': 'smoother', 'version': '1.3'}, {'type': 'r', 'name': 'dynamicTreeCut', 'version': '1.63-1'}, {'type': 'r', 'name': 'beeswarm', 'version': '0.4.0'}, {'type': 'r', 'name': 'vipor', 'version': '0.4.7'}, {'type': 'r', 'name': 'ggbeeswarm', 'version': '0.7.2'}, {'type': 'r', 'name': 'shinydashboard', 'version': '0.7.2'}, {'type': 'r', 'name': 'rrcov', 'version': '1.7-6'}, {'type': 'r', 'name': 'WriteXLS', 'version': '6.7.0'}, {'type': 'r', 'name': 'bst', 'version': '0.3-24'}, {'type': 'r', 'name': 'pamr', 'version': '1.57'}, {'type': 'r', 'name': 'WeightSVM', 'version': '1.7-16'}, {'type': 'r', 'name': 'mpath', 'version': '0.4-2.26'}, {'type': 'r', 'name': 'timereg', 'version': '2.0.6'}, {'type': 'r', 'name': 'peperr', 'version': '1.5'}, {'type': 'r', 'name': 'heatmap3', 'version': '1.1.9'}, {'type': 'r', 'name': 'GlobalOptions', 'version': '0.1.2'}, {'type': 'r', 'name': 'circlize', 'version': '0.4.16'}, {'type': 'r', 'name': 'GetoptLong', 'version': '1.0.5'}, {'type': 'r', 'name': 'dendextend', 'version': '1.19.0'}, {'type': 'r', 'name': 'RInside', 'version': '0.2.18'}, {'type': 'r', 'name': 'limSolve', 'version': '1.5.7.1'}, {'type': 'r', 'name': 'dbplyr', 'version': '2.5.0'}, {'type': 'r', 'name': 'debugme', 'version': '1.2.0'}, {'type': 'r', 'name': 'reprex', 'version': '2.1.1'}, {'type': 'r', 'name': 'selectr', 'version': '0.4-2'}, {'type': 'r', 'name': 'rvest', 'version': '1.0.4'}, {'type': 'r', 'name': 'dtplyr', 'version': '1.3.1'}, {'type': 'r', 'name': 'gargle', 'version': '1.5.2'}, {'type': 'r', 'name': 'googledrive', 'version': '2.1.1'}, {'type': 'r', 'name': 'ids', 'version': '1.0.1'}, {'type': 'r', 'name': 'googlesheets4', 'version': '1.1.1'}, {'type': 'r', 'name': 'conflicted', 'version': '1.2.0'}, {'type': 'r', 'name': 'tidyverse', 'version': '2.0.0'}, {'type': 'r', 'name': 'R.rsp', 'version': '0.46.0'}, {'type': 'r', 'name': 'gdistance', 'version': '1.6.4'}, {'type': 'r', 'name': 'vioplot', 'version': '0.5.0'}, {'type': 'r', 'name': 'emulator', 'version': '1.2-24'}, {'type': 'r', 'name': 'gmm', 'version': '1.8'}, {'type': 'r', 'name': 'tmvtnorm', 'version': '1.6'}, {'type': 'r', 'name': 'IDPmisc', 'version': '1.1.21'}, {'type': 'r', 'name': 'gap.datasets', 'version': '0.0.6'}, {'type': 'r', 'name': 'gap', 'version': '1.6'}, {'type': 'r', 'name': 'qrnn', 'version': '2.1.1'}, {'type': 'r', 'name': 'TMB', 'version': '1.9.15'}, {'type': 'r', 'name': 'reformulas', 'version': '0.4.0'}, {'type': 'r', 'name': 'glmmTMB', 'version': '1.1.10'}, {'type': 'r', 'name': 'gmp', 'version': '0.7-5'}, {'type': 'r', 'name': 'ROI', 'version': '1.0-1'}, {'type': 'r', 'name': 'Rglpk', 'version': '0.6-5.1'}, {'type': 'r', 'name': 'ROI.plugin.glpk', 'version': '1.0-0'}, {'type': 'r', 'name': 'spaMM', 'version': '4.5.0'}, {'type': 'r', 'name': 'qgam', 'version': '1.3.4'}, {'type': 'r', 'name': 'DHARMa', 'version': '0.4.7'}, {'type': 'r', 'name': 'mvnfast', 'version': '0.2.8'}, {'type': 'r', 'name': 'bridgesampling', 'version': '1.1-2'}, {'type': 'r', 'name': 'BayesianTools', 'version': '0.1.8'}, {'type': 'r', 'name': 'gomms', 'version': '1.0'}, {'type': 'r', 'name': 'feather', 'version': '0.3.5'}, {'type': 'r', 'name': 'dummies', 'version': '1.5.6'}, {'type': 'r', 'name': 'SimSeq', 'version': '1.4.0'}, {'type': 'r', 'name': 'uniqueAtomMat', 'version': '0.1-3-2'}, {'type': 'r', 'name': 'PoissonSeq', 'version': '1.1.2'}, {'type': 'r', 'name': 'aod', 'version': '1.3.3'}, {'type': 'r', 'name': 'cghFLasso', 'version': '0.2-1'}, {'type': 'r', 'name': 'svd', 'version': '0.5.7'}, {'type': 'r', 'name': 'Rssa', 'version': '1.1'}, {'type': 'r', 'name': 'JBTools', 'version': '0.7.2.9'}, {'type': 'r', 'name': 'RUnit', 'version': '0.4.33'}, {'type': 'r', 'name': 'DistributionUtils', 'version': '0.6-1'}, {'type': 'r', 'name': 'gapfill', 'version': '0.9.6-1'}, {'type': 'r', 'name': 'gee', 'version': '4.13-27'}, {'type': 'r', 'name': 'Matching', 'version': '4.10-15'}, {'type': 'r', 'name': 'chk', 'version': '0.9.2'}, {'type': 'r', 'name': 'MatchIt', 'version': '4.6.0'}, {'type': 'r', 'name': 'RItools', 'version': '0.3-4'}, {'type': 'r', 'name': 'mitools', 'version': '2.4'}, {'type': 'r', 'name': 'survey', 'version': '4.4-2'}, {'type': 'r', 'name': 'rlemon', 'version': '0.2.1'}, {'type': 'r', 'name': 'optmatch', 'version': '0.10.8'}, {'type': 'r', 'name': 'SPAtest', 'version': '3.1.2'}, {'type': 'r', 'name': 'RSpectra', 'version': '0.16-2'}, {'type': 'r', 'name': 'SKAT', 'version': '2.2.5'}, {'type': 'r', 'name': 'GillespieSSA', 'version': '0.6.2'}, {'type': 'r', 'name': 'startupmsg', 'version': '0.9.7'}, {'type': 'r', 'name': 'distr', 'version': '2.9.5'}, {'type': 'r', 'name': 'distrEx', 'version': '2.9.5'}, {'type': 'r', 'name': 'minerva', 'version': '1.5.10'}, {'type': 'r', 'name': 'RcppTOML', 'version': '0.2.2'}, {'type': 'r', 'name': 'here', 'version': '1.0.1'}, {'type': 'r', 'name': 'reticulate', 'version': '1.40.0'}, {'type': 'r', 'name': 'umap', 'version': '0.2.10.0'}, {'type': 'r', 'name': 'KODAMA', 'version': '2.4.1'}, {'type': 'r', 'name': 'locfdr', 'version': '1.1-8'}, {'type': 'r', 'name': 'ica', 'version': '1.0-3'}, {'type': 'r', 'name': 'dtw', 'version': '1.23-1'}, {'type': 'r', 'name': 'SDMTools', 'version': '1.1-221.2'}, {'type': 'r', 'name': 'ggridges', 'version': '0.5.6'}, {'type': 'r', 'name': 'TFisher', 'version': '0.2.0'}, {'type': 'r', 'name': 'lsei', 'version': '1.3-0'}, {'type': 'r', 'name': 'npsurv', 'version': '0.5-0'}, {'type': 'r', 'name': 'fitdistrplus', 'version': '1.2-1'}, {'type': 'r', 'name': 'hdf5r', 'version': '1.3.11'}, {'type': 'r', 'name': 'DTRreg', 'version': '2.2'}, {'type': 'r', 'name': 'pulsar', 'version': '0.3.11'}, {'type': 'r', 'name': 'bayesm', 'version': '3.1-6'}, {'type': 'r', 'name': 'gsl', 'version': '2.1-8'}, {'type': 'r', 'name': 'energy', 'version': '1.7-12'}, {'type': 'r', 'name': 'compositions', 'version': '2.0-8'}, {'type': 'r', 'name': 'clustree', 'version': '0.5.1'}, {'type': 'r', 'name': 'tweedie', 'version': '2.3.5'}, {'type': 'r', 'name': 'RcppGSL', 'version': '0.3.13'}, {'type': 'r', 'name': 'mvabund', 'version': '4.2.1'}, {'type': 'r', 'name': 'fishMod', 'version': '0.29.2'}, {'type': 'r', 'name': 'alabama', 'version': '2023.1.0'}, {'type': 'r', 'name': 'gllvm', 'version': '1.4.3'}, {'type': 'r', 'name': 'grpreg', 'version': '3.5.0'}, {'type': 'r', 'name': 'trust', 'version': '0.1-8'}, {'type': 'r', 'name': 'lpSolveAPI', 'version': '5.5.2.0-17.12'}, {'type': 'r', 'name': 'ergm', 'version': '4.7.5'}, {'type': 'r', 'name': 'networkLite', 'version': '1.0.5'}, {'type': 'r', 'name': 'networkDynamic', 'version': '0.11.5'}, {'type': 'r', 'name': 'ergm.multi', 'version': '0.2.1.1'}, {'type': 'r', 'name': 'tergm', 'version': '4.2.1'}, {'type': 'r', 'name': 'ergm.count', 'version': '4.1.2'}, {'type': 'r', 'name': 'tsna', 'version': '0.3.5'}, {'type': 'r', 'name': 'statnet', 'version': '2019.6'}, {'type': 'r', 'name': 'aggregation', 'version': '1.0.1'}, {'type': 'r', 'name': 'ComICS', 'version': '1.0.4'}, {'type': 'r', 'name': 'dtangle', 'version': '2.0.9'}, {'type': 'r', 'name': 'mcmc', 'version': '0.9-8'}, {'type': 'r', 'name': 'MCMCpack', 'version': '1.7-1'}, {'type': 'r', 'name': 'shinythemes', 'version': '1.2.0'}, {'type': 'r', 'name': 'csSAM', 'version': '1.2.4'}, {'type': 'r', 'name': 'bridgedist', 'version': '0.1.3'}, {'type': 'r', 'name': 'asnipe', 'version': '1.1.17'}, {'type': 'r', 'name': 'liquidSVM', 'version': '1.2.4'}, {'type': 'r', 'name': 'oddsratio', 'version': '2.0.1'}, {'type': 'r', 'name': 'mltools', 'version': '0.3.5'}, {'type': 'r', 'name': 'h2o', 'version': '3.44.0.3'}, {'type': 'r', 'name': 'mlegp', 'version': '3.1.9'}, {'type': 'r', 'name': 'itertools', 'version': '0.1-3'}, {'type': 'r', 'name': 'missForest', 'version': '1.5'}, {'type': 'r', 'name': 'bartMachineJARs', 'version': '1.2.1'}, {'type': 'r', 'name': 'bartMachine', 'version': '1.3.4.1'}, {'type': 'r', 'name': 'lqa', 'version': '1.0-3'}, {'type': 'r', 'name': 'PresenceAbsence', 'version': '1.1.11'}, {'type': 'r', 'name': 'GUTS', 'version': '1.2.5'}, {'type': 'r', 'name': 'GenSA', 'version': '1.1.14.1'}, {'type': 'r', 'name': 'parsedate', 'version': '1.3.1'}, {'type': 'r', 'name': 'circular', 'version': '0.5-1'}, {'type': 'r', 'name': 'cobs', 'version': '1.3-8'}, {'type': 'r', 'name': 'resample', 'version': '0.6'}, {'type': 'r', 'name': 'MIIVsem', 'version': '0.5.8'}, {'type': 'r', 'name': 'medflex', 'version': '0.6-10'}, {'type': 'r', 'name': 'Rserve', 'version': '1.8-13'}, {'type': 'r', 'name': 'spls', 'version': '2.2-3'}, {'type': 'r', 'name': 'Boruta', 'version': '8.0.0'}, {'type': 'r', 'name': 'dr', 'version': '3.0.10'}, {'type': 'r', 'name': 'CovSel', 'version': '1.2.1'}, {'type': 'r', 'name': 'tmle', 'version': '2.0.1.1'}, {'type': 'r', 'name': 'ctmle', 'version': '0.1.2'}, {'type': 'r', 'name': 'BayesPen', 'version': '1.0'}, {'type': 'r', 'name': 'inline', 'version': '0.3.20'}, {'type': 'r', 'name': 'BMA', 'version': '3.18.19'}, {'type': 'r', 'name': 'BCEE', 'version': '1.3.2'}, {'type': 'r', 'name': 'bacr', 'version': '1.0.1'}, {'type': 'r', 'name': 'clue', 'version': '0.3-66'}, {'type': 'r', 'name': 'bdsmatrix', 'version': '1.3-7'}, {'type': 'r', 'name': 'fftwtools', 'version': '0.9-11'}, {'type': 'r', 'name': 'imagerExtra', 'version': '1.3.2'}, {'type': 'r', 'name': 'MALDIquant', 'version': '1.22.3'}, {'type': 'r', 'name': 'threejs', 'version': '0.3.3'}, {'type': 'r', 'name': 'LaplacesDemon', 'version': '16.1.6'}, {'type': 'r', 'name': 'rda', 'version': '1.2-1'}, {'type': 'r', 'name': 'sampling', 'version': '2.10'}, {'type': 'r', 'name': 'lda', 'version': '1.5.2'}, {'type': 'r', 'name': 'jiebaRD', 'version': '0.1'}, {'type': 'r', 'name': 'jiebaR', 'version': '0.11'}, {'type': 'r', 'name': 'hdm', 'version': '0.3.2'}, {'type': 'r', 'name': 'abe', 'version': '3.0.1'}, {'type': 'r', 'name': 'SignifReg', 'version': '4.3'}, {'type': 'r', 'name': 'bbmle', 'version': '1.0.25.1'}, {'type': 'r', 'name': 'emdbook', 'version': '1.3.13'}, {'type': 'r', 'name': 'SOAR', 'version': '0.99-11'}, {'type': 'r', 'name': 'rasterVis', 'version': '0.51.6'}, {'type': 'r', 'name': 'tictoc', 'version': '1.2.1'}, {'type': 'r', 'name': 'ISOcodes', 'version': '2024.02.12'}, {'type': 'r', 'name': 'stopwords', 'version': '2.3'}, {'type': 'r', 'name': 'janeaustenr', 'version': '1.0.0'}, {'type': 'r', 'name': 'SnowballC', 'version': '0.7.1'}, {'type': 'r', 'name': 'tokenizers', 'version': '0.3.0'}, {'type': 'r', 'name': 'hunspell', 'version': '3.0.5'}, {'type': 'r', 'name': 'topicmodels', 'version': '0.2-17'}, {'type': 'r', 'name': 'tidytext', 'version': '0.4.2'}, {'type': 'r', 'name': 'splitstackshape', 'version': '1.4.8'}, {'type': 'r', 'name': 'grImport2', 'version': '0.3-3'}, {'type': 'r', 'name': 'preseqR', 'version': '4.0.0'}, {'type': 'r', 'name': 'idr', 'version': '1.3'}, {'type': 'r', 'name': 'entropy', 'version': '1.3.1'}, {'type': 'r', 'name': 'kedd', 'version': '1.0.4'}, {'type': 'r', 'name': 'HiddenMarkov', 'version': '1.8-13'}, {'type': 'r', 'name': 'lmerTest', 'version': '3.1-3'}, {'type': 'r', 'name': 'distributional', 'version': '0.5.0'}, {'type': 'r', 'name': 'posterior', 'version': '1.6.0'}, {'type': 'r', 'name': 'loo', 'version': '2.8.0'}, {'type': 'r', 'name': 'RcppParallel', 'version': '5.1.9'}, {'type': 'r', 'name': 'StanHeaders', 'version': '2.32.10'}, {'type': 'r', 'name': 'V8', 'version': '6.0.0'}, {'type': 'r', 'name': 'QuickJSR', 'version': '1.4.0'}, {'type': 'r', 'name': 'rstan', 'version': '2.32.6'}, {'type': 'r', 'name': 'Rborist', 'version': '0.3-7'}, {'type': 'r', 'name': 'VSURF', 'version': '1.2.0'}, {'type': 'r', 'name': 'mRMRe', 'version': '2.1.2.2'}, {'type': 'r', 'name': 'dHSIC', 'version': '2.1'}, {'type': 'r', 'name': 'ggsci', 'version': '3.2.0'}, {'type': 'r', 'name': 'ggsignif', 'version': '0.6.4'}, {'type': 'r', 'name': 'corrplot', 'version': '0.95'}, {'type': 'r', 'name': 'rstatix', 'version': '0.7.2'}, {'type': 'r', 'name': 'ggfan', 'version': '0.1.3'}, {'type': 'r', 'name': 'ggpubr', 'version': '0.6.0'}, {'type': 'r', 'name': 'yaImpute', 'version': '1.0-34.1'}, {'type': 'r', 'name': 'intrinsicDimension', 'version': '1.2.0'}, {'type': 'r', 'name': 'leiden', 'version': '0.4.3.1'}, {'type': 'r', 'name': 'sctransform', 'version': '0.4.1'}, {'type': 'r', 'name': 'packrat', 'version': '0.9.2'}, {'type': 'r', 'name': 'colourpicker', 'version': '1.3.0'}, {'type': 'r', 'name': 'ggExtra', 'version': '0.10.1'}, {'type': 'r', 'name': 'findpython', 'version': '1.0.9'}, {'type': 'r', 'name': 'argparse', 'version': '2.2.4'}, {'type': 'r', 'name': 'intergraph', 'version': '2.0-4'}, {'type': 'r', 'name': 'ggnetwork', 'version': '0.5.13'}, {'type': 'r', 'name': 'qqman', 'version': '0.1.9'}, {'type': 'r', 'name': 'rstantools', 'version': '2.4.0'}, {'type': 'r', 'name': 'bayesplot', 'version': '1.11.1'}, {'type': 'r', 'name': 'dygraphs', 'version': '1.1.1.6'}, {'type': 'r', 'name': 'renv', 'version': '1.0.11'}, {'type': 'r', 'name': 'PKI', 'version': '0.1-14'}, {'type': 'r', 'name': 'rsconnect', 'version': '1.3.3'}, {'type': 'r', 'name': 'shinystan', 'version': '2.6.0'}, {'type': 'r', 'name': 'optimx', 'version': '2023-10.21'}, {'type': 'r', 'name': 'gamm4', 'version': '0.2-6'}, {'type': 'r', 'name': 'memisc', 'version': '0.99.31.8.1'}, {'type': 'r', 'name': 'mclogit', 'version': '0.9.6'}, {'type': 'r', 'name': 'projpred', 'version': '2.8.0'}, {'type': 'r', 'name': 'brms', 'version': '2.22.0'}, {'type': 'r', 'name': 'drgee', 'version': '1.1.10'}, {'type': 'r', 'name': 'stdReg', 'version': '3.4.1'}, {'type': 'r', 'name': 'mcmcse', 'version': '1.5-0'}, {'type': 'r', 'name': 'copCAR', 'version': '2.0-4'}, {'type': 'r', 'name': 'batchmeans', 'version': '1.0-4'}, {'type': 'r', 'name': 'ngspatial', 'version': '1.2-2'}, {'type': 'r', 'name': 'BIGL', 'version': '1.9.3'}, {'type': 'r', 'name': 'drugCombo', 'version': '1.2.1'}, {'type': 'r', 'name': 'betareg', 'version': '3.2-1'}, {'type': 'r', 'name': 'unmarked', 'version': '1.4.3'}, {'type': 'r', 'name': 'maxlike', 'version': '0.1-11'}, {'type': 'r', 'name': 'coxme', 'version': '2.2-22'}, {'type': 'r', 'name': 'AICcmodavg', 'version': '2.3-3'}, {'type': 'r', 'name': 'pacman', 'version': '0.5.1'}, {'type': 'r', 'name': 'spaa', 'version': '0.2.2'}, {'type': 'r', 'name': 'maxnet', 'version': '0.1.4'}, {'type': 'r', 'name': 'oai', 'version': '0.4.0'}, {'type': 'r', 'name': 'wellknown', 'version': '0.7.4'}, {'type': 'r', 'name': 'rgbif', 'version': '3.8.1'}, {'type': 'r', 'name': 'rgdal', 'version': '1.6-7'}, {'type': 'r', 'name': 'rgeos', 'version': '0.6-4'}, {'type': 'r', 'name': 'mapproj', 'version': '1.2.11'}, {'type': 'r', 'name': 'rbison', 'version': '1.0.0'}, {'type': 'r', 'name': 'rebird', 'version': '1.3.0'}, {'type': 'r', 'name': 'rvertnet', 'version': '0.8.4'}, {'type': 'r', 'name': 'leaflet.providers', 'version': '2.0.0'}, {'type': 'r', 'name': 'leaflet', 'version': '2.2.2'}, {'type': 'r', 'name': 'svglite', 'version': '2.1.3'}, {'type': 'r', 'name': 'kableExtra', 'version': '1.4.0'}, {'type': 'r', 'name': 'ridigbio', 'version': '0.4.1'}, {'type': 'r', 'name': 'spocc', 'version': '1.2.3'}, {'type': 'r', 'name': 'spThin', 'version': '0.2.0'}, {'type': 'r', 'name': 'RPostgreSQL', 'version': '0.7-7'}, {'type': 'r', 'name': 'fasterize', 'version': '1.1.0'}, {'type': 'r', 'name': 'BIEN', 'version': '1.2.6'}, {'type': 'r', 'name': 'rangeModelMetadata', 'version': '0.1.5'}, {'type': 'r', 'name': 'ENMeval', 'version': '2.0.4'}, {'type': 'r', 'name': 'plotmo', 'version': '3.6.4'}, {'type': 'r', 'name': 'earth', 'version': '5.3.4'}, {'type': 'r', 'name': 'mda', 'version': '0.5-5'}, {'type': 'r', 'name': 'xgboost', 'version': '1.7.8.1'}, {'type': 'r', 'name': 'biomod2', 'version': '4.2-5-2'}, {'type': 'r', 'name': 'poLCA', 'version': '1.6.0.1'}, {'type': 'r', 'name': 'PermAlgo', 'version': '1.2'}, {'type': 'r', 'name': 'coxed', 'version': '0.3.3'}, {'type': 'r', 'name': 'testit', 'version': '0.13'}, {'type': 'r', 'name': 'NISTunits', 'version': '1.0.1'}, {'type': 'r', 'name': 'celestial', 'version': '1.4.6'}, {'type': 'r', 'name': 'RPMM', 'version': '1.25'}, {'type': 'r', 'name': 'RefFreeEWAS', 'version': '2.2'}, {'type': 'r', 'name': 'wordcloud', 'version': '2.6'}, {'type': 'r', 'name': 'JADE', 'version': '2.0-4'}, {'type': 'r', 'name': 'awsMethods', 'version': '1.1-1'}, {'type': 'r', 'name': 'aws', 'version': '2.5-6'}, {'type': 'r', 'name': 'ruv', 'version': '0.9.7.1'}, {'type': 'r', 'name': 'mhsmm', 'version': '0.4.21'}, {'type': 'r', 'name': 'dbarts', 'version': '0.9-28'}, {'type': 'r', 'name': 'proftools', 'version': '0.99-3'}, {'type': 'r', 'name': 'NCmisc', 'version': '1.2.0'}, {'type': 'r', 'name': 'reader', 'version': '1.0.6'}, {'type': 'r', 'name': 'gnumeric', 'version': '0.7-10'}, {'type': 'r', 'name': 'tcltk2', 'version': '1.2-11'}, {'type': 'r', 'name': 'minty', 'version': '0.0.4'}, {'type': 'r', 'name': 'readODS', 'version': '2.3.1'}, {'type': 'r', 'name': 'nortest', 'version': '1.0-4'}, {'type': 'r', 'name': 'EnvStats', 'version': '3.0.0'}, {'type': 'r', 'name': 'outliers', 'version': '0.15'}, {'type': 'r', 'name': 'gWidgets2', 'version': '1.0-9'}, {'type': 'r', 'name': 'gWidgets2tcltk', 'version': '1.0-8'}, {'type': 'r', 'name': 'mgsub', 'version': '1.7.3'}, {'type': 'r', 'name': 'ie2misc', 'version': '0.9.1'}, {'type': 'r', 'name': 'assertive.base', 'version': '0.0-9'}, {'type': 'r', 'name': 'assertive.properties', 'version': '0.0-5'}, {'type': 'r', 'name': 'assertive.types', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.numbers', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.strings', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.datetimes', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.files', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.sets', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.matrices', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.models', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.data', 'version': '0.0-3'}, {'type': 'r', 'name': 'assertive.data.uk', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.data.us', 'version': '0.0-2'}, {'type': 'r', 'name': 'assertive.reflection', 'version': '0.0-5'}, {'type': 'r', 'name': 'assertive.code', 'version': '0.0-4'}, {'type': 'r', 'name': 'assertive', 'version': '0.3-6'}, {'type': 'r', 'name': 'rdrop2', 'version': '0.8.2.1'}, {'type': 'r', 'name': 'Exact', 'version': '3.3'}, {'type': 'r', 'name': 'lmom', 'version': '3.2'}, {'type': 'r', 'name': 'gld', 'version': '2.6.6'}, {'type': 'r', 'name': 'DescTools', 'version': '0.99.58'}, {'type': 'r', 'name': 'orthopolynom', 'version': '1.0-6.1'}, {'type': 'r', 'name': 'gaussquad', 'version': '1.0-3'}, {'type': 'r', 'name': 'nlsem', 'version': '0.8-1'}, {'type': 'r', 'name': 'tableone', 'version': '0.13.2'}, {'type': 'r', 'name': 'jstable', 'version': '1.3.6'}, {'type': 'r', 'name': 'RCAL', 'version': '2.0'}, {'type': 'r', 'name': 'stargazer', 'version': '5.2.3'}, {'type': 'r', 'name': 'sensemakr', 'version': '0.1.6'}, {'type': 'r', 'name': 'CompQuadForm', 'version': '1.4.3'}, {'type': 'r', 'name': 'nonnest2', 'version': '0.5-8'}, {'type': 'r', 'name': 'blavaan', 'version': '0.5-6'}, {'type': 'r', 'name': 'mathjaxr', 'version': '1.6-0'}, {'type': 'r', 'name': 'metadat', 'version': '1.2-0'}, {'type': 'r', 'name': 'metafor', 'version': '4.6-0'}, {'type': 'r', 'name': 'RNifti', 'version': '1.7.0'}, {'type': 'r', 'name': 'oro.nifti', 'version': '0.11.4'}, {'type': 'r', 'name': 'fmri', 'version': '1.9.12.1'}, {'type': 'r', 'name': 'linkcomm', 'version': '1.0-14'}, {'type': 'r', 'name': 'rnetcarto', 'version': '0.2.6'}, {'type': 'r', 'name': 'optextras', 'version': '2019-12.4'}, {'type': 'r', 'name': 'setRNG', 'version': '2024.2-1'}, {'type': 'r', 'name': 'Rvmmin', 'version': '2018-4.17.1'}, {'type': 'r', 'name': 'Rcgmin', 'version': '2022-4.30'}, {'type': 'r', 'name': 'optimr', 'version': '2019-12.16'}, {'type': 'r', 'name': 'DMCfun', 'version': '4.0.1'}, {'type': 'r', 'name': 'miceadds', 'version': '3.17-44'}, {'type': 'r', 'name': 'visdat', 'version': '0.6.0'}, {'type': 'r', 'name': 'UpSetR', 'version': '1.4.0'}, {'type': 'r', 'name': 'norm', 'version': '1.0-11.1'}, {'type': 'r', 'name': 'naniar', 'version': '1.1.0'}, {'type': 'r', 'name': 'stringdist', 'version': '0.9.12'}, {'type': 'r', 'name': 'image.binarization', 'version': '0.1.3'}, {'type': 'r', 'name': 'lassosum', 'version': '0.4.5'}, {'type': 'r', 'name': 'lslx', 'version': '0.6.11'}, {'type': 'r', 'name': 'truncnorm', 'version': '1.0-9'}, {'type': 'r', 'name': 'Rsolnp', 'version': '1.16'}, {'type': 'r', 'name': 'regsem', 'version': '1.9.5'}, {'type': 'r', 'name': 'semPLS', 'version': '1.0-10'}, {'type': 'r', 'name': 'GxEScanR', 'version': '2.0.2'}, {'type': 'r', 'name': 'admisc', 'version': '0.36'}, {'type': 'r', 'name': 'polycor', 'version': '0.8-1'}, {'type': 'r', 'name': 'multipol', 'version': '1.0-9'}, {'type': 'r', 'name': 'symmoments', 'version': '1.2.1'}, {'type': 'r', 'name': 'rngWELL', 'version': '0.10-10'}, {'type': 'r', 'name': 'randtoolbox', 'version': '2.0.5'}, {'type': 'r', 'name': 'qrng', 'version': '0.0-10'}, {'type': 'r', 'name': 'spacefillr', 'version': '0.3.3'}, {'type': 'r', 'name': 'TruncatedNormal', 'version': '2.3'}, {'type': 'r', 'name': 'cSEM', 'version': '0.5.0'}, {'type': 'r', 'name': 'cubelyr', 'version': '1.0.2'}, {'type': 'r', 'name': 'furrr', 'version': '0.3.1'}, {'type': 'r', 'name': 'broom.mixed', 'version': '0.2.9.6'}, {'type': 'r', 'name': 'DiceKriging', 'version': '1.6.0'}, {'type': 'r', 'name': 'grf', 'version': '2.4.0'}, {'type': 'r', 'name': 'twang', 'version': '2.6.1'}, {'type': 'r', 'name': 'neuralnet', 'version': '1.44.2'}, {'type': 'r', 'name': 'PCAmatchR', 'version': '0.3.3'}, {'type': 'r', 'name': 'origami', 'version': '1.0.7'}, {'type': 'r', 'name': 'hal9001', 'version': '0.4.6'}, {'type': 'r', 'name': 'cobalt', 'version': '4.5.5'}, {'type': 'r', 'name': 'CBPS', 'version': '0.23'}, {'type': 'r', 'name': 'SBdecomp', 'version': '1.2'}, {'type': 'r', 'name': 'naturalsort', 'version': '0.1.3'}, {'type': 'r', 'name': 'lwgeom', 'version': '0.2-14'}, {'type': 'r', 'name': 'finalfit', 'version': '1.0.8'}, {'type': 'r', 'name': 'bigD', 'version': '0.3.0'}, {'type': 'r', 'name': 'juicyjuice', 'version': '0.1.0'}, {'type': 'r', 'name': 'reactR', 'version': '0.6.1'}, {'type': 'r', 'name': 'reactable', 'version': '0.4.4'}, {'type': 'r', 'name': 'gt', 'version': '0.11.1'}, {'type': 'r', 'name': 'gtsummary', 'version': '2.0.3'}, {'type': 'r', 'name': 'ncdf4', 'version': '1.23'}, {'type': 'r', 'name': 'geex', 'version': '1.1.1'}, {'type': 'r', 'name': 'momentfit', 'version': '0.5'}, {'type': 'r', 'name': 'StatMatch', 'version': '1.4.2'}, {'type': 'r', 'name': 'stars', 'version': '0.6-7'}, {'type': 'r', 'name': 'rapidjsonr', 'version': '1.2.0'}, {'type': 'r', 'name': 'jsonify', 'version': '1.2.2'}, {'type': 'r', 'name': 'geometries', 'version': '0.2.4'}, {'type': 'r', 'name': 'sfheaders', 'version': '0.4.4'}, {'type': 'r', 'name': 'geojsonsf', 'version': '2.0.3'}, {'type': 'r', 'name': 'leafsync', 'version': '0.1.0'}, {'type': 'r', 'name': 'leafem', 'version': '0.2.3'}, {'type': 'r', 'name': 'widgetframe', 'version': '0.3.1'}, {'type': 'r', 'name': 'tmaptools', 'version': '3.1-1'}, {'type': 'r', 'name': 'tmap', 'version': '3.3-4'}, {'type': 'r', 'name': 'collapse', 'version': '2.0.18'}, {'type': 'r', 'name': 'genoPlotR', 'version': '0.8.11'}, {'type': 'r', 'name': 'VineCopula', 'version': '2.5.1'}, {'type': 'r', 'name': 'Rmpfr', 'version': '1.0-0'}, {'type': 'r', 'name': 'scam', 'version': '1.2-17'}, {'type': 'r', 'name': 'copula', 'version': '1.1-4'}, {'type': 'r', 'name': 'evd', 'version': '2.3-7.1'}, {'type': 'r', 'name': 'ismev', 'version': '1.42'}, {'type': 'r', 'name': 'GJRM', 'version': '0.2-6.7'}, {'type': 'r', 'name': 'penfa', 'version': '0.1.1'}, {'type': 'r', 'name': 'kde1d', 'version': '1.0.7'}, {'type': 'r', 'name': 'RcppThread', 'version': '2.1.7'}, {'type': 'r', 'name': 'wdm', 'version': '0.2.4'}, {'type': 'r', 'name': 'rvinecopulib', 'version': '0.6.3.1.1'}, {'type': 'r', 'name': 'PearsonDS', 'version': '1.3.1'}, {'type': 'r', 'name': 'covsim', 'version': '1.1.0'}, {'type': 'r', 'name': 'semTools', 'version': '0.5-6'}, {'type': 'r', 'name': 'dcurver', 'version': '0.9.2'}, {'type': 'r', 'name': 'beepr', 'version': '2.0'}, {'type': 'r', 'name': 'RPushbullet', 'version': '0.3.4'}, {'type': 'r', 'name': 'SimDesign', 'version': '2.17.1'}, {'type': 'r', 'name': 'mirt', 'version': '1.43'}, {'type': 'r', 'name': 'rpf', 'version': '1.0.14'}, {'type': 'r', 'name': 'OpenMx', 'version': '2.21.13'}, {'type': 'r', 'name': 'matlab', 'version': '1.0.4.1'}, {'type': 'r', 'name': 'FactorCopula', 'version': '0.9.3'}, {'type': 'r', 'name': 'rpact', 'version': '4.1.0'}, {'type': 'r', 'name': 'ldbounds', 'version': '2.0.2'}, {'type': 'r', 'name': 'catlearn', 'version': '1.0'}, {'type': 'r', 'name': 'MetaUtility', 'version': '2.1.2'}, {'type': 'r', 'name': 'EValue', 'version': '4.1.3'}, {'type': 'r', 'name': 'dagitty', 'version': '0.3-4'}, {'type': 'r', 'name': 'ggdag', 'version': '0.2.13'}, {'type': 'r', 'name': 'simex', 'version': '1.8'}, {'type': 'r', 'name': 'hash', 'version': '2.2.6.3'}, {'type': 'r', 'name': 'nabor', 'version': '0.5.0'}, {'type': 'r', 'name': 'RhpcBLASctl', 'version': '0.23-42'}, {'type': 'r', 'name': 'harmony', 'version': '1.2.1'}, {'type': 'r', 'name': 'apcluster', 'version': '1.4.13'}, {'type': 'r', 'name': 'DataCombine', 'version': '0.2.21'}, {'type': 'r', 'name': 'docstring', 'version': '1.0.0'}, {'type': 'r', 'name': 'gdalUtils', 'version': '2.0.3.2'}, {'type': 'r', 'name': 'openair', 'version': '2.18-2'}, {'type': 'r', 'name': 'pdp', 'version': '0.8.2'}, {'type': 'r', 'name': 'date', 'version': '1.2-42'}, {'type': 'r', 'name': 'cmprsk', 'version': '2.2-12'}, {'type': 'r', 'name': 'mets', 'version': '1.3.4'}, {'type': 'r', 'name': 'Publish', 'version': '2023.01.17'}, {'type': 'r', 'name': 'riskRegression', 'version': '2023.12.21'}, {'type': 'r', 'name': 'pec', 'version': '2023.04.12'}, {'type': 'r', 'name': 'pammtools', 'version': '0.5.93'}, {'type': 'r', 'name': 'relsurv', 'version': '2.2-9'}, {'type': 'r', 'name': 'mstate', 'version': '0.3.3'}, {'type': 'r', 'name': 'prettyGraphs', 'version': '2.1.6'}, {'type': 'r', 'name': 'ExPosition', 'version': '2.8.23'}, {'type': 'r', 'name': 'alluvial', 'version': '0.1-2'}, {'type': 'r', 'name': 'SNFtool', 'version': '2.3.1'}, {'type': 'r', 'name': 'BayesLogit', 'version': '2.1'}, {'type': 'r', 'name': 'Hmsc', 'version': '3.0-13'}, {'type': 'r', 'name': 'MonteCarlo', 'version': '1.0.6'}, {'type': 'r', 'name': 'chkptstanr', 'version': '0.1.1'}, {'type': 'r', 'name': 'MLmetrics', 'version': '1.1.3'}, {'type': 'r', 'name': 'elliptic', 'version': '1.4-0'}, {'type': 'r', 'name': 'contfrac', 'version': '1.1-12'}, {'type': 'r', 'name': 'hypergeo', 'version': '1.2-13'}, {'type': 'r', 'name': 'rtdists', 'version': '0.11-5'}, {'type': 'r', 'name': 'AMAPVox', 'version': '2.2.1'}, {'type': 'r', 'name': 'LCFdata', 'version': '2.0'}, {'type': 'r', 'name': 'LMERConvenienceFunctions', 'version': '3.0'}, {'type': 'r', 'name': 'HGNChelper', 'version': '0.8.15'}, {'type': 'r', 'name': 'logger', 'version': '0.4.0'}, {'type': 'r', 'name': 'parallelDist', 'version': '0.2.6'}, {'type': 'r', 'name': 'roptim', 'version': '0.1.6'}, {'type': 'r', 'name': 'yulab.utils', 'version': '0.1.8'}, {'type': 'r', 'name': 'ggfun', 'version': '0.1.7'}, {'type': 'r', 'name': 'gridGraphics', 'version': '0.5-1'}, {'type': 'r', 'name': 'ggplotify', 'version': '0.1.2'}, {'type': 'r', 'name': 'aplot', 'version': '0.2.3'}, {'type': 'r', 'name': 'tidytree', 'version': '0.4.6'}, {'type': 'r', 'name': 'ggvenn', 'version': '0.1.10'}, {'type': 'r', 'name': 'scatterpie', 'version': '0.2.4'}, {'type': 'r', 'name': 'shadowtext', 'version': '0.1.4'}, {'type': 'r', 'name': 'random', 'version': '0.2.6'}, {'type': 'r', 'name': 'R2WinBUGS', 'version': '2.1-22.1'}, {'type': 'r', 'name': 'aricode', 'version': '1.0.3'}, {'type': 'r', 'name': 'DepthProc', 'version': '2.1.5'}, {'type': 'r', 'name': 'dbscan', 'version': '1.2-0'}, {'type': 'r', 'name': 'ggh4x', 'version': '0.2.8'}, {'type': 'r', 'name': 'ComplexUpset', 'version': '1.3.3'}, {'type': 'r', 'name': 'proxyC', 'version': '0.4.1'}, {'type': 'r', 'name': 'changepoint', 'version': '2.3'}, {'type': 'r', 'name': 'geeM', 'version': '0.10.1'}, {'type': 'r', 'name': 'ggstance', 'version': '0.3.7'}, {'type': 'r', 'name': 'mosaicCore', 'version': '0.9.4.0'}, {'type': 'r', 'name': 'ggformula', 'version': '0.12.0'}, {'type': 'r', 'name': 'kinship2', 'version': '1.9.6.1'}, {'type': 'r', 'name': 'MESS', 'version': '0.5.12'}, {'type': 'r', 'name': 'smoof', 'version': '1.6.0.3'}, {'type': 'r', 'name': 'mlrMBO', 'version': '1.1.5.1'}, {'type': 'r', 'name': 'emoa', 'version': '0.5-3'}, {'type': 'r', 'name': 'webutils', 'version': '1.2.2'}, {'type': 'r', 'name': 'swagger', 'version': '5.17.14.1'}, {'type': 'r', 'name': 'varhandle', 'version': '2.0.6'}, {'type': 'r', 'name': 'dlm', 'version': '1.1-6.1'}, {'type': 'r', 'name': 'PMA', 'version': '1.2-4'}, {'type': 'r', 'name': 'unikn', 'version': '1.0.0'}, {'type': 'r', 'name': 'ppcor', 'version': '1.1'}, {'type': 'r', 'name': 'berryFunctions', 'version': '1.22.5'}, {'type': 'r', 'name': 'cld2', 'version': '1.2.5'}, {'type': 'r', 'name': 'crfsuite', 'version': '0.4.2'}, {'type': 'r', 'name': 'doc2vec', 'version': '0.2.0'}, {'type': 'r', 'name': 'fastDummies', 'version': '1.7.4'}, {'type': 'r', 'name': 'quanteda', 'version': '4.1.0'}, {'type': 'r', 'name': 'ISOweek', 'version': '0.6-2'}, {'type': 'r', 'name': 'sentometrics', 'version': '1.0.0'}, {'type': 'r', 'name': 'tau', 'version': '0.0-26'}, {'type': 'r', 'name': 'textcat', 'version': '1.0-9'}, {'type': 'r', 'name': 'textplot', 'version': '0.2.2'}, {'type': 'r', 'name': 'udpipe', 'version': '0.8.11'}, {'type': 'r', 'name': 'word2vec', 'version': '0.4.0'}, {'type': 'r', 'name': 'epitools', 'version': '0.5-10.1'}, {'type': 'r', 'name': 'RBesT', 'version': '1.7-4'}, {'type': 'r', 'name': 'rARPACK', 'version': '0.11-0'}, {'type': 'r', 'name': 'FKSUM', 'version': '1.0.1'}, {'type': 'r', 'name': 'warp', 'version': '0.2.1'}, {'type': 'r', 'name': 'slider', 'version': '0.3.2'}, {'type': 'r', 'name': 'rsample', 'version': '1.2.1'}, {'type': 'r', 'name': 'haldensify', 'version': '0.2.3'}, {'type': 'r', 'name': 'Polychrome', 'version': '1.5.1'}, {'type': 'r', 'name': 'shinycssloaders', 'version': '1.1.0'}, {'type': 'r', 'name': 'princurve', 'version': '2.1.6'}, {'type': 'r', 'name': 'ECOSolveR', 'version': '0.5.5'}, {'type': 'r', 'name': 'scs', 'version': '3.2.4'}, {'type': 'r', 'name': 'osqp', 'version': '0.6.3.3'}, {'type': 'r', 'name': 'CVXR', 'version': '1.0-15'}, {'type': 'r', 'name': 'tabletools', 'version': '0.1.0'}, {'type': 'r', 'name': 'officer', 'version': '0.6.7'}, {'type': 'r', 'name': 'gfonts', 'version': '0.2.0'}, {'type': 'r', 'name': 'fontBitstreamVera', 'version': '0.1.1'}, {'type': 'r', 'name': 'fontLiberation', 'version': '0.1.0'}, {'type': 'r', 'name': 'fontquiver', 'version': '0.2.1'}, {'type': 'r', 'name': 'gdtools', 'version': '0.4.1'}, {'type': 'r', 'name': 'flextable', 'version': '0.9.7'}, {'type': 'r', 'name': 'ridge', 'version': '3.3'}, {'type': 'r', 'name': 'ggdist', 'version': '3.3.2'}, {'type': 'r', 'name': 'svUnit', 'version': '1.0.6'}, {'type': 'r', 'name': 'arrayhelpers', 'version': '1.1-0'}, {'type': 'r', 'name': 'tidybayes', 'version': '3.0.7'}, {'type': 'r', 'name': 'spdep', 'version': '1.3-6'}, {'type': 'r', 'name': 'stringmagic', 'version': '1.1.2'}, {'type': 'r', 'name': 'dreamerr', 'version': '1.4.0'}, {'type': 'r', 'name': 'fixest', 'version': '0.12.1'}, {'type': 'r', 'name': 'cmna', 'version': '1.0.5'}, {'type': 'r', 'name': 'XBRL', 'version': '0.99.19.1'}, {'type': 'r', 'name': 'rhandsontable', 'version': '0.3.8'}, {'type': 'r', 'name': 'missMDA', 'version': '1.19'}, {'type': 'r', 'name': 'insight', 'version': '0.20.5'}, {'type': 'r', 'name': 'datawizard', 'version': '0.13.0'}, {'type': 'r', 'name': 'bayestestR', 'version': '0.15.0'}, {'type': 'r', 'name': 'performance', 'version': '0.12.4'}, {'type': 'r', 'name': 'fastlogranktest', 'version': '0.2.1'}, {'type': 'r', 'name': 'pbmcapply', 'version': '1.5.1'}, {'type': 'r', 'name': 'PWEALL', 'version': '1.3.0.1'}, {'type': 'r', 'name': 'goldilocks', 'version': '0.3.0'}, {'type': 'r', 'name': 'r2rtf', 'version': '1.1.1'}, {'type': 'r', 'name': 'gsDesign', 'version': '3.6.5'}, {'type': 'r', 'name': 'gcmr', 'version': '1.0.3'}, {'type': 'r', 'name': 'frbs', 'version': '3.2-0'}, {'type': 'r', 'name': 'pander', 'version': '0.6.6'}, {'type': 'r', 'name': 'texreg', 'version': '1.39.4'}, {'type': 'r', 'name': 'gsubfn', 'version': '0.7'}, {'type': 'r', 'name': 'fastGHQuad', 'version': '1.0.1'}, {'type': 'r', 'name': 'MplusAutomation', 'version': '1.1.1'}, {'type': 'r', 'name': 'modsem', 'version': '1.0.6'}, {'type': 'r', 'name': 'sgdGMF', 'version': '1.0'}, {'type': 'r', 'name': 'statip', 'version': '0.2.3'}, {'type': 'r', 'name': 'gss', 'version': '2.2-9'}, {'type': 'r', 'name': 'timeSeries', 'version': '4041.111'}, {'type': 'r', 'name': 'fBasics', 'version': '4041.97'}, {'type': 'r', 'name': 'rmutil', 'version': '1.1.10'}, {'type': 'r', 'name': 'stable', 'version': '1.1.6'}, {'type': 'r', 'name': 'modeest', 'version': '2.4.0'}, {'type': 'r', 'name': 'MicrobiomeStat', 'version': '1.2'}, {'type': 'r', 'name': 'ggprism', 'version': '1.0.6'}, {'type': 'r', 'name': 'logging', 'version': '0.10-108'}, {'type': 'r', 'name': 'biglm', 'version': '0.9-3'}, {'type': 'r', 'name': 'cplm', 'version': '0.7-12.1'}]}], 'homepage': 'https://www.r-project.org/', 'license': [], 'image': '', 'categories': [], 'identifier': '', 'description': 'Bundle of R packages from CRAN'} installations


### abc


|`abc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### abc.data


|`abc.data` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### abe


|`abe` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### abind


|`abind` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4-8|`R-bundle-CRAN/2024.11-foss-2024a`|

### acepack


|`acepack` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### adabag


|`adabag` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ade4


|`ade4` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-22|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ADGofTest


|`ADGofTest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### admisc


|`admisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.34|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.35|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.36|`R-bundle-CRAN/2024.11-foss-2024a`|

### aggregation


|`aggregation` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### AICcmodavg


|`AICcmodavg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### akima


|`akima` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-3.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### alabama


|`alabama` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### AlgDesign


|`AlgDesign` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### alluvial


|`alluvial` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### AMAPVox


|`AMAPVox` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### animation


|`animation` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### aod


|`aod` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### apcluster


|`apcluster` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.11|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ape


|`ape` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.7-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### aplot


|`aplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### argparse


|`argparse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.2.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### aricode


|`aricode` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### arm


|`arm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.13-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.14-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### arrayhelpers


|`arrayhelpers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### asnipe


|`asnipe` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive


|`assertive` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.base


|`assertive.base` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.code


|`assertive.code` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.data


|`assertive.data` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.data.uk


|`assertive.data.uk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.data.us


|`assertive.data.us` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.datetimes


|`assertive.datetimes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.files


|`assertive.files` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.matrices


|`assertive.matrices` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.models


|`assertive.models` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.numbers


|`assertive.numbers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.properties


|`assertive.properties` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.reflection


|`assertive.reflection` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.sets


|`assertive.sets` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.strings


|`assertive.strings` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertive.types


|`assertive.types` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### assertthat


|`assertthat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### AUC


|`AUC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### audio


|`audio` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### aws


|`aws` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.5-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.5-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.5-6|`R-bundle-CRAN/2024.11-foss-2024a`|

### awsMethods


|`awsMethods` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### backports


|`backports` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bacr


|`bacr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bartMachine


|`bartMachine` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bartMachineJARs


|`bartMachineJARs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### base64


|`base64` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### BatchJobs


|`BatchJobs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### batchmeans


|`batchmeans` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BayesianTools


|`BayesianTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BayesLogit


|`BayesLogit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bayesm


|`bayesm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BayesPen


|`BayesPen` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bayesplot


|`bayesplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.10.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.11.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bayestestR


|`bayestestR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.14.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.15.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### BB


|`BB` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2019.10-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BBmisc


|`BBmisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bbmle


|`bbmle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.25.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BCEE


|`BCEE` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BDgraph


|`BDgraph` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.72|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.73|`R-bundle-CRAN/2024.11-foss-2024a`|

### bdsmatrix


|`bdsmatrix` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-6|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### beanplot


|`beanplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### beepr


|`beepr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### beeswarm


|`beeswarm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### berryFunctions


|`berryFunctions` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.22.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.22.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### betareg


|`betareg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### BH


|`BH` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.81.0-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.84.0-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BiasedUrn


|`BiasedUrn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.11|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bibtex


|`bibtex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BIEN


|`BIEN` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bigD


|`bigD` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### BIGL


|`BIGL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.9.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.9.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### biglm


|`biglm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### bigmemory


|`bigmemory` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.6.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.6.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bigmemory.sri


|`bigmemory.sri` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bindr


|`bindr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### bindrcpp


|`bindrcpp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bio3d


|`bio3d` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.4-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### biom


|`biom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### biomod2


|`biomod2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.2-5-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bit


|`bit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### bit64


|`bit64` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.5.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### bitops


|`bitops` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-9|`R-bundle-CRAN/2024.11-foss-2024a`|

### blavaan


|`blavaan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.5-6|`R-bundle-CRAN/2024.11-foss-2024a`|

### blob


|`blob` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### BMA


|`BMA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.18.17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.18.19|`R-bundle-CRAN/2024.11-foss-2024a`|

### bmp


|`bmp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bnlearn


|`bnlearn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.9.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.9.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|5.0.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### bold


|`bold` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### boot


|`boot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-28.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-30|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3-31|`R-bundle-CRAN/2024.11-foss-2024a`|

### bootstrap


|`bootstrap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2019.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Boruta


|`Boruta` version|R-bundle-CRAN modules that include it|
| --- | --- |
|8.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### brglm


|`brglm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### bridgedist


|`bridgedist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### bridgesampling


|`bridgesampling` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### brms


|`brms` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.20.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.21.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.22.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### Brobdingnag


|`Brobdingnag` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### broom


|`broom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.6|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### broom.helpers


|`broom.helpers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.14.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.15.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.17.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### broom.mixed


|`broom.mixed` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.9.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.9.5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.2.9.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### bst


|`bst` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-24|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Cairo


|`Cairo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### calibrate


|`calibrate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### car


|`car` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### carData


|`carData` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cards


|`cards` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### caret


|`caret` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.0-94|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### catlearn


|`catlearn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### caTools


|`caTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.18.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.18.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### CBPS


|`CBPS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.23|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### celestial


|`celestial` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cellranger


|`cellranger` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cgdsr


|`cgdsr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cghFLasso


|`cghFLasso` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### changepoint


|`changepoint` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### checkmate


|`checkmate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### chemometrics


|`chemometrics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### chk


|`chk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### chkptstanr


|`chkptstanr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### chron


|`chron` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3-61|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### circlize


|`circlize` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.15|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.16|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### circular


|`circular` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### class


|`class` version|R-bundle-CRAN modules that include it|
| --- | --- |
|7.3-22|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### classInt


|`classInt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cld2


|`cld2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### clisymbols


|`clisymbols` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### clock


|`clock` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.7.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### clue


|`clue` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-65|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3-66|`R-bundle-CRAN/2024.11-foss-2024a`|

### cluster


|`cluster` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### clusterGeneration


|`clusterGeneration` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### clusterRepro


|`clusterRepro` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### clustree


|`clustree` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### clValid


|`clValid` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cmna


|`cmna` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cmprsk


|`cmprsk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-11|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2-12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cNORM


|`cNORM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### cobalt


|`cobalt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.5.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.5.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cobs


|`cobs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### coda


|`coda` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.19-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.19-4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### codetools


|`codetools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-19|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2-20|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### coin


|`coin` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### collapse


|`collapse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.14|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.0.18|`R-bundle-CRAN/2024.11-foss-2024a`|
|2.0.7|`R-bundle-CRAN/2023.12-foss-2023a`|

### colorspace


|`colorspace` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### colourpicker


|`colourpicker` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### combinat


|`combinat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ComICS


|`ComICS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ComplexUpset


|`ComplexUpset` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### compositions


|`compositions` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-6|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### CompQuadForm


|`CompQuadForm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### conditionz


|`conditionz` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### conflicted


|`conflicted` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### conquer


|`conquer` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ConsRank


|`ConsRank` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### contfrac


|`contfrac` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### copCAR


|`copCAR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### copula


|`copula` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### corpcor


|`corpcor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### corrplot


|`corrplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.92|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.95|`R-bundle-CRAN/2024.11-foss-2024a`|

### covr


|`covr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.6.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### CovSel


|`CovSel` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### covsim


|`covsim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cowplot


|`cowplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### coxed


|`coxed` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### coxme


|`coxme` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-18.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2-20|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.2-22|`R-bundle-CRAN/2024.11-foss-2024a`|

### cplm


|`cplm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7-12.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### crfsuite


|`crfsuite` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### crosstalk


|`crosstalk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### crul


|`crul` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### cSEM


|`cSEM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### csSAM


|`csSAM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ctmle


|`ctmle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cubature


|`cubature` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### cubelyr


|`cubelyr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### cvAUC


|`cvAUC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### CVST


|`CVST` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### CVXR


|`CVXR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-11|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-13|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0-15|`R-bundle-CRAN/2024.11-foss-2024a`|

### d3Network


|`d3Network` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dagitty


|`dagitty` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### data.table


|`data.table` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.14.10|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.15.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.16.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### data.tree


|`data.tree` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DataCombine


|`DataCombine` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### datawizard


|`datawizard` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.12.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.13.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### date


|`date` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-42|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dbarts


|`dbarts` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-25|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9-28|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DBI


|`DBI` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dbplyr


|`dbplyr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dbscan


|`dbscan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### dcurver


|`dcurver` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ddalpha


|`ddalpha` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.13|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.15|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.16|`R-bundle-CRAN/2024.11-foss-2024a`|

### deal


|`deal` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-42|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### debugme


|`debugme` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### deldir


|`deldir` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dendextend


|`dendextend` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.17.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.19.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### DEoptim


|`DEoptim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DEoptimR


|`DEoptimR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-3-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### DepthProc


|`DepthProc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Deriv


|`Deriv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.1.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### DescTools


|`DescTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.99.52|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.99.54|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.99.58|`R-bundle-CRAN/2024.11-foss-2024a`|

### deSolve


|`deSolve` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.40|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dfidx


|`dfidx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### DHARMa


|`DHARMa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### dHSIC


|`dHSIC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### diagram


|`diagram` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DiagrammeR


|`DiagrammeR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.10|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DiceKriging


|`DiceKriging` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dichromat


|`dichromat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dimRed


|`dimRed` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### diptest


|`diptest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.77-0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.77-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DiscriMiner


|`DiscriMiner` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-29|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dismo


|`dismo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### distillery


|`distillery` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### distr


|`distr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.9.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.9.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.9.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### distrEx


|`distrEx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.9.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.9.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.9.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### distributional


|`distributional` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### DistributionUtils


|`DistributionUtils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### diveRsity


|`diveRsity` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.90|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dlm


|`dlm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-6.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### DMCfun


|`DMCfun` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.5.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|4.0.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### doBy


|`doBy` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.6.24|`R-bundle-CRAN/2024.11-foss-2024a`|

### doc2vec


|`doc2vec` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### docstring


|`docstring` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### doMC


|`doMC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### doParallel


|`doParallel` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### doRNG


|`doRNG` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### doSNOW


|`doSNOW` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.20|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dotCall64


|`dotCall64` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### downloader


|`downloader` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dplyr


|`dplyr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dr


|`dr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dreamerr


|`dreamerr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### drgee


|`drgee` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DRR


|`DRR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### drugCombo


|`drugCombo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DT


|`DT` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.31|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.33|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dtangle


|`dtangle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dtplyr


|`dtplyr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### DTRreg


|`DTRreg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dtw


|`dtw` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.23-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dummies


|`dummies` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dygraphs


|`dygraphs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### dynamicTreeCut


|`dynamicTreeCut` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.63-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### e1071


|`e1071` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-16|`R-bundle-CRAN/2024.11-foss-2024a`|

### earth


|`earth` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.3.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.3.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|5.3.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### EasyABC


|`EasyABC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ECOSolveR


|`ECOSolveR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ellipse


|`ellipse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### elliptic


|`elliptic` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### emdbook


|`emdbook` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### emmeans


|`emmeans` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.10.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.10.5|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.8.9|`R-bundle-CRAN/2023.12-foss-2023a`|

### emoa


|`emoa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5-2|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.5-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### emulator


|`emulator` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-21|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-24|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### energy


|`energy` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-12|`R-bundle-CRAN/2024.11-foss-2024a`|

### ENMeval


|`ENMeval` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### entropy


|`entropy` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### EnvStats


|`EnvStats` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.8.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### epitools


|`epitools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-10.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ergm


|`ergm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.5.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.6.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|4.7.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### ergm.count


|`ergm.count` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ergm.multi


|`ergm.multi` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.2.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### estimability


|`estimability` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### EValue


|`EValue` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### evd


|`evd` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3-6.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3-7|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.3-7.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### Exact


|`Exact` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### expm


|`expm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.999-8|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.999-9|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### ExPosition


|`ExPosition` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.8.23|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### expsmooth


|`expsmooth` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### extrafont


|`extrafont` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.19|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### extrafontdb


|`extrafontdb` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### extRemes


|`extRemes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### FactoMineR


|`FactoMineR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|
|2.9|`R-bundle-CRAN/2023.12-foss-2023a`|

### FactorCopula


|`FactorCopula` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fail


|`fail` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### farver


|`farver` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fastcluster


|`fastcluster` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fastDummies


|`fastDummies` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### fasterize


|`fasterize` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### fastGHQuad


|`fastGHQuad` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### fastICA


|`fastICA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-5.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### fastlogranktest


|`fastlogranktest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### fastmatch


|`fastmatch` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fBasics


|`fBasics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4041.97|`R-bundle-CRAN/2024.11-foss-2024a`|

### fdrtool


|`fdrtool` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.18|`R-bundle-CRAN/2024.11-foss-2024a`|

### feather


|`feather` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ff


|`ff` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.0.12|`R-bundle-CRAN/2024.06-foss-2023b`|
|4.0.9|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### fftw


|`fftw` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-7|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-8|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0-9|`R-bundle-CRAN/2024.11-foss-2024a`|

### fftwtools


|`fftwtools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fields


|`fields` version|R-bundle-CRAN modules that include it|
| --- | --- |
|15.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|16.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### filehash


|`filehash` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.4-6|`R-bundle-CRAN/2024.11-foss-2024a`|

### finalfit


|`finalfit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### findpython


|`findpython` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.9|`R-bundle-CRAN/2024.11-foss-2024a`|

### fishMod


|`fishMod` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.29|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.29.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### fitdistrplus


|`fitdistrplus` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### fixest


|`fixest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.12.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### FKSUM


|`FKSUM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### flashClust


|`flashClust` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.01-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### flexclust


|`flexclust` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### flexmix


|`flexmix` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3-19|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### flextable


|`flextable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.6|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.9.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### fma


|`fma` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### FME


|`FME` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.6.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fmri


|`fmri` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.9.12.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### FNN


|`FNN` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.3.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.1.4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### fontBitstreamVera


|`fontBitstreamVera` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fontLiberation


|`fontLiberation` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fontquiver


|`fontquiver` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### forcats


|`forcats` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### foreach


|`foreach` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### forecast


|`forecast` version|R-bundle-CRAN modules that include it|
| --- | --- |
|8.21.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|8.23.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### foreign


|`foreign` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8-86|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.8-87|`R-bundle-CRAN/2024.11-foss-2024a`|

### formatR


|`formatR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Formula


|`Formula` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### formula.tools


|`formula.tools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fossil


|`fossil` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fpc


|`fpc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-10|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2-12|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.2-13|`R-bundle-CRAN/2024.11-foss-2024a`|

### fpp


|`fpp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### fracdiff


|`fracdiff` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### frbs


|`frbs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### furrr


|`furrr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### futile.logger


|`futile.logger` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### futile.options


|`futile.options` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### future


|`future` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.33.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.33.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.34.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### future.apply


|`future.apply` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.11.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.11.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.11.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### gam


|`gam` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.22-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.22-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### gamlss


|`gamlss` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.4-20|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.4-22|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gamlss.data


|`gamlss.data` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.0-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|6.0-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gamlss.dist


|`gamlss.dist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.1-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gamlss.tr


|`gamlss.tr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.1-7|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.1-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gamm4


|`gamm4` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gap


|`gap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### gap.datasets


|`gap.datasets` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gapfill


|`gapfill` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.6-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gargle


|`gargle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gaussquad


|`gaussquad` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gbm


|`gbm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.8.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.9|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.2.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### gbRd


|`gbRd` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-11|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gclus


|`gclus` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gcmr


|`gcmr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### gdalUtils


|`gdalUtils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gdata


|`gdata` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### gdistance


|`gdistance` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gdtools


|`gdtools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.7|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### gee


|`gee` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.13-26|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.13-27|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### geeM


|`geeM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### geepack


|`geepack` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.11|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.12|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.3.9|`R-bundle-CRAN/2023.12-foss-2023a`|

### geex


|`geex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### geiger


|`geiger` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GeneNet


|`GeneNet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.16|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### generics


|`generics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### genoPlotR


|`genoPlotR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GenSA


|`GenSA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.10.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.14|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.1.14.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### geojsonsf


|`geojsonsf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### geometries


|`geometries` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### geometry


|`geometry` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### getopt


|`getopt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.20.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GetoptLong


|`GetoptLong` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gfonts


|`gfonts` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GGally


|`GGally` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggbeeswarm


|`ggbeeswarm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggdag


|`ggdag` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.10|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.12|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.2.13|`R-bundle-CRAN/2024.11-foss-2024a`|

### ggdist


|`ggdist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.3.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggExtra


|`ggExtra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggfan


|`ggfan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggforce


|`ggforce` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggformula


|`ggformula` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.12.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggfun


|`ggfun` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.1.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### ggh4x


|`ggh4x` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggnetwork


|`ggnetwork` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.12|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggplot2


|`ggplot2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.4.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggplotify


|`ggplotify` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggprism


|`ggprism` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### ggpubr


|`ggpubr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggraph


|`ggraph` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggrepel


|`ggrepel` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.9.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### ggridges


|`ggridges` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggsci


|`ggsci` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggsignif


|`ggsignif` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggstance


|`ggstance` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggstats


|`ggstats` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.7.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### ggvenn


|`ggvenn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ggvis


|`ggvis` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.8|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GillespieSSA


|`GillespieSSA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### git2r


|`git2r` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.33.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.35.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### GJRM


|`GJRM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-6.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2-6.5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.2-6.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### glasso


|`glasso` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gld


|`gld` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gllvm


|`gllvm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### glmmML


|`glmmML` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### glmmTMB


|`glmmTMB` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.10|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.1.8|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.9|`R-bundle-CRAN/2024.06-foss-2023b`|

### glmnet


|`glmnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.1-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GlobalOptions


|`GlobalOptions` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### globals


|`globals` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.16.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.16.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gmm


|`gmm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gmodels


|`gmodels` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.18.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.19.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gmp


|`gmp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.7-4|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.7-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### gnumeric


|`gnumeric` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### goftest


|`goftest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### goldilocks


|`goldilocks` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### gomms


|`gomms` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### googledrive


|`googledrive` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### googlesheets4


|`googlesheets4` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gower


|`gower` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GPArotation


|`GPArotation` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.11-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2024.3-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gplots


|`gplots` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.2.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### graphlayouts


|`graphlayouts` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.2.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### grf


|`grf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### gridBase


|`gridBase` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gridExtra


|`gridExtra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gridGraphics


|`gridGraphics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### grImport2


|`grImport2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### grpreg


|`grpreg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### GSA


|`GSA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.03.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.03.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gsalib


|`gsalib` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gsDesign


|`gsDesign` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.6.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### gsl


|`gsl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gss


|`gss` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-9|`R-bundle-CRAN/2024.11-foss-2024a`|

### gsubfn


|`gsubfn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### gsw


|`gsw` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### gt


|`gt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.10.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.11.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### gtable


|`gtable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.3.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### gtools


|`gtools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.9.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gtsummary


|`gtsummary` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### GUTS


|`GUTS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gWidgets2


|`gWidgets2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### gWidgets2tcltk


|`gWidgets2tcltk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### GxEScanR


|`GxEScanR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### h2o


|`h2o` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.42.0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.44.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### hal9001


|`hal9001` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### haldensify


|`haldensify` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### hardhat


|`hardhat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### harmony


|`harmony` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### hash


|`hash` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.6.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### haven


|`haven` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.5.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### hdf5r


|`hdf5r` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.10|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.11|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.3.8|`R-bundle-CRAN/2023.12-foss-2023a`|

### hdm


|`hdm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### heatmap3


|`heatmap3` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### here


|`here` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### hexbin


|`hexbin` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.28.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.28.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### HGNChelper


|`HGNChelper` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.8.14|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.8.15|`R-bundle-CRAN/2024.11-foss-2024a`|

### HiddenMarkov


|`HiddenMarkov` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Hmisc


|`Hmisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.1-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.1-3|`R-bundle-CRAN/2024.06-foss-2023b`|
|5.2-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### hms


|`hms` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Hmsc


|`Hmsc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### htmlTable


|`htmlTable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.4.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### httpcode


|`httpcode` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### huge


|`huge` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### hunspell


|`hunspell` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### hwriter


|`hwriter` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### HWxtest


|`HWxtest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### hypergeo


|`hypergeo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ica


|`ica` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### IDPmisc


|`IDPmisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.20|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### idr


|`idr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ids


|`ids` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ie2misc


|`ie2misc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### igraph


|`igraph` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### image.binarization


|`image.binarization` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### imager


|`imager` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.45.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### imagerExtra


|`imagerExtra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ineq


|`ineq` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### influenceR


|`influenceR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### infotheo


|`infotheo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### inline


|`inline` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.19|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.20|`R-bundle-CRAN/2024.11-foss-2024a`|

### insight


|`insight` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.20.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.20.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### intergraph


|`intergraph` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### interp


|`interp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### interpretR


|`interpretR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### intrinsicDimension


|`intrinsicDimension` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### inum


|`inum` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ipred


|`ipred` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9-15|`R-bundle-CRAN/2024.11-foss-2024a`|

### irace


|`irace` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### irlba


|`irlba` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ismev


|`ismev` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.42|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Iso


|`Iso` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### isoband


|`isoband` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ISOcodes


|`ISOcodes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.12.07|`R-bundle-CRAN/2023.12-foss-2023a`|
|2024.02.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ISOweek


|`ISOweek` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### iterators


|`iterators` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### itertools


|`itertools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### JADE


|`JADE` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### janeaustenr


|`janeaustenr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### JBTools


|`JBTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.2.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### jiebaR


|`jiebaR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### jiebaRD


|`jiebaRD` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### jomo


|`jomo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.7-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### jpeg


|`jpeg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### jsonify


|`jsonify` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### jstable


|`jstable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.6|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### juicyjuice


|`juicyjuice` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### kableExtra


|`kableExtra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### kde1d


|`kde1d` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### kedd


|`kedd` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### kernlab


|`kernlab` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-32|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9-33|`R-bundle-CRAN/2024.11-foss-2024a`|

### KernSmooth


|`KernSmooth` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.23-22|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.23-24|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### kinship2


|`kinship2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.9.6.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### klaR


|`klaR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### KODAMA


|`KODAMA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### kohonen


|`kohonen` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ks


|`ks` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.14.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.14.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.14.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### labdsv


|`labdsv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### labeling


|`labeling` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### labelled


|`labelled` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.12.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.13.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### laeken


|`laeken` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lambda.r


|`lambda.r` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### LaplacesDemon


|`LaplacesDemon` version|R-bundle-CRAN modules that include it|
| --- | --- |
|16.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lars


|`lars` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lassosum


|`lassosum` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lattice


|`lattice` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.22-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.22-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### latticeExtra


|`latticeExtra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-30|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lava


|`lava` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.8.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lavaan


|`lavaan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-16|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6-18|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.6-19|`R-bundle-CRAN/2024.11-foss-2024a`|

### lazy


|`lazy` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-18|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lazyeval


|`lazyeval` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### LCFdata


|`LCFdata` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lda


|`lda` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ldbounds


|`ldbounds` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### leafem


|`leafem` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### leaflet


|`leaflet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### leaflet.providers


|`leaflet.providers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### leafsync


|`leafsync` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### leaps


|`leaps` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### LearnBayes


|`LearnBayes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.15.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### leiden


|`leiden` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lhs


|`lhs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### libcoin


|`libcoin` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### limSolve


|`limSolve` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.7|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### linkcomm


|`linkcomm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### linprog


|`linprog` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### liquidSVM


|`liquidSVM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### listenv


|`listenv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lme4


|`lme4` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-35.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-35.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.1-35.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### LMERConvenienceFunctions


|`LMERConvenienceFunctions` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lmerTest


|`lmerTest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lmom


|`lmom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### Lmoments


|`Lmoments` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lmtest


|`lmtest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-40|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lobstr


|`lobstr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### locfdr


|`locfdr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### locfit


|`locfit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-9.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|
|1.5-9.8|`R-bundle-CRAN/2023.12-foss-2023a`|

### logcondens


|`logcondens` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### logger


|`logger` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### logging


|`logging` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10-108|`R-bundle-CRAN/2024.11-foss-2024a`|

### logistf


|`logistf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.26.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### logspline


|`logspline` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.21|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.22|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### longitudinal


|`longitudinal` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### longmemo


|`longmemo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### loo


|`loo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.7.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.8.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### lpSolve


|`lpSolve` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.6.19|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.6.20|`R-bundle-CRAN/2024.06-foss-2023b`|
|5.6.22|`R-bundle-CRAN/2024.11-foss-2024a`|

### lpSolveAPI


|`lpSolveAPI` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.5.2.0-17.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|5.5.2.0-17.12|`R-bundle-CRAN/2024.11-foss-2024a`|

### lqa


|`lqa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lsei


|`lsei` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lslx


|`lslx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lubridate


|`lubridate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### lwgeom


|`lwgeom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-13|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### magic


|`magic` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### magick


|`magick` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.8.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.8.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.8.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### MALDIquant


|`MALDIquant` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.22.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.22.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.22.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### manipulateWidget


|`manipulateWidget` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mapproj


|`mapproj` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### maps


|`maps` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.4.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.4.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.4.2.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### maptools


|`maptools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### markdown


|`markdown` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.12|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MASS


|`MASS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|7.3-60|`R-bundle-CRAN/2023.12-foss-2023a`|
|7.3-61|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Matching


|`Matching` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.10-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.10-15|`R-bundle-CRAN/2024.11-foss-2024a`|

### MatchIt


|`MatchIt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.5.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.6.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### mathjaxr


|`mathjaxr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### matlab


|`matlab` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### Matrix


|`Matrix` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.7-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### matrixcalc


|`matrixcalc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MatrixModels


|`MatrixModels` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### matrixStats


|`matrixStats` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### maxLik


|`maxLik` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5-2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### maxlike


|`maxlike` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-10|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### maxnet


|`maxnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mboost


|`mboost` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.9-10|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.9-11|`R-bundle-CRAN/2024.11-foss-2024a`|
|2.9-9|`R-bundle-CRAN/2023.12-foss-2023a`|

### mclogit


|`mclogit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mclust


|`mclust` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.0.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|6.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mcmc


|`mcmc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MCMCpack


|`MCMCpack` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.7-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### mcmcse


|`mcmcse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mda


|`mda` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### medflex


|`medflex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mediation


|`mediation` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### memisc


|`memisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.99.31.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.99.31.7|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.99.31.8.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### memuse


|`memuse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MESS


|`MESS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### metadat


|`metadat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### metafor


|`metafor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.4-0|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.6-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MetaUtility


|`MetaUtility` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mets


|`mets` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mgcv


|`mgcv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9-0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.9-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mgsub


|`mgsub` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mhsmm


|`mhsmm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mi


|`mi` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mice


|`mice` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.16.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### miceadds


|`miceadds` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.16-18|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.17-44|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### microbenchmark


|`microbenchmark` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### MicrobiomeStat


|`MicrobiomeStat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### MIIVsem


|`MIIVsem` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### minerva


|`minerva` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### minpack.lm


|`minpack.lm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### minqa


|`minqa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.7|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.2.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### minty


|`minty` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.0.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### mirt


|`mirt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.41|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.43|`R-bundle-CRAN/2024.11-foss-2024a`|

### misc3d


|`misc3d` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### miscTools


|`miscTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-28|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### missForest


|`missForest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### missMDA


|`missMDA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.19|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mitml


|`mitml` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mitools


|`mitools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mixtools


|`mixtools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mlbench


|`mlbench` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-3.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mlegp


|`mlegp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MLmetrics


|`MLmetrics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mlogit


|`mlogit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mlr


|`mlr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.19.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.19.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mlrMBO


|`mlrMBO` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mltools


|`mltools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mnormt


|`mnormt` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### modeest


|`modeest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### ModelMetrics


|`ModelMetrics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### modelr


|`modelr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### modeltools


|`modeltools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-23|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### modsem


|`modsem` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### momentfit


|`momentfit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### moments


|`moments` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.14.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### MonteCarlo


|`MonteCarlo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mosaicCore


|`mosaicCore` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mpath


|`mpath` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-2.23|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4-2.25|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.4-2.26|`R-bundle-CRAN/2024.11-foss-2024a`|

### MplusAutomation


|`MplusAutomation` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### mRMRe


|`mRMRe` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.2.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### msm


|`msm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.8.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### mstate


|`mstate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### multcomp


|`multcomp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-25|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4-26|`R-bundle-CRAN/2024.11-foss-2024a`|

### multcompView


|`multcompView` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|
|0.1-9|`R-bundle-CRAN/2023.12-foss-2023a`|

### multicool


|`multicool` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### multipol


|`multipol` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### multitaper


|`multitaper` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### munsell


|`munsell` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mvabund


|`mvabund` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mvnfast


|`mvnfast` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### mvtnorm


|`mvtnorm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### nabor


|`nabor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### naniar


|`naniar` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### natserv


|`natserv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### naturalsort


|`naturalsort` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ncbit


|`ncbit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2013.03.29.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ncdf4


|`ncdf4` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.22|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.23|`R-bundle-CRAN/2024.11-foss-2024a`|

### NCmisc


|`NCmisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### network


|`network` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.18.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### networkDynamic


|`networkDynamic` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.11.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.11.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### networkLite


|`networkLite` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### neuralnet


|`neuralnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.44.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### neuRosim


|`neuRosim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ngspatial


|`ngspatial` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### NISTunits


|`NISTunits` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### nleqslv


|`nleqslv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### nlme


|`nlme` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-164|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-165|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.1-166|`R-bundle-CRAN/2024.11-foss-2024a`|

### nloptr


|`nloptr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### NLP


|`NLP` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### nlsem


|`nlsem` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### nnet


|`nnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|7.3-19|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### nnls


|`nnls` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### nonnest2


|`nonnest2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-6|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5-7|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.5-8|`R-bundle-CRAN/2024.11-foss-2024a`|

### nor1mix


|`nor1mix` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### norm


|`norm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-11.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### nortest


|`nortest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### np


|`np` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.60-17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### npsurv


|`npsurv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### numDeriv


|`numDeriv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2016.8-1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### oai


|`oai` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### oce


|`oce` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.8-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### OceanView


|`OceanView` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### oddsratio


|`oddsratio` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### officer


|`officer` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6.6|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.6.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### openair


|`openair` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.18-0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.18-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### OpenMx


|`OpenMx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.21.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.21.13|`R-bundle-CRAN/2024.11-foss-2024a`|

### openxlsx


|`openxlsx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.2.7.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### operator.tools


|`operator.tools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### optextras


|`optextras` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2019-12.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### optimParallel


|`optimParallel` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### optimr


|`optimr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2019-12.16|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### optimx


|`optimx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023-10.21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### optmatch


|`optmatch` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.10.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### optparse


|`optparse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ordinal


|`ordinal` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.12-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2023.12-4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### origami


|`origami` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### oro.nifti


|`oro.nifti` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### orthopolynom


|`orthopolynom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-6.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### osqp


|`osqp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.3.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### outliers


|`outliers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.15|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### packrat


|`packrat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pacman


|`pacman` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pammtools


|`pammtools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.92|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.93|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pamr


|`pamr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.56.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.56.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.57|`R-bundle-CRAN/2024.11-foss-2024a`|

### pan


|`pan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pander


|`pander` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### parallelDist


|`parallelDist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### parallelly


|`parallelly` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.36.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.37.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.39.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### parallelMap


|`parallelMap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ParamHelpers


|`ParamHelpers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.14.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### parsedate


|`parsedate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### party


|`party` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-14|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-15|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3-17|`R-bundle-CRAN/2024.11-foss-2024a`|

### partykit


|`partykit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-20|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-22|`R-bundle-CRAN/2024.11-foss-2024a`|

### pastecs


|`pastecs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.21|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### patchwork


|`patchwork` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### pbapply


|`pbapply` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pbivnorm


|`pbivnorm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pbkrtest


|`pbkrtest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### pbmcapply


|`pbmcapply` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### PCAmatchR


|`PCAmatchR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pcaPP


|`pcaPP` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### pdp


|`pdp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.8.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### PearsonDS


|`PearsonDS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pec


|`pec` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.04.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### penalized


|`penalized` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-52|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### penfa


|`penfa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### peperr


|`peperr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### performance


|`performance` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.12.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.12.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### PermAlgo


|`PermAlgo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### permute


|`permute` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### phangorn


|`phangorn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.11.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.12.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### pheatmap


|`pheatmap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### phylobase


|`phylobase` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.10|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.8.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### phytools


|`phytools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pim


|`pim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pinfsc50


|`pinfsc50` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pixmap


|`pixmap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-12|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pkgmaker


|`pkgmaker` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.32.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### PKI


|`PKI` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### plogr


|`plogr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### plot3D


|`plot3D` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### plot3Drgl


|`plot3Drgl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### plotly


|`plotly` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.10.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.10.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### plotmo


|`plotmo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.6.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.6.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.6.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### plotrix


|`plotrix` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.8-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pls


|`pls` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.8-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.8-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### plyr


|`plyr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### PMA


|`PMA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-3|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.2-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### png


|`png` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### PoissonSeq


|`PoissonSeq` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### poLCA


|`poLCA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.0.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### polspline


|`polspline` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.24|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.25|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Polychrome


|`Polychrome` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### polyclip


|`polyclip` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.10-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.10-7|`R-bundle-CRAN/2024.11-foss-2024a`|

### polycor


|`polycor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### polynom


|`polynom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### posterior


|`posterior` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.6.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### ppcor


|`ppcor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### prabclus


|`prabclus` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### pracma


|`pracma` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### PresenceAbsence


|`PresenceAbsence` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### preseqR


|`preseqR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### prettyGraphs


|`prettyGraphs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### princurve


|`princurve` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pROC


|`pROC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.18.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### prodlim


|`prodlim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.08.28|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2024.06.25|`R-bundle-CRAN/2024.11-foss-2024a`|

### profileModel


|`profileModel` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### proftools


|`proftools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.99-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### progress


|`progress` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### progressr


|`progressr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.14.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.15.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### projpred


|`projpred` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.7.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.8.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### proto


|`proto` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### proxy


|`proxy` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-27|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### proxyC


|`proxyC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pryr


|`pryr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pscl


|`pscl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.5.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pspline


|`pspline` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-19|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-20|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### psych


|`psych` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.9|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.4.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.4.6.26|`R-bundle-CRAN/2024.11-foss-2024a`|

### Publish


|`Publish` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.01.17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pulsar


|`pulsar` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### pvclust


|`pvclust` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### PWEALL


|`PWEALL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### qgam


|`qgam` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### qgraph


|`qgraph` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### qqman


|`qqman` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### qrng


|`qrng` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-10|`R-bundle-CRAN/2024.11-foss-2024a`|

### qrnn


|`qrnn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### quadprog


|`quadprog` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### quanteda


|`quanteda` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.3.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.0.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|4.1.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### quantmod


|`quantmod` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.25|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.26|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### quantreg


|`quantreg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.97|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.98|`R-bundle-CRAN/2024.06-foss-2023b`|
|5.99.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### questionr


|`questionr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### QuickJSR


|`QuickJSR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.8|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### R.cache


|`R.cache` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.16.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### R.matlab


|`R.matlab` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.7.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### R.methodsS3


|`R.methodsS3` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### R.oo


|`R.oo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.25.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.26.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.27.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### R.rsp


|`R.rsp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.45.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.46.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### R.utils


|`R.utils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.12.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### r2rtf


|`r2rtf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### R2WinBUGS


|`R2WinBUGS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-21|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-22.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### random


|`random` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### randomForest


|`randomForest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.7-1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.7-1.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### randomForestSRC


|`randomForestSRC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.3.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### randtoolbox


|`randtoolbox` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.5|`R-bundle-CRAN/2024.11-foss-2024a`|

### rangeModelMetadata


|`rangeModelMetadata` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ranger


|`ranger` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.16.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.17.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### RANN


|`RANN` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.6.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### rapidjsonr


|`rapidjsonr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rARPACK


|`rARPACK` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### raster


|`raster` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.6-26|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.6-30|`R-bundle-CRAN/2024.11-foss-2024a`|

### rasterVis


|`rasterVis` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.51.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ratelimitr


|`ratelimitr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RBesT


|`RBesT` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-3|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.7-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### rbibutils


|`rbibutils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.16|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### rbison


|`rbison` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rborist


|`Rborist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3-7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RCAL


|`RCAL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rcgmin


|`Rcgmin` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2022-4.30|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RCircos


|`RCircos` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RColorBrewer


|`RColorBrewer` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppArmadillo


|`RcppArmadillo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.12.6.6.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.12.8.4.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|14.2.0-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppEigen


|`RcppEigen` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.3.9.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.4.0.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.3.4.0.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppGSL


|`RcppGSL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppParallel


|`RcppParallel` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.1.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|5.1.9|`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppProgress


|`RcppProgress` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppRoll


|`RcppRoll` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppThread


|`RcppThread` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RcppTOML


|`RcppTOML` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RCurl


|`RCurl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.98-1.13|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.98-1.14|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.98-1.16|`R-bundle-CRAN/2024.11-foss-2024a`|

### rda


|`rda` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rdpack


|`Rdpack` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.6.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### rdrop2


|`rdrop2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reactable


|`reactable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reactR


|`reactR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### readbitmap


|`readbitmap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reader


|`reader` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### readODS


|`readODS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.3.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### readr


|`readr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### readxl


|`readxl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rebird


|`rebird` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### recipes


|`recipes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.10|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0.8|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### RefFreeEWAS


|`RefFreeEWAS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reformulas


|`reformulas` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### registry


|`registry` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### regsem


|`regsem` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### relsurv


|`relsurv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rematch


|`rematch` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rentrez


|`rentrez` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### renv


|`renv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.11|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.0.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.7|`R-bundle-CRAN/2024.06-foss-2023b`|

### reprex


|`reprex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### resample


|`resample` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reshape


|`reshape` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reshape2


|`reshape2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### reticulate


|`reticulate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.34.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.38.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.40.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### rex


|`rex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rgbif


|`rgbif` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.7.8|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.8.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.8.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### RGCCA


|`RGCCA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rgdal


|`rgdal` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6-7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rgeos


|`rgeos` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rgexf


|`rgexf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.16.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.16.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### rgl


|`rgl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.8|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.14|`R-bundle-CRAN/2024.11-foss-2024a`|

### Rglpk


|`Rglpk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6-5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rhandsontable


|`rhandsontable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RhpcBLASctl


|`RhpcBLASctl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.23-42|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ridge


|`ridge` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ridigbio


|`ridigbio` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.7|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.8|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.4.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### RInside


|`RInside` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.18|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rio


|`rio` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.2.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### riskRegression


|`riskRegression` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2023.09.08|`R-bundle-CRAN/2023.12-foss-2023a`|
|2023.12.21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ritis


|`ritis` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RItools


|`RItools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rJava


|`rJava` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-10|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rjson


|`rjson` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.21|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.23|`R-bundle-CRAN/2024.11-foss-2024a`|

### RJSONIO


|`RJSONIO` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-1.9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rle


|`rle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rlecuyer


|`rlecuyer` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rlemon


|`rlemon` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rlist


|`rlist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.6.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rmeta


|`rmeta` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rmpfr


|`Rmpfr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### rms


|`rms` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.7-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|6.8-1|`R-bundle-CRAN/2024.06-foss-2023b`|
|6.8-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### RMTstat


|`RMTstat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rmutil


|`rmutil` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.10|`R-bundle-CRAN/2024.11-foss-2024a`|

### rncl


|`rncl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rnetcarto


|`rnetcarto` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RNeXML


|`RNeXML` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rngtools


|`rngtools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rngWELL


|`rngWELL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10-10|`R-bundle-CRAN/2024.11-foss-2024a`|
|0.10-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|

### RNifti


|`RNifti` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### robustbase


|`robustbase` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.99-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.99-2|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.99-4-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### ROCR


|`ROCR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ROI


|`ROI` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ROI.plugin.glpk


|`ROI.plugin.glpk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rook


|`Rook` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rootSolve


|`rootSolve` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### roptim


|`roptim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rotl


|`rotl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rpact


|`rpact` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.4.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.0.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|4.1.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### rpart


|`rpart` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.1.23|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rpf


|`rpf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.14|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RPMM


|`RPMM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.25|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RPostgreSQL


|`RPostgreSQL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.7-6|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.7-7|`R-bundle-CRAN/2024.11-foss-2024a`|

### RPushbullet


|`RPushbullet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### rrcov


|`rrcov` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.7-6|`R-bundle-CRAN/2024.11-foss-2024a`|

### rredlist


|`rredlist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rsample


|`rsample` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rsconnect


|`rsconnect` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### Rserve


|`Rserve` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RSNNS


|`RSNNS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rsolnp


|`Rsolnp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.16|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RSpectra


|`RSpectra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.16-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.16-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### RSQLite


|`RSQLite` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3.7|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.3.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### Rssa


|`Rssa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### rstan


|`rstan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.32.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.32.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rstantools


|`rstantools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rstatix


|`rstatix` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rtdists


|`rtdists` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.11-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rtsne


|`Rtsne` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rttf2pt1


|`Rttf2pt1` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RUnit


|`RUnit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.32|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.33|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ruv


|`ruv` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rvertnet


|`rvertnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.8.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rvest


|`rvest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### rvinecopulib


|`rvinecopulib` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.3.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### Rvmmin


|`Rvmmin` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2018-4.17.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RWeka


|`RWeka` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-46|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### RWekajars


|`RWekajars` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.9.3-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### s2


|`s2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.6|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.1.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### sampling


|`sampling` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sandwich


|`sandwich` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-0|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.1-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### SBdecomp


|`SBdecomp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### scales


|`scales` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### scam


|`scam` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-14|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### scatterpie


|`scatterpie` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.2.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### scatterplot3d


|`scatterplot3d` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-44|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### scs


|`scs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sctransform


|`sctransform` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SDMTools


|`SDMTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-221.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### seewave


|`seewave` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### segmented


|`segmented` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-0|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.1-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### selectr


|`selectr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sem


|`sem` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-15|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-16|`R-bundle-CRAN/2024.11-foss-2024a`|

### semPLS


|`semPLS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### semTools


|`semTools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5-6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sendmailR


|`sendmailR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sensemakr


|`sensemakr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### sentometrics


|`sentometrics` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### seqinr


|`seqinr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2-36|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### servr


|`servr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.27|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.30|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.32|`R-bundle-CRAN/2024.11-foss-2024a`|

### setRNG


|`setRNG` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2022.4-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2024.2-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sf


|`sf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-14|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-16|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0-19|`R-bundle-CRAN/2024.11-foss-2024a`|

### sfheaders


|`sfheaders` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sfsmisc


|`sfsmisc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-16|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-18|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.1-20|`R-bundle-CRAN/2024.11-foss-2024a`|

### sgdGMF


|`sgdGMF` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### shadowtext


|`shadowtext` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.3|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.1.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### shape


|`shape` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.6.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### shapefiles


|`shapefiles` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### shinycssloaders


|`shinycssloaders` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### shinydashboard


|`shinydashboard` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### shinyjs


|`shinyjs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### shinystan


|`shinystan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### shinythemes


|`shinythemes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### signal


|`signal` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.8-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### SignifReg


|`SignifReg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SimDesign


|`SimDesign` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.17.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### simex


|`simex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SimSeq


|`SimSeq` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SKAT


|`SKAT` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### slam


|`slam` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-50|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1-55|`R-bundle-CRAN/2024.11-foss-2024a`|

### slider


|`slider` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### sm


|`sm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-5.7.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.2-6.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### smoof


|`smoof` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### smoother


|`smoother` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sn


|`sn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sna


|`sna` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.7-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### SNFtool


|`SNFtool` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### snow


|`snow` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SnowballC


|`SnowballC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### snowfall


|`snowfall` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.84-6.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SOAR


|`SOAR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.99-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### solrium


|`solrium` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### som


|`som` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3-5.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3-5.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### soundecology


|`soundecology` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### sp


|`sp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spaa


|`spaa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spacefillr


|`spacefillr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### spam


|`spam` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.10-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.11-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### spaMM


|`spaMM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.4.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SparseM


|`SparseM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.81|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.83|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.84-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### SPAtest


|`SPAtest` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spatial


|`spatial` version|R-bundle-CRAN modules that include it|
| --- | --- |
|7.3-17|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat


|`spatstat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-7|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0-8|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.3-0|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.core


|`spatstat.core` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.4-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.data


|`spatstat.data` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-2|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.1-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.explore


|`spatstat.explore` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2-7|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.3-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.geom


|`spatstat.geom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2-7|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2-9|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.3-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.linnet


|`spatstat.linnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.2-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.model


|`spatstat.model` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2-11|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.2-8|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.3-3|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.random


|`spatstat.random` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.2-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.2-3|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.3-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.sparse


|`spatstat.sparse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.1-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.univar


|`spatstat.univar` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### spatstat.utils


|`spatstat.utils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.1-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### spData


|`spData` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.3.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### spdep


|`spdep` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.3-6|`R-bundle-CRAN/2024.11-foss-2024a`|

### splitstackshape


|`splitstackshape` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spls


|`spls` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spocc


|`spocc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### spThin


|`spThin` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SQUAREM


|`SQUAREM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2021.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### stable


|`stable` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### stabledist


|`stabledist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.7-2|`R-bundle-CRAN/2024.11-foss-2024a`|

### stabs


|`stabs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### StanHeaders


|`StanHeaders` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.26.28|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.32.10|`R-bundle-CRAN/2024.11-foss-2024a`|
|2.32.9|`R-bundle-CRAN/2024.06-foss-2023b`|

### stargazer


|`stargazer` version|R-bundle-CRAN modules that include it|
| --- | --- |
|5.2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### stars


|`stars` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6-5|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.6-7|`R-bundle-CRAN/2024.11-foss-2024a`|

### startupmsg


|`startupmsg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.6.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.9.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### statip


|`statip` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### StatMatch


|`StatMatch` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### statmod


|`statmod` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### statnet


|`statnet` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2019.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### statnet.common


|`statnet.common` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.10.0|`R-bundle-CRAN/2024.11-foss-2024a`|
|4.9.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|

### stdReg


|`stdReg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### stopwords


|`stopwords` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### stringdist


|`stringdist` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### stringmagic


|`stringmagic` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### strucchange


|`strucchange` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5-4|`R-bundle-CRAN/2024.11-foss-2024a`|

### styler


|`styler` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.10.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.10.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### subplex


|`subplex` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.9|`R-bundle-CRAN/2024.11-foss-2024a`|

### SuperLearner


|`SuperLearner` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0-28.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0-29|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### SuppDists


|`SuppDists` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-9.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.1-9.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### survey


|`survey` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.4-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### survival


|`survival` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.5-7|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.7-0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### survivalROC


|`survivalROC` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### svd


|`svd` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### svglite


|`svglite` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### svUnit


|`svUnit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### swagger


|`swagger` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.33.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|5.17.14|`R-bundle-CRAN/2024.06-foss-2023b`|
|5.17.14.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### symmoments


|`symmoments` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tableone


|`tableone` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.13.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tabletools


|`tabletools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tau


|`tau` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-25|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.0-26|`R-bundle-CRAN/2024.11-foss-2024a`|

### taxize


|`taxize` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.100|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.100.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### tcltk2


|`tcltk2` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2-11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tclust


|`tclust` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5-5|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0-4|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.0-5|`R-bundle-CRAN/2024.11-foss-2024a`|

### TeachingDemos


|`TeachingDemos` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.12|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tensor


|`tensor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tensorA


|`tensorA` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.36.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.36.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tergm


|`tergm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|4.2.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### terra


|`terra` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-55|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-78|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.7-83|`R-bundle-CRAN/2024.11-foss-2024a`|

### testit


|`testit` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### texreg


|`texreg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.39.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### textcat


|`textcat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-9|`R-bundle-CRAN/2024.11-foss-2024a`|

### textplot


|`textplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### TFisher


|`TFisher` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### TH.data


|`TH.data` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### threejs


|`threejs` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tictoc


|`tictoc` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tidybayes


|`tidybayes` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|3.0.7|`R-bundle-CRAN/2024.11-foss-2024a`|

### tidygraph


|`tidygraph` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tidyr


|`tidyr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tidyselect


|`tidyselect` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tidytext


|`tidytext` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tidytree


|`tidytree` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tidyverse


|`tidyverse` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tiff


|`tiff` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### timechange


|`timechange` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### timeDate


|`timeDate` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4022.108|`R-bundle-CRAN/2023.12-foss-2023a`|
|4032.109|`R-bundle-CRAN/2024.06-foss-2023b`|
|4041.110|`R-bundle-CRAN/2024.11-foss-2024a`|

### timereg


|`timereg` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.6|`R-bundle-CRAN/2024.11-foss-2024a`|

### timeSeries


|`timeSeries` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4041.111|`R-bundle-CRAN/2024.11-foss-2024a`|

### tkrplot


|`tkrplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.0-27|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tm


|`tm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7-11|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.7-13|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.7-15|`R-bundle-CRAN/2024.11-foss-2024a`|

### tmap


|`tmap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.3-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tmaptools


|`tmaptools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.1-1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### TMB


|`TMB` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.9.12|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.9.15|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.9.9|`R-bundle-CRAN/2023.12-foss-2023a`|

### tmle


|`tmle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.1.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tmvnsim


|`tmvnsim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tmvtnorm


|`tmvtnorm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tokenizers


|`tokenizers` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### topicmodels


|`topicmodels` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2-15|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.2-16|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.2-17|`R-bundle-CRAN/2024.11-foss-2024a`|

### TraMineR


|`TraMineR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2-10|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|
|2.2-8|`R-bundle-CRAN/2023.12-foss-2023a`|

### tree


|`tree` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-43|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### triebeard


|`triebeard` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### trimcluster


|`trimcluster` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tripack


|`tripack` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-9.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-9.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### TruncatedNormal


|`TruncatedNormal` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### truncnorm


|`truncnorm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-9|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### trust


|`trust` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-8|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tseries


|`tseries` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.10-55|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.10-56|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.10-58|`R-bundle-CRAN/2024.11-foss-2024a`|

### tseriesChaos


|`tseriesChaos` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-13.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tsna


|`tsna` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tsne


|`tsne` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### TTR


|`TTR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.24.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tuneR


|`tuneR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.6|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### twang


|`twang` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.6.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### tweedie


|`tweedie` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tweenr


|`tweenr` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.0.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### tzdb


|`tzdb` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### ucminf


|`ucminf` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.2.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### udpipe


|`udpipe` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8.11|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### umap


|`umap` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.10.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### unbalanced


|`unbalanced` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### unikn


|`unikn` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### uniqueAtomMat


|`uniqueAtomMat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1-3-2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### units


|`units` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.8-5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### unmarked


|`unmarked` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.4.3|`R-bundle-CRAN/2024.11-foss-2024a`|

### UpSetR


|`UpSetR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### urca


|`urca` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.3-3|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.3-4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### urltools


|`urltools` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### uroot


|`uroot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1-2|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.1-3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### uuid


|`uuid` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2-0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.2-1|`R-bundle-CRAN/2024.11-foss-2024a`|

### V8


|`V8` version|R-bundle-CRAN modules that include it|
| --- | --- |
|4.4.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|4.4.2|`R-bundle-CRAN/2024.06-foss-2023b`|
|6.0.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### varhandle


|`varhandle` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.0.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### vcd


|`vcd` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4-11|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.4-12|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.4-13|`R-bundle-CRAN/2024.11-foss-2024a`|

### vcfR


|`vcfR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.15.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### vegan


|`vegan` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6-4|`R-bundle-CRAN/2023.12-foss-2023a`|
|2.6-6.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|2.6-8|`R-bundle-CRAN/2024.11-foss-2024a`|

### VennDiagram


|`VennDiagram` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### VGAM


|`VGAM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.1-11|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.1-12|`R-bundle-CRAN/2024.11-foss-2024a`|
|1.1-9|`R-bundle-CRAN/2023.12-foss-2023a`|

### VIM


|`VIM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.2.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### VineCopula


|`VineCopula` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.5.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|2.5.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### vioplot


|`vioplot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.5.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### vipor


|`vipor` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.5|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.4.7|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### viridis


|`viridis` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.6.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### viridisLite


|`viridisLite` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### visdat


|`visdat` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### visNetwork


|`visNetwork` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.1.2|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### vroom


|`vroom` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.6.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### VSURF


|`VSURF` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### warp


|`warp` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### waveslim


|`waveslim` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8.4|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.8.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### wdm


|`wdm` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.2.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### webshot


|`webshot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.5.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### webutils


|`webutils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.2.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.2.2|`R-bundle-CRAN/2024.11-foss-2024a`|

### weights


|`weights` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### WeightSVM


|`WeightSVM` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7-13|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7-16|`R-bundle-CRAN/2024.11-foss-2024a`|

### wellknown


|`wellknown` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.7.4|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### widgetframe


|`widgetframe` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.3.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### WikidataQueryServiceR


|`WikidataQueryServiceR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### WikidataR


|`WikidataR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.3.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### WikipediR


|`WikipediR` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.5.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### wikitaxa


|`wikitaxa` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### wk


|`wk` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.9.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`|
|0.9.4|`R-bundle-CRAN/2024.11-foss-2024a`|

### word2vec


|`word2vec` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### wordcloud


|`wordcloud` version|R-bundle-CRAN modules that include it|
| --- | --- |
|2.6|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### worrms


|`worrms` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.4.3|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### writexl


|`writexl` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.4.2|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.5.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.5.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### WriteXLS


|`WriteXLS` version|R-bundle-CRAN modules that include it|
| --- | --- |
|6.4.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|6.6.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|6.7.0|`R-bundle-CRAN/2024.11-foss-2024a`|

### XBRL


|`XBRL` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.99.19.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### xgboost


|`xgboost` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.7.6.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.7.7.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.7.8.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### xlsx


|`xlsx` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.5|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### xlsxjars


|`xlsxjars` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.6.1|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### XML


|`XML` version|R-bundle-CRAN modules that include it|
| --- | --- |
|3.99-0.16|`R-bundle-CRAN/2023.12-foss-2023a`|
|3.99-0.16.1|`R-bundle-CRAN/2024.06-foss-2023b`|
|3.99-0.17|`R-bundle-CRAN/2024.11-foss-2024a`|

### xts


|`xts` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.13.1|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.14.0|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.14.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### yaImpute


|`yaImpute` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.0-33|`R-bundle-CRAN/2023.12-foss-2023a`|
|1.0-34|`R-bundle-CRAN/2024.06-foss-2023b`|
|1.0-34.1|`R-bundle-CRAN/2024.11-foss-2024a`|

### yulab.utils


|`yulab.utils` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2023.12-foss-2023a`|
|0.1.4|`R-bundle-CRAN/2024.06-foss-2023b`|
|0.1.8|`R-bundle-CRAN/2024.11-foss-2024a`|

### zeallot


|`zeallot` version|R-bundle-CRAN modules that include it|
| --- | --- |
|0.1.0|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|

### zoo


|`zoo` version|R-bundle-CRAN modules that include it|
| --- | --- |
|1.8-12|`R-bundle-CRAN/2024.06-foss-2023b`<br/>`R-bundle-CRAN/2023.12-foss-2023a`<br/>`R-bundle-CRAN/2024.11-foss-2024a`|