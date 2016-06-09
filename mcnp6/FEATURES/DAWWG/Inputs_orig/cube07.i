 Fire one particle into mesh along x axis.
11   2    -0.001     0       u=e10 imp:n=1
12   0               0       u=e10 imp:n=1 $ background
20   0              -1    fill=e10 imp:n=1
c
21   2    -0.001     1 -2          imp:n=1
22         0         2             imp:n=0
 
1  so    17.4  
2  so    100

sdef pos = -12.0 0.0 0.0  vec=1 0 0 dir=1.0
totnu no
m2        1001.60c   1.0
prdmp    j    275
dbcn j j 1 1 
embed10    meshgeo = lnk3dnt 
            mgeoin = CUBE01.linkout 
             debug = echomesh
         calc_vols = yes
        background = 12
           matcell = 1 11 $ material(1) maps to cell(11)
nps 1
print
