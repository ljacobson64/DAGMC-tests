Conical Test Problem
c
c This simple MCNP problem is intended to illustrate
c several radiographic projections.
c
c 05 Jan 2010
c Erik F. Shores
c Duane P. Flamig
c John D. Zumbro
c
c file = cone ; 05 Jan 10 ; problem creation
c --------------------------------------------------------------------
c CELL CARDS
c --------------------------------------------------------------------
10        0         0 u=e10 imp:p=1 $ void elements
1000    101 -18.0   0 u=e10 imp:p=1 $ W sphere
2000    103 -2.7    0 u=e10 imp:p=1 $ Al cone
4000    104 -7.8    0 u=e10 imp:p=1 $ SS sphere for orientation
3000    105 -1.0e-3 0 u=e10 imp:p=1 $ air
5000      0    -98 fill=e10 imp:p=1
6000      0     98 -99      imp:p=1  
9999      0     99          imp:p=0
c end cells with blank space
c --------------------------------------------------------------------

c --------------------------------------------------------------------
c SURFACE CARDS
c --------------------------------------------------------------------
1    so    1.0
2    sz    2.5  1
3    sz   -2.5  1
4   trc    0    0   -5    0 0 10   2.5 5
5     s    5    5    5    1
10  c/x    0    0    0.5
11  c/x    0    2.5  0.75
12  c/x    0   -2.5  0.25
98   so   50
99   so  1000
c end surfaces with blank space
c --------------------------------------------------------------------

c --------------------------------------------------------------------
c DATA CARDS
c --------------------------------------------------------------------
c -8 degree rotation about y (up)*
tr3   0.                  0.        0.
      0.99026806874157036 0.       -0.13917310096006544
      0.                  1.        0.
      0.13917310096006544 0.        0.99026806874157036 1
c
c --------------------------------------------------------------------
c MATERIAL CARDS
c --------------------------------------------------------------------
m101   74184 1.000000 $ W
m103   13027 1.000000 $ Al
m102   73181 1.000000 $ Ta
m105    7014 0.770900  8016 0.219500 18000 0.009600 $ air
c mpn105  7014 8016 18040
m104   26056 0.698000 24052 0.206000 28058 0.096000 $  SS
m106   71175 2.000000 14028 1.000000 8016 5.000000  $ LSO
mpn106 73181 14028 8016
c
c --------------------------------------------------------------------
c SOURCE: CARDS
c --------------------------------------------------------------------
mode p
phys:p j 0 0
cut:p j 0.1
sdef pos -133 0. 0.
     vec    1 0  0
c sdef pos -131.70565314262884726 0.  -18.51002242768870332 $ small end to source
c      vec 0.99026806874157036    0.    0.13917310096006544 
c sdef pos -131.70565314262884726 0.   18.51002242768870332 $ large end to source
c      vec 0.99026806874157036    0.   -0.13917310096006544
c
c --------------------------------------------------------------------
c TALLY CARDS
c --------------------------------------------------------------------
fc5 Sample Radiograph
fir5:p   392                   0.  0.   0   0. 0. 0.  0 0 0 
c fir5:p 388.18508294559555880 0.  54.55585557534554954
c                                       0   0. 0. 0.  0 0 0 $ small end to source
c firS:p 388.18508294559555880 0. -54.55585557534554954
c                                       0   0. 0. 0.  0 0 0 $ large end to source
fs5 -22.48 1123i 22.48
c5  -22.48 1123i 22.48 $ radiographic grid
talnp 5                $ don't print tally bins
nps 1                  $ histories
notrn                  $ ray trace
prdmp j 1 1 2          $ dump control
print                  $ make some output!
c
c for LNK3DNT file creation
c mesh  geom xyz origin=-8 -8 -8  ref=0 0 0 
c        imesh 8
c        iints 80
c        jmesh 8
c        jints 80
c        kmesh 8
c        kints 80
c dawwg points=10 xsec=ndilib
c
embed10 meshgeo    = lnk3dnt
        mgeoin     = efslinktest
        matcell    = 0 10
                     1 1000
                     2 2000
                     3 3000
                     4 4000
        background = 4000








Converting MCNP Geometry to LNK3DNT Mesh
                       Start time =  07/20/11 15:37:29 

 Done with conversion of MCNP Geometry to LNK3DNT Mesh
                       End time =  07/20/11 15:46:05 


The ORDERED list of materials written to the LNK3DNT file is:
                                             void; material index #       0
   index #    1 listed as material card #     101; material index #       1
   index #    2 listed as material card #     103; material index #       2
   index #    3 listed as material card #     105; material index #       3
   index #    4 listed as material card #     104; material index #       4
