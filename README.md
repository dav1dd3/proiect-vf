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


Building for Linux
--------

```bash
# You can build in any directory, just name the minisat directory in the cmake
# command.
mkdir build && cd build
cmake ..
make
```

Installing MiniSAT on Windows
========

1. Install the prerequisite software, in this case MinGW and CMake if it isn't alredy installed.
   Make sure that the directories of MinGW and CMake that you extracted are included in the PATH environment variables.
2. Clone this [git repository](https://github.com/master-keying/minisat/) to your local environment.
3. Create a directory in the root directory of the repository.
4. Run `bash cmake -G "MinGW Makefiles" .. ` in the new created directory.
5. Run bash cmake --build . to compile the Makefiles generated in the previous step.
6. To use MiniSAT you need to create a text file input.txt and fill it with the DIMACS format of your formula.

Installing MiniSAT on macOS using Homebrew
--------

Run this command in terminal:

brew install minisat

Run MiniSAT on Windows
========

Run `.\minisat.exe input.txt` in the newly created directory.

Run MiniSAT on macOS
========

Run `minisat file.cnf` in terminal and it will display in console the results

or `minisat file.cnf output.txt` and it will display in console the results and in the `output.txt` file only if it is SAT/UNSAT

