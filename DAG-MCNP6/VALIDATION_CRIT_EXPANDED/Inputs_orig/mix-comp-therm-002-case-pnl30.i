MIX-COMP-THERM-002 PNL-30: square lattice, pitch=1.778 cm, pure water(1.7ppm)
c    **********
c    cell cards
c    **********
1    0               21 23 -25 4 -12 fill=11  imp:n=1  $ Cube for Fuelled Core
2    5  0.100059     21 23 -25 (1 -2:14 -15)  imp:n=1  $ Bottom and Top Refl
3    6  0.059721     21 23 -25 2 -4           imp:n=1  $ Aluminum Plate
4    7  0.031723     21 23 -25 12 -14         imp:n=1  $ Lead Shield
5    0               25:-1:15:-21:-23         imp:n=0  $ Out of core
c
c     filling universe                          $ Cube cell filled Fuel
c
6    0 -32 31 -34 33 lat=1 u=11 imp:n=1 fill=0:28 0:28 0:0
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
         2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
c
c     fuel cell universe (u=1)
c
21   1  0.064971   7 -11 -35                 u=1 imp:n=1  $ MOX
22   2  0.062618   6 -7  -35                 u=1 imp:n=1  $ UO2 layer
23   3  0.043306   3 -11 -36 #21 #22         u=1 imp:n=1  $ ENDF/B-VII.0 Clad
24   6  0.059721 (5 -8:9 -10)(-37:38:-39:40) u=1 imp:n=1  $ Al Egg-Crate
25   5  0.100059   #21 #22 #23 #24 #26       u=1 imp:n=1  $ Moderator
26   3  0.043306   11 -13 -36                u=1 imp:n=1  $ ENDF/B-VII.0 Plug
c
c     Part of Radial reflector cell universe (u=2)
c
31   5  0.100059     #32                       u=2 imp:n=1  $ Water
32   6  0.059721   (5 -8:9 -10)(-37:38:-39:40) u=2 imp:n=1  $ Al Egg-Crate

c    *************
c    surface cards
c    *************
c
c     Axial Position
c
  1   pz -30.0                                       $ bottom of reflector
  2   pz   0.0                                       $ bottom of Al Plate
  3   pz   2.85749                                   $ bottom of Fuel Zone
  4   pz   2.8575                                    $ bottom of clad(plug)
  5   pz   3.1750                                    $ bottom of B-eggcrate
  6   pz   3.5560                                    $ bottom of UO2
  7   pz   4.0560                                    $ bottom of PuO2
  8   pz   5.715                                     $ top    of B-eggcrate
  9   pz  92.3925                                    $ bottom of T-eggcrate
 10   pz  94.9325                                    $ top    of T-eggcrate
 11   pz  94.9960                                    $ top    of PuO2 (plug)
 12   pz  95.8215                                    $ top    of clad
 13   pz  95.82151                                   $ top    of Fuel Zone
 14   pz  96.774                                     $ top    of lead
 15   pz 110.236                                     $ critical water height
c
c     Radial Position (core and reflector)
c
*21   px   0.0                                       $ X-Axis
 22   px  50.6729                                    $ X-Fuel Boundary
*23   py   0.0                                       $ Y-Axis
 24   py  50.6729                                    $ Y-Fuel Boundary
 25   cz  50.0                                       $ Core Radial Boundary
c     fuel cell universe
 31   px  -0.889                                     $ - X Cell Boundary
 32   px   0.889                                     $ + X Cell Boundary
 33   py  -0.889                                     $ - Y Cell Boundary
 34   py   0.889                                     $ + Y Cell Boundary
 35   cz   0.64135                                   $ Fuel Outer Radius
 36   cz   0.71755                                   $ Clad Outer Radius
 37   px  -0.73025                                   $ - X Egg-Crate Bndry
 38   px   0.73025                                   $ + X Egg-Crate Bndry
 39   py  -0.73025                                   $ - Y Egg-Crate Bndry
 40   py   0.73025                                   $ + Y Egg-Crate Bndry

