---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Safetensors is a new simple format for storing tensors safely (as
    opposed to

    pickle) and that is still fast (zero-copy). Safetensors is really fast.


    This variant of Safetensors is installed with support for numpy and PyTorch

    '
  license: Not confirmed
  name: Safetensors
  offers:
    '@type': Offer
    price: 0
  operatingSystem: LINUX
  review:
    '@type': Review
    author:
      '@type': Organization
      name: EESSI
    reviewBody: Application has been successfully made available on all architectures
      supported by EESSI
    reviewRating:
      '@type': Rating
      ratingValue: 5
  softwareRequirements: See https://www.eessi.io/docs/ for how to make EESSI available
    on your system
  softwareVersion: '[''0.4.3'']'
  url: https://huggingface.co/docs/safetensors
---
# Safetensors


Safetensors is a new simple format for storing tensors safely (as opposed to
pickle) and that is still fast (zero-copy). Safetensors is really fast.

This variant of Safetensors is installed with support for numpy and PyTorch


<small>homepage: </small><span class="software-link">[https://huggingface.co/docs/safetensors](https://huggingface.co/docs/safetensors)</span>

## Available installations


|Safetensors version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|0.4.3|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202306">2023.06</span>|`Safetensors/0.4.3-gfbf-2023a`|

## Extensions

Overview of extensions included in Safetensors installations


### safetensors


|`safetensors` version|Safetensors modules that include it|
| --- | --- |
|0.4.3|`Safetensors/0.4.3-gfbf-2023a`|