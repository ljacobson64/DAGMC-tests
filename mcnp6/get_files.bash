#!/bin/bash

tarballs="mcnp6_Inputs_native.tar.gz
          mcnp6_Inputs_mcnp2cad.tar.gz
          mcnp6_Inputs_dagmc.tar.gz
          mcnp6_Files.tar.gz
          mcnp6_xsec_data.tar.gz
          mcnp6_Templates.tar.gz
          mcnp6_Geom_sat.tar.gz
          mcnp6_Geom_h5m.tar.gz"

for tarball in $tarballs; do
  wget cnergdata.engr.wisc.edu/DAGMC-tests/tarballs/$tarball
  tar -xzvf $tarball
  rm -f $tarball
done
