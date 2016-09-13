#!/bin/bash

tarballs="mcnp5_Inputs_dagmc.tar.gz
          mcnp5_Files.tar.gz
          mcnp5_xsec_data.tar.gz
          mcnp5_Templates.tar.gz
          mcnp5_Geom_sat.tar.gz
          mcnp5_Geom_h5m.tar.gz"

for tarball in $tarballs; do
  wget cnergdata.engr.wisc.edu/DAGMC-tests/tarballs/$tarball
  tar -xzvf $tarball
  rm -f $tarball
done
