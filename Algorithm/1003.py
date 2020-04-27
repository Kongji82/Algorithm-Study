cache = [0] * 41
cache[1] = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif cache[n] != 0:
        return cache[n]
    else:
        cache[n] =  fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

N = int(input())

for i in range(N):
    num = int(input())
    fibonacci(num)    
    if num == 0:
        print(1, 0)
    else:
        print(cache[num-1], cache[num])
    