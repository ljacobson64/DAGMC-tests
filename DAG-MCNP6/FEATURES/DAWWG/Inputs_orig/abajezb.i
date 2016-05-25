UM Jezebel: Bare plutonium sphere w/nickel shell
c cells
1   1   4.0290e-2     0   u=1
2   2   9.1322e-2     0   u=1
3   3  -0.989352e-3   0   u=1
4   0                 0   u=1
5   0                -9   fill=1
9   0                 9

c surfaces
9  so 25

c data
m1    94239 3.7047e-2    94240 1.751e-3
      94241 1.17e-4      31000 1.375e-3
m2    28000 1.0
m3    7014 1.0
imp:n 1 1 1 1 1 0
mode n
f4:n 1 2 3
f6:n 1
embed1  meshgeo=lnk3dnt    
        mgeoin=abajez.linkout
        background=2
        matcell=   1  1
                   2  2
                   3  3
embee4:n  embed=1
embee6:n  embed=1
kcode 100 1.0 15 115
ksrc  0.0001 0.0001 0.0001
c sdef
c nps 100000
print
prdmp  2000  2000  1  2

