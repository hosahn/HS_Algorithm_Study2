import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    stack.append(list(map(int, sys.stdin.readline().split(" "))) + [1])
sub = [1]*(n+1)
stack.append(sub)

dp = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(0,n):
    for t in range(0,n):
        for k in range(0,3):
            if dp[k][i][t] > 0:
                if k == 0:
                    if stack[i][t+1] != 1:
                        dp[0][i][t+1] += dp[0][i][t]
                    if stack[i+1][t+1] != 1 and stack[i+1][t] != 1 and stack[i][t+1] != 1:
                        dp[2][i+1][t+1] += dp[0][i][t]
                elif k == 1:
                    if stack[i+1][t] != 1:
                        dp[1][i+1][t] += dp[1][i][t]
                    if stack[i+1][t+1] != 1 and stack[i+1][t] != 1 and stack[i][t+1] != 1:
                        dp[2][i+1][t+1] += dp[1][i][t]
                elif k == 2:
                    if stack[i][t + 1] != 1:
                        dp[0][i][t+1] += dp[2][i][t]
                    if stack[i + 1][t + 1] != 1 and stack[i+1][t] != 1 and stack[i][t+1] != 1:
                        dp[2][i+1][t+1] += dp[2][i][t]
                    if stack[i + 1][t] != 1:
                        dp[1][i+1][t] += dp[2][i][t]

if stack[n-1][n-1] == 1:
    print(0)
else:
    print(dp[0][n-1][n-1] + dp[2][n-1][n-1] + dp[1][n-1][n-1])