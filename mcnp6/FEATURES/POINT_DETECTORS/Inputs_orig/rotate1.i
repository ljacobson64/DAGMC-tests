Rotated poing detector P->P point detector
10  1 -18.7  -1                 
20  0  1 -9                
30  0  9 -10               

1 1 rpp   -1 1  -.25 .25 -1 1
9  so 1000
10  so 2000

c           xx' yx' zx'  xy' yy' zy' xz' yz' zz'
*tr1 0 0 0  45 -45  90  135  45  90  90  90   0
mode p 
imp:p 1 1 0
c unc:p 0 0 0
sdef pos= 0 0 -.001 vec= 0 0 1 dir=1 erg=20 par=p ara=1.0
m1 74000 1.0
nps 1e4
f5:p  0 50 0 0.0 
     50  0 0 0.0
     50 50 0 0.0
prdmp 999999 999999 -1 999999 8000
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn 66j 200

