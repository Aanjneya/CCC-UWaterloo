n = int(input())
x, y = [], []
for i in range(n):
    xp, yp = input().split(',')
    x.append(int(xp))
    y.append(int(yp))
print(str(min(x)-1)+","+str(min(y)-1))
print(str(max(x)+1)+","+str(max(y)+1))
