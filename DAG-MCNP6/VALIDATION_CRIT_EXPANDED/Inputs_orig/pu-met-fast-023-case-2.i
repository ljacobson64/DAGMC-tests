Simplified Plutonium Sphere reflected by graphite, VNIIEF:  PU-MET-FAST-023
C Graphite thermal S(alpha,beta) treatment applied at 300K
1   0              -1
2   1   4.1846e-2   1 -2
3   2   9.1842e-2   2 -3
4   0               3

1   so   1.715
2   so   6.000
3   so   8.35

imp:n   1  1  1  0
totnu
kcode   10000  1.  100 600
ksrc    2  0  0
c      Materials specified with atom densities
m1   94239.  3.6603e-2     94240.  6.6913e-4
#ifdef ENDF7
     31069.  1.3197e-3     31071.  8.7587e-4  $ ENDF/B-VII.0
#else
     31000.  2.1956e-3                        $ ENDF/B-VI
#endif
     26054.  8.3107e-6     26056.  1.2920e-4
     26057.  2.9581e-6     26058.  3.9441e-7
      6000.  2.8927e-4
     28058.  1.3302e-3     28060.  5.0853e-4
     28061.  2.2017e-5     28062.  6.9948e-5
     28064.  1.7730e-5
m2    6000.  9.1842e-2
mt2   grph
prdmp  999999  999999  1  1  999999
