BAPL SB Crits  Core 5  U-235 Seed, ThO2 Blanket  U233-COMP-THERM-001, case 6
c    U233-COMP-THERM-001  Case 6
c     Universe 1:  Seed Pin Cell
1     6   0.082231    -2    11   -15        u=1   $ Seed Pin
2     1   0.043036    -2   -11              u=1   $ ENDF/B-VII.0 Bottom End Plug
3     1   0.043036    -2    15              u=1   $ ENDF/B-VII.0 Top End Plug
4     0                2    -3              u=1   $ Void
5     1   0.043036     3    -4              u=1   $ ENDF/B-VII.0 Cladding
6     2   0.118281     4    -5    12   -13  u=1   $ Polyethylene Ring
7     3   0.100103     4                #6  u=1   $ Water
c    Universe 2:  Blanket Pin Cell
8     8   0.064923    -6    11   -15        u=2   $ Th02 Pin
9     1   0.043036    -6   -11              u=2   $ ENDF/B-VII.0 Bottom End Plug
10    1   0.043036    -6    15              u=2   $ ENDF/B-VII.0 Top End Plug
11    0                6    -7              u=2   $ Void
12    1   0.043036     7    -8              u=2   $ ENDF/B-VII.0 Cladding
13    3   0.100103     8                    u=2   $ Water
14    3   0.100103    -1                    u=3   $ Water
15    4   0.088821    14   -17    28   -31    24   -25  $ Control Blade C
16    4   0.088821    14   -17    28   -31    26   -27  $ Control Blade D
17    4   0.088821    14   -17    28   -31    19   -20  $ Control Blade A
18    4   0.088821    14   -17    28   -31    21   -22  $ Control Blade B
c    Fuel Pin Array with Water Boundary
19    0              -30    29   -32    34   -33    35
                     lat=2  u=4  fill=-21:21  -21:21   0:0
                       3  42r
                       3  20r  2  20r                  3
                       3  19r  2  21r                  3
                       3  18r  2  22r                  3
                       3  17r  2  23r                  3
                       3  16r  2  24r                  3
                       3  15r  2  25r                  3
                       3  14r  2  26r                  3
                       3  13r  2  27r                  3
                       3  12r  2  28r                  3
                       3  11r  2  29r                  3
                       3  10r  2  30r                  3
                       3   9r  2  31r                  3
                       3   8r  2  11r  1   8r  2  11r  3
                       3   7r  2  11r  1   9r  2  11r  3
                       3   6r  2  11r  1  10r  2  11r  3
                       3   5r  2  11r  1  11r  2  11r  3
                       3   4r  2  11r  1  12r  2  11r  3
                       3   3r  2  11r  1  13r  2  11r  3
                       3   2r  2  11r  1  14r  2  11r  3
                       3   3   2  11r  1  15r  2  11r  3
                       3       2  11r  1  16r  2  11r  3
                       3       2  11r  1  15r  2  11r  3   3
                       3       2  11r  1  14r  2  11r  3   2r
                       3       2  11r  1  13r  2  11r  3   3r
                       3       2  11r  1  12r  2  11r  3   4r
                       3       2  11r  1  11r  2  11r  3   5r
                       3       2  11r  1  10r  2  11r  3   6r
                       3       2  11r  1   9r  2  11r  3   7r
                       3       2  11r  1   8r  2  11r  3   8r
                       3       2  31r                  3   9r
                       3       2  30r                  3  10r
                       3       2  29r                  3  11r
                       3       2  28r                  3  12r
                       3       2  27r                  3  13r
                       3       2  26r                  3  14r
                       3       2  25r                  3  15r
                       3       2  24r                  3  16r
                       3       2  23r                  3  17r
                       3       2  22r                  3  18r
                       3       2  21r                  3  19r
                       3       2  20r                  3  20r
                       3  42r
20    0               10   -16    18  -23  -36  -37    38
                      39   #15   #16   #17   #18   fill=4    $ Core
21    3   0.100103    -1    16   -17   #15   #16   #17   #18 $ Top Reflector
22    3   0.100103    -1     9   -10                         $ Bottom Reflector
23    3   0.100103    -1    10   -16  -18                    $ Front Reflector
24    3   0.100103    -1    10   -16   23                    $ Back Reflector
25    3   0.100103    -1    10   -16   18  -23   36          $ BR Reflector
26    3   0.100103    -1    10   -16   18  -23  -36    37    $ BL Reflector
27    3   0.100103    -1    10   -16   18  -23  -38          $ FL Reflector
28    3   0.100103    -1    10   -16   18  -23   38   -39    $ FR Reflector
29    0                1:-9:17

