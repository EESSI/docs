---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: 'Optuna is an automatic hyperparameter optimization software framework,

    particularly designed for machine learning. It features an imperative,

    define-by-run style user API. Thanks to our define-by-run API, the code written

    with Optuna enjoys high modularity, and the user of Optuna can dynamically

    construct the search spaces for the hyperparameters.'
  license: Not confirmed
  name: Optuna
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
  softwareVersion: '[''4.5.0'']'
  url: https://optuna.org/
---
# Optuna


Optuna is an automatic hyperparameter optimization software framework,
particularly designed for machine learning. It features an imperative,
define-by-run style user API. Thanks to our define-by-run API, the code written
with Optuna enjoys high modularity, and the user of Optuna can dynamically
construct the search spaces for the hyperparameters.

<small>homepage: </small><span class="software-link">[https://optuna.org/](https://optuna.org/)</span>

## Available installations


|Optuna version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.5.0|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`Optuna/4.5.0-foss-2025a`|

## Extensions

Overview of extensions included in Optuna installations


### cmaes


|`cmaes` version|Optuna modules that include it|
| --- | --- |
|0.12.0|`Optuna/4.5.0-foss-2025a`|

### colorlog


|`colorlog` version|Optuna modules that include it|
| --- | --- |
|6.9.0|`Optuna/4.5.0-foss-2025a`|

### optuna


|`optuna` version|Optuna modules that include it|
| --- | --- |
|4.5.0|`Optuna/4.5.0-foss-2025a`|