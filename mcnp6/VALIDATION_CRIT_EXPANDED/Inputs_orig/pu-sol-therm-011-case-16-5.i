PNL-5  16" Bare Sphere, 43.43g Pu/l, 4.17 wt% Pu-240  PU-SOL-THERM-011 Case 16-5
c   CSEWG: T-17
1   1   1.002582e-1   -1      imp:n=1   $ Pu(NO3)4 Solution
2   2   8.6914e-2      1 -2   imp:n=1   $ SS347 Sphere
3   0                  2      imp:n=0   $ Outside Everything

1   so   20.1206   $ Sphere Inner Radius
2   so   20.2476   $ Sphere Outer Radius

mode   n
kcode  10000 1. 100 600
sdef   pos 0.0 0.0 0.0  rad d1
sc1    Spherical Source about origin
si1    20.1205
c      Materials specified with atom densities
m1    94239.  1.0484e-4      94240.  4.5432e-6
       7014.  2.7369e-3
       1001.  6.0233e-2
       8016.  3.7162e-2       8017.  1.4871e-5
      26054.  1.1388e-7      26056.  1.7704e-6
      26057.  4.0534e-8      26058.  5.4046e-9
mt1    lwtr
m2    26054.  3.5628e-3      26056.  5.5386e-2
      26057.  1.2681e-3      26058.  1.6908e-4
      24050.  7.2466e-4      24052.  1.3975e-2
      24053.  1.5844e-3      24054.  3.9444e-4
      28058.  6.7249e-3      28060.  2.5710e-3
      28061.  1.1131e-4      28062.  3.5363e-4
      28064.  8.9639e-5
totnu
prdmp  999999  999999  1  1  999999
