MIX-COMP-THERM-002 PNL-35:  square lattice, pitch=2.51447 cm, 767.2 PPM
c    **********
c    cell cards
c    **********
 1   0              21 23 -25 4 -12 fill=11  imp:n=1  $ Cube for Fuelled Core
 2   5  0.100130    21 23 -25 (1 -2:14 -15)  imp:n=1  $ Bottom / Top Reflector
 3   6  0.059721    21 23 -25 2 -4           imp:n=1  $ Aluminum Plate
 4   7  0.031723    21 23 -25 12 -14         imp:n=1  $ Lead Shield
 5   0              25:-1:15:-21:-23         imp:n=0  $ Out of core
c
c     filling universe                          $ Cube cell filled Fuel
c
 6   0 -32 31 -34 33 lat=1 u=11 imp:n=1 fill=0:28 0:28 0:0
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 13r
         1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 13r
         1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 13r
         1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 13r
         1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 13r
         1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 13r
         1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 13r
         2 405r
c
c     fuel cell universe (u=1)
c
21   1  0.064971     7 -11 -35              u=1 imp:n=1  $ MOX
22   2  0.062618     6 -7  -35              u=1 imp:n=1  $ UO2 layer
23   3  0.043306     3 -11 -36 #21 #22      u=1 imp:n=1  $  ENDF/B-VII.0 Clad
24   6  0.059721    (5 -8:9 -10) (-37 38:39 -40:41 -42:-43 44)
                                            u=1 imp:n=1  $ Al Egg-Crate
25   5  0.100130     #21 #22 #23 #24 #26    u=1 imp:n=1  $ Moderator
26   3  0.043306    11 -13 -36              u=1 imp:n=1  $ ENDF/B-VII.0 Top Plug
c
c     Part of Radial reflector cell universe (u=2)
c
31   5  0.100130     #32                    u=2 imp:n=1  $ Water
32   6  0.059721    (5 -8:9 -10) (-37 38:39 -40:41 -42:-43 44)
                                            u=2 imp:n=1  $ Al Egg-Crate

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
 22   px  36.4598149                                 $ X-Fuel Boundary
*23   py   0.0                                       $ Y-Axis
 24   py  36.4598149                                 $ Y-Fuel Boundary
 25   cz  70.0                                       $ Core Radial Boundary
c     fuel cell universe
 31   px  -1.257235                                  $ - X Cell Boundary
 32   px   1.257235                                  $ + X Cell Boundary
 33   py  -1.257235                                  $ - Y Cell Boundary
 34   py   1.257235                                  $ + Y Cell Boundary
 35   cz   0.64135                                   $ Fuel Outer Radius
 36   cz   0.71755                                   $ Clad Outer Radius
 37   p  1. -1. 0.  1.48174226                       $ - X Cell Boundary
 38   p  1. -1. 0.  1.03272945                       $ - X Cell Boundary
 39   p  1. -1. 0. -1.48174226                       $ - X Cell Boundary
 40   p  1. -1. 0. -1.03272945                       $ - X Cell Boundary
 41   p  1.  1. 0. -1.48174226                       $ - X Cell Boundary
 42   p  1.  1. 0. -1.03272945                       $ - X Cell Boundary
 43   p  1.  1. 0.  1.48174226                       $ - X Cell Boundary
 44   p  1.  1. 0.  1.03272945                       $ - X Cell Boundary

