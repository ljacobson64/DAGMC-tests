Conical Test Problem to create a LNK3DNT mesh
c --------------------------------------------------------------------
c CELL CARDS
1    101 -18.0  -1 10       imp:p=1 $ W sphere
2    101 -18.0  -2 11       imp:p=1 $ W sphere
3    101 -18.0  -3 12       imp:p=1 $ W sphere
4    103 -2.7   (1 2 3) -4  imp:p=1 $ Al cone
5    104 -7.8   -5          imp:p=1 $ SS sphere for orientation
6    105 -1.0e-3 4 5 -98    imp:p=1 $ air
10     0        -1 -10      imp:p=1 $ W void
11     0        -2 -11      imp:p=1 $ W void
12     0        -3 -12      imp:p=1 $ W void
80   105 -1.0e-3 98 -99     imp:p=1
99     0             99     imp:p=0

c --------------------------------------------------------------------
c SURFACE CARDS
1    so    1.0
2    sz    2.5  1
3    sz   -2.5  1
4   trc    0    0   -5    0 0 10   2.5 5
5     s    5    5    5    1
10  c/x    0    0    0.5
11  c/x    0    2.5  0.75
12  c/x    0   -2.5  0.25
98   so  900
99   so 1000

c --------------------------------------------------------------------
c DATA CARDS
c --------------------------------------------------------------------
c MATERIAL CARDS
m101   74184 1.000000 $ W
m103   13027 1.000000 $ Al
m105    7014 0.770900  8016 0.219500 18000 0.009600 $ air
m104   26056 0.698000 24052 0.206000 28058 0.096000 $  SS
c
c --------------------------------------------------------------------
c SOURCE: CARDS
c --------------------------------------------------------------------
mode p
phys:p j 0 0
cut:p j 0.1
sdef pos -133 0. 0.
     vec    1 0  0
c
c --------------------------------------------------------------------
c TALLY CARDS
fc5 Sample Radiograph
c         x   y   z    R   x2 y2 z2  f1 f2 f3
fir5:p   392  0.  0.   0   0. 0. 0.  0  0  0 
fs5 0 224i 22.5    $ 0.1cm radiographic grid
c5  0 224i 22.5    $ 0.1cm radiographic grid
talnp 5                $ don't print tally bins
c
c --------------------------------------------------------------------
c GENERAL CARDS
nps 1                  $ histories
notrn                  $ ray trace
prdmp j 1 -1 2          $ dump control
print                  $ make some output!
c
c --------------------------------------------------------------------
c LNK3DNT FILE MESH CARDS
mesh  geom xyz origin=-6 -6 -6  ref=0 0 0 
       imesh 6
       iints 60
       jmesh 6
       jints 60
       kmesh 6
       kints 60
dawwg points=5 xsec=ndilib

