---
json_ld:
  '@context': https://schema.org
  '@type': SoftwareApplication
  applicationCategory: DeveloperApplication
  description: "JAGS is Just Another Gibbs Sampler.  It is a program for analysis\n\
    \ of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation\
    \  "
  license: Not confirmed
  name: JAGS
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
  softwareVersion: '[''4.3.2'']'
  url: http://mcmc-jags.sourceforge.net/
---
# JAGS


JAGS is Just Another Gibbs Sampler.  It is a program for analysis
 of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation  

<small>homepage: </small><span class="software-link">[http://mcmc-jags.sourceforge.net/](http://mcmc-jags.sourceforge.net/)</span>

## Available installations


|JAGS version|Supported CPU targets|Supported GPU targets|EESSI version|Module|
| --- | --- | --- | --- | --- |
|4.3.2|`generic`: `aarch64`, `x86_64`<br/><span class="software-cpu-arm">Arm</span>: `a64fx`, `neoverse_n1`, `neoverse_v1`, `nvidia/grace`<br/><span class="software-cpu-amd">AMD</span>: `zen2`, `zen3`, `zen4`, `zen5`<br/><span class="software-cpu-intel">Intel</span>: `haswell`, `skylake_avx512`, `sapphirerapids`, `icelake`, `cascadelake`<br/>|*(none)*|<span class="software-eessi-version-202506">2025.06</span>|`JAGS/4.3.2-foss-2025b`|