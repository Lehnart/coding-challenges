import math

abcs = {}
for m in range(1,10) :
    for n in range(1,m):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2



        l = [a,b,c]
        l.sort()
        print (l)
        if a not in abcs :
            abcs[a] = {}
        if b not in abcs[a] :
            abcs[a][b] = []
        abcs[a][b].append(c)



m = 50
count = 0
for a in range(1,m+1):
    for b in range(a,m+1):

        if b not in abcs[a] : continue
        for c in range(b,m+1):


            #print("a " + str(a) + " b " + str(b) + " c " + str(c))

            if {a, b, c} not in abcs : continue

            l1 = math.sqrt( a**2 + (b+c)**2 )
            l2 = math.sqrt( b**2 + (a+c)**2 )
            l3 = math.sqrt( c**2 + (a+b)**2 )

            l = min(l1,l2,l3)
            if l == int(l) :
                count += 1

print("m " + str(m) + " count " + str(count))
