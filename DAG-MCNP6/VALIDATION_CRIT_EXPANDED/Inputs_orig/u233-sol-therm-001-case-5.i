CSEWG: ORNL-9  1.0286 g/l Unreflected 27.24" Sphere;  U233-SOL-THERM-001 #5
1 1 0.10019 -1      $ Spherical Solution U(NO3)2-H2O
2 2 0.060275 1 -2   $ Spherical Shell of Al-1100
3 0 2

1 so 34.595    $ Inner Radius of Al-1100 Sphell
2 so 34.915    $ Outer RAdius of Al-1100 Sphell

mode n
imp:n 1 1 0
kcode 10000 1. 100 600
sdef pos 0.0 0.0 0.0 rad d1
sc1 Spherical Source
si1 34.595
c Solution
c      Materials specified with atom densities
m1    1001.  6.6329e-02
      5010.  1.0114e-06      5011.  4.0708e-06
      7014.  1.3586e-04
      8016.  3.3653e-02      8017.  1.3466e-05
     90232.  2.2691e-07
     92233.  5.0043e-05     92234.  8.2623e-07
     92235.  2.0314e-08     92238.  3.2091e-07
c Al-1100
m2   13027.  5.9881e-02
     14028.  2.0097E-04     14029.  1.0176E-05
     14030.  6.7549E-06
     25055.  1.4853e-05
     26054.  6.4652e-06     26056.  1.0051e-04
     26057.  2.3012e-06     26058.  3.0682e-07
     29063.  3.5528e-05     29065.  1.5836e-05
mt1   lwtr
totnu
prdmp  999999  999999  1  1  999999