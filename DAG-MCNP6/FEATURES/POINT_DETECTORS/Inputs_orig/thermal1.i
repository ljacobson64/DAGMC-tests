Rotated poing detector P->P point detector
10  1 -1.0   -1   u=1 
11  0         1   u=1              
12  0        -2   fill=1 (1)              
20  0  2 -9                
30  0  9 -10               

1  rpp   0 2  0 .5 0 2 
2  rpp   -20 20  -20 20 -20 20 
9  so 1000
10  so 2000

c             xx' yx' zx'  xy' yy' zy' xz' yz' zz'
*tr1 1. .25 1  45 -45  90  135  45  90  90  90   0 -1
c *tr1 -1. -.25 -1  
mode n 
imp:n 1 1 1 1 0
sdef pos= 0 0 -.001 vec= 0 0 1 dir=1 erg=1e-8 par=n ara=1.0
m1 1001 2.0 8016 1.0
nps 1e4
f5:n  0 50 0 0.0 
     50  0 0 0.0
     50 50 0 0.0
f15:n  0 50 0 0.0 
     50  0 0 0.0
     50 50 0 0.0
prdmp 999999 999999 -1 999999 8000
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn 66j 200
totnu no