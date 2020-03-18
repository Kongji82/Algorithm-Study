N = int(input())
num = 0
for i in range(N+1):
    for j in range(i+1):
        num += (i+j)
print(num)