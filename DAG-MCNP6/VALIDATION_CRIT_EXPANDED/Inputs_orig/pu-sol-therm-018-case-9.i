PNL-11  PU-SOL-THERM-018 case 9  42.9 wt.% Pu-240  Water-Reflected
c  tank with plutonium nitrate solution with traces of Am and Gd
1    1  0.100115  -104 126 -128        $ Fissile Solution
2    2  0.086320   100 -110 120 -122   $ Bottom of Reflector Tank
3    2  0.086320   100 -102 122 -124   $ Support Pipe
4    2  0.086320  -106 124 -126        $ Bottom of Solution Tank
5    2  0.086320   104 -106 126 -130   $ Wall of Solution Tank
6    2  0.086320  -106 130 -132        $ Top of Solution Tank
7    2  0.086320   108 -110 122 -134   $ Wall of Reflector Tank
8    3  0.100037   102 -108 122 -124   $ Water Surrounding Pipe
9    3  0.100037   106 -108 124 -132   $ Water Surrounding Tank
10   0            -100 120 -124        $ Center of Support Pipe
11   0            -104 128 -130        $ Void In Solution Tank
12   0            -108 132 -134        $ Void Above Solution Tank
13   0             110:-120:134

100   cz     2.555                  $ Pipe Inner Radius
102   cz     2.860                  $ Pipe Outer Radius
104   cz    30.514                  $ Solution Tank Inner Radius
106   cz    30.593                  $ Solution Tank Outer Radius
108   cz    50.523                  $ Reflector Tank Inner Radius
110   cz    50.800                  $ Reflector Tank Outer Radius
120   pz     0                      $ Bottom of Reflector Tank
122   pz     0.277                  $ Bottom of Water Reflector
124   pz    21.227                  $ Top of Support Pipe
126   pz    22.177                  $ Bottom of Solution Tank
128   pz   103.097                  $ Fissile Solution Height
130   pz   127.828                  $ Top of Solution Tank
132   pz   127.907                  $ Water Reflector Height
134   pz   143.000                  $ Top of Reflector Tank

kcode  10000  1.0  100 600
imp:n    1.0  11r  0.0
sdef   cel=1  erg=d1  rad=d2  pos 0.0 0.0 62.6
sp1    -3
si2    0.0  30.0
totnu
c     Plutonium Nitrate Solution, with Am and Gd
m1     1001.  6.3362e-02
       7014.  1.2902e-03
       8016.  3.5098e-02       8017.  1.4045e-05
      64152.  2.7662e-11      64154.  3.0152e-10
      64155.  2.0470e-09      64156.  2.8312e-09
      64157.  2.1646e-09      64158.  3.4357e-09
      64160.  3.0235e-09
      94238.  2.0831e-07      94239.  4.2266e-05
      94240.  4.3641e-05      94241.  1.1029e-05
      94242.  4.7482e-06
      95241.  1.0949e-06
mt1   lwtr
c     Stainless Steel 304
m2    26054.  3.6986e-03      26056.  5.8060e-02
      26057.  1.3409e-03      26058.  1.7844e-04
      24050.  7.1832e-04      24052.  1.3852e-02
      24053.  1.5707e-03      24054.  3.9098e-04
      28058.  4.4315e-03      28060.  1.7070e-03
      28061.  7.4202e-05      28062.  2.3659e-04
      28064.  6.0252e-05
c     Water
m3     1001.  6.6691e-02
       8016.  3.3333e-02       8017.  1.3338e-05
mt3   lwtr
prdmp  999999  999999  1  1  999999
