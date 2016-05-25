PNL-4  18" Cadmium-covered Bare Sphere of Pu Nitrate,27.49 g Pu/l,4.2 wt% Pu-240
c  PU-SOl-THERM-011 Case 18-6 and CSEWG: T-16
1   1   1.003191e-1  -1      imp:n=1   $ Pu(NO3)4 Solution
2   2   8.6914e-2     1 -2   imp:n=1   $ SS347 Sphere
3   3   4.6340e-2     2 -3   imp:n=1   $ Cadmium Cover
4   0                 3      imp:n=0   $ Outside Everything

1   so   22.6974   $ Sphere Inner Radius
2   so   22.8244   $ Sphere Outer Radius
3   so   22.8752   $ Cadmium Cover Outer Radius

mode n
kcode 10000 1. 100 600
sdef pos 0.0 0.0 0.0 rad d1
sc1 Spherical Source about origin
 si1 22.6973
c      Materials specified with atom densities
m1    94239.  6.6343e-5      94240.  2.8964e-6
       7014.  2.7753e-3
       1001.  6.0264e-2
       8016.  3.7194e-2       8017.  1.4884e-5
      26054.  8.9704e-8      26056.  1.3945e-6
      26057.  3.1928e-8      26058.  4.2571e-9
mt1    lwtr
m2    26054.  3.5628e-3      26056.  5.5386e-2
      26057.  1.2681e-3      26058.  1.6908e-4
      24050.  7.2466e-4      24052.  1.3975e-2
      24053.  1.5844e-3      24054.  3.9444e-4
      28058.  6.7249e-3      28060.  2.5710e-3
      28061.  1.1131e-4      28062.  3.5363e-4
      28064.  8.9639e-5
m3    48106.  5.7925e-4      48108.  4.1243e-4
      48110.  5.7879e-3      48111.  5.9315e-3
      48112.  1.1182e-2      48114.  1.3314e-2
      48116.  3.4709e-3
totnu
prdmp  999999  999999  1  1  999999
