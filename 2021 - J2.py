#@author: Aanjneya

n = int(input())
name, bid = [],[]
for i in range(n):
    nm = input()
    bd = int(input())
    name.append(nm)
    bid.append(bd)
    
temp = max(bid) 
res = [i for i, j in enumerate(bid) if j == temp]

res.sort()

z = res[0]

print(name[z])