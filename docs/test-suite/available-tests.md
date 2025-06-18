# Available tests { #available-tests }

For a complete overview of all available tests in the EESSI test suite, see the
[`eessi/testsuite/tests/apps`](https://github.com/EESSI/test-suite/tree/main/eessi/testsuite/tests/apps) subdirectory in the `EESSI/test-suite` GitHub repository.

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

## OSU Micro-Benchmarks { #osumicrobenchmarks }

A test for [OSU Micro-Benchmarks](https://mvapich.cse.ohio-state.edu/benchmarks/), which provides an MPI benchmark. 

It is implemented in [`tests/apps/osu.py`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/apps/osu.py).

To run this OSU Micro-Benchmark, use:

```bash
reframe --run --name OSU-Micro-Benchmarks
```

!!! warning
    This test requires OSU Micro-Benchmarks v5.9 or newer, using an older OSU -Micro-Benchmark version will not work!

## ESPResSo { #espresso }

A test for [ESPResSo](https://espressomd.org), a software package for performing and analysing scientific molecular dynamics simulations.

It is implemented in [`tests/apps/espresso/`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/apps/espresso).

2 test cases are included:
* P3M (ionic crystals)
* LJ (Lennard Jones particle box)

Both tests are weak scaling tests and therefore the number of particles are scaled based on the number of MPI ranks.

To run this ESPResSo test, use:

```bash
reframe --run --name ESPResSo
```

## QuantumESPRESSO { #quantumespresso }

A test for [QuantumESPRESSO](https://www.quantum-espresso.org), an integrated suite of computer codes for electronic-structure calculations and materials modeling at the nanoscale. It is based on density-functional theory, plane waves, and pseudopotentials (both norm-conserving and ultrasoft).

It is implemented in [`tests/apps/QuantumESPRESSO.py`](https://github.com/EESSI/test-suite/blob/main/eessi/testsuite/tests/apps/QuantumESPRESSO.py).

To run this QuantumESPRESSO test, use:

```bash
reframe --run --name QuantumESPRESSO
```

!!! warning
    This test requires ReFrame v4.6.0 or newer, in older versions the QuantumESPRESSO test is not included in hpctestlib!

## PyTorch { #pytorch }

A test for [PyTorch](https://pytorch.org/), a machine learning library based on the Torch library, used for applications such as computer vision and natural language processing, originally developed by Meta AI and now part of the Linux Foundation umbrella.

This particular benchmark runs a selected torchvision model from the list:
* VGG16
* Resnet50
* Resnet152
* Densenet121
* Mobilenet_v3_large
on synthetic data. The test runs on both CPUs and GPUs (currently only supports CUDA).

To run this PyTorch test, use:

```bash
reframe --run --name PyTorch
```


## CP2K { #cp2k }

A test for [CP2K](https://www.cp2k.org/), a quantum chemistry and solid state physics software package that can perform atomistic simulations of solid state, liquid, molecular, periodic, material, crystal, and biological systems.

This particular benchmark runs a system with a selected number of H2O molecules and compares to a final reference energy
once equillibrium is attained. Three systems are possible based on the number of water molecules:
* 32
* 128
* 512

To run this CP2K test, use:

```bash
reframe --run --name CP2K
```


## LAMMPS { #lammps }

A test for [LAMMPS](https://www.lammps.org/#gsc.tab=0), a classical molecular dynamics code with a focus on materials modeling. It's an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator.

This module tests the binary 'lmp' in available modules containing substring 'LAMMPS'.
The tests come from the lammps github repository and test the LJ and Rhodo tests described
[here](https://docs.lammps.org/Speed_bench.html).

To run this LAMMPS test, use:

```bash
reframe --run --name LAMMPS
```


## MetalWalls { #metalwalls }

A test for [MetalWalls](https://gitlab.com/ampere2/metalwalls), a molecular dynamics code dedicated to the modelling of electrochemical systems.

The benchmarks consist of a set of different inputs files that vary in the number of atoms and the type of simulation performed. They can be found in the repository linked above, which is also versioned.

To run this MetalWalls test, use:

```bash
reframe --run --name MetalWalls
```

## OpenFOAM {  #openfoam }

A test for [OpenFOAM](https://www.openfoam.com/), an open source CFD software package.

The test runs a Lid-driven cavity flow.

To run this OpenFOAM test, use:

```bash
reframe --run --name OpenFOAM
```
