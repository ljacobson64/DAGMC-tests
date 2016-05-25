UM Jezebel: Bare plutonium sphere w/nickel shell
c cells
1   1   4.0290e-2     0   u=1
2   2   9.1322e-2     0   u=1
3   3  -0.989352e-3   0   u=1
4   0                 0   u=1
5   0                -9   fill=1
9   0                 9

c surfaces
c 1  so 30
9  so 25

c data
m1    94239 3.7047e-2    94240 1.751e-3
      94241 1.17e-4      31000 1.375e-3
m2    28000 1.0
m3    7014 1.0
imp:n 1 1 1 1 1 0
mode n
kcode 10000 1.0 150 1150
ksrc  0.0001 0.0001 0.0001
print
prdmp  2000  2000  1  2
c abaqus embed
embed1  meshgeo=abaqus    mgeoin=abajez.inp 
         meeout=abajez.u gmvfile=abajez.g
         length=0.1   background=4
       filetype=ascii
        matcell=   1  1
                   2  2
                   3  3
c
c
c LNK3DNT generation stuff
mesh  geom sph
       ref      0.0   0.0   0.0
       origin   0.0   0.0   0.0
       imesh    3.19245 6.38493 8.0  $ radial zoning: 2 snm, 1 void
       iints    1   1       1        $  1 zone per radii
       jmesh   0.5  jints   1        $ angular zoning not supported
       kmesh   1.0  kints   1   
dawwg xsec=ndilib points=10
c

