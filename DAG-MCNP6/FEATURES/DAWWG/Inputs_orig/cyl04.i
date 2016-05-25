 Generate a LNK3DNT r-z-t mesh w/ multiple materials
c upper-inner
1   1   -18.7         -11  1  2  3     imp:n=1
2   2   -0.001        -11  1 -2  3     imp:n=1
3   1   -18.7         -11 -1 -2  3     imp:n=1
4   2   -0.001        -11 -1  2  3     imp:n=1 
c upper-outer
6   2   -0.001     -10 11  1  2  3     imp:n=1
7   1   -18.7      -10 11  1 -2  3     imp:n=1
8   2   -0.001     -10 11 -1 -2  3     imp:n=1
9   1   -18.7      -10 11 -1  2  3     imp:n=1 
c lower-inner
11  2   -0.001        -11  1  2 -3     imp:n=1
12  1   -18.7         -11  1 -2 -3     imp:n=1
13  2   -0.001        -11 -1 -2 -3     imp:n=1
14  1   -18.7         -11 -1  2 -3     imp:n=1 
c lower-outer
16  1   -18.7      -10 11  1  2 -3     imp:n=1
17  2   -0.001     -10 11  1 -2 -3     imp:n=1
18  1   -18.7      -10 11 -1 -2 -3     imp:n=1
19  2   -0.001     -10 11 -1  2 -3     imp:n=1 
c
c outer void
20         0           10              imp:n=0

10  rcc  0. 0. -10. 0. 0. 20. 10. $ outer rcc
11  rcc  0  0  -10  0  0  20  5   $ inner rcc
1   py   0.0                       
2   px   0.0
3   pz   0.0

vol 196.35 3r 589.049 3r 196.35 3r 589.049 3r j
kcode     5000     1.0  50   250
ksrc 0.0 0.0 0.0
totnu no
m1        92235.69c   1.0
m2        6012 1.0
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
      kints    4 $ 0, pi/2, 2pi/2, 3pi/2, 4pi/2
f4:n (1 3 7 9 12 14 16 18)
dawwg xsec=ndilib points=10
print

end of input
