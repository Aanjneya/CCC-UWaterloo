P = int(input()) # The total people count on final day
N = int(input()) # Diseased on day 0
R = int(input()) # Rate of infection

count = 0

infected  = N
people = N

while True:
    people = people + infected*R
    infected = infected * R
    count += 1
    if people >= P :
        if people == P:
            print (count + 1)
        else:
            print (count)
   
        break
    
