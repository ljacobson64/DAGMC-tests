PROBLEM K-code, assembly from ROMB-catalog (number 43)
c SNM parts
1  1 4.7832e-2 -1 20 -80  imp:n=1      $ bottom SNM
2  0             -20      imp:n=1      $ source cavity
3  0            1 -2 -80  imp:n=1      $ gap
4  2 4.7767e-2  2 50 -80  imp:n=1      $ top SNM
5  0             -50      imp:n=1      $ top axial hole
c
c Other parts
6  3 8.1133e-2 -70              imp:n=1      $ steel plate
8  3 8.1133e-2  80 -130         imp:n=1      $ steel diaphragm
11 0            -9   70 80 130  imp:n=1      $ inner void
12 0             9              imp:n=0      $ outer void

  1  pz  0.0
  2  pz  0.05
  9  so  15.0
 20  rcc 0.0 0.0 -1.0  0.0 0.0   1.0   0.6     $ source cavity
 50  rcc 0.0 0.0  0.05 0.0 0.0   5.17  1.75    $ top axial hole
 70  rcc 0.0 0.0 -6.17 0.0 0.0   0.21  9.8     $ steel plate
 80  rcc 0.0 0.0 -5.96 0.0 0.0  11.18  9.995   $ overall SNM cylinder area
130  rcc 0.0 0.0  0.05 0.0 0.0   0.21  13.0    $ diaphram (w/o hole)

mode   n
kcode  1000 1 50 150
ksrc   0 0 -2
m1     92235.50c 4.5774e-2 92238.50c 1.3381e-3 92234.50c 5.6597e-4
        6012.50c 1.0270e-4 26000.50c 5.0201e-5 74182.50c 3.2083e-7
       74183.50c 1.7420e-7 74184.50c 3.7451e-7 74186.50c 3.4889e-7
m2     92235.50c 4.5708e-2 92238.50c 1.3404e-3 92234.50c 5.6404e-4
        6012.50c 1.0256e-4 26000.50c 5.0131e-5 74182.50c 3.2041e-7
       74183.50c 1.7397e-7 74184.50c 3.7402e-7 74186.50c 3.4843e-7
m3     26000.50c 8.1133e-2
mesh   geom cyl
       ref    0.0   0.0  -1.001 $ just below lower void
       axs    0.0   0.0   1.0   
       vec    1.0   0.0   0.0
       origin 0.0   0.0  -5.96  $ bottom center
       imesh  0.6   1.75  9.995 
       iints  1     3     14
       jmesh  4.96 5.96  6.01  11.18
       jints  10   2     1     10
       kmesh  1.0
       kints  1
cut:n  1e6 1e-9
phys:n 20 1e-9
e0     1-6 1-3 20
f1:n   9
f4:n   1 4
dawwg xsec=ndilib points=10
