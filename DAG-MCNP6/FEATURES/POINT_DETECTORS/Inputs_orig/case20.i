P->P point detector
10  1 -18.7  -1                 
20  0  1 -9                
30  0  9 -10               

1  rpp   -1 1  -1 1 0 1 
9  so 1000
10  so 2000

mode p 
imp:p 1 1 0
c unc:p 0 0 0
sdef pos= 0 0 -.001 vec= 0 0 1 dir=1 erg=20 par=p ara=1.0
m1 74000 1.0
nps 1e4
f5:p  50 0 100.0 1.0 
c
f15:p  50 0 100.0 1.0 
c
f25:p  50 0 100.0 1.0 
e25   .01 0.1   1.0  10.0 19.0 20.0
em25  .01  0.1   .2   .3    .4   .5
c
f35:p  50 0 100.0 1.0 
e35   .01 0.1   1.0  10.0 19.0 20.0
em35  .9 0.5   .4   .3    .2   .1
c
f45z:p 0.5   50.0  1.0 
f55z:p 100.0 50.0  1.0 
C
f65z:p 0.5   50.0  1.0 
f75z:p 100.0 50.0  1.0 
C
FIR85:p 50.0 0.0 100.0 0 0.0 0.0 0.0 0  0 0
fs85 -1 0.0 1
c85  -1 0.0 1
c
FIR95:p 50.0 0.0 100.0 0 0.0 0.0 0.0 -1 0 0
fs95 -1 0.0 1
c95  -1 0.0 1
c
prdmp 999999 999999 -1 999999 8000
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn 66j 200
