 Simple test of converting MCNP geometry to LNK3DNT using a cube
1         1        -18.7         -1        imp:n=1
2         0                       1        imp:n=0

1  rpp  -10 10 -10 10 -10 10

kcode     5000     1.0  50   250
ksrc 0.0 0.0 0.0
totnu no
m1        92235.69c   1.0
dm1 92235 92235.50
prdmp    j    275
mesh  geom xyz
      ref 0.0 -0.0 -0.0
      origin -10.000 -10.000 -10.000
      imesh  10
      iints  2
      jmesh  10
      jints  2
      kmesh  10
      kints  2
f4:n 1
dawwg points=10
      block=1 ngroup=16 isn=16 iquad=4
      block=3 libname=mendf5 lib=ndilib
      block=5 trcor=diag srcacc=dsa diffsol=mg isct=2
      block=6 massed=1 edoutf=3
print

end of input

  
