Big Ten  IEU-MET-FAST-007  Improved Benchmark  Case 4
1      2     0.047609               -3     8   -10             $ Bottom 10% Cyl
2      2     0.047609               -4    10   -11             $ Lower 10% Cyl
3      2     0.047609               -2    11   -13             $ Upper 10% Cyl
4      2     0.047609               -1    13   -14             $ Top 10% Cyl
5      3     0.048196          3    -5     8    -9             $ Bottom NU Plate
6      1     0.048159          2    -5     9   -12
                              #1    #2    #3                   $ Homog HEU + NU
7      3     0.048196          2    -5    12   -13             $ Top NU Plate
8      4     0.047779          5    -6     7   -14             $ DU Otr Annulus
9      4     0.047779               -5     7    -8             $ DU Btm Annulus
10     4     0.047779          1    -5    13   -14             $ DU Top Annulus
11     0                      (6:-7:14)

1     cz     2.25014             $ OR of Top 10% Cylinder
2     cz     3.10996             $ OR of Upper 10% Cylinder
3     cz     7.62000             $ OR of Bottom 10% Cylinder
4     cz    12.54604             $ OR of Lower 10% Cylinder
5     cz    26.67000             $ IR of DU Reflector Annulus
6     cz    41.91000             $ OR of DU Reflector Annulus
7     pz   -57.46750             $ Bottom of DU Reflector
8     pz   -41.73361             $ Top of DU Reflector Bottom
9     pz   -38.24644             $ Bottom of Homogenized HEU and Nat U
10    pz   -22.39010             $ Bottom of Bottom 10% Cylinder
11    pz     4.35102             $ Bottom of Lower 10% Cylinder
12    pz    17.16665             $ Top of Homogenized HEU and Nat U
13    pz    23.81250             $ Bottom of DU Reflector Top
14    pz    39.05250             $ Top of DU Reflector

totnu
kcode    10000    1.0   100    600
imp:n    1.0      9r    0.0
sdef   erg=d1    pos = 0 0 -10     axs = 0 0 1    rad=d2    ext=d3
sp1    -3
si2      0.0  7.62
si3    -30   30
c       Homogenized HEU, Natural U, and Voids
m1      92234.    5.4058e-5         92235.    4.9831e-3
        92236.    1.3733e-5         92238.    4.3108e-2
c       Intermediate Enriched Uranium (10 wt.%)
m2      92234.    2.4761e-5         92235.    4.8461e-3
        92236.    4.3348e-5         92238.    4.2695e-2
c       Natural Uranium
m3      92234.    2.6518e-6         92235.    3.4701e-4
        92238.    4.7846e-2
c       Depleted Uranium
m4      92234.    2.8672e-7         92235.    1.0058e-4
        92236.    1.1468e-6         92238.    4.7677e-2
prdmp  999999  999999  1  1  999999
