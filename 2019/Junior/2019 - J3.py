n = int(input()) 
line = []

count = 0
counta = count+1

for i in range(n):
   line.append(input()) 
   
for z in range(n):
    for j in range(len(line[z])):
        if line[z][count] == line[z][counta]:
           count += 1
        elif line[z][count] != line[z][counta]:
            char = line[z][count]
            countof_char = line[z][count].count(char)
            print(str(countof_charchar) + " " + str(char))
            break
                
