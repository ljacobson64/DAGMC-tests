 Simple test of converting MCNP geometry to LNK3DNT using a cube
1    1     -18.0      -1        imp:n=1
2    2     -0.001      1 -2     imp:n=1
3    0                 2        imp:n=0

1  rpp  -10 10 -10 10 -10 10
2  so   17.4

kcode     1000     1.0  10   100
ksrc -5.0  0.0  0.0   5.0  0.0  0.0 
      0.0 -5.0  0.0   0.0  5.0  0.0
      0.0  0.0 -5.0   0.0  0.0  5.0
totnu no
m1        92235.69c   1.0
m2        1001.60c   1.0
prdmp    j    275
print

end of input
