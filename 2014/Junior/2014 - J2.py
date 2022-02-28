x = int(input())
l = input()

a = l.count("A")
b = l.count("B")

if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("Tie")
