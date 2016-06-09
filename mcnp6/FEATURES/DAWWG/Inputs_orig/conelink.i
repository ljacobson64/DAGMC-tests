Conical Test Problem to create a LNK3DNT mesh
c --------------------------------------------------------------------
c CELL CARDS
10        0              0    u=e10  imp:p=1 $ void elements
1000    101 -18.0        0    u=e10  imp:p=1 $ W sphere
2000    103 -2.7         0    u=e10  imp:p=1 $ Al cone
4000    104 -7.8         0    u=e10  imp:p=1 $ SS sphere for orientation
3000    105 -1.0e-3      0    u=e10  imp:p=1 $ air
20      105 -1.0e-3      0    u=e10  imp:p=1 $ air (background) 
5000      0            -98 fill=e10  imp:p=1 $ fill cell
c
6000    105 -1.0e-3     98 -99       imp:p=1 $ air shell around fill cell
9999      0             99           imp:p=0 $ outer void

c --------------------------------------------------------------------
c SURFACE CARDS
98   so  12  $ just large enough to hold the mesh
99   so 400  $ just large enough to contain the source and image plane

c --------------------------------------------------------------------
c DATA CARDS
c --------------------------------------------------------------------
c MATERIAL CARDS
m101   74184 1.000000                               $ W
m103   13027 1.000000                               $ Al
m104   26056 0.698000 24052 0.206000 28058 0.096000 $ stainless
m105    7014 0.770900  8016 0.219500 18000 0.009600 $ air
c
c --------------------------------------------------------------------
c SOURCE: CARDS
c --------------------------------------------------------------------
mode p
phys:p j 0 0
cut:p j 0.1
sdef pos -133 0. 0.
     vec    1 0  0
c --------------------------------------------------------------------
c TALLY CARDS
fc5 Sample Radiograph
fir5:p   392                   0.  0.   0   0. 0. 0.  0 0 0 
fs5 0 224i 22.5
c5  0 224i 22.5        $ radiographic grid
talnp 5                $ don't print tally bins
c
nps 1                  $ histories
notrn                  $ ray trace
prdmp j 1 -1 2          $ dump control
print                  $ make some output!
c
c for LNK3DNT file embed
embed10 meshgeo    = lnk3dnt
        mgeoin     = cone.linkout
        calc_vols  = yes
        matcell    = 0 10
                     1 1000
                     2 2000
                     3 3000
                     4 4000
        background = 20
        debug=echomesh
