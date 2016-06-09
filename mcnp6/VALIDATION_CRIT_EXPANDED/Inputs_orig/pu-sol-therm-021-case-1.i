PNL-1  PU-SOL-THERM-021 case 1  Unreflected sphere of plutonium-nitrate solution
c  CSEWG T13
1    1    0.100785  -1          $ Plutonium-nitrate solution
2    2    0.086240   1  -2      $ Stainless steel shell
3    0               2

1    so  19.3304                $ Outer radius of solution
2    so  19.4523                $ Outer radius of shell

kcode  10000 1. 100 600
imp:n  1  1  0
sdef   pos 0.0 0.0 0.0  rad d1
sc1    Spherical Source
si1    19.3
totnu
c      Materials specified with atom densities
m1     1001.  6.5515e-2
       7014.  6.3382e-4
       8016.  3.4524e-2      8017.  1.3815e-5
      94238.  5.9197e-9     94239.  9.3366e-5
      94240.  4.5680e-6     94241.  2.7573e-7
      94242.  8.7324e-9
mt1   lwtr
c    Stainless Steel
m2    24050.  7.5725e-4     24052.  1.4603e-2
      24053.  1.6557e-3     24054.  4.1217e-4
      25055.  1.7363e-3
      26054.  3.5019e-3     26056.  5.4440e-2
      26057.  1.2465e-3     26058.  1.6619e-4
      28058.  5.2706e-3     28060.  2.0150e-3
      28061.  8.7239e-5     28062.  2.7716e-4
      28064.  7.0255e-5
prdmp  999999  999999  1  1  999999
