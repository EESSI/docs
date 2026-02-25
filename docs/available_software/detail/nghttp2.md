# nghttp2



This is an implementation of the Hypertext Transfer Protocol version 2 in C.

The framing layer of HTTP/2 is implemented as a reusable C library.
On top of that, we have implemented an HTTP/2 client, server and proxy.
We have also developed load test and benchmarking tools for HTTP/2.

An HPACK encoder and decoder are available as a public API.

<small>homepage: </small><span class="software-link">[https://github.com/nghttp2/nghttp2](https://github.com/nghttp2/nghttp2)</span>

## Available installations


|nghttp2 version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|1.58.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`nghttp2/1.58.0-GCC-12.3.0`|