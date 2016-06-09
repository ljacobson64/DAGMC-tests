message: fatal

stat2:  MCNP estimate of pi
1 0 -1
2 0  1

1 rcc  0 0 0  10 0 0  10
2 cx   1

imp:p 1 0
phys:p j 1
mode p
sdef x=0 y=d1 z=d1 vec=1 0 0 dir=1 sur 1.3
si1 -1 1
sp1 0 1
f1:p 1.2
fs1 -2 t
fm1 4
tf1 3j 1
fq1 s m
nps 100000
prdmp 2j -1 j -1
c                         

