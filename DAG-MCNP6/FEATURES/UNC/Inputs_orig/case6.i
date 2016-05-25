LAQGSM Test problem h->Pb  70GeV
c
1   1  -10   -501      imp:n=1
2   0         501  -502  imp:n=1
99  0         502      imp:n=0

501   so 0.01
502   so 1000
c
c  tally surfaces
c

unc:n 1 1 1
unc:h 1 1 1
unc:# 1 1 1
unc:a 1 1 1
unc:t 1 1 1
unc:d 1 1 1
unc:s 1 1 1
unc:/ 1 1 1
unc:z 1 1 1
unc:p 1 1 1
c
m1 82208 1
lca 7j -2 j 1    $ LAQGSM
prdmp 2J -1
sdef par=h erg=70000 vec=0 0 1 dir 1
nps 500
phys:# 70100
phys:h 70100
phys:n 70100
mode n h # a t d s / z p
c
f5:n   20.0 0.0 0.0 1.0
f15:p  20.0 0.0 0.0 1.0
FIR25:n 20.0 0.0 0.0 0 0.0 0.0 0.0 0  0 0
FIR35:n 20.0 0.0 0.0 0 0.0 0.0 0.0 -1 0 0 
fs25 -1 0.0 1
c25  -1 0.0 1
fs35 -1 0.0 1
c35  -1 0.0 1
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn   26j  1  j  0  2j  0  j  8j  1   0 j 1 20j 200
