 RZT Test using embed twice via container universe + TR
c
c pseudo cells 1/2 constitute embedded geometry
11   1 -18.7     0            u=e1  imp:n=1
12   2 -0.001    0            u=e1  imp:n=1
13   0           0            u=e1  imp:n=1 $ background
c
c container and buffer constitute u(2)
20   0          -1    u=2  fill=e1  imp:n=1 $ container
21   2 -0.001    1    u=2           imp:n=1 $ infinite buffer
c
c holders for the container/buffer u(2), w/TR
30   0          -2 fill=2 (1)       imp:n=1 $ first  use, crops buffer
31   0          -3 fill=2 (2)       imp:n=1 $ second use, crops buffer
c        
40   0          -4 2 3              imp:n=1 $ void
41   0           4                  imp:n=0 $ null & void
 
1  so      20
2  sx   21 21
3  sx  -21 21
4  so      42

tr1  21 0 0
tr2 -21 0 0  -1 1 0  1 1 0  0 0 1
embed1 meshgeo=lnk3dnt mgeoin=CYL04.linkout debug=echomesh
        matcell= 1 11 
                 2 12
     background= 13
      calc_vols=yes
c
kcode     500     1.0  50   100
ksrc      -21    6    -1     -21    3    1 $ points in 30(20(...))
          -21   -6    -1     -21   -3    1
          -24    0    -1     -28    0    1
          -18    0    -1     -14    0    1
           22.5 -1.5  -1      26   -5    1 $ points in 31(20(...))
           19.5  1.5  -1      16    5    1
           26    5    -1      22.5  1.5  1
           16   -1    -1      19.5 -1.5  1
totnu no
c
m1        92235.69c   1.0
m2        6012 1.0
dm1 92235 92235.50
c
prdmp    j    275
print

end of input
