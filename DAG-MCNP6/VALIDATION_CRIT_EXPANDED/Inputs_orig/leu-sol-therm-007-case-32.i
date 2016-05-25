STACY-32  Uranyl Nitrate  9.97 wt.% Enr  270.0 g/l U  63.55 cm
c  LEU-SOL-THERM-007  Case 32
1    1    0.086845     1   -2    4   -6           $ Tank Wall
2    1    0.086845    -2    3   -4                $ Tank Bottom
3    1    0.086845    -2    6   -7                $ Tank Top
4    2    0.099288    -1    4   -5                $ Uranyl Nitrate Solution
5    3    4.9425e-5   -1    5   -6                $ Air inside Tank
6    0                 2:-3:7

1   cz   29.5                                     $ Inner Radius of Tank
2   cz   29.8                                     $ Outer Radius of Tank
3   pz   -2.0                                     $ Bottom of Tank
4   pz    0.0                                     $ Bottom of Uranyl Nitrate
5   pz   63.55                                    $ Top of Uranyl Nitrate
6   pz  150.0                                     $ Top of Air
7   pz  152.5                                     $ Top of Tank

kcode    10000    1.0   100   600
imp:n   1.0   4r  0.0
totnu
sdef   cel=4  erg=d1  pos= 0 0 40
sp1    -3
c   SS304  7.93 g/cc
m1      6000.   4.3736e-5
       14028.   9.8013e-4       14029.   4.9628e-5
       14030.   3.2944e-5
       15031.   4.3170e-5
#ifdef ENDF7
       16032.   2.8299e-6       16033.   2.2337e-8     $ ENDF/B-VII.0
       16034.   1.2538e-7       16036.   5.9564e-10    $ ENDF/B-VII.0
#else
       16000.   2.9782e-6                              $ ENDF/B-VI
#endif
       24050.   7.2887e-4       24052.   1.4056e-2
       24053.   1.5936e-3       24054.   3.9673e-4
       25055.   1.1561e-3
       26054.   3.5058e-3       26056.   5.4501e-2
       26057.   1.2478e-3       26058.   1.6638e-4
       28058.   5.6939e-3       28060.   2.1768e-3
       28061.   9.4245e-5       28062.   2.9942e-4
       28064.   7.5897e-5
c   Uranyl Nitrate Solution  270.0 g/l U  1.4348 g/cc
m2      1001.   5.8085e-2
        7014.   2.6828e-3        7015.   9.9091e-6
        8016.   3.7811e-2        8017.   1.5130e-5
       92234.   5.5579e-7       92235.   6.8970e-5
       92236.   6.8884e-8       92238.   6.1432e-4
mt2     lwtr
c   Air as Nitrogen and Oxygen  0.001184 g/cc
m3      7014.   3.8872e-5        7015.   1.4436e-7
        8016.   1.0405e-5        8017.   4.1636e-9
prdmp  999999  999999  1  1  999999
