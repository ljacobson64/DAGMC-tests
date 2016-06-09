 Test of Cube with hole lnk3dnt file being imported
11   1 -18.0         0    u=e10 imp:n=1
12   0               0    u=e10 imp:n=1 $ background
20         0        -1 fill=e10 imp:n=1
c
21         0         1          imp:n=0
 
1  s 0.0 0.0 0.0   11

kcode     100     1.0  2  4
ksrc -5.0  0.0  0.0  
      5.0  0.0  0.0 
      0.0 -5.0  0.0
      0.0  5.0  0.0
      0.0  0.0 -5.0
      0.0  0.0  5.0
totnu no
m1        92235.69c   1.0
m2        1001.60c   1.0
prdmp    j    275
embed10 meshgeo=lnk3dnt mgeoin=CUBE01.linkout debug=echomesh
        calc_vols=yes
        background=12
        matcell= 1 11
print
