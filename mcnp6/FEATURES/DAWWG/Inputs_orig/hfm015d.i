PROBLEM K-code, assembly from ROMB-catalog (number 43)
c SNM parts
10 0             0     u=e10   imp:n=1 $ mesh voids
11 1 4.7832e-2   0     u=e10   imp:n=1 $ lower SNM in mesh
12 2 4.7767e-2   0     u=e10   imp:n=1 $ upper SNM in mesh
13 0             0     u=e10   imp:n=1 $ background
20 0           -80  fill=e10   imp:n=1 $ container RCC
c Other parts
6  3 8.1133e-2 -70              imp:n=1 $ bottom steel plate
8  3 8.1133e-2  80 -130         imp:n=1 $ middle steel diaphragm
c rest of the universe
30 0            -9   70 80 130  imp:n=1 $ inner void
40 0             9              imp:n=0 $ outer void

  9  so  15.0
c rccs shifted to align with embedded mesh
 70  rcc 0.0 0.0 -5.80  0.0 0.0   0.21   9.8     $ bottom steel plate
 80  rcc 0.0 0.0 -5.589 0.0 0.0  11.178  9.994   $ overall SNM cylinder area
130  rcc 0.0 0.0  0.41  0.0 0.0   0.21  13.0     $ diaphram (w/o hole)

mode   n
prdmp 4j 8000
kcode  1000 1 50 150
ksrc   0 0 -2
m1     92235.50c 4.5774e-2 92238.50c 1.3381e-3 92234.50c 5.6597e-4
        6012.50c 1.0270e-4 26000.50c 5.0201e-5 74182.50c 3.2083e-7
       74183.50c 1.7420e-7 74184.50c 3.7451e-7 74186.50c 3.4889e-7
m2     92235.50c 4.5708e-2 92238.50c 1.3404e-3 92234.50c 5.6404e-4
        6012.50c 1.0256e-4 26000.50c 5.0131e-5 74182.50c 3.2041e-7
       74183.50c 1.7397e-7 74184.50c 3.7402e-7 74186.50c 3.4843e-7
m3     26000.50c 8.1133e-2
cut:n  1e6 1e-9
phys:n 20 1e-9
e0     1-6 1-3 20
f1:n   9
f4:n   11 12
sd4    1839.3863 1572.8384
embed10 meshgeo=lnk3dnt mgeoin=HFM015.linkout debug=echomesh
        calc_vols=yes
        matcell= 0 10 1 11 2 12
        background=13

