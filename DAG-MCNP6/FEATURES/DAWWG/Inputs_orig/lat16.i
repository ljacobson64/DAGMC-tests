lat16n -- Generate LNK3DNT from REGRESSION inp16
1 0  1:-3:-4:5:6:-7  imp:p=0
2  0  -2 3 4 -5 -6 7  imp:p=1  fill=1 (-25 0 0)
3     0  -1 2 4 -5 -6 7  imp:p=1  fill=2 (0 -20 0)
4     0  -11 12 -14 13  imp:p=1  lat=1  u=1 fill=3
5     0  -15 16 -18 17  imp:p=2  lat=1  u=2
c       interrupt card
         fill=0: &
1 0:3 0:0 4 4 4(5 0 0) 4 4 5 4 4
6     1 -.9  21:-22:-23:24  imp:p=1  u=3
7     1 -.9  19  imp:p=1  u=4
8     2 -18  -21 22 23 -24  imp:p=1  u=3
9     1 -.9  20(31:-32:-33:34) 9  imp:p=1  u=5
11    2 -18  -19  imp:p=1  u=4
12    1 -.9   -9  imp:p=1  u=5
13    2 -18  -20  imp:p=1  u=5
15    2 -18  -31 32 33 -34  imp:p=1  u=5
 
1     -3 px 50
2 px 0
3 -1 px -50
4     -5 p 0.00000000001 1 0.000 -20
5   -4 p 0.00000000001 1 0.000 20
6+    pz 60
7+    pz -60
9     s 5 5 3 .5
11    px 8.334
12    px -8.334
13    py -6.67
14    py 6.67
15    px 25.0000001
16    px -.0000001
17    py -.0000001
18    py 10.0000001
19    c/z 10 5 3
20    c/z 10 5 3
21    px 4
22    px -4
23    py -3
24    py 3
31    px 20
32    px 16
33    py 3
34    py 6

mesh  geom xyz
      ref  0 0 0 
      origin -50.000 -20.000 -60.000
      imesh  50
      iints  200
      jmesh  20
      jints  80
      kmesh  60
      kints  240
mode p 
m1    6012.50m .4 8016.50m .2 
m2    92238.50m .98  92235.50m .02
sdef  erg fcel d1  cel d6  x fcel d11  y fcel d13  z fcel d15 &
    rad fcel d17  ext fcel d19  pos fcel d21  axs fcel d23
ds1   s d2 d3 d4 d5
# sp2 sp3 sp4 sp5 &
-2 -2 -2 -2 &
     1.2 1.3 1.4 1.42 &
si6   s d7 d8 d9 d10
sp6   .65 .2 .1 .05
si7   l -2:4:8
sp7   1
si8   l 3:5(0 0 0):11 3:5(1 0 0):11 3:5(0 1 0):11 3:5(1 1 0):11
      3:5(0 2 0):11 3:5(0 3 0):11 3:5(1 3 0):11
sp8   1 1 1 1 1 1 1
si9   l 3:5(1 2 0):13
sp9   1
si10  l 3:5(1 2 0):15
sp10  1
ds11  s d12 0 0 d25
ds13  s d14 0 0 d26
ds15  s d16 0 0 d16
ds17  s 0 d18 d18 0
ds19  s 0 d20 d20 0
ds21  s 0 d22 d22 0
si22  l 10 5 0
sp22  1
ds23  s 0 d24 d44 0
si24  l 0 0 1 
sp24  1 
si44 s 45 46
sp44 .5 .5
si45 l 0 0 1
sp45 1
si46 l 1 1 1
sp46 1
# sp12 si12 si14 sp14 si16 sp16 si18 sp18 si20 sp20 si25 sp25 si26 sp26
0 -46 -17 0 -60 0 0 -21 -60 0 16 0 3 0
1 -4   17 1  60 1 3   1  60 1 20 1 6 1
f2:p  2
e2    .1 1 20
f6:p  2 4 6 8   7 11 12 13 15
sd6   1 1 1 1   1  1  1  1  1
print 10 70 128 170
fq6  f e
f5:p -48 -18 -58 0 
dxt:p 30 5 3 0.6 0.9
nps   2000
mgopt f 12
prdmp 2j -1
elpt:p 0 4r .05 .06 .05 .06 3r
phys:p 1
cut:p 30
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn  j  j  1  1  62j   200
