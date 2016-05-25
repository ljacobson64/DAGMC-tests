 Zeus 2  9 Units, 6 C Plates/Unit  HEU-MET-INTER-006    RN2
1         1        -1.0        0  u=1 imp:n=1 $
2         2        -1.0        0  u=1 imp:n=1 $
3         3        -1.0        0  u=1 imp:n=1 $
4         4        -1.0        0  u=1 imp:n=1 $ 
20        0                    0  u=1 imp:n=1 $ background void
c
100        0                       -1  fill=1 imp:n=1
200        0                        1         imp:n=0

1         sph     0.0   0.0   0.0   300.0

embed1  meshgeo=lnk3dnt debug=echomesh
        calc_vols = yes
        mgeoin=zeus2.linkout
        background=20
        matcell=   0  20
                   1  1
                   2  2
                   3  3
                   4  4
c
mode     n
kcode    1000    1.0    30   150 999999
dbcn       7j 3147300
ksrc      0.0   15.0   73.85198
c ---------------------------------------------------- ENDF/B-VII -------
c        Average HEU (93.22 wt.%)
m1       92234     4.9576e-4       
         92235     4.4941e-2
         92236     1.5931e-4       
         92238     2.5799e-3
c        Aluminum 6061 (2.70 g/cc)
m2       12000     6.6049e-4
         13027     5.7816e-2
         14028     3.1630e-4       14029     1.6016e-5
         14030     1.0631e-5
         22000     2.5146e-5
         24050     3.3536e-6       24052     6.4673e-5
         24053     7.3325e-6       24054     1.8254e-6
         25055     2.1915e-5
         26054     5.9360e-6       26056     9.2280e-5
         26057     2.1128e-6       26058     2.8171e-7
         29063     4.8053e-5       29065     2.1418e-5
c        Graphite (1.7106 g/cc)
m3        6000     0.085764
c mt3      grph.10t
c        Pure Copper (Average:  8.7451 g/cc)
m4       29063     5.7325e-2       
         29065     2.5550e-2
c -----------------------------------------------------------------------
totnu
prdmp     j   999999
print
phys:n 100 100 1

 end of input
