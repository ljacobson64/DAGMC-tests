Bare HEU Cylinder, VNIITF: HEU-MET-FAST-015
1   1   4.7832e-2   (5  -8  -1) #2     imp:n=1   $ bottom U
2   0                4  -6  -1         imp:n=1   $ source cavity
3   0                1  -8  -2         imp:n=1   $ gap
4   2   4.7767e-2    2  -8  -3   7     imp:n=1   $ top U
5   0                2  -7  -3         imp:n=1   $ top axial hole
6   3   8.1133e-2   11 -10  -5         imp:n=1   $ steel plate
7   0               11  10  -8  -5     imp:n=1   $ bot hollows
8   3   8.1133e-2    2 -12   8 -13     imp:n=1   $ diaphragm
9   0              (-9 -11):(-9 -2 8)  imp:n=1   $ inner OUTSIDE 1
10  0              (-9 3):(-9 8 12)    imp:n=1   $ inner outside 2
11  0                2  -9 -12  13     imp:n=1   $ outside diaphr
12  0                9                 imp:n=0   $ outer OUTSIDE

1   pz    0
2   pz    0.05
3   pz    5.22
4   pz   -1.0
5   pz   -5.96
6   cz    0.6
7   cz    1.75
8   cz    9.995
9   so   15
10  cz    9.8
11  pz   -6.17
12  pz    0.26
13  cz   13

mode n
totnu
kcode 10000 1. 100 600
ksrc  0  0 -2
c      Materials specified with atom densities
m1   92235.  4.5774e-2     92238.  1.3381e-3
     92234.  5.6597e-4
      6000.  1.0270e-4
     26054.  2.9619e-6     26056.  4.6044e-5
     26057.  1.0542e-6     26058.  1.4056e-7
     74182.  3.2083e-7     74183.  1.7420e-7
     74184.  3.7451e-7     74186.  3.4889e-7
m2   92235.  4.5708e-2     92238.  1.3404e-3
     92234.  5.6404e-4
      6000.  1.0256e-4
     26054.  2.9577e-6     26056.  4.5980e-5
     26057.  1.0528e-6     26058.  1.4037e-7
     74182.  3.2041e-7     74183.  1.7397e-7
     74184.  3.7402e-7     74186.  3.4843e-7
m3   26054.  4.7869e-3     26056.  7.4415e-2
     26057.  1.7038e-3     26058.  2.2717e-4
prdmp  999999  999999  1  1  999999
