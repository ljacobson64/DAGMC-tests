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
nps 1e5
f4:p 10 
f5:p  50 0 100.0 1.0 
f15:p  50 0 90.0 1.0 
f25:p  50 0 80.0 1.0 
f35:p  50 0 70.0 1.0 
f45:p  50 0 10.0 1.0 
prdmp 999999 999999 -1 999999 8000
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn 49j 1 16j 200 $ turn on extend percision tfc print.

