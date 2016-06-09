 Test of Cube with hole lnk3dnt file being imported
11   1 -18.0         0     u=e10  imp:n=1
12   2  -1.0         0 -1  u=e10  imp:n=1
13   2  -1.0         0 0   u=e10  imp:n=1
14   2  -1.0         -1 0  u=e10  imp:n=1
15   2  -1.0         0     u=e10  imp:n=1
16   0               0     u=e10  imp:n=1 $ background
20         0        -1  fill=e10  imp:n=1
c
21         0         1            imp:n=0
 
1  s 0.0 0.0 0.0   11
2  s 0.0 0.0 0.0   1000

kcode     1     1.0  1   1
ksrc 5.0 0.0 0.0
totnu no
m1        92235.69c   1.0
m2        1001.60c   1.0
prdmp    j    275
embed10 meshgeo=lnk3dnt mgeoin=CUBE01.linkout debug=echomesh
        background=16
        calc_vols=yes
        matcell= 1 11 
                 2 12 
                 3 13 
                 4 14  
                 5 15  
                 6
print
