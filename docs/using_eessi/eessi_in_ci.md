# Leveraging EESSI for Continuous Integration

EESSI is already available as both a GitHub Action and a GitLab CI/CD component, which means you can easily integrate
it if you use continuous integration within those ecosystems.

!!! note

    Both of these EESSI CI tools support the use of [`direnv`](https://direnv.net/) to allow you to store your desired
    environment within a `.envrc` file within your repository. See the documentation of the individual tools for
    detailed usage.

## The EESSI GitHub Action

You can find the EESSI GitHub Action can be found on the [GitHub Marketplace](https://github.com/marketplace),
at [https://github.com/marketplace/actions/eessi](https://github.com/marketplace/actions/eessi) .
Below is a minimal example of how to leverage the action, for detailed usage please refer to the official action
documentation.

``` { .yaml .copy }
name: Minimal usage
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: eessi/github-action-eessi@v3
    - name: Test EESSI
      run: |
        module avail
      shell: bash
```

## The EESSI GitLab CI/CD component

The EESSI GitLab CI/CD component can be found in the [GitLab CI/CD Catalog](https://gitlab.com/explore/catalog), at
[https://gitlab.com/explore/catalog/eessi/gitlab-eessi](https://gitlab.com/explore/catalog/eessi/gitlab-eessi) .
Below is a minimal example of how to leverage the component, for detailed usage please refer to the official
component documentation.

``` { .yaml .copy }
include:
  - component: $CI_SERVER_FQDN/eessi/gitlab-eessi/eessi@1.0.5

build:
  stage: build
  script:
    - module spider GROMACS
```

