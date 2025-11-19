# Proiect Verificare Formală

[![Build Status](https://travis-ci.org/master-keying/minisat.svg?branch=master)](https://travis-ci.org/master-keying/minisat)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/master-keying/minisat?svg=true)](https://ci.appveyor.com/project/horenmar/minisat)

Forked off MiniSAT 2.2.



Directory overview
------------------

- `minisat/mtl`     Mini Template Library
- `minisat/utils`   Generic helper code (I/O, Parsing, CPU-time, etc)
- `minisat/core`    A core version of the solver
- `minisat/simp`    An extended solver with simplification capabilities
- `README.md`       This read-me file
- `LICENSE`         Licence files



Building
--------

```bash
# You can build in any directory, just name the minisat directory in the cmake
# command.
mkdir build && cd build
cmake ..
make
```

Building for Windows
--------

1. Clone this git repository to your local environment.
2. Open the build directory in the root directory of the repository.
3. To use MiniSAT you need to fill input.txt with the DIMACS format of your formula.

Run MiniSAT
========

Run `.\minisat.exe input.txt` in the newly created directory.

