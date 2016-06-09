Point detector test - multigroup photons creating photons
10  1 -18.7  -1                 
20  0  1 -9                
30  0  9 -10               

1  rpp   -1 1  -1 1 0 1 
9  so 1000
10  so 2000

mode n p
imp:n 1 1 0
imp:p 1 1 0
c unc:p 0 0 0 
c unc:n 0 0 0 
sdef pos= 0 0 -.001 vec= 0 0 1 dir=1 erg=20 par=p ara=1.0
m1 92235.50m 1.0
mgopt f 42 $ mode np
nps 1e4
f5:p  50 0 100.0 1.0 $ uncollided should be zero
f15:n  50 0 100.0 1.0 $ uncollided should be zero
prdmp j j -1
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn 66j 200
totnu no
