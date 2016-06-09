c  ORNL-3 Uranyl nitrate in H2O Sphere;  HEU-SOL-THERM-013  case #3
c  and CSEWG: T-3
1 1 9.985904038e-2 -1    imp:n=1
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
m1    92234.  7.1630e-7      92235.  6.3904e-5
      92236.  1.8438e-7      92238.  3.7311e-6
       7014.  2.3909e-4
       5010.  2.0725e-6       5011.  8.3421e-6
       8016.  3.3713e-2       8017.  1.3490e-5
       1001.  6.5815e-2
m2    13027.  5.9699e-2
      14028.  5.0913e-4      14029.  2.5779e-5
      14030.  1.7113e-5
      25055.  1.4853e-5
      29063.  3.5529e-5      29065.  1.5835e-5
mt1    lwtr
totnu
c  print
prdmp  999999  999999  1  1  999999
