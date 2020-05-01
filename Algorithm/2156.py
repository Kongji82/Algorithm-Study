n = int(input())
wine = [int(input()) for x in range(n)]

dp = [0]
dp.append(wine[0])
if n > 1:
    dp.append(wine[0] + wine[1])
    
for i in range(3, n+1):
    case_1 = wine[i-1] + dp[i-2]
    case_2 = wine[i-1] + wine[i-2] + dp[i-3]
    case_3 = dp[i-1]
    value = max(case_1, case_2, case_3)
    
    dp.append(value)
    
print(dp[n])