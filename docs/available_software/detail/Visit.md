---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: '

    VisIt is an Open Source, interactive, scalable, visualization, animation

    and analysis tool. From Unix, Windows or Mac workstations, users can

    interactively visualize and analyze data ranging in scale from small

    (<10 core) desktop-sized projects to large (>10^5 core) leadership-class

    computing facility simulation campaigns. Users can quickly generate

    visualizations, animate them through time, manipulate them with a

    variety of operators and mathematical expressions, and save the

    resulting images and animations for presentations. VisIt contains a rich

    set of visualization features to enable users to view a wide variety of

    data including scalar and vector fields defined on two- and

    three-dimensional (2D and 3D) structured, adaptive and unstructured

    meshes. Owing to its customizable plugin design, VisIt is capable of

    visualizing data from over 120 different scientific data formats.

    '
  license: Not confirmed
  name: Visit
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
  softwareVersion: '[''3.4.2'']'
  url: https://github.com/visit-dav/visit
---
# Visit



VisIt is an Open Source, interactive, scalable, visualization, animation
and analysis tool. From Unix, Windows or Mac workstations, users can
interactively visualize and analyze data ranging in scale from small
(<10 core) desktop-sized projects to large (>10^5 core) leadership-class
computing facility simulation campaigns. Users can quickly generate
visualizations, animate them through time, manipulate them with a
variety of operators and mathematical expressions, and save the
resulting images and animations for presentations. VisIt contains a rich
set of visualization features to enable users to view a wide variety of
data including scalar and vector fields defined on two- and
three-dimensional (2D and 3D) structured, adaptive and unstructured
meshes. Owing to its customizable plugin design, VisIt is capable of
visualizing data from over 120 different scientific data formats.


<small>homepage: </small><span class="software-link">[https://github.com/visit-dav/visit](https://github.com/visit-dav/visit)</span>

## Available installations


|Visit version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|3.4.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Visit/3.4.2-foss-2024a`|