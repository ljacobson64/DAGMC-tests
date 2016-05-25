PNL-10   PU-SOL-THERM-034  case 1  8.3 wt.% Pu-240  116 gPu/l
c  Water-reflected SS304L cylindrical tank with plutonium nitrate solution
1    0           -100  120 -124        $ Center of Support Pipe
2    0           -104  128 -130        $ Void In Solution Tank
3    0           -108  132 -134        $ Void Above Solution Tank
4    1  .100476  -104  126 -128        $ Fissile Solution
5    2  .086320   100 -110  120 -122   $ Bottom of Reflector Tank
6    2  .086320   100 -102  122 -124   $ Support Pipe
7    2  .086320  -106  124 -126        $ Bottom of Solution Tank
8    2  .086320   104 -106  126 -130   $ Wall of Solution Tank
9    2  .086320  -106  130 -132        $ Top of Solution Tank
10   2  .086320   108 -110  122 -134   $ Wall of Reflector Tank
11   3  .100037   102 -108  122 -124   $ Water Surrounding Pipe
12   3  .100037   106 -108  124 -132   $ Water Surrounding Tank
13   0            110:-120:134         $ Room

100  cz    2.555              $ Pipe Inner Radius
102  cz    2.860              $ Pipe Outer Radius
104  cz   30.514              $ Solution Tank Inner Radius
106  cz   30.593              $ Solution Tank Outer Radius
108  cz   50.523              $ Reflector Tank Inner Radius
110  cz   50.800              $ Reflector Tank Outer Radius
120  pz    0                  $ Bottom of Reflector Tank
122  pz    0.277              $ Bottom of Water Reflector
124  pz   21.227              $ Top of Support Pipe
126  pz   22.177              $ Bottom of Solution Tank
128  pz   37.617              $ Fissile Solution Height
130  pz  127.828              $ Top of Solution Tank
132  pz  127.907              $ Water Reflector Height
134  pz  143.000              $ Top of Reflector Tank

kcode  10000  1.0  100  600
imp:n  1.0  11r  0.0
sdef   cel=4  erg=d1  rad=d2  pos 0.0 0.0 30.0
sp1    -3
si2    0.0  30.0
c     Plutonium Nitrate Solution
m1     1001.  6.0973e-2
       7014.  2.3203e-3
       8016.  3.6875e-2          8017.  1.4756e-5
      94238.  1.2912e-7         94239.  2.6498e-4
      94240.  2.4383e-5         94241.  2.4661e-6
      94242.  1.4141e-7
mt1    lwtr
c     Stainless Steel
m2    26054.  3.6986e-3         26056.  5.8060e-2
      26057.  1.3409e-3         26058.  1.7844e-4
      24050.  7.1832e-4         24052.  1.3852e-2
      24053.  1.5707e-3         24054.  3.9098e-4
      28058.  4.4315e-3         28060.  1.7070e-3
      28061.  7.4202e-5         28062.  2.3659e-4
      28064.  6.0252e-5
c     Water
m3     1001.  6.6691E-2
       8016.  3.3333E-2          8017.  1.3338e-5
mt3    lwtr
prdmp  999999  999999  1  1  999999
