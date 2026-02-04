---
authors: [jngrad]
date: 2025-12-04
slug: gh-ci-workflow-for-EESSI
render_macros: false
---

# GitHub CI/CD workflows with EESSI

In a previous blog post, [“An example CI workflow that leverages EESSI CI tools”](https://www.eessi.io/docs/blog/2024/10/11/ci-workflow-for-EESSI/),
Pedro Santos Neves explained how to set up a GitLab CI workflow.
This post will focus on GitHub CI workflows and show how to access the development repository of EESSI.

<!-- more -->

## Using the CI component in GitHub

We will use the [pyMBE](https://github.com/pyMBE-dev/pyMBE)[^Beyer2024] and
[SwarmRL](https://github.com/SwarmRL/SwarmRL)[^Tovey2025] projects as examples.
They both rely on the molecular dynamics simulation package
[ESPResSo](https://github.com/espressomd/espresso)[^Weik2019] available in EESSI.
SwarmRL requires features only available in the development version of ESPResSo,
while pyMBE supports both the last stable release of ESPResSo and the development branch of ESPResSo.
EESSI can satisfy both communities: [`software.eessi.io`](https://software.eessi.io)
provides stable releases of scientific software identified by their version number,
while [`dev.eessi.io`](https://dev.eessi.io) provides development snapshots identified by a commit hash.

Historically, both SwarmRL and pyMBE had to build ESPResSo from sources in every CI job.
This added 15 min of build time and required extra steps to properly install build dependencies (pyMBE)
or configure a custom Docker image (SwarmRL).
Both projects migrated to the [EESSI GitHub Action](https://github.com/marketplace/actions/eessi)
to reduce the complexity and execution times of their CI/CD workflows.

### Quickstart

The SwarmRL project uses a compact CI/CD workflow[^swarmrl-commit-181edfa-cicd-workflow]
that loads project dependencies from EESSI, installs extra Python dependencies
in a virtual environment, runs the testsuite, and uploads a code coverage report.
It is reproduced here, simplified for clarity, with annotations:

```yaml linenums="1" title="CI/CD workflow definition"
name: ESPResSo tests
on:
  pull_request:
  push:
    branches:
jobs:
  testsuite:
    runs-on: ubuntu-latest # (1)
    steps:
      - uses: actions/checkout@v4 # (2)
      - name: Setup EESSI
        uses: eessi/github-action-eessi@v3 # (3)
        with:
          eessi_stack_version: "2023.06"
      - name: Install dependencies # (4)
        run: |
          test "${RUNNER_ARCH}" = "X64" && module use /cvmfs/dev.eessi.io/espresso/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all
          module load ESPResSo/dc87ede3f6c218bb71624460752bc8c26a271c33-foss-2023b
          module save espresso
          python -m venv --system-site-packages venv
          source venv/bin/activate
          python -m pip install .
      - name: Run test suite # (5)
        run: |
          module restore espresso
          source venv/bin/activate
          export NUM_PROC=$(nproc)
          export OMP_PROC_BIND=false OMP_NUM_THREADS=1
          COVERAGE=1 sh CI/run_espresso_test_suite.sh -j ${NUM_PROC}
          python -m coverage combine . CI/espresso_tests
          python -m coverage report
          python -m coverage xml
      - name: Upload coverage to Codecov # (6)
        if: ${{ github.repository == 'SwarmRL/SwarmRL' }}
        uses: codecov/codecov-action@v5
        with:
          files: "./coverage.xml"
          disable_search: true
          env_vars: OS,PYTHON
          token: ${{ secrets.CODECOV_TOKEN }}
```

1. Run the testsuite in a virtual machine with the latest Ubuntu operating system, using an AMD Zen3 host machine.
2. Locally clone the repository and checkout the branch that triggered the workflow.
3. Set up the EESSI software stack version 2023.06 for the automatically-detected microarchitecture of the host machine.
4. Set up project dependencies:
     * activate the `dev.eessi.io` development repository using version 2023.06 and microarchitecture AMD Zen2 (line 17 not required when only `software.eessi.io` is needed)
     * load the ESPResSo package from commit hash [`dc87ede`](https://github.com/espressomd/espresso/commit/dc87ede3f6c218bb71624460752bc8c26a271c33)
     * create a Python virtual environment and install project dependencies not available in EESSI
5. Reload the software environment and run the testsuite with code coverage enabled.
6. Publish the code coverage report.

This workflow is transferable to other software projects with minimal changes.
For a Python project, it is only a matter of substituting lines 18 and 29 by the appropriate commands.
For projects in other programming languages, Python-specific commands can be safely removed.

When a workflow grows in complexity, it might be desirable to decouple
the dependencies installation step from the testsuite step.
One can leverage the modular architecture of GitHub Action workflows
and delegate dependencies management to a self-contained action
that can be called from the CI/CD workflow.
We will explore this strategy in the next section.

### A custom action to manage dependencies

Actions are reusable building blocks that are called from a workflow.
We already saw the EESSI action and the Codecov action in the previous section.
[Custom actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions)
use the same syntax and structure as workflows, but are stored in a different folder:
actions go to `.github/actions/my_action/action.yml`,
while workflows go to `.github/workflows/my_workflow.yml`.

Here is how pyMBE defines a custom action to manage dependencies with EESSI and pip[^pymbe-tag-100-deps-action]:

```yaml linenums="1" title="Custom action to manage dependencies"
name: 'dependencies'
description: 'Install project dependencies'
inputs:
  modules:
    description: Newline-separated list of arguments for module load.
    required: true
  extra-python-packages:
    description: Newline-separated list of arguments for pip install.
    required: false
runs:
  using: "composite"
  steps:
    - run: |
        test "${RUNNER_ARCH}" = "X64" && module use /cvmfs/dev.eessi.io/espresso/versions/2023.06/software/linux/x86_64/amd/zen2/modules/all
        module load ${{ inputs.modules }}
        module save espresso
        python3 -m venv --system-site-packages venv
        source venv/bin/activate
        echo -e "\n" >> requirements.txt
        echo "${{ inputs.extra-python-packages }}" >> requirements.txt
        python3 -m pip install -r requirements.txt
        git restore requirements.txt
        deactivate
        module purge
      shell: bash
```

A workflow that calls this action will load software from an EESSI stack (argument `modules`)
and install Python packages from PyPI (argument `extra-python-packages`).
Packages are managed by a Lmod [module collection](https://lmod.readthedocs.io/en/latest/010_user.html#rules-for-loading-modules-from-a-collection)
and by a Python [virtual environment](https://docs.python.org/3/library/venv.html).

The steps can be broken down as follows:

* source the `dev.eessi.io` development repository, which extends the `software.eessi.io` production repository already sourced by the EESSI GitHub Action
    * line 14 can be removed when only the `software.eessi.io` repository is needed
    * microarchitecture `x86_64/amd/zen2` is selected, which is forward-compatible with the Zen3 microarchitecture
      available on [standard GitHub-hosted runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories)
    * Ubuntu ARM64 runners have microarchitecture compatible with  the `aarch64/nvidia/grace` software stack that EESSI ships
* load the list of EESSI modules provided by the workflow and stash them to a collection called `espresso`
* create a Python virtual environment that gives priority to Python packages available in EESSI
  (`venv` option `--system-site-packages`, other package managers have a different syntax)
* source the Python virtual environment
* paste the list of Python package requirements from the workflow into the project's
  `requirements.txt`, pip install them, and restore `requirements.txt`
* clean up the session

This action allows us to "hide" the logic for package installation,
and should only be edited by project maintainers.
Project developers can ignore this file and focus on the workflow, described in the next section.

### A modular CI/CD workflow

We will define a CI/CD workflow that sets up project dependencies, runs the testsuite,
uploads a code coverage report, and builds the software documentation for deployment
to [GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages).
Since the file is rather long, we will break it down into reusable code fragments and go through them with the help
of the [workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) reference page.

We start by defining a workflow called `testsuite` that is automatically triggered
when pushing a commit to a branch (`push` event) or updating a pull request (`pull_request` event):

```yaml linenums="1" title="Workflow general properties"
name: testsuite
on:
  push:
  pull_request:
permissions:
  contents: read # to fetch code (actions/checkout)
```

We then define a job to run in an Ubuntu 24.04 virtual machine:

```yaml linenums="7" title="Virtual machine settings"
jobs:
  ubuntu:
    runs-on: ubuntu-24.04
    env:
      FI_PROVIDER: "^psm3,psm3;ofi_rxd"
      OMPI_MCA_mtl_ofi_provider_exclude: psm3
```

Since details about the host machine hardware can be fuzzy in a virtual machine,
we need to help OpenMPI select a suitable communication mechanism with environment variables (`env` field).
Other MPI implementations and virtual machines may require their own workarounds.

Next, we define a [matrix strategy](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations)
to automatically create jobs with different input parameters:

```yaml linenums="13" title="Job matrix configuration"
    strategy:
      matrix:
        espresso:
          - version: "4.2.2"
            eessi: ESPResSo/4.2.2-foss-2023a
          - version: "5.0-dev"
            eessi: ESPResSo/8aa60cecd56cdd10ab62042c567552f347374f36-foss-2023b
    name: ubuntu - ESPResSo ${{ matrix.espresso.version }}
```

In this case, we simply define a flat list with two elements, one for each ESPResSo version,
and give the job a name that reflects the input parameters combination.
The syntax also accepts lists of values, in which case the *n*-fold Cartesian product would be evaluated.

We can now define the steps that will be executed by every job of the job matrix:

```yaml linenums="21" title="Cloning the repository and setting up project dependencies"
    steps:
      - name: Checkout repository
        uses: actions/checkout@main
      - name: Setup EESSI
        uses: eessi/github-action-eessi@v3
        with:
          eessi_stack_version: "2023.06"
      - name: Install dependencies
        uses: ./.github/actions/dependencies
        with:
          modules: |-
            ${{ matrix.espresso.eessi }}
          extra-python-packages: |-
            pylint==3.0.3
            coverage==7.4.4
            pdoc==15.0.3
```

We start by cloning the git repository and checking out the branch that triggered the workflow.
We then set up the EESSI 2023.06 stack version (it needs to match the one defined in our custom action
in the [previous section](#a-custom-action-to-manage-dependencies)).
Finally, we use our custom action to install dependencies,
using the job matrix parameters to select a specific ESPResSo version
and providing a list of extra packages for code linting, code coverage and documentation generation.

We now have a complete environment to run the actual testsuite:

```yaml linenums="37" title="Testing the code"
      - name: Run testsuite
        run: |
          module restore espresso
          source venv/bin/activate
          make pylint
          make unit_tests -j4 COVERAGE=1
          make docs
          make coverage_xml
          deactivate
          module purge
        shell: bash
```

This step:

* reloads the module collection called `espresso` (which contains ESPResSo and its dependencies, such as Python and NumPy)
  and sources the Python virtual environment (which contains tools for code linting and coverage)
* runs static code analysis (`make pylint`) to detect anti-patterns
* runs the testsuite (`make unit_tests`)
    * `-j4` lets the test driver run the tests concurrently on all 4 CPU cores
    * `COVERAGE=1` is a pyMBE-specific Makefile variable to enable code coverage collection (injects `-m coverage run --parallel-mode` in the Python invocation of ESPResSo)
* generates the software documentation in HTML format (`make docs`)
* generates the code coverage report in XML format (`make coverage_xml`)

We now turn our attention to the continuous delivery part of the workflow:

```yaml linenums="48" title="Saving the software documentation as an artifact"
      - name: Upload artifact
        if: ${{ matrix.espresso.upload_artifact }}
        uses: actions/upload-artifact@v4
        with:
          path: "./documentation"
          name: documentation
          retention-days: 2
          if-no-files-found: error
```

The software documentation is uploaded to
[workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts)
with a 48h retention policy, but only with the stable release of ESPResSo.
When the CI/CD workflow runs on the main branch of the repository and is successful,
a separate deployment workflow[^pymbe-tag-100-deploy-workflow] is automatically triggered
to download the artifact and publish it to [pymbe-dev.github.io/pyMBE](https://pymbe-dev.github.io/pyMBE).

The code coverage report is submitted to [Codecov](https://about.codecov.io/) using an upload token:

```yaml linenums="56" title="Publishing the code coverage report"
      - name: Upload coverage to Codecov
        if: ${{ github.repository == 'pyMBE-dev/pyMBE' }}
        uses: codecov/codecov-action@v4
        with:
          file: "./coverage.xml"
          disable_search: true
          env_vars: OS,PYTHON
          fail_ci_if_error: false
          flags: unittests
          token: ${{ secrets.CODECOV_TOKEN }}
          verbose: true
```

Coverage reports are published to [app.codecov.io/gh/pyMBE-dev/pyMBE](https://app.codecov.io/gh/pyMBE-dev/pyMBE).
The readme file of the pyMBE project also displays a code coverage badge that
dynamically refreshes every time the main branch is updated.
This step is skipped on forked projects, although fork owners can manually activate it
in a new branch by removing the `if` field and setting up their own token.

Here is the complete workflow[^pymbe-tag-100-cicd-workflow]:

```yaml linenums="1" title="CI/CD workflow definition"
name: testsuite
on:
  push:
  pull_request:
permissions:
  contents: read # to fetch code (actions/checkout)
jobs:
  ubuntu:
    runs-on: ubuntu-24.04
    env:
      FI_PROVIDER: "^psm3,psm3;ofi_rxd"
      OMPI_MCA_mtl_ofi_provider_exclude: psm3
    strategy:
      matrix:
        espresso:
          - version: "4.2.2"
            eessi: ESPResSo/4.2.2-foss-2023a
          - version: "5.0-dev"
            eessi: ESPResSo/8aa60cecd56cdd10ab62042c567552f347374f36-foss-2023b
    name: ubuntu - ESPResSo ${{ matrix.espresso.version }}
    steps:
      - name: Checkout repository
        uses: actions/checkout@main
      - name: Setup EESSI
        uses: eessi/github-action-eessi@v3
        with:
          eessi_stack_version: "2023.06"
      - name: Install dependencies
        uses: ./.github/actions/dependencies
        with:
          modules: |-
            ${{ matrix.espresso.eessi }}
          extra-python-packages: |-
            pylint==3.0.3
            coverage==7.4.4
            pdoc==15.0.3
      - name: Run testsuite
        run: |
          module restore espresso
          source venv/bin/activate
          make pylint
          make unit_tests -j4 COVERAGE=1
          make docs
          make coverage_xml
          deactivate
          module purge
        shell: bash
      - name: Upload artifact
        if: ${{ matrix.espresso.upload_artifact }}
        uses: actions/upload-artifact@v4
        with:
          path: "./documentation"
          name: documentation
          retention-days: 2
          if-no-files-found: error
      - name: Upload coverage to Codecov
        if: ${{ github.repository == 'pyMBE-dev/pyMBE' }}
        uses: codecov/codecov-action@v4
        with:
          file: "./coverage.xml"
          disable_search: true
          env_vars: OS,PYTHON
          fail_ci_if_error: false
          flags: unittests
          token: ${{ secrets.CODECOV_TOKEN }}
          verbose: true
```

## Conclusion

We have just learned how to configure CI/CD workflows to install dependencies,
run a testsuite, upload coverage reports, and generate software documentation.
The pyMBE and SwarmRL workflows are modular and can be easily adapted to fit the needs of your own project.

If you are new to the GitHub workflow syntax, don't worry:
it is easy to learn and the GitHub documentation is extremely well-written.
To troubleshoot any issue with your first workflow, consider using the GitHub Action
[tmate](https://github.com/marketplace/actions/debugging-with-tmate) to remotely
log into the virtual machine via SSH or web shell.
To do so, add the following step after the checkout step:

```yaml linenums="1" title="Remotely logging into a virtual machine"
      - name: Setup tmate session
        uses: mxschmitt/action-tmate@v3
        with:
          detached: true
          limit-access-to-actor: true
```

The EESSI GitHub Action streamlines the installation of scientific software
in the cloud, reduces the complexity of CI/CD workflows, tightens the CI feedback
loop for developers and saves on billable hours for cloud resources.

Another use case for the EESSI GitHub Action is executable research papers[^Lasser2020].
There is more than one way to design them; in the case of pyMBE, all simulation scripts
from the pyMBE paper[^Beyer2024] were added to the code repository as code samples
that run every two weeks in a samples workflow[^pymbe-tag-100-samples-workflow]
to detect regressions in the development branch of the software.
The workflow can be triggered manually, for example before merging a large pull request,
and takes 1h of runtime, compared to the 10min runtime of the CI/CD workflow.

[^Beyer2024]: David Beyer, Paola B. Torres, Sebastian P. Pineda, Claudio F. Narambuena, Jean-Noël Grad, Peter Košovan, and Pablo M. Blanco. “pyMBE: the Python-based molecule builder for ESPResSo”. In: The Journal of Chemical Physics 161.2 (Modular and Interoperable Software for Chemical Physics, July 2024), pp. 022502, doi:[10.1063/5.0216389](https://doi.org/10.1063/5.0216389).
[^Tovey2025]: Samuel Tovey, Christoph Lohrmann, Tobias Merkt, David Zimmer, Konstantin Nikolaou, Simon Koppenhöfer, Anna Bushmakina, Jonas Scheunemann, and Christian Holm. “SwarmRL: building the future of smart active systems”. In: The European Physical Journal E 48.4–5 (April 2025), pp. 16, doi:[10.1140/epje/s10189-025-00477-4](https://doi.org/10.1140/epje/s10189-025-00477-4).
[^Weik2019]: Florian Weik, Rudolf Weeber, Kai Szuttor, Konrad Breitsprecher, Joost de Graaf, Michael Kuron, Jonas Landsgesell, Henri Menke, David Sean, and Christian Holm. “ESPResSo 4.0 – an extensible software package for simulating soft matter systems”. In: The European Physical Journal Special Topics, 227.14 (March 2019), pp. 1789–1816, doi:[10.1140/epjst/e2019-800186-9](https://doi.org/10.1140/epjst/e2019-800186-9).
[^Lasser2020]: Jana Lasser. “Creating an executable paper is a journey through Open Science”. In: Communications Physics 3.1 (August 2020), pp.143, doi:[10.1038/s42005-020-00403-4](https://doi.org/10.1038/s42005-020-00403-4).
[^swarmrl-commit-181edfa-cicd-workflow]: SwarmRL `181edfa` CI/CD workflow: [SwarmRL/SwarmRL@`181edfa`:`.github/workflows/espresso.yml`](https://github.com/SwarmRL/SwarmRL/blob/181edfa/.github/workflows/espresso.yml)
[^pymbe-tag-100-deps-action]: pyMBE v1.0.0 custom action: [pyMBE-dev/pyMBE@1.0.0:`.github/actions/dependencies/action.yml`](https://github.com/pyMBE-dev/pyMBE/blob/1.0.0/.github/actions/dependencies/action.yml)
[^pymbe-tag-100-cicd-workflow]: pyMBE v1.0.0 CI/CD workflow: [pyMBE-dev/pyMBE@1.0.0:`.github/workflows/testsuite.yml`](https://github.com/pyMBE-dev/pyMBE/blob/1.0.0/.github/workflows/testsuite.yml)
[^pymbe-tag-100-deploy-workflow]: pyMBE v1.0.0 GitHub Pages workflow: [pyMBE-dev/pyMBE@1.0.0:`.github/workflows/deploy.yml`](https://github.com/pyMBE-dev/pyMBE/blob/1.0.0/.github/workflows/deploy.yml)
[^pymbe-tag-100-samples-workflow]: pyMBE v1.0.0 samples workflow: [pyMBE-dev/pyMBE@1.0.0:`.github/workflows/samples.yml`](https://github.com/pyMBE-dev/pyMBE/blob/1.0.0/.github/workflows/samples.yml)
