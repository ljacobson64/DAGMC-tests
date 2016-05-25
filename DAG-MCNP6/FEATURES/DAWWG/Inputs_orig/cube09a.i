Standard MCNP to compare with cube09 - neutrons through Fe
1   1 -7.874 -10                     imp:n=1  u=1
2   0        10                      imp:n=1  u=1
c
20  0        -1                      imp:n=1 fill=1
21  0         1 -2 (-4:5:-6:7:-8:9)  imp:n=1
22  0         4 -5 6 -7 8 -9         imp:n=1      
23  0         2                      imp:n=0
 
1  so  20
2  so  100
3  so  1000
4  px  20
5  px  21
6  py -10
7  py  10
8  pz -10
9  pz  10
c
10  rpp  -10 10 -10 10 -10 10

sdef pos = -9.0 0.01 0.01  vec=1 0 0 dir=1.0
totnu no
m1   26056.66c 1.0
f4:n 22
sd4 1
dbcn j j 1 10 
nps 100000
prdmp 4j 8000
print
