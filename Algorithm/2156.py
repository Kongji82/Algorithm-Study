N = int(input())
grape = [0 for i in range(10001)]
dp = [0 for i in range(10001)]
for i in range(N):
    grape[i] = int(input())

dp[0] = grape[0]
dp[1] = grape[0] + grape[1]
dp[2] = max(grape[1] + grape[2] , grape[0] + grape[2])
for i in range(3, N):
    dp[i] = max(dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i])
    
print(max(dp))