1     cz     60.28                               $ Reflector Outer Radius
2     cz     0.26797                             $ Seed Fuel Outer Radius
3     cz     0.27940                             $ Seed Clad Inner Radius
4     cz     0.32385                             $ Seed Clad Outer Radius
5     cz     0.72517                             $ Poly Ring Outer Radius
6     cz     0.62103                             $ Blanket Fuel Outer Radius
7     cz     0.63373                             $ Blanket Clad Inner Radius
8     cz     0.72390                             $ Blanket Clad Outer Radius
9     pz    -56.2991                             $ Bottom of Relector
10    pz    -25.8191                             $ Bottom of End Plug
11    pz    -19.05                               $ Bottom of Fuel
12    pz     -0.3175                             $ Bottom of Polyethylene Ring
13    pz      0.3175                             $ Top of Polyethylene Ring
14    pz     15.765                              $ Bottom of Control Blades
15    pz     19.05                               $ Top of Fuel
16    pz     25.8191                             $ Top of End Plug
17    pz     56.2991                             $ Top of Reflector
18    py    -26.37666                            $ Front of Core
19    py      1.75006                            $ Front Edge of Control Blade A
20    py      1.92786                            $ Back Edge of Control Blade A
21    py      5.42798                            $ Front Edge of Control Blade B
22    py      5.60578                            $ Back Edge of Control Blade B
23    py     26.37666                            $ Back of Core
24    py     -5.60578                            $ Front Edge of Control Blade C
25    py     -5.42798                            $ Back Edge of Control Blade C
26    py     -1.92786                            $ Front Edge of Control Blade D
27    py     -1.75006                            $ Back Edge of Control Blade D
28    px     -3.81                               $ Left Edge of Control Blades
29    px     -0.72517                            $ Front Edge of Fuel Pin Cell
30    px      0.72517                            $ Back Edge of Fuel Pin Cell
31    px      3.81                               $ Right Edge of Control Blades
32     p      1.0   1.7320508076   0.0   1.45034 $
33     p     -1.0   1.7320508076   0.0   1.45034 $
34     p      1.0   1.7320508076   0.0  -1.45034 $
35     p     -1.0   1.7320508076   0.0  -1.45034 $
36     p      1.7320508076   1.0   0.0  52.75331 $
37     p      1.7320508076  -1.0   0.0  52.75331 $
38     p      1.7320508076   1.0   0.0 -52.75331 $
39     p      1.7320508076  -1.0   0.0 -52.75331 $

mode      n
kcode  10000  1.0  100  600
rand   hist=7314730
imp:n    1.0  27r  0.0
totnu
sdef     x=d1  y=d2  z=d3
si1     -11.0     11.0
sp1        0        1
si2     -11.0     11.0
sp2        0        1
si3     -19.0     19.0
sp3        0        1
c         Zircaloy-2 Cladding
m1        40090.  2.1885e-2         40091.  4.7727e-3
          40092.  7.2951e-3         40094.  7.3929e-3
          40096.  1.1910e-3
          50112.  4.8420e-6         50114.  3.2447e-6  $ ENDF/B-VII.0
          50115.  1.6972e-6         50116.  7.2581e-5  $ ENDF/B-VII.0
          50117.  3.8337e-5         50118.  1.2090e-4  $ ENDF/B-VII.0
          50119.  4.2880e-5         50120.  1.6268e-4  $ ENDF/B-VII.0
          50122.  2.3112e-5         50124.  2.8902e-5  $ ENDF/B-VII.0
c         Polyethylene  (0.9183 g/cc)  N-tot=0.11828
m2         1001.  7.8854e-2
           6000.  3.9427e-2
mt2        poly
c         Water at 20 Degrees C  (0.9982 g/cc)  N-tot=0.100103
m3         1001.  6.6735e-2
           8016.  3.3355e-2          8017.  1.3347e-5
mt3        lwtr
c         Borated Steel for Control Blade  N-tot=0.088821
m4         5010.  3.7488e-3
          24050.  7.5725e-4         24052.  1.4603e-2
          24053.  1.6557e-3         24054.  4.1217e-4
          25055.  8.6816e-4
          26054.  3.4963e-3         26056.  5.4352e-2
          26057.  1.2444e-3         26058.  1.6593e-4
          28058.  5.1319e-3         28060.  1.9620e-3
          28061.  8.4943e-5         28062.  2.6986e-4
          28064.  6.8406e-5
c        UO2-ZrO2 Seed Fuel (97.19 w/o U-233)  N-tot=0.080898
m5         8016.  5.3910e-2          8017.  2.1573e-5
          40090.  1.1765e-2         40091.  2.5657e-3
          40092.  3.9217e-3         40094.  3.9743e-3
          40096.  6.4028e-4
          92233.  3.9891e-3         92234.  6.3690e-5
          92238.  4.5759e-5
c        UO2-ZrO2 Seed Fuel (92.73 w/o U-235)  N-tot=0.082231
m6         8016.  5.4799e-2          8017.  2.1928e-5
          40090.  1.1958e-2         40091.  2.6078e-3
          40092.  3.9860e-3         40094.  4.0395e-3
          40096.  6.5078e-4
          92234.  3.7302e-5         92235.  3.8783e-3
          92238.  2.5273e-4
c        UO2-ThO2 Blanket Fuel (97.19 w/o U-233, 5 PPM Gd)  N-tot=0.064620
m7         8016.  4.3063e-2          8017.  1.7232e-5
          64152.  3.1447e-10        64154.  3.4277e-9
          64155.  2.3270e-8         64156.  3.2186e-8
          64157.  2.4607e-8         64158.  3.9057e-8
          64160.  3.4371e-8
          90232.  2.1311e-2
          92233.  2.2283e-4         92234.  3.5385e-6
          92238.  2.7607e-6
c        ThO2 Fuel Blanket Fuel (2.9 PPM Gd)  N-tot=0.064923
m8         8016.  4.3265e-2          8017.  1.7313e-5
          64152.  1.8521e-10        64154.  2.0188e-9
          64155.  1.3706e-8         64156.  1.8957e-8
          64157.  1.4493e-8         64158.  2.3003e-8
          64160.  2.0244e-8
          90232.  2.1641e-2
prdmp  999999  999999  1  1  999999
