Godiva solid bare HEU sphere. mesh generator
1 1 -18.74     -1     imp:n=1
2 0             1 -2  imp:n=1
3 0                2  imp:n=0

1 sx 5  8.7407
2 sx 5  20

m1 92235.50c 4.4994E-02 92238.50c 2.4984E-03 92234.50c 4.9184E-04
kcode 3000 1.0 10 150
ksrc 0. 0. 0.
mesh  geom sph
       ref      0.0   0.0   0.0
       origin   5.0   0.0   0.0
       imesh    4.0 8.7407 10.0  $ radial zoning: 2 snm, 1 void
       iints    1   1      1     $  1 zone per radii
       jmesh   0.5  jints   1    $ angular zoning not supported
       kmesh   1.0  kints   1   
dawwg xsec=ndilib points=10
print
