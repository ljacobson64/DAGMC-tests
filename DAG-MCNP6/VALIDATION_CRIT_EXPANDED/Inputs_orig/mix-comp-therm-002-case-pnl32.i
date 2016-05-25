MIX-COMP-THERM-002 PNL-32:  sq lattice, pitch=2.20914 cm, pure water(0.9ppm)
c    **********
c    cell cards
c    **********
 1   0              -25 4 -12 fill=11    imp:n=1  $ Cube for Fueled Core
 2   5  0.100059    -25 (1 -2:14 -15)    imp:n=1  $ Bottom/Top Reflector
 3   6  0.059721    -25 2 -4             imp:n=1  $ Aluminum Plate
 4   7  0.031723    -25 12 -14           imp:n=1  $ Lead Shield
 5   0               25:-1:15            imp:n=0  $ Out of core
c
c     filling universe                          $ Cube cell filled Fuel
c
 6   0 -32 31 -34 33 lat=1 u=11 imp:n=1 fill=-27:27 -27:27 0:0
        2 1044r
        2 18r 2 2 2 2 2 2 2 1 1 1 2 2 2 2 2 2 2 2 18r
        2 18r 2 2 2 2 2 2 1 1 1 1 1 1 2 2 2 2 2 2 18r
        2 18r 2 2 2 2 1 1 1 1 1 1 1 1 1 2 2 2 2 2 18r
        2 18r 2 2 2 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 18r
        2 18r 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 18r
        2 18r 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 18r
        2 18r 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 18r
        2 18r 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 18r
        2 18r 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 18r
        2 18r 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 18r
        2 18r 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 18r
        2 18r 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 18r
        2 18r 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 18r
        2 18r 2 2 2 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 18r
        2 18r 2 2 2 2 1 1 1 1 1 1 1 1 1 2 2 2 2 2 18r
        2 18r 2 2 2 2 2 1 1 1 1 1 1 2 2 2 2 2 2 2 18r
        2 18r 2 2 2 2 2 2 2 1 1 1 2 2 2 2 2 2 2 2 18r
        2 1044r
c
c     fuel cell universe (u=1)
c
21   1  0.064971     7 -11 -35              u=1 imp:n=1  $ MOX
22   2  0.062618     6 -7  -35              u=1 imp:n=1  $ UO2 layer
#ifdef ENDF7
23   3  0.043306     3 -11 -36 #21 #22      u=1 imp:n=1  $ ENDF/B-VII.0 Clad
#else
23   3  0.042843     3 -11 -36 #21 #22    u=1 imp:n=1  $ ENDF/B-VI Clad
#endif
24   6  0.059721    (5 -8:9 -10) (-37 38:-39 40:-41 42:-43 44)
                                            u=1 imp:n=1  $ Al Egg-Crate
25   5  0.100059     #21 #22 #23 #24 #26    u=1 imp:n=1  $ Moderator
#ifdef ENDF7
26   3  0.043306     11 -13 -36             u=1 imp:n=1  $ ENDF/B-VII.0 Plug
#else
26   3  0.042843     11 -13 -36             u=1 imp:n=1  $ ENDF/B-VI Plug
#endif
c
c     Part of Radial reflector cell universe (u=2)
c
31   5  0.100059     #32                       u=2 imp:n=1  $ Water
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
 15   pz 100.711                                     $ critical water height
c
c     Radial Position (core and reflector)
c
 21   px -18.777689                                  $ X-Axis
 22   px  18.777689                                  $ X-Fuel Boundary
 23   py -18.777689                                  $ Y-Axis
 24   py  18.777689                                  $ Y-Fuel Boundary
 25   cz  60.0                                       $ Core Radial Boundary
