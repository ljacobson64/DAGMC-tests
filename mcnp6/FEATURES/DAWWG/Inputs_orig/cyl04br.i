 RZT Test of checkerboard cylinder with lnk3dnt 
11   1 -18.7         0    u=e10 imp:n=1
12   2  -1.0         0    u=e10 imp:n=1
13   0               0    u=e10 imp:n=1
14   0               0    u=e10 imp:n=1
20      0           -1 fill=e10 imp:n=1
c
21         0         1          imp:n=0
 
1  so   20

kcode     500     1.0  50   100
ksrc 1 1  5 1 -1  5 -1 -1  5 -1 1  5
     5 5  5 5 -5  5 -5 -5  5 -5 5  5
     1 1 -5 1 -1 -5 -1 -1 -5 -1 1 -5
     5 5 -5 5 -5 -5 -5 -5 -5 -5 5 -5
totnu no
m1        92235.69c   1.0
m2        6012 1.0
dm1 92235 92235.50
prdmp    j    275
print
embed10 meshgeo=lnk3dnt mgeoin=CYL04R.linkout debug=echomesh
        matcell= 0 13
                 1 11
                 2 12
        background=14
        calc_vols=yes

end of input
