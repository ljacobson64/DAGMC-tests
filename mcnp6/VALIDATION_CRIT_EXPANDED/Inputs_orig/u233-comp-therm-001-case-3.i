BAPL SB Criticals  Core 2 1/2  Full U-233 Core  U233-COMP-THERM-001  Case 3
c     Universe 1:  Fuel Pin Cell
1     5   0.080898    -2     7    -9    u=1      $ Fuel Pin
2     1   0.043036    -2    -7          u=1      $ ENDF/B-VII.0  Bottom End Plug
3     1   0.043036    -2     9          u=1      $ ENDF/B-VII.0  Top End Plug
4     0                2    -3          u=1      $ Void
5     1   0.043036     3    -4          u=1      $ ENDF/B-VII.0  Cladding
6     3   0.100103     4                u=1      $ Water
7     4   0.088821     8   -11    13   -16    19   -20      $ Control Blade D
8     4   0.088821     8   -11    13   -16    21   -22      $ Control Blade C
9     4   0.088821     8   -11    13   -16    25   -26      $ Control Blade B
10    4   0.088821     8   -11    13   -16    27   -28      $ Control Blade A
11    0              -15    14   -24    23  lat=1  u=2
                     fill=-8:7 -9:8 0:0   1  287r           $ Fuel Pin Array
12    0               12   -17    18   -29     6   -10
                      #7    #8    #9   #10    fill=2        $ Core
13    3   0.100103    -1    10   -11
                      #7    #8    #9   #10                  $ Top Reflector
14    3   0.100103    -1     5    -6                        $ Bottom Reflector
15    3   0.100103    -1     6   -10   -12                  $ Left Reflector
16    3   0.100103    -1     6   -10    17                  $ Right Reflector
17    3   0.100103    -1     6   -10    12   -17   -18      $ Front Reflector
18    3   0.100103    -1     6   -10    12   -17    29      $ Back Reflector
19    0                1:-5:11

1     cz     42.18                               $ Reflector Outer Radius
2     c/z     0.45974   0.45974   0.26797        $ Fuel Outer Radius
3     c/z     0.45974   0.45974   0.27940        $ Clad Inner Radius
4     c/z     0.45974   0.45974   0.32385        $ Clad Outer Radius
5     pz    -56.2991                             $ Bottom of Relector
6     pz    -25.8191                             $ Bottom of End Plug
7     pz    -19.05                               $ Bottom of Fuel
8     pz     16.05                               $ Bottom of Control Blades
9     pz     19.05                               $ Top of Fuel
10    pz     25.8191                             $ Top of End Plug
11    pz     56.2991                             $ Top of Reflector
12    px     -7.35584                            $ Left Edge of Core
13    px     -3.81                               $ Left Edge of Control Blades
14    px      0.0                                $ Left Edge of Cell
15    px      0.91948                            $ Right Edge of Cell
16    px      3.81                               $ Right Edge of Control Blades
17    px      7.35584                            $ Right Edge of Core
18    py     -8.27532                            $ Front Edge of Core
19    py     -5.60578                            $ Front Edge of Control Blade D
20    py     -5.42798                            $ Back Edge of Control Blade D
21    py     -1.92786                            $ Front Edge of Control Blade C
22    py     -1.75006                            $ Back Edge of Control Blade C
23    py      0.0                                $ Front Edge of Cell
24    py      0.91948                            $ Back Edge of Cell
25    py      1.75006                            $ Front Edge of Control Blade B
26    py      1.92786                            $ Back Edge of Control Blade B
27    py      5.42798                            $ Front Edge of Control Blade A
28    py      5.60578                            $ Back Edge of Control Blade A
29    py      8.27532                            $ Back Edge of Core

mode      n
kcode    10000    1.0   100   600
rand     hist=3147300
imp:n    1.0  17r  0.0
totnu
sdef     x=d1  y=d2  z=d3
si1      -7.1      7.1
sp1        0        1
si2      -8.2      8.2
sp2        0        1
si3     -19.0     19.0
sp3        0        1
c         Zircaloy-2 Cladding
m1        40090.    2.1885e-2         40091.    4.7727e-3
          40092.    7.2951e-3         40094.    7.3929e-3
          40096.    1.1910e-3
          50112.    4.8420e-6         50114.    3.2447e-6       $ ENDF/B-VII.0
          50115.    1.6972e-6         50116.    7.2581e-5       $ ENDF/B-VII.0
          50117.    3.8337e-5         50118.    1.2090e-4       $ ENDF/B-VII.0
          50119.    4.2880e-5         50120.    1.6268e-4       $ ENDF/B-VII.0
          50122.    2.3112e-5         50124.    2.8902e-5       $ ENDF/B-VII.0
c         Polyethylene  (0.9183 g/cc)  N-tot=0.11828
m2         1001.    7.8854e-2
           6000.    3.9427e-2
mt2        poly
c         Water at 20 Degrees C  (0.9982 g/cc)  N-tot=0.100103
m3         1001.    6.6735e-2
           8016.    3.3355e-2          8017.    1.3347e-5
mt3        lwtr
c         Borated Steel for Control Blade  N-tot=0.088821
m4         5010.    3.7488e-3
          24050.    7.5725e-4         24052.    1.4603e-2
          24053.    1.6557e-3         24054.    4.1217e-4
          25055.    8.6816e-4
          26054.    3.4963e-3         26056.    5.4352e-2
          26057.    1.2444e-3         26058.    1.6593e-4
          28058.    5.1319e-3         28060.    1.9620e-3
          28061.    8.4943e-5         28062.    2.6986e-4
          28064.    6.8406e-5
c        UO2-ZrO2 Seed Fuel (97.19 w/o U-233)  N-tot=0.080898
m5         8016.    5.3910e-2          8017.    2.1573e-5
          40090.    1.1765e-2         40091.    2.5657e-3
          40092.    3.9217e-3         40094.    3.9743e-3
          40096.    6.4028e-4
          92233.    3.9891e-3         92234.    6.3690e-5
          92238.    4.5759e-5
prdmp  999999  999999  1  1  999999