c     fuel cell universe
 31   px  -1.10457                                   $ - X Cell Boundary
 32   px   1.10457                                   $ + X Cell Boundary
 33   py  -1.10457                                   $ - Y Cell Boundary
 34   py   1.10457                                   $ + Y Cell Boundary
 35   cz   0.64135                                   $ Fuel Outer Radius
 36   cz   0.71755                                   $ Clad Outer Radius
 37   p  1. -1. 0.  1.16204514                       $ - X Cell Boundary
 38   p  1. -1. 0.  1.04709786                       $ - X Cell Boundary
 39   p  1. -1. 0. -1.16204514                       $ - X Cell Boundary
 40   p  1. -1. 0. -1.04709786                       $ - X Cell Boundary
 41   p  1.  1. 0. -1.16204514                       $ - X Cell Boundary
 42   p  1.  1. 0. -1.04709786                       $ - X Cell Boundary
 43   p  1.  1. 0.  1.16204514                       $ - X Cell Boundary
 44   p  1.  1. 0.  1.04709786                       $ - X Cell Boundary

c    **********
c    data cards
c    **********
mode  n
kcode 10000 1.0 100 600
ksrc   -2.20914 -17.67312 45.   0.0     -17.67312 45.   2.20914 -17.67312 45.
       -6.62742 -15.46398 45.  -4.41828 -15.46398 45.  -2.20914 -15.46398 45.
        0.0     -15.46398 45.   2.20914 -15.46398 45.   4.41828 -15.46398 45.
       -8.83656 -13.25484 45.  -6.62742 -13.25484 45.  -4.41828 -13.25484 45.
       -2.20914 -13.25484 45.   0.0     -13.25484 45.   2.20914 -13.25484 45.
        4.41828 -13.25484 45.   6.62742 -13.25484 45.   8.83656 -13.25484 45.
      -11.04570 -11.04570 45.  -8.83656 -11.04570 45.  -6.62742 -11.04570 45.
       -4.41828 -11.04570 45.  -2.20914 -11.04570 45.   0.0     -11.04570 45.
        2.20914 -11.04570 45.   4.41828 -11.04570 45.   6.62742 -11.04570 45.
        8.83656 -11.04570 45.  11.04570 -11.04570 45.
      -13.25484  -8.83656 45. -11.04570  -8.83656 45.  -8.83656  -8.83656 45.
       -6.62742  -8.83656 45.  -4.41828  -8.83656 45.  -2.20914  -8.83656 45.
        0.0      -8.83656 45.   2.20914  -8.83656 45.   4.41828  -8.83656 45.
        6.62742  -8.83656 45.   8.83656  -8.83656 45.  11.04570  -8.83656 45.
       13.25484  -8.83656 45.
      -15.46398  -6.62742 45. -13.25484  -6.62742 45. -11.04570  -6.62742 45.
       -8.83656  -6.62742 45.  -6.62742  -6.62742 45.  -4.41828  -6.62742 45.
       -2.20914  -6.62742 45.   0.0      -6.62742 45.   2.20914  -6.62742 45.
        4.41828  -6.62742 45.   6.62742  -6.62742 45.   8.83656  -6.62742 45.
       11.04570  -6.62742 45.  13.25484  -6.62742 45.  15.46398  -6.62742 45.
      -15.46398  -4.41828 45. -13.25484  -4.41828 45. -11.04570  -4.41828 45.
       -8.83656  -4.41828 45.  -6.62742  -4.41828 45.  -4.41828  -4.41828 45.
       -2.20914  -4.41828 45.   0.0      -4.41828 45.   2.20914  -4.41828 45.
        4.41828  -4.41828 45.   6.62742  -4.41828 45.   8.83656  -4.41828 45.
       11.04570  -4.41828 45.  13.25484  -4.41828 45.  15.46398  -4.41828 45.
      -17.67312  -2.20914 45. -15.46398  -2.20914 45. -13.25484  -2.20914 45.
      -11.04570  -2.20914 45.  -8.83656  -2.20914 45.  -6.62742  -2.20914 45.
       -4.41828  -2.20914 45.  -2.20914  -2.20914 45.   0.0      -2.20914 45.
        2.20914  -2.20914 45.   4.41828  -2.20914 45.   6.62742  -2.20914 45.
        8.83656  -2.20914 45.  11.04570  -2.20914 45.  13.25484  -2.20914 45.
       15.46398  -2.20914 45.  17.67312  -2.20914 45.
      -17.67312   0.0     45. -15.46398   0.0     45. -13.25484   0.0     45.
      -11.04570   0.0     45.  -8.83656   0.0     45.  -6.62742   0.0     45.
       -4.41828   0.0     45.  -2.20914   0.0     45.   0.0       0.0     45.
        2.20914   0.0     45.   4.41828   0.0     45.   6.62742   0.0     45.
        8.83656   0.0     45.  11.04570   0.0     45.  13.25484   0.0     45.
       15.46398   0.0     45.  17.67312   0.0     45.
      -17.67312   2.20914 45. -15.46398   2.20914 45. -13.25484   2.20914 45.
      -11.04570   2.20914 45.  -8.83656   2.20914 45.  -6.62742   2.20914 45.
       -4.41828   2.20914 45.  -2.20914   2.20914 45.   0.0       2.20914 45.
        2.20914   2.20914 45.   4.41828   2.20914 45.   6.62742   2.20914 45.
        8.83656   2.20914 45.  11.04570   2.20914 45.  13.25484   2.20914 45.
       15.46398   2.20914 45.  17.67312   2.20914 45.
      -15.46398   4.41828 45. -13.25484   4.41828 45. -11.04570   4.41828 45.
       -8.83656   4.41828 45.  -6.62742   4.41828 45.  -4.41828   4.41828 45.
       -2.20914   4.41828 45.   0.0       4.41828 45.   2.20914   4.41828 45.
        4.41828   4.41828 45.   6.62742   4.41828 45.   8.83656   4.41828 45.
       11.04570   4.41828 45.  13.25484   4.41828 45.  15.46398   4.41828 45.
      -15.46398   6.62742 45. -13.25484   6.62742 45. -11.04570   6.62742 45.
       -8.83656   6.62742 45.  -6.62742   6.62742 45.  -4.41828   6.62742 45.
       -2.20914   6.62742 45.   0.0       6.62742 45.   2.20914   6.62742 45.
        4.41828   6.62742 45.   6.62742   6.62742 45.   8.83656   6.62742 45.
       11.04570   6.62742 45.  13.25484   6.62742 45.  15.46398   6.62742 45.
      -13.25484   8.83656 45. -11.04570   8.83656 45.  -8.83656   8.83656 45.
       -6.62742   8.83656 45.  -4.41828   8.83656 45.  -2.20914   8.83656 45.
        0.0       8.83656 45.   2.20914   8.83656 45.   4.41828   8.83656 45.
        6.62742   8.83656 45.   8.83656   8.83656 45.  11.04570   8.83656 45.
       13.25484   8.83656 45.
      -11.04570  11.04570 45.  -8.83656  11.04570 45.  -6.62742  11.04570 45.
       -4.41828  11.04570 45.  -2.20914  11.04570 45.   0.0      11.04570 45.
        2.20914  11.04570 45.   4.41828  11.04570 45.   6.62742  11.04570 45.
        8.83656  11.04570 45.  11.04570  11.04570 45.
       -8.83656  13.25484 45.  -6.62742  13.25484 45.  -4.41828  13.25484 45.
       -2.20914  13.25484 45.   0.0      13.25484 45.   2.20914  13.25484 45.
        4.41828  13.25484 45.   6.62742  13.25484 45.   8.83656 -13.25484 45.
       -4.41828  15.46398 45.  -2.20914  15.46398 45.   0.0      15.46398 45.
        2.20914  15.46398 45.   4.41828  15.46398 45.   6.62742  15.46398 45.
       -2.20914  17.67312 45.   0.0      17.67312 45.   2.20914  17.67312 45.
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
#ifdef ENDF7
      50112. 4.6878e-6  50114. 3.1413e-6  50115. 1.6432e-6  $ ENDF/B-VII.0
      50116. 7.0269e-5  50117. 3.7116e-5  50118. 1.1705e-4  $ ENDF/B-VII.0
      50119. 4.1514e-5  50120. 1.5750e-4  50122. 2.2376e-5  $ ENDF/B-VII.0
      50124. 2.7982e-5                                      $ ENDF/B-VII.0
