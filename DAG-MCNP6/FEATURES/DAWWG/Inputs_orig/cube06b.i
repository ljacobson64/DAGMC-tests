 Test of Cube with hole lnk3dnt file being imported
11   1 -18.0         0     u=e10 imp:n=1
12   0               0     u=e10 imp:n=1 $ background
20   2 -0.001       -2  fill=e10 imp:n=1
c
21         0         2           imp:n=0
 
2  so 17.4

kcode     1000     1.0  10   100
ksrc -5.0  0.0  0.0   5.0  0.0  0.0 
      0.0 -5.0  0.0   0.0  5.0  0.0
      0.0  0.0 -5.0   0.0  0.0  5.0
totnu no
m1        92235.69c   1.0
m2        1001.60c   1.0
prdmp    j    275
embed10 meshgeo=lnk3dnt mgeoin=CUBE01.linkout debug=echomesh
        background=12
        matcell= 1 11
        calc_vols=yes
print
