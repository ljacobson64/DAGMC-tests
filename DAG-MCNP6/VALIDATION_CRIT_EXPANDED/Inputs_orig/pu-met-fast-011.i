 Pu sphere in sphere of H2O  PU-MET-FAST-011
1        1   0.049726       -1                   $ Plutonium sphere
2        2   0.100149        1    -2             $ Water sphere
3        0                   2

1        so      4.1217                          $ radius of plutonium sphere
2        so     29.5217                          $ radius of water sphere

mode     n
kcode    10000   1.0   100   600
imp:n    1.0    1.0   0.0
sdef     cel=1    erg=d1   rad=d2   pos=0.0 0.0 0.0
sp1      -3
si2      0.0    4.1217
sp2      -21    2
c        Plutonium (5.18 w/o Pu-240)
m1       94239.     4.6982e-2     94240.     2.5852e-3
         94241.     1.4915e-4     94242.     9.9432e-6
c        Water
m2        1001.     6.6766e-2
          8016.     3.3370e-2      8017.     1.3353e-5
mt2       lwtr
totnu
prdmp  999999  999999  1  1  999999