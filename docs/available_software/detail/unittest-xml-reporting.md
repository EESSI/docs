---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'A unittest test runner that can save test results to XML files in
    xUnit format.

    The files can be consumed by a wide range of tools, such as build systems, IDEs
    and continuous integration servers.'
  license: Not confirmed
  name: unittest-xml-reporting
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
  softwareVersion: '[''3.1.0'']'
  url: http://github.com/xmlrunner/unittest-xml-reporting
---
# unittest-xml-reporting


A unittest test runner that can save test results to XML files in xUnit format.
The files can be consumed by a wide range of tools, such as build systems, IDEs and continuous integration servers.

<small>homepage: </small><span class="software-link">[http://github.com/xmlrunner/unittest-xml-reporting](http://github.com/xmlrunner/unittest-xml-reporting)</span>

## Available installations


|unittest-xml-reporting version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.1.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`unittest-xml-reporting/3.1.0-GCCcore-13.3.0`|