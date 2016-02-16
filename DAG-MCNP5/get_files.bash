#!/bin/bash

tarballs="MCNP5_Geom_all_Meshtally.tar.gz
          MCNP5_Geom_h5m_DAGMC.tar.gz
          MCNP5_Geom_h5m_Regression.tar.gz
          MCNP5_Geom_h5m_VALIDATION_CRITICALITY.tar.gz
          MCNP5_Geom_h5m_VALIDATION_SHIELDING.tar.gz
          MCNP5_Geom_h5m_VERIFICATION_KEFF.tar.gz
          MCNP5_Geom_sat_DAGMC.tar.gz
          MCNP5_Geom_sat_Regression.tar.gz
          MCNP5_Geom_sat_VALIDATION_CRITICALITY.tar.gz
          MCNP5_Geom_sat_VALIDATION_SHIELDING.tar.gz
          MCNP5_Geom_sat_VERIFICATION_KEFF.tar.gz
          MCNP5_xsec_data.tar.gz"

for tarball in $tarballs; do
  wget cnergdata.engr.wisc.edu/DAGMC-tests/tarballs/$tarball
  tar -xzvf $tarball
  rm -f $tarball
done
