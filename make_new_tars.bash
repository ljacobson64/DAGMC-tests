#!/bin/bash

names="Inputs Geom_h5m"
for name in $names; do
  files=`find fluka -type f | grep /$name/ | sort`
  tar -czvf fluka_${name}.tar.gz $files
done

names="Inputs_dagmc Files xsec_data Templates Geom_sat Geom_h5m "
for name in $names; do
  files=`find mcnp5 -type f | grep /$name/ | sort`
  tar -czvf mcnp5_${name}.tar.gz $files
done

names="Inputs_native Inputs_mcnp2cad Inputs_dagmc Files xsec_data Templates
       Geom_sat Geom_h5m"
for name in $names; do
  files=`find mcnp6 -type f | grep /$name/ | sort`
  tar -czvf mcnp6_${name}.tar.gz $files
done