#endif
c      Moderator + Aluminum
m4     1001. 5.6593e-2
       5010. 8.4020e-9   5011. 3.4033e-8
       8016. 2.8229e-2   8017. 1.1319e-5
#ifdef ENDF7
      12024. 7.9819e-5  12025. 1.0105e-5  12026. 1.1126e-5  $ ENDF/B-VII.0
#else
      12000. 1.0105e-4                                      $ ENDF/B-VI
#endif
      13027. 8.8588e-3
      14028. 4.8390e-5  14029. 2.4502e-6  14030. 1.6265e-6
#ifdef ENDF7
      22046. 3.1738e-7  22047. 2.8622e-7  22048. 2.8360e-6  $ ENDF/B-VII.0
      22049. 2.0812e-7  22050. 1.9927e-7                    $ ENDF/B-VII.0
#else
      22000. 3.8470e-6                                      $ ENDF/B-VI
#endif
      24050. 4.1093e-7  24052. 7.9153e-6  24053. 8.9743e-7
      24054. 2.2294e-7
      25055. 3.3528e-6
      26054. 9.0043e-7  26056. 1.4122e-5  26057. 3.2631e-7
      26058. 4.3098e-8
      29063. 6.6833e-6  29065. 2.9788e-6
m5     1001. 6.6706e-2
       5010. 9.9034e-9   5011. 4.0114e-8
       8016. 3.3340e-2   8017. 1.3341e-5
