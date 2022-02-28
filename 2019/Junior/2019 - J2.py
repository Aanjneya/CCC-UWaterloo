n = int(input())
intgr, strng = [],[]

for i in range(n):
    xint, xstr = input().split()
    intgr.append(int(xint))
    strng.append(xstr)
    
for z in range(n):
    print (intgr[z]*strng[z])
