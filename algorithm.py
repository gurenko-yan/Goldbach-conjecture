n = int(input())

l = [0,0]

for x in range(2, n, 1):
    for i in range(1, x, 1):
        if x%i == 0 and i != 1:
            break
        
        if i == x-1:
            for j in range(2, n-x+1, 1):
                if (n-x)%j == 0 and n-x != j:
                    break

                if j == n-x:
                    l = [x,j]
    
    if l != [0,0]:
        print(l[0], l[1])
        break