Godiva solid bare HEU sphere. XYZ 1cc mesh
10 0             0      u=e10 imp:n=1 $ void elements
11 1 4.7984E-02  0      u=e10 imp:n=1
12 0             0      u=e10 imp:n=1 $ background
20 0            -2   fill=e10 imp:n=1
30 0             2            imp:n=0

2 so 20

m1 92235.50c 4.4994E-02 92238.50c 2.4984E-03 92234.50c 4.9184E-04
kcode 3000 1.0 10 150
ksrc 0. 0. 0.
embed10  meshgeo=lnk3dnt
          mgeoin=HFM001.linkout
           debug=echomesh
         matcell= 0 10 1 11 
      background=12
        calc_vols=yes
print
