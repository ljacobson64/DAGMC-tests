stat3:  MCNP estimate of mean free path
1 1 1 -1
2 0    1

1 rcc  0 0 0  10 0 0  10

imp:p 1 0
phys:p j 1 2j 1
mode p
m1 1001 2 8016 1
sdef pos=0 0 0 vec=1 0 0 dir=1 erg=1 sur=1.3
nps 100000
prdmp 2j -1 j -1
cut:p j .999
print 160 161 162
f4:p 1
sd4 1
fu4 0 1 2 t
ft4 inc
tf4 2j 1
fq4 u f
c                         