c    **********
c    data cards
c    **********
mode  n
kcode 10000 1.0 100 600
ksrc   0.1    0.1   45.  1.778  0.1   45.  3.556  0.1   45.  5.334  0.1   45.
       7.112  0.1   45.  8.890  0.1   45. 10.668  0.1   45. 12.446  0.1   45.
      14.224  0.1   45. 16.002  0.1   45. 17.780  0.1   45. 19.558  0.1   45.
       0.1    1.778 45.  1.778  1.778 45.  3.556  1.778 45.  5.334  1.778 45.
       7.112  1.778 45.  8.890  1.778 45. 10.668  1.778 45. 12.446  1.778 45.
      14.224  1.778 45. 16.002  1.778 45. 17.780  1.778 45. 19.558  1.778 45.
       0.1    3.556 45.  1.778  3.556 45.  3.556  3.556 45.  5.334  3.556 45.
       7.112  3.556 45.  8.890  3.556 45. 10.668  3.556 45. 12.446  3.556 45.
      14.224  3.556 45. 16.002  3.556 45. 17.780  3.556 45. 19.558  3.556 45.
       0.1    5.334 45.  1.778  5.334 45.  3.556  5.334 45.  5.334  5.334 45.
       7.112  5.334 45.  8.890  5.334 45. 10.668  5.334 45. 12.446  5.334 45.
      14.224  5.334 45. 16.002  5.334 45. 17.780  5.334 45. 19.558  5.334 45.
       0.1    7.112 45.  1.778  7.112 45.  3.556  7.112 45.  5.334  7.112 45.
       7.112  7.112 45.  8.890  7.112 45. 10.668  7.112 45. 12.446  7.112 45.
      14.224  7.112 45. 16.002  7.112 45. 17.780  7.112 45. 19.558  7.112 45.
       0.1    8.890 45.  1.778  8.890 45.  3.556  8.890 45.  5.334  8.890 45.
       7.112  8.890 45.  8.890  8.890 45. 10.668  8.890 45. 12.446  8.890 45.
      14.224  8.890 45. 16.002  8.890 45. 17.780  8.890 45. 19.558  8.890 45.
       0.1   10.668 45.  1.778 10.668 45.  3.556 10.668 45.  5.334 10.668 45.
       7.112 10.668 45.  8.890 10.668 45. 10.668 10.668 45. 12.446 10.668 45.
      14.224 10.668 45. 16.002 10.668 45. 17.780 10.668 45. 19.558 10.668 45.
       0.1   12.446 45.  1.778 12.446 45.  3.556 12.446 45.  5.334 12.446 45.
       7.112 12.446 45.  8.890 12.446 45. 10.668 12.446 45. 12.446 12.446 45.
      14.224 12.446 45. 16.002 12.446 45. 17.780 12.446 45.
       0.1   14.224 45.  1.778 14.224 45.  3.556 14.224 45.  5.334 14.224 45.
       7.112 14.224 45.  8.890 14.224 45. 10.668 14.224 45. 12.446 14.224 45.
      14.224 14.224 45. 16.002 14.224 45.
       0.1   16.002 45.  1.778 16.002 45.  3.556 16.002 45.  5.334 16.002 45.
       7.112 16.002 45.  8.890 16.002 45. 10.668 16.002 45. 12.446 16.002 45.
      14.224 16.002 45.
       0.1   17.780 45.  1.778 17.780 45.  3.556 17.780 45.  5.334 17.780 45.
       7.112 17.780 45.  8.890 17.780 45. 10.668 17.780 45. 12.446 17.780 45.
       0.1   19.558 45.  1.778 19.558 45.  3.556 19.558 45.  5.334 19.558 45.
       7.112 19.558 45.  8.890 19.558 45. 10.668 19.558 45.
c    **************
c    material cards
c    **************
c      MOX
m1     8016. 4.3761e-2   8017. 1.7512e-5
      92234. 1.2458e-6  92235. 1.4886e-4  92236. 2.0936e-9
      92238. 2.0611e-2
      94238. 3.8836e-8  94239. 3.9462e-4  94240. 3.3206e-5
      94241. 1.6081e-6  94242. 1.1882e-7
      95241. 1.4954e-6
c      UO2
m2     8016. 4.1926e-2   8017. 1.6777e-5
      92234. 1.2406e-6  92235. 1.4824e-4  92236. 2.0848e-9
      92238. 2.0525e-2
