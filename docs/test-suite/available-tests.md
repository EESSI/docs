# Available tests { #available-tests }

The EESSI test suite currently includes tests for:

* [GROMACS](#gromacs)
* [TensorFlow](#tensorflow)

For a complete overview of all available tests in the EESSI test suite, see the
[`eessi/testsuite/tests`](https://github.com/EESSI/test-suite/tree/main/eessi/testsuite/tests) subdirectory in the `EESSI/test-suite` GitHub repository.

## GROMACS { #gromacs }

Several tests for [GROMACS](https://www.gromacs.org), a software package to perform molecular dynamics simulations,
are included, which use the systems included in the [HECBioSim benchmark suite](https://www.hecbiosim.ac.uk/access-hpc/benchmarks):

* `Crambin` (20K atom system)
* `Glutamine-Binding-Protein` (61K atom system)
- `hEGFRDimer` (465K atom system)
- `hEGFRDimerSmallerPL` (465K atom system, only 10k steps)
- `hEGFRDimerPair` (1.4M atom system)
- `hEGFRtetramerPair` (3M atom system)

It is implemented in [`tests/apps/gromacs.py`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/apps/gromacs.py),
on top of the GROMACS test that is included in the [ReFrame test library `hpctestlib`](https://reframe-hpc.readthedocs.io/en/stable/hpctestlib.html).

To run this GROMACS test with all HECBioSim systems, use:

```bash
reframe --run --name GROMACS
```

To run this GROMACS test only for a specific HECBioSim system, use for example:

```bash
reframe --run --name 'GROMACS.*HECBioSim/hEGFRDimerPair'
```

To run this GROMACS test with the smallest HECBioSim system (`Crambin`), you can use the `CI` tag:

```bash
reframe --run --name GROMACS --tag CI
```

## TensorFlow { #tensorflow }

A test for [TensorFlow](https://www.tensorflow.org), a machine learning framework, is included,
which is based on the ["Multi-worker training with Keras" TensorFlow tutorial](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras).

It is implemented in [`tests/apps/tensorflow/`](https://github.com/EESSI/test-suite/tree/main/eessi/testsuite/tests/apps/tensorflow).

To run this TensorFlow test, use:

```bash
reframe --run --name TensorFlow
```

!!! warning
    This test requires TensorFlow v2.11 or newer, using an older TensorFlow version will not work!
