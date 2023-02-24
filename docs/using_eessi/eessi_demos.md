# Running EESSI demos

To really experience how using EESSI can significantly facilitate the work of scientific researchers,
we recommend running one or more of the EESSI demos.

First, clone the ``eessi-demo`` Git repository, and move into the resulting directory:

``` { .bash .copy }
git clone https://github.com/EESSI/eessi-demo.git
cd eessi-demo
```

The contents of the directory should be something like this:

```
$ ls -l
drwxr-xr-x  5 example  users    160 Nov 23  2020 Bioconductor
drwxr-xr-x  3 example  users     96 Jan 26 20:17 CitC
drwxr-xr-x  5 example  users    160 Jan 26 20:17 GROMACS
-rw-r--r--  1 example  users  18092 Jan 26 20:17 LICENSE
drwxr-xr-x  3 example  users     96 Jan 26 20:17 Magic_Castle
drwxr-xr-x  4 example  users    128 Nov 24  2020 OpenFOAM
-rw-r--r--  1 example  users    546 Jan 26 20:17 README.md
drwxr-xr-x  5 example  users    160 Nov 23  2020 TensorFlow
drwxr-xr-x  6 example  users    192 Jan 26 20:17 scripts
```

The directories we care about are those that correspond to particular scientific software,
like ``Bioconductor``, ``GROMACS``, ``OpenFOAM``, ``TensorFlow``, ...

These each contain a ``run.sh`` script that can be used to start a small example run with that software,
each takes a couple of minutes max. to run (even with limited resources).

## Example: running GROMACS

Let's try running the GROMACS example.

First, we need to make sure that [our environment is set up to use EESSI](setting_up_environment):

``` { .bash .copy }
source /cvmfs/pilot.eessi-hpc.org/latest/init/bash
```

Change to the ``GROMACS`` subdirectory of the ``eessi-demo`` Git repository, and execute the ``run.sh`` script:

``` { .bash .no-copy }
[EESSI pilot 2021.12] $ cd GROMACS
[EESSI pilot 2021.12] $ ./run.sh
```

Shortly after starting the script you should see output as shown below, which indicates that GROMACS has started
running:

``` { .no-copy }
GROMACS:      gmx mdrun, version 2020.1-EasyBuild-4.5.0
Executable:   /cvmfs/pilot.eessi-hpc.org/versions/2021.12/software/linux/x86_64/intel/haswell/software/GROMACS/2020.1-foss-2020a-Python-3.8.2/bin/gmx
...
starting mdrun 'Protein'
1000 steps,      2.5 ps.
```
