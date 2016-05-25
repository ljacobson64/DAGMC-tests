Jemima #2, Idealized Model; IEU-MET-FAST-001 Case 2
c Note ... no uranium fillers.
1 0 101 -148 -2
c Uranium disks (without fillers).
51 4 4.79558e-02 101 -105 2 -12
52 3 4.80510e-02 105 -106 2 -12
53 4 4.79558e-02 106 -109 2 -12
54 3 4.80510e-02 109 -110 2 -12
55 4 4.79558e-02 110 -113 2 -12
56 3 4.80510e-02 113 -114 2 -12
57 4 4.79558e-02 114 -117 2 -12
58 3 4.80510e-02 117 -118 2 -12
59 4 4.79558e-02 118 -121 2 -12
60 3 4.80510e-02 121 -122 2 -12
61 4 4.79558e-02 122 -125 2 -12
62 3 4.80510e-02 125 -126 2 -12
63 4 4.79558e-02 126 -129 2 -12
64 3 4.80510e-02 129 -131 2 -10 $** tailored Tu disk **
65 4 4.79558e-02 131 -134 2 -12
66 3 4.80510e-02 134 -136 2 -12
67 4 4.79558e-02 136 -138 2 -12
68 3 4.80510e-02 138 -140 2 -12
69 4 4.79558e-02 140 -142 2 -12
70 3 4.80510e-02 142 -144 2 -12
71 4 4.79558e-02 144 -146 2 -12
72 3 4.80510e-02 146 -148 2 -12
c Note ... no extra tuballoy on top for this configuration.
c Cells defining support structures for uranium disks.
103 1 6.02041e-02 129 -131 10 -17
106 0 201 -101 -8
107 0 202 -201 3 -8
108 1 6.02041e-02 202 -101 8 -18
110 1 6.02041e-02 203 -201 -3
111 1 6.02041e-02 205 -203 -7
112 1 6.02041e-02 204 -202 12 -14
113 0 (204 -202 3 -12) (203: 7)
114 0 204 -202 14 -21
118 1 6.02041e-02 205 -204 11 -19
119 0 205 -204 7 -11
120 2 8.63195e-02 206 -205 -20
121 0 (202 -148 12 -21) (-129: 131: 17) (101: 18)
122 0 205 -204 19 -21
123 0 206 -205 20 -21
c External cell.
200 0 -206: 148: 21

c Cylindrical surfaces defining uranium disks and surrounding supports.
2 cz 1.11125 $** inner radius of uranium disks **
3 cz 1.74625 $** rad. of upper Al filler support cylinder **
7 cz 4.60375 $** rad. of lower Al filler support cylinder **
8 cz 12.06500 $** inner radius of lower Al support ring **
10 cz 12.66939 $** idlzd. Tu/Al bndry in upper supp. ring **
11 cz 12.70000 $** o.r. unique Tu disk; i.r. spacer platform **
12 cz 13.33500 $** outer radius of uranium disks **
14 cz 13.67711 $** outer rad. of idealized Al rect. spacers **
17 cz 15.29416 $** outer edge of idlzd. Al upper supp. ring **
18 cz 15.82055 $** outer rad. of idealized lower Al ring **
19 cz 17.19650 $** outer rad. of idealized Al platform spacer **
20 cz 19.22627 $** rad. of cyl. equiv. to 12"x15" Fe plate **
21 cz 21.00000 $** inner rad. ext. cell (idealized models) **
c Horizontal planes defining uranium disks and fillers.
101 pz 0.000 $** lower surface of bottom uranium disk **
105 pz 0.804
106 pz 1.408
109 pz 2.212
110 pz 2.816
113 pz 3.620
114 pz 4.224
117 pz 5.028
118 pz 5.632
121 pz 6.436
122 pz 7.040
125 pz 7.844
126 pz 8.448
129 pz 9.252 $** parting plane **
131 pz 9.856
134 pz 10.660
136 pz 11.264
138 pz 12.068
140 pz 12.672
142 pz 13.476
144 pz 14.080
146 pz 14.884
148 pz 15.488
c Horizontal planes defining structural support below uranium disks.
201 pz -0.3175
202 pz -0.9525
203 pz -3.1750
204 pz -4.7625
205 pz -6.0325
206 pz -8.5725

imp:n 1 37r 0
totnu
kcode 10000 1. 100 600
ksrc 8. 0. 00.402 0. 8. 00.402 -8. 0. 00.402 0. -8. 00.402
     8. 0. 01.810 0. 8. 01.810 -8. 0. 01.810 0. -8. 01.810
     8. 0. 03.218 0. 8. 03.218 -8. 0. 03.218 0. -8. 03.218
     8. 0. 04.626 0. 8. 04.626 -8. 0. 04.626 0. -8. 04.626
     8. 0. 06.034 0. 8. 06.034 -8. 0. 06.034 0. -8. 06.034
     8. 0. 07.442 0. 8. 07.442 -8. 0. 07.442 0. -8. 07.442
     8. 0. 08.850 0. 8. 08.850 -8. 0. 08.850 0. -8. 08.850
     8. 0. 10.258 0. 8. 10.258 -8. 0. 10.258 0. -8. 10.258
     8. 0. 11.666 0. 8. 11.666 -8. 0. 11.666 0. -8. 11.666
     8. 0. 13.074 0. 8. 13.074 -8. 0. 13.074 0. -8. 13.074
     8. 0. 14.482 0. 8. 14.482 -8. 0. 14.482 0. -8. 14.482
c      Materials specified with atom fractions
#ifdef ENDF7
m1   12024.  1.35073e-2     12025.  1.71000e-3   $ ENDF/B-VII.0
     12026.  1.88271e-3                          $ ENDF/B-VII.0
#else
m1   12000.  1.71000e-02                         $ ENDF/B-VI
#endif
     13027.  9.61193e-1
     25055.  2.52173e-3
     29063.  1.32704e-2     29065.  5.91480e-3
m2   24050.  8.32154e-3     24052.  1.60475e-1
     24053.  1.81944e-2     24054.  4.52945e-3
     26054.  4.32510e-2     26056.  6.72370e-1
     26057.  1.53944e-2     26058.  2.05259e-3
     28058.  5.14835e-2     28060.  1.96824e-2
     28061.  8.52151e-4     28062.  2.70728e-3
     28064.  6.86246e-4
m3   92234.  5.50000e-5     92235.  7.20000e-3
     92238.  9.92745e-1
m4   92234.  1.02505e-2     92235.  9.34717e-1
     92238.  5.50328e-2
prdmp  999999  999999  1  1  999999
