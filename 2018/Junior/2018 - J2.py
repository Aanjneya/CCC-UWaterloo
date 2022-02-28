n = int(input())

yesterday = list(input())
today = list(input())

count = 0

for i in range(n):
    if yesterday[i] == today[i] == "C":
       count += 1
       
print(count)
