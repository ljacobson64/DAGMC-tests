Test for sampling of all reaction channels for point detector contributions.
c
c From: T. Booth and D. Verwaerde, "Benchmark Calculations", in Monte-Carlo 
c Methods and Applications in Neutronics, Photonics and Statistical Physics,
c R. Alcouffe, R. Dautray, A. Forster, G. Ledanois and B. Mercier, eds., 
c Springer-Verlag, Berlin (1985), p.432.
c
c
10 1 -1.0 -10               $ concrete
20 0 50 -60 30 -40          $ void for tally
30 0 10 -20 #20             $ void
40 0 20                     $ outside

10 RCC 0 0 0 0 0 400 20     $ concrete cylinder
20 RCC 0 0 -40 0 0 480 500  $ enclosing cylinder
30 cz 399.5
40 cz 400.5
50 pz 174.5 
60 pz 175.5 
 
imp:p 1 1 1 0
mode p
sdef par=2 pos=0 0 0.0000001  dir=1 vec=0 0 1 erg=d1 ara=1.0
sp1 -2 1.30 
c
c concrete 
m1   1000  0.006094
     8000  0.043421
     14000 0.01739
     13000 0.002686
     22000 0.001958
     26000 0.000334
c
f4:p 20
c 
f5:p 0 400 175 1
c
f15:p  400         0           175 1 $   0 degrees
f25:p  282.842712  282.842712  175 1 $  45 degrees
f35:p  0           400         175 1 $  90 degrees
f45:p -282.842712  282.842712  175 1 $ 135 degrees
f55:p -400         0           175 1 $ 180 degrees
f65:p -282.842712 -282.842712  175 1 $ 225 degrees
f75:p  0          -400         175 1 $ 270 degrees
f85:p  282.842712 -282.842712  175 1 $ 315 degrees
c ft15  pds 0 $ control point detector sampling
c ft25  pds 0 $ control point detector sampling
c ft35  pds 0 $ control point detector sampling
c ft45  pds 0 $ control point detector sampling
c ft55  pds 0 $ control point detector sampling
c ft65  pds 0 $ control point detector sampling
c ft75  pds 0 $ control point detector sampling
c ft85  pds 0 $ control point detector sampling
c
f95:p 0 400 175 1
c ft95 pds 1
c
f105:p 0 400 175 1
c ft105 pds 2
c
f125z:p 175 400    1
c
f135z:p 175 400    1
c ft135 pds 1
c
f145z:p 175 400    1
c ft145 pds 2
c
#    de0   df0
     0.01  2.78E-06
     0.015 1.11E-06
     0.02  5.88E-07
     0.03  2.56E-07
     0.04  1.56E-07
     0.05  1.20E-07
     0.06  1.11E-07
     0.08  1.20E-07
     0.10  1.47E-07
     0.15  2.38E-07
     0.20  3.45E-07
     0.30  5.56E-07
     0.40  7.69E-07
     0.50  9.09E-07
     0.60  1.14E-06
     0.80  1.47E-06
     1.00  1.79E-06
     1.50  2.44E-06
     2.00  3.03E-06
     3.00  4.00E-06
     4.00  4.76E-06
     5.00  5.56E-06
     6.00  6.25E-06
     8.00  7.69E-06
    10.00  9.09E-06
c
c dd 0
c dd15 0
nps 1e5
prdmp 2j -1
print
c    For backward compatability, set the first calculation of the
c  point detector average contribution at nps =  200
dbcn 66j 200
