#!/bin/bash

tarballs="FLUKA_Geom_h5m.tar.gz"

for tarball in $tarballs; do
  wget cnergdata.engr.wisc.edu/DAGMC-tests/tarballs/$tarball
  tar -xzvf $tarball
  rm -f $tarball
done