c      Cladding
m3    24050. 3.3101e-6  24052. 6.3758e-5  24053. 7.2288e-6
      24054. 1.7958e-6
      26054. 5.5951e-6  26056. 8.7752e-5  26057. 2.0276e-6
      26058. 2.6780e-7
      28058. 2.0653e-5  28060. 7.9541e-6  28061. 3.4583e-7
      28062. 1.1012e-6  28064. 2.8212e-7
      40090. 2.1939e-2  40091. 4.7843e-3  40092. 7.3129e-3
      40094. 7.4110e-3  40096. 1.1939e-3
      50112. 4.6878e-6  50114. 3.1413e-6  50115. 1.6432e-6  $ ENDF/B-VII.0
      50116. 7.0269e-5  50117. 3.7116e-5  50118. 1.1705e-4  $ ENDF/B-VII.0
      50119. 4.1514e-5  50120. 1.5750e-4  50122. 2.2376e-5  $ ENDF/B-VII.0
      50124. 2.7982e-5                                      $ ENDF/B-VII.0
c      Moderator + Aluminum
m4     1001. 2.2276e-2
       5010. 6.2468e-9   5011. 2.5302e-8
       8016. 1.1111e-2   8017. 4.4552e-6
      12024. 3.5066e-4  12025. 4.4393e-5  12026. 4.8877e-5  $ ENDF/B-VII.0
      13027. 3.8920e-2
      14028. 2.1260e-4  14029. 1.0765e-5  14030. 7.1458e-6
      22046. 1.3943e-6  22047. 1.2574e-6  22048. 1.2459e-5  $ ENDF/B-VII.0
      22049. 9.1434e-7  22050. 8.7547e-7                    $ ENDF/B-VII.0
      24050. 1.8053e-6  24052. 3.4775e-5  24053. 3.9427e-6
      24054. 9.7945e-7
      25055. 1.4730e-5
      26054. 3.9558e-6  26056. 6.2042e-5  26057. 1.4336e-6
      26058. 1.8934e-7
      29063. 2.9362e-5  29065. 1.3087e-5
c      Moderator
m5     1001. 6.6706e-2
       5010. 1.8706e-8   5011. 7.5770e-5
       8016. 3.3273e-2   8017. 1.3341e-5
c      Aluminum
m6    12024. 5.2648e-4  12025. 6.6651e-5  12026. 7.3383e-5  $ ENDF/B-VII.0
      13027. 5.8433e-2
      14028. 3.1918e-4  14029. 1.6161e-5  14030. 1.0728e-5
      22046. 2.0934e-6  22047. 1.8879e-6  22048. 1.8706e-5  $ ENDF/B-VII.0
      22049. 1.3728e-6  22050. 1.3144e-6                    $ ENDF/B-VII.0
      24050. 2.7105e-6  24052. 5.2210e-5  24053. 5.9195e-6
      24054. 1.4705e-6
      25055. 2.2115e-5
      26054. 5.9389e-6  26056. 9.3145e-5  26057. 2.1522e-6
      26058. 2.8426e-7
      29063. 4.4083e-5  29065. 1.9648e-5
c      Lead
m7    82206. 7.7539e-3  82207. 7.1105e-3  82208. 1.6859e-2
c      Water + Aluminum (Reflector)
m8     1001. 4.5010e-2
       5010. 1.2622e-8   5011. 5.1125e-8
       8016. 2.2451e-2   8017. 9.0020e-6
      12024. 1.7123e-4  12025. 2.1678e-5  12026. 2.3867e-5  $ ENDF/B-VII.0
      13027. 1.9006e-2
      14028. 1.0381e-4  14029. 5.2566e-6  14030. 3.4894e-6
      22046. 6.8091e-7  22047. 6.1405e-7  22048. 6.0844e-6  $ ENDF/B-VII.0
      22049. 4.4651e-7  22050. 4.2753e-7                    $ ENDF/B-VII.0
      24050. 8.8161e-7  24052. 1.6982e-5  24053. 1.9254e-6
      24054. 4.7830e-7
      25055. 7.1931e-6
      26054. 1.9312e-6  26056. 3.0289e-5  26057. 6.9985e-7
      26058. 9.2434e-8
      29063. 1.4338e-5  29065. 6.3908e-6
mt4   lwtr
mt5   lwtr
mt8   lwtr
prdmp  999999  999999  1  1  999999