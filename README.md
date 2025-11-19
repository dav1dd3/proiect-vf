# Proiect Verificare Formală

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

```bash
brew install minisat
```

Run MiniSAT on Windows
========

Run `.\minisat.exe input.txt` in the newly created directory.

Run MiniSAT on macOS
========

Run in terminal:

```bash
minisat file.cnf # it will display in console the results
```

or 

```bash
minisat file.cnf output.txt # it will display in console the results and in `output.txt` - SAT/UNSAT
```
