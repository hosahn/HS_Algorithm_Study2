'''
[연속합]
- 순차적으로 연속합을 해당 인덱스 위치의 dp에 저장
- 순차적으로 가다가 합이 0보다 작아질 때까지 각 인덱스까지의 합을 dp에 저장
- for문으로 가다가 양의 수를 만나면 순차적으로

[10, -4, 3,  1,  5,  6, -35, 12, 21, -1] = 원래 수열
[10,  6, 9, 10, 14, 20, -15, 12, 33, 32] = dp
'''

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]] + [0] * (n-1) # 첫번째 수 넣고 생성

for i in range(1, n):
    if dp[i-1] < 0: # 직전 순차합이 0보다 작을 경우
        dp[i] = nums[i] # 현재 인덱스의 값을 그대로 저장
        continue
    
    dp[i] = dp[i-1] + nums[i]
        
print(max(dp))