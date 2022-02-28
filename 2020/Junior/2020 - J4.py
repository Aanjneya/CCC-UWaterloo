t = input()
s = input()
#cl = []
ans = "no"
#for i in range(len(s)):
 #   if s in t:
  #      ans = "yes"
   #     break
    #s = s[-1] + s[:-1]
#print(ans)
for i in range(len(s)):
    if s in t:
        ans="yes"
    else:
        s1 = s[1:]
        s2 = s[0]
        s=s1 + s2

print(ans)