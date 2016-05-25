LNK3DNT mesh to compare w/ Standard MCNP cube08 - neutrons through Fe
11  1 -7.874  0                      imp:n=1    u=e1
12  0         0                      imp:n=1    u=e1
20  0        -1                      imp:n=1 fill=e1
c
21  0         1 -2 (-4:5:-6:7:-8:9)  imp:n=1
22  0         4 -5 6 -7 8 -9         imp:n=1      
23  0         2                      imp:n=0
 
1  so  15
2  so  100
4  px  20
5  px  21
6  py -10
7  py  10
8  pz -10
9  pz  10
c

embed1  meshgeo=lnk3dnt mgeoin=CUBE01.linkout debug=echomesh
        matcell= 1 11
        background=12
        calc_vols=yes
sdef pos = -16.0 0.01 0.01  vec=1 0 0 dir=1.0
totnu no
m1   26056.66c 1.0
f4:n 22
sd4 1
dbcn j j 1 10 
nps 100000
prdmp 4j 8000
print
