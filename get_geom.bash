#!/bin/bash

declare -a tarballs=(All_Meshtally.tar.gz \
                     Geom_sat_DAGMC.tar.gz \
                     Geom_sat_Regression.tar.gz \
                     Geom_sat_VALIDATION_CRITICALITY.tar.gz \
                     Geom_sat_VALIDATION_SHIELDING.tar.gz \
                     Geom_sat_VERIFICATION_KEFF.tar.gz \
                     xsec_data.tar.gz)

for tarball in ${tarballs[@]}; do
  wget cnergdata.engr.wisc.edu/DAGMC-tests/$tarball
  tar -xzvf $tarball
  rm -f $tarball
done
