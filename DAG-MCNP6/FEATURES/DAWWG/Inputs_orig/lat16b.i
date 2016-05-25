lat16b -- plot of lattice generated LNK3DNT
 1  1  -0.9  0    u=e10 imp:n=1
 2  2 -18.0  0    u=e10 imp:n=1
 3  0        0    u=e10 imp:n=1
 4  0       -1 fill=e10 imp:n=1
 5  0        1          imp:n=0

 1 so  100

 mode p
 nps  1
 m1     6012 .40   8016 .20 
 m2    92238 .98  92235 .02
 embed10 meshgeo=lnk3dnt mgeoin=lat16.linkout debug=echomesh
         matcell= 0 3 1 1 2 2
         background= 3
         calc_vols=yes

end of input
