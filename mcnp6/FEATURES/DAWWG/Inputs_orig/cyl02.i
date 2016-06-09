 Generate a LNK3DNT r-z-t mesh w/ 3 azimuthal divisions 
1         1        -18.7         -1        imp:n=1
2         0                       1        imp:n=0

1  rcc  0. 0. -10. 0. 0. 20. 10.

kcode     5000     1.0  50   250
ksrc 0.0 0.0 0.0
totnu no
m1        92235.69c   1.0
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
f4:n 1
dawwg xsec=ndilib points=10
print

end of input
