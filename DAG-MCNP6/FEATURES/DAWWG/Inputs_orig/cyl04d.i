 RZT Test using embed twice via container universe + TR
c embed pseudo cells
11   1 -18.7     0        u=e1      imp:n=1 
12   2 -0.001    0        u=e1      imp:n=1 
13   0           0        u=e1      imp:n=1
c
c first container and buffer
20      0       -1     fill=e1 (1)  imp:n=1 $ container
21   2 -0.001    1 -11              imp:n=1 $ buffer
c
c second container and buffer
30      0       -2     fill=e1 (2)  imp:n=1 $ container
31   2 -0.001    2 -22              imp:n=1 $ buffer
c 
40      0       -3 11 22            imp:n=1 $ void
c 40      0       -3 1 2              imp:n=1 $ void
41      0        3                  imp:n=0 $ null & void
 
1  sx   21 20
11 sx   21 21
2  sx  -21 20
22 sx  -21 21
3  so      42

tr1  21 0 0
tr2 -21 0 0  -1 1 0  1 1 0  0 0 1
embed1  meshgeo=lnk3dnt 
         mgeoin=CYL04.linkout 
          debug=echomesh
        matcell= 1 11
                 2 12
     background=13
      calc_vols=yes
c
kcode     500     1.0  50   100
ksrc      -21  6  1     -21  3 -1
          -21 -6  1     -21 -3 -1
          -23  0  1     -27  0 -1
          -19  0  1     -15  0 -1
           19  3  1      19  7 -1
           19  7  1      19 -3 -1
           22 -3  1     -22  3 -1
           22  7  1     -22 -7 -1
totnu no
c
m1        92235.69c   1.0
m2        6012 1.0
dm1 92235 92235.50
c
prdmp    j    275
print

end of input
