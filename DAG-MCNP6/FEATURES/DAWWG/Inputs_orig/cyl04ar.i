 Generate a LNK3DNT r-z-t mesh w/ multiple materials
c upper-inner
1   1   -9.85         -11  1  2  3     imp:n=1
2   1   -9.85         -11  1 -2  3     imp:n=1
3   1   -9.85         -11 -1 -2  3     imp:n=1
4   1   -9.85         -11 -1  2  3     imp:n=1 
c upper-outer
6   1   -9.85      -10 11  1  2  3     imp:n=1
7   1   -9.85      -10 11  1 -2  3     imp:n=1
8   1   -9.85      -10 11 -1 -2  3     imp:n=1
9   1   -9.85      -10 11 -1  2  3     imp:n=1 
c lower-inner
11  1   -9.85         -11  1  2 -3     imp:n=1
12  1   -9.85         -11  1 -2 -3     imp:n=1
13  1   -9.85         -11 -1 -2 -3     imp:n=1
14  1   -9.85         -11 -1  2 -3     imp:n=1 
c lower-outer
16  1   -9.85      -10 11  1  2 -3     imp:n=1
17  1   -9.85      -10 11  1 -2 -3     imp:n=1
18  1   -9.85      -10 11 -1 -2 -3     imp:n=1
19  1   -9.85      -10 11 -1  2 -3     imp:n=1 
c container
20  0               10 -4              imp:n=1
c outer void
21  0                   4              imp:n=0

10  rcc  0. 0. -10. 0. 0. 20. 10. $ outer rcc
11  rcc  0. 0. -10. 0. 0. 20.  5. $ inner rcc
1   py   0.0                       
2   px   0.0
3   pz   0.0
4   so   20

vol 196.35 3r 589.049 3r 196.35 3r 589.049 3r j
kcode     500     1.0  50   100
ksrc 1 1  5 1 -1  5 -1 -1  5 -1 1  5
     5 5  5 5 -5  5 -5 -5  5 -5 5  5
     1 1 -5 1 -1 -5 -1 -1 -5 -1 1 -5
     5 5 -5 5 -5 -5 -5 -5 -5 -5 5 -5
totnu no
m1        92235.69c  -18.7 6012 -1
dm1 92235 92235.50
prdmp    j    275
print

end of input
