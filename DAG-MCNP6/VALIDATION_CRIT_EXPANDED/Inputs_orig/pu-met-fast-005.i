TUNGSTEN REFLECTED PU(4.9) SPHERE [PLANET]: PU-MET-FAST-005
1   1   0.04070346 -1   imp:n=1
2   2   0.06605308 1 -2 imp:n=1
3   0   2               imp:n=0

1   so   5.0419
2   so   9.7409

kcode 10000 1. 100 600
ksrc  0 0 0
totnu
c  print
c      Materials specified with atom densities
m1    94239.  3.7291e-2      94240.  1.9277e-3
      94241.  1.2196e-4
#ifdef ENDF7
      31069.  8.1915e-4      31071.  5.4365e-4  $ ENDF/B-VII.0
#else
      31000.  1.3628e-3                         $ ENDF/B-VI
#endif
m2    74182.  1.3536e-2      74183.  7.3496e-3
      74184.  1.5801e-2      74186.  1.4720e-2
      28058.  6.3066e-3      28060.  2.5349e-3
      28061.  1.0975e-4      28062.  3.4868e-4
      28064.  8.8383e-5
      29063.  2.8203e-3      29065.  1.2571e-3
#ifdef ENDF7
      40090.  4.0917e-4      40091.  8.9230e-5  $ ENDF/B-VII.0
      40092.  1.3639e-4      40094.  1.3822e-4  $ ENDF/B-VII.0
      40096.  2.2268e-5                         $ ENDF/B-VII.0
#else
      40000.  7.9528e-4                         $ ENDF/B-VI
#endif
prdmp  999999  999999  1  1  999999
