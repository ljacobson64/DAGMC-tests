c  ORNL-1 Uranyl nitrate in H2O Sphere;  HEU-SOL-THERM-013  case #1
c  and CSEWG: T-1
1 1 9.992137412e-2 -1    imp:n=1
2 2 6.0317237e-2    1 -2 imp:n=1
3 0                 2    imp:n=0

1 so 34.5948
2 so 34.9148

mode n
kcode 10000 1. 100 600
sdef  pos 0.0 0.0 0.0  rad d1
sc1   Spherical Source
si1   34.5
c material cards
c      Materials specified with atom densities
m1    92234.  5.3850e-7      92235.  4.8042e-5
      92236.  1.3862e-7      92238.  2.8050e-6
       7014.  1.8685e-4
       8016.  3.3629e-2       8017.  1.3457e-5
       1001.  6.6041e-2
m2    13027.  5.9699e-2
      14028.  5.0913e-4      14029.  2.5779e-5
      14030.  1.7113e-5
      25055.  1.4853e-5
      29063.  3.5529e-5      29065.  1.5835e-5
mt1 lwtr
totnu
prdmp  999999  999999  1  1  999999
