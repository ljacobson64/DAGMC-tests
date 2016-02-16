#!/bin/bash

# Order for runs is from longest to shortest

cd Regression
runs="42_dag 03_dag 02_dag 13_dag 12_dag 03_nat 02_nat 41_dag 51_dag 52_dag
      13_nat 12_nat 42_nat 52_nat 51_nat 21_dag 22_dag 01_dag 11_dag 41_nat
      22_nat 21_nat 01_nat 11_nat"
python run_tests.py $runs -s -r -j $jobs
cd ..
