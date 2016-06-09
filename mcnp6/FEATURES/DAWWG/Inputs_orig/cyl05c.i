 RZT Test of cylinder with lnk3dnt 
11   1 -18.0         0    u=e10 imp:n=1
13   0               0    u=e10 imp:n=1
20       0          -1 fill=e10 imp:n=1
c
21         0         1          imp:n=0
 
1  so   20

kcode     500     1.0  50 150
ksrc  0.0  0.0  0.0  
totnu no
m1        92235.69c   1.0
m2        1001.60c   1.0
prdmp    j    275
embed10  meshgeo = lnk3dnt 
          mgeoin = CYL02.linkout 
           debug = echomesh
         matcell =  1 11
      background = 13
       calc_vols = yes
print

end of input
