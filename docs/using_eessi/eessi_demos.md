# Running EESSI demos

To really experience how using EESSI can significantly facilitate the work of researchers,
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

Each of these contains a ``run.sh`` script that can be used to start a small
example run with that software. Every example takes a couple of minutes to run,
even with limited resources only.

## Example: running TensorFlow

Let's try running the TensorFlow example.

First, we need to make sure that [our environment is set up to use EESSI](setting_up_environment.md):

``` { .bash .copy }
source /cvmfs/software.eessi.io/versions/2023.06/init/bash
```

Change to the ``TensorFlow`` subdirectory of the ``eessi-demo`` Git repository, and execute the ``run.sh`` script:

``` { .no-copy }
[EESSI 2023.06] $ cd TensorFlow
[EESSI 2023.06] $ ./run.sh
```

Shortly after starting the script you should see output as shown below, which indicates that GROMACS has started
running:

``` { .no-copy }
Epoch 1/5
   1875/1875 [==============================] - 3s 1ms/step - loss: 0.2983 - accuracy: 0.9140
Epoch 2/5
   1875/1875 [==============================] - 3s 1ms/step - loss: 0.1444 - accuracy: 0.9563
Epoch 3/5
   1875/1875 [==============================] - 3s 1ms/step - loss: 0.1078 - accuracy: 0.9670
Epoch 4/5
   1875/1875 [==============================] - 3s 1ms/step - loss: 0.0890 - accuracy: 0.9717
Epoch 5/5
   1875/1875 [==============================] - 3s 1ms/step - loss: 0.0732 - accuracy: 0.9772
313/313 - 0s - loss: 0.0679 - accuracy: 0.9790 - 391ms/epoch - 1ms/step

real	1m24.645s
user	0m16.467s
sys	0m0.910s
```
