#!/bin/bash

# Run longer tests in MPI mode
# Order for runs is from longest to shortest
# Runs with PTRAC must be run in serial
# Runs with dependencies on other runs must come after those runs

cd DAGMC
mpi_runs="13 09 15 14"
python run_tests.py $mpi_runs -s -r -j $jobs --mpi
ser_runs="05 06 01 08 07 11 10 02 03 04 12"
python run_tests.py $ser_runs -s -r -j $jobs
cd ..

cd Meshtally
python run_tests.py -s -r -j $jobs --mpi
cd ..

cd Regression
mpi_runs="35 37"
python run_tests.py $mpi_runs -s -r -j $jobs --mpi
ser_runs="36 02 41 31 42 04 39 98 99 06 90 93 33 95 30 01 07 64 12 03 68 20 32 21 23 10 28 19 09 94 47 61 63 65 66 67 86 62"
python run_tests.py $ser_runs -s -r -j $jobs
ser_runs="22 08 29 34 26 27"  # dependencies
python run_tests.py $ser_runs -s -r -j $jobs
cd ..

cd VALIDATION_CRITICALITY
python run_tests.py -s -r -j $jobs --mpi
cd ..

cd VALIDATION_SHIELDING
python run_tests.py -s -r -j $jobs --mpi
cd ..

cd VERIFICATION_KEFF
ser_runs="10 23 09"  # ptrac
mpi_runs="01 02 03 04 05 06 07 08 09 "$(seq 10 75)
for s_run in $ser_runs; do mpi_runs=${mpi_runs/$s_run}; done
python run_tests.py $mpi_runs -s -r -j $jobs --mpi
python run_tests.py $ser_runs -s -r -j $jobs
cd ..

python write_summaries.py