c    **********
c    data cards
c    **********
mode  n
kcode 10000 1.0 100 600
ksrc   0.1      0.1     45.  2.51447  0.1     45.  5.02894  0.1     45.
       7.54341  0.1     45. 10.05788  0.1     45. 12.57235  0.1     45.
      15.08682  0.1     45. 17.60129  0.1     45. 20.11576  0.1     45.
      22.63023  0.1     45. 25.14470  0.1     45. 27.65917  0.1     45.
      30.17364  0.1     45. 32.68811  0.1     45. 35.20258  0.1     45.
       0.1      2.51447 45.  2.51447  2.51447 45.  5.02894  2.51447 45.
       7.54341  2.51447 45. 10.05788  2.51447 45. 12.57235  2.51447 45.
      15.08682  2.51447 45. 17.60129  2.51447 45. 20.11576  2.51447 45.
      22.63023  2.51447 45. 25.14470  2.51447 45. 27.65917  2.51447 45.
      30.17364  2.51447 45. 32.68811  2.51447 45. 35.20258  2.51447 45.
       0.1      5.02894 45.  2.51447  5.02894 45.  5.02894  5.02894 45.
       7.54341  5.02894 45. 10.05788  5.02894 45. 12.57235  5.02894 45.
      15.08682  5.02894 45. 17.60129  5.02894 45. 20.11576  5.02894 45.
      22.63023  5.02894 45. 25.14470  5.02894 45. 27.65917  5.02894 45.
      30.17364  5.02894 45. 32.68811  5.02894 45. 35.20258  5.02894 45.
       0.1      7.54341 45.  2.51447  7.54341 45.  5.02894  7.54341 45.
       7.54341  7.54341 45. 10.05788  7.54341 45. 12.57235  7.54341 45.
      15.08682  7.54341 45. 17.60129  7.54341 45. 20.11576  7.54341 45.
      22.63023  7.54341 45. 25.14470  7.54341 45. 27.65917  7.54341 45.
      30.17364  7.54341 45. 32.68811  7.54341 45. 35.20258  7.54341 45.
       0.1     10.05788 45.  2.51447 10.05788 45.  5.02894 10.05788 45.
       7.54341 10.05788 45. 10.05788 10.05788 45. 12.57235 10.05788 45.
      15.08682 10.05788 45. 17.60129 10.05788 45. 20.11576 10.05788 45.
      22.63023 10.05788 45. 25.14470 10.05788 45. 27.65917 10.05788 45.
      30.17364 10.05788 45. 32.68811 10.05788 45. 35.20258 10.05788 45.
       0.1     12.57235 45.  2.51447 12.57235 45.  5.02894 12.57235 45.
       7.54341 12.57235 45. 10.05788 12.57235 45. 12.57235 12.57235 45.
      15.08682 12.57235 45. 17.60129 12.57235 45. 20.11576 12.57235 45.
      22.63023 12.57235 45. 25.14470 12.57235 45. 27.65917 12.57235 45.
      30.17364 12.57235 45. 32.68811 12.57235 45. 35.20258 12.57235 45.
       0.1     15.08682 45.  2.51447 15.08682 45.  5.02894 15.08682 45.
       7.54341 15.08682 45. 10.05788 15.08682 45. 12.57235 15.08682 45.
      15.08682 15.08682 45. 17.60129 15.08682 45. 20.11576 15.08682 45.
      22.63023 15.08682 45. 25.14470 15.08682 45. 27.65917 15.08682 45.
      30.17364 15.08682 45. 32.68811 15.08682 45.
       0.1     17.60129 45.  2.51447 17.60129 45.  5.02894 17.60129 45.
       7.54341 17.60129 45. 10.05788 17.60129 45. 12.57235 17.60129 45.
      15.08682 17.60129 45. 17.60129 17.60129 45. 20.11576 17.60129 45.
      22.63023 17.60129 45. 25.14470 17.60129 45. 27.65917 17.60129 45.
      30.17364 17.60129 45. 32.68811 17.60129 45.
       0.1     20.11576 45.  2.51447 20.11576 45.  5.02894 20.11576 45.
       7.54341 20.11576 45. 10.05788 20.11576 45. 12.57235 20.11576 45.
      15.08682 20.11576 45. 17.60129 20.11576 45. 20.11576 20.11576 45.
      22.63023 20.11576 45. 25.14470 20.11576 45. 27.65917 20.11576 45.
      30.17364 20.11576 45.
       0.1     22.63023 45.  2.51447 22.63023 45.  5.02894 22.63023 45.
       7.54341 22.63023 45. 10.05788 22.63023 45. 12.57235 22.63023 45.
      15.08682 22.63023 45. 17.60129 22.63023 45. 20.11576 22.63023 45.
      22.63023 22.63023 45. 25.14470 22.63023 45. 27.65917 22.63023 45.
       0.1     25.14470 45.  2.51447 25.14470 45.  5.02894 25.14470 45.
       7.54341 25.14470 45. 10.05788 25.14470 45. 12.57235 25.14470 45.
      15.08682 25.14470 45. 17.60129 25.14470 45. 20.11576 25.14470 45.
      22.63023 25.14470 45. 25.14470 25.14470 45.
       0.1     27.65917 45.  2.51447 27.65917 45.  5.02894 27.65917 45.
       7.54341 27.65917 45. 10.05788 27.65917 45. 12.57235 27.65917 45.
      15.08682 27.65917 45. 17.60129 27.65917 45. 20.11576 27.65917 45.
      22.63023 27.65917 45.
       0.1     30.17364 45.  2.51447 30.17364 45.  5.02894 30.17364 45.
       7.54341 30.17364 45. 10.05788 30.17364 45. 12.57235 30.17364 45.
      15.08682 30.17364 45. 17.60129 30.17364 45. 20.11576 30.17364 45.
       0.1     32.68811 45.  2.51447 32.68811 45.  5.02894 32.68811 45.
       7.54341 32.68811 45. 10.05788 32.68811 45. 12.57235 32.68811 45.
      15.08682 32.68811 45. 17.60129 32.68811 45.
       0.1     35.20258 45.  2.51447 35.20258 45.  5.02894 35.20258 45.
       7.54341 35.20258 45. 10.05788 35.20258 45. 12.57235 35.20258 45.
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
m4     1001. 3.7537e-2
       5010. 4.7622e-6   5011. 1.9289e-5
       8016. 1.8796e-2   8017. 7.5216e-6
      12024. 2.3011e-4  12025. 2.9131e-5  12026. 3.2073e-5  $ ENDF/B-VII.0
      13027. 2.5540e-2
      14028. 1.3951e-4  14029. 7.0638e-6  14030. 4.6891e-6
      22046. 9.1501e-7  22047. 8.2517e-7  22048. 8.1763e-6  $ ENDF/B-VII.0
      22049. 6.0002e-7  22050. 5.7451e-7                    $ ENDF/B-VII.0
      24050. 1.1847e-6  24052. 2.2819e-5  24053. 2.5872e-6
      24054. 6.4272e-7
      25055. 9.6659e-6
      26054. 2.5959e-6  26056. 4.0713e-5  26057. 9.4073e-7
      26058. 1.2425e-7
      29063. 1.9267e-5  29065. 8.5877e-6
c      Moderator
m5     1001. 6.6682e-2
       5010. 8.4597e-6   5011. 3.4266e-5
       8016. 3.3392e-2   8017. 1.3362e-5
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
m8     1001. 4.4994e-2
       5010. 5.7082e-6   5011. 2.3121e-5
       8016. 2.2531e-2   8017. 9.0160e-6
      12024. 1.7123e-4  12025. 2.1678e-5  12026. 2.3867e-5  $ ENDF/B-VII.0
      13027. 1.9006e-2
      14028. 1.3951e-4  14029. 7.0638e-6  14030. 4.6891e-6
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