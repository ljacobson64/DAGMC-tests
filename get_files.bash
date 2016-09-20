#!/bin/bash

tarballs=
for arg in "$@"; do
  if [ "$arg" == "fluka" ]; then
    tarballs+=" fluka_Inputs.tar.gz"
    tarballs+=" fluka_Geom_h5m.tar.gz"
  elif [ "$arg" == "mcnp5" ]; then
    tarballs+=" mcnp5_Inputs_dagmc.tar.gz"
    tarballs+=" mcnp5_Files.tar.gz"
    tarballs+=" mcnp5_xsec_data.tar.gz"
    tarballs+=" mcnp5_Templates.tar.gz"
    tarballs+=" mcnp5_Geom_sat.tar.gz"
    tarballs+=" mcnp5_Geom_h5m.tar.gz"
  elif [ "$arg" == "mcnp6" ]; then
    tarballs+=" mcnp6_Inputs_native.tar.gz"
    tarballs+=" mcnp6_Inputs_mcnp2cad.tar.gz"
    tarballs+=" mcnp6_Inputs_dagmc.tar.gz"
    tarballs+=" mcnp6_Files.tar.gz"
    tarballs+=" mcnp6_xsec_data.tar.gz"
    tarballs+=" mcnp6_Templates.tar.gz"
    tarballs+=" mcnp6_Geom_sat.tar.gz"
    tarballs+=" mcnp6_Geom_h5m.tar.gz"
  fi
done

for tarball in $tarballs; do
  wget cnergdata.engr.wisc.edu/DAGMC-tests/tarballs/$tarball
  tar -xzvf $tarball
  rm -f $tarball
done