c      Aluminum
#ifdef ENDF7
m6    12024. 5.2648e-4  12025. 6.6651e-5  12026. 7.3383e-5  $ ENDF/B-VII.0
#else
m6    12000. 6.6651e-4                                      $ ENDF/B-VI
#endif
      13027. 5.8433e-2
      14028. 3.1918e-4  14029. 1.6161e-5  14030. 1.0728e-5
#ifdef ENDF7
      22046. 2.0934e-5  22047. 1.8879e-6  22048. 1.8706e-5  $ ENDF/B-VII.0
      22049. 1.3728e-6  22050. 1.3144e-6                    $ ENDF/B-VII.0
#else
      22000. 2.5375e-5                                      $ ENDF/B-VI
#endif
      24050. 2.7105e-6  24052. 5.2210e-5  24053. 5.9195e-6
      24054. 1.4705e-6
      25055. 2.2115e-5
      26054. 5.9389e-6  26056. 9.3145e-5  26057. 2.1522e-6
      26058. 2.8426e-7
      29063. 4.4083e-5  29065. 1.9648e-5
c      Lead
m7    82206. 7.7539e-3  82207. 7.1105e-3  82208. 1.6859e-2
c      Water + Aluminum (Reflector)
m8     1001. 5.9945e-2
       5010. 8.8996e-9   5011. 3.6048e-8
       8016. 2.9961e-2   8017. 1.1989e-5
#ifdef ENDF7
      12024. 5.3362e-5  12025. 6.7556e-6  12026. 7.4379e-6  $ ENDF/B-VII.0
#else
      12000. 6.7556e-5                                      $ ENDF/B-VI
#endif
      13027. 5.9226e-3
      14028. 3.2352e-5  14029. 1.6381e-6  14030. 1.0874e-6
#ifdef ENDF7
      22046. 2.1219e-7  22047. 1.9136e-7  22048. 1.8961e-6  $ ENDF/B-VII.0
      22049. 1.3915e-7  22050. 1.3323e-7                    $ ENDF/B-VII.0
#else
      22000. 2.5720e-6                                      $ ENDF/B-VI
#endif
      24050. 2.7473e-7  24052. 5.2918e-6  24053. 5.9998e-7
      24054. 1.4905e-7
      25055. 2.2415e-6
      26054. 6.0197e-7  26056. 9.4411e-6  26057. 2.1815e-7
      26058. 2.8812e-8
      29063. 4.4681e-6  29065. 1.9915e-6
mt4   lwtr
mt5   lwtr
mt8   lwtr
prdmp  999999  999999  1  1  999999
