Godiva solid bare HEU sphere. mesh generator
1 1 4.7984E-02 -1     imp:n=1
2 0             1 -2  imp:n=1
3 0                2  imp:n=0

1 so  8.7407
2 so 20

m1 92235.50c 4.4994E-02 92238.50c 2.4984E-03 92234.50c 4.9184E-04
kcode 3000 1.0 10 150
ksrc 0. 0. 0.
mesh  geom xyz
       ref      0.0       0.0   0.0
       origin -10.0     -10.0 -10.0
       imesh   -8.74707  -8.18061  -7.18061 -6.18061   0.0 
                6.18061   7.18061   8.18061  8.74707  10.0 
       iints    1         1         1        1         1   
                1         1         1        1         1   
       jmesh   -8.74707  -8.18061  -7.18061 -6.18061   0.0 
                6.18061   7.18061   8.18061  8.74707  10.0 
       jints    1         1         1        1         1   
                1         1         1        1         1   
       kmesh   -8.74707  -8.18061  -7.18061 -6.18061   0.0 
                6.18061   7.18061   8.18061  8.74707  10.0 
       kints    1         1         1        1         1   
                1         1         1        1         1   
dawwg xsec=ndilib points=10
print
