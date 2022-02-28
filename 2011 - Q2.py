h = int(input("Enter the humidity factor:\n"))
m = int(input("Enter the time:\n"))

t = 1
a = -6*(t**4) + h*(t**3) + 2*(t**2) + t
    
while t < m and a > 0:
    t += 1
    a = -6*(t**4) + h*(t**3) + 2*(t**2) + t
if a>0:
    print("a")
else:
    print(t)
