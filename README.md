# Proiect Verificare Formală

[![Build Status](https://travis-ci.org/master-keying/minisat.svg?branch=master)](https://travis-ci.org/master-keying/minisat)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/master-keying/minisat?svg=true)](https://ci.appveyor.com/project/horenmar/minisat)

Forked off MiniSAT 2.2, this repository aims at providing
a production-ready version of the famous library.



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

Examples
========

Run minisat with same heuristics as version 2.0:

```minisat <cnf-file> -no-luby -rinc=1.5 -phase-saving=0 -rnd-freq=0.02```
