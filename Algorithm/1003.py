fibo = [0] * 41
fibo[0] = 0
fibo[1] = 1
for i in range(2, 41):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
print(len(fibo))
    
# N = int(input())
# for _ in range(N):
#     num = int(input())
#     fibonacci(num)