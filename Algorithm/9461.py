def p(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for j in range(6, n+1):
        dp[j] = dp[j-1] + dp[j-5]
    print(dp[n])
    
T = int(input())
for i in range(T):
    num = int(input())
    p(num)