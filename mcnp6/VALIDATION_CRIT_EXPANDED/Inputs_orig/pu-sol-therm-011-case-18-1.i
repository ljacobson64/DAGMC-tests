PNL-3 18" Cadmium-covered Bare Sphere of Pu Nitrate, 22.35 gPu/l, 4.2 wt% Pu-240
c  PU-SOL-THERM-011 Case 18-1 and CSEWG T-15
1   1   1.004758e-1  -1      imp:n=1   $ Pu(NO3)4 Solution
2   2   8.6914e-2     1 -2   imp:n=1   $ SS347 Sphere
3   3   4.6340e-2     2 -3   imp:n=1   $ Cadmium Cover
4   0                 3      imp:n=0   $ Outside Everything

1   so   22.6974   $ Sphere Inner Radius
2   so   22.8244   $ Sphere Outer Radius
3   so   22.8752   $ Cadmium Cover Outer Radius

mode    n
kcode   10000 1. 100 600
sdef    pos 0.0 0.0 0.0  rad d1
sc1     Spherical Source about origin
si1     22.6973
c      Materials specified with atom densities
m1    94239.  5.3938e-5      94240.  2.3549e-6   $ Solution
       7014.  7.3930e-4
       1001.  6.5147e-2
       8016.  3.4520e-2       8017.  1.3814e-5
      26054.  7.6346e-8      26056.  1.1869e-6
      26057.  2.7174e-8      26058.  3.6232e-9
mt1    lwtr
m2    26054.  3.5628e-3      26056.  5.5386e-2
      26057.  1.2681e-3      26058.  1.6908e-4
      24050.  7.2466e-4      24052.  1.3975e-2
      24053.  1.5844e-3      24054.  3.9444e-4
      28058.  6.7249e-3      28060.  2.5710e-3
      28061.  1.1131e-4      28062.  3.5363e-4
      28064.  8.9639e-5
 m3   48106.  5.7925e-4      48108.  4.1243e-4
      48110.  5.7879e-3      48111.  5.9315e-3
      48112.  1.1182e-2      48114.  1.3314e-2
      48116.  3.4709e-3
totnu
prdmp  999999  999999  1  1  999999
