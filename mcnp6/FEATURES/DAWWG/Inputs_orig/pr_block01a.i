CSG version of block geometry for lnk2dnt comparison
c
c  protons
c
10   1   -7.874  -1     u=1          
30   0            1  2  u=1        
40   0           -3            fill=1
50   0            3  

c  Surfaces
c
1   rpp  -10 10  -10 10 -12 12
2   rpp  -10 10  -10 10   0  8
3   rpp  -20 20  -20 20 -20 20

c  Data Cards
c
mode h
sdef pos= 0 0 -9  vec=0 0 1  dir=1.0  par=h  erg=20000
c
m1     26056 1.0
m2     74180 0.001300  74182 0.263000  74183 0.143000
       74184 0.306700  74186 0.286000
c
imp:h 1 2r 0
c
tropt eloss off                                                  
c                    E-loss      Striganov    Int==Atten    Elastic on
phys:h 23080  3j   j     5j    j            1
cut:h J 1000
c
f4:h 10
c
c dbcn j j 1 10 
nps 100000
c rand hist=9
prdmp 4j 1000000
print
c
fmesh14:h geom=rec  origin= -10 -10 -12
          imesh= 10  iints= 5
          jmesh= 10  jints= 5
          kmesh=  8  kints= 4
c
