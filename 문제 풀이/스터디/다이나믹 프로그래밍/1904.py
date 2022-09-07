import sys

input = sys.stdin.readline

N= int(input())

dp=[0]*(N+1)
print(N)
dp[1] = 1
dp[2] = 2

for i in range(3,N+1):
    dp[i] = (dp[i-1]*2 +dp[i-2])%15746
print(dp)
print(dp[N])