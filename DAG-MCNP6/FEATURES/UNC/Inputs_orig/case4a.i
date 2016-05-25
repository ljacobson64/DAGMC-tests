Test of unc - uncollided secondaries card
10  1 -18.7  -1                 
20  0  1 -9                
30  0  9 -10               

1  rpp   -1 1  -1 1 0 1 
9  so 100
10  so 200

mode n p
imp:n 1 1 0
imp:p 1 1 0
sdef pos= 0 0 -.001 vec= 0 0 1 dir=1 erg=20 par=n ara=1.0
m1 92235.69c 1.0
nps 1e6
f5:p  50 0 0.5 1.0 $ uncollided should be zero
f15:n  50 0 0.5 1.0 $ uncollided should be zero
prdmp 999999 999999 -1 999999 8000
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn  42j  0 23j 200
totnu no
