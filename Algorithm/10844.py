n = int(input())
step = [0 for i in range(n)]
step[0] = 9
step[1] = 17
for i in range(2, n):
    step[i] = (step[i-2] * 2) + step[i-1]
    
print(step[n-1])