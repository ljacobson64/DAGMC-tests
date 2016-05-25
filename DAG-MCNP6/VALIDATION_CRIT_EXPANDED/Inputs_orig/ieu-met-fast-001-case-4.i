Jemima  #4, Idealized Model; IEU-MET-FAST-001 Case 4
c Note ... no uranium fillers.
1 0 101 -180 -2
c Uranium disks (without fillers).
51 3 4.80510e-02 101 -103 2 -12
52 4 4.79730e-02 103 -106 2 -12
53 3 4.80510e-02 106 -108 2 -12
54 3 4.80510e-02 108 -109 2 -12
55 4 4.79730e-02 109 -112 2 -12
56 3 4.80510e-02 112 -114 2 -12
57 3 4.80510e-02 114 -115 2 -12
58 4 4.79730e-02 115 -118 2 -12
59 3 4.80510e-02 118 -120 2 -12
60 3 4.80510e-02 120 -121 2 -12
61 4 4.79730e-02 121 -124 2 -12
62 3 4.80510e-02 124 -126 2 -12
63 3 4.80510e-02 126 -127 2 -12
64 4 4.79730e-02 127 -130 2 -12
65 3 4.80510e-02 130 -132 2 -12
66 3 4.80510e-02 132 -133 2 -12
67 4 4.79730e-02 133 -136 2 -12
68 3 4.80510e-02 136 -138 2 -12
69 3 4.80510e-02 138 -139 2 -12
70 4 4.79730e-02 139 -142 2 -12
71 3 4.80510e-02 142 -144 2 -12
72 3 4.80510e-02 144 -146 2 -10 $** tailored Tu disk **
73 4 4.79730e-02 146 -149 2 -12
74 3 4.80510e-02 149 -151 2 -12
75 3 4.80510e-02 151 -153 2 -12
76 4 4.79730e-02 153 -155 2 -12
77 3 4.80510e-02 155 -157 2 -12
78 3 4.80510e-02 157 -159 2 -12
79 4 4.79730e-02 159 -161 2 -12
80 3 4.80510e-02 161 -163 2 -12
81 3 4.80510e-02 163 -165 2 -12
82 4 4.79730e-02 165 -167 2 -12
83 3 4.80510e-02 167 -169 2 -12
84 3 4.80510e-02 169 -171 2 -12
85 4 4.79730e-02 171 -173 2 -12
86 3 4.80510e-02 173 -175 2 -12
87 3 4.80510e-02 175 -177 2 -12
88 4 4.79730e-02 177 -179 2 -12
c Extra tuballoy on top (disk equiv. to six pies).
89 3 4.80510e-02 179 -180 2 -12
c Cells defining support structure below uranium disks.
103 1 6.02041e-02 144 -146 10 -17
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
121 0 (202 -180 12 -21) (-144: 146: 17) (101: 18)
122 0 205 -204 19 -21
123 0 206 -205 20 -21
c External cell.
200 0 -206: 180: 21

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
103 pz 0.604
106 pz 1.408
108 pz 2.012
109 pz 2.616
112 pz 3.420
114 pz 4.024
115 pz 4.628
118 pz 5.432
120 pz 6.036
121 pz 6.640
124 pz 7.444
126 pz 8.048
127 pz 8.652
130 pz 9.456
132 pz 10.060
133 pz 10.664
136 pz 11.468
138 pz 12.072
139 pz 12.676
142 pz 13.480
144 pz 14.084 $** parting plane **
146 pz 14.688
149 pz 15.492
151 pz 16.096
153 pz 16.700
155 pz 17.504
157 pz 18.108
159 pz 18.712
161 pz 19.516
163 pz 20.120
165 pz 20.724
167 pz 21.528
169 pz 22.132
171 pz 22.736
173 pz 23.540
175 pz 24.144
177 pz 24.748
179 pz 25.552
180 pz 26.005
c Horizontal planes defining structural support below uranium disks.
201 pz -0.3175
202 pz -0.9525
203 pz -3.1750
204 pz -4.7625
205 pz -6.0325
206 pz -8.5725

imp:n 1 54r 0
totnu
kcode 10000 1. 100 600
ksrc 8. 0. 01.006 0. 8. 01.006 -8. 0. 01.006 0. -8. 01.006
     8. 0. 03.018 0. 8. 03.018 -8. 0. 03.018 0. -8. 03.018
     8. 0. 05.030 0. 8. 05.030 -8. 0. 05.030 0. -8. 05.030
     8. 0. 07.042 0. 8. 07.042 -8. 0. 07.042 0. -8. 07.042
     8. 0. 09.054 0. 8. 09.054 -8. 0. 09.054 0. -8. 09.054
     8. 0. 11.066 0. 8. 11.066 -8. 0. 11.066 0. -8. 11.066
     8. 0. 13.078 0. 8. 13.078 -8. 0. 13.078 0. -8. 13.078
     8. 0. 15.090 0. 8. 15.090 -8. 0. 15.090 0. -8. 15.090
     8. 0. 17.102 0. 8. 17.102 -8. 0. 17.102 0. -8. 17.102
     8. 0. 19.114 0. 8. 19.114 -8. 0. 19.114 0. -8. 19.114
     8. 0. 21.126 0. 8. 21.126 -8. 0. 21.126 0. -8. 21.126
     8. 0. 23.138 0. 8. 23.138 -8. 0. 23.138 0. -8. 23.138
c      Materials specified with atom fractions
#ifdef ENDF7
m1   12024.  1.35073e-2     12025.  1.71000e-3  $ ENDF/B-VII.0
     12026.  1.88271e-3                         $ ENDF/B-VII.0
#else
m1   12000.  1.71000e-02                        $ ENDF/B-VI
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
m4   92234.  1.02504e-2     92235.  9.34915e-1
     92238.  5.48350e-2
prdmp  999999  999999  1  1  999999
