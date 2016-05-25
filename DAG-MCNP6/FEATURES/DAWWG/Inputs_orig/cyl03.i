 Generate a LNK3DNT r-z-t mesh w/ multiple materials
c upper-inner
1   1   -18.7         -11 -1  2  4     imp:n=1
2   2   -0.001        -11 -2 -3  4     imp:n=1
3   1   -18.7         -11  3  1  4     imp:n=1
c upper-outer
4   2   -0.001     -10 11 -1  2  4     imp:n=1
5   1   -18.7      -10 11 -2 -3  4     imp:n=1
6   2   -0.001     -10 11  3  1  4     imp:n=1
c lower-inner
7   2   -0.001        -11 -1  2 -4    imp:n=1
8   1   -18.7         -11 -2 -3 -4    imp:n=1
9   2   -0.001        -11  3  1 -4    imp:n=1
c lower-outer
10  1   -18.7      -10 11 -1  2 -4    imp:n=1
11  2   -0.001     -10 11 -2 -3 -4    imp:n=1
12  1   -18.7      -10 11  3  1 -4    imp:n=1
c outer void
13         0           10              imp:n=0

10  rcc  0. 0. -10. 0. 0. 20. 10. $ outer rcc
11  rcc  0  0  -10  0  0  20  5   $ inner rcc
1  py   0.0                       
2  p    1.732050808 -1.0  0 0
3  p    1.732050808  1.0  0 0 
4  pz   0.0

vol 261.8 2r 785.4 2r 261.8 2r 785.4 2r j
kcode     5000     1.0  50   250
ksrc 0.0 0.0 0.0
totnu no
m1        92235.69c   1.0
m2        1001  1.0
dm1 92235 92235.50
prdmp    j    275
mesh  geom cyl
      ref     0.0   0.0  -0.0
      origin  0.0   0.0 -10.0
      axs     0.0   0.0   1.0
      vec     1.0   0.0   0.0
      imesh   10 $ cylinder radius
      iints    2
      jmesh   20 $ axis length
      jints    2 $ 
      kmesh    1 $ azimuth
      kints    3 $ 0, (2/3)*pi, (4/3)*pi, (6/3)*pi
f4:n 1 3 5 8 10 12
dawwg xsec=ndilib points=10
print

end of input
