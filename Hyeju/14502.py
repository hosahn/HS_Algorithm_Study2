import sys
from collections import deque
from itertools import combinations
import copy

N, M = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
v = [(i, j) for i in range(N) for j in range(M) if Map[i][j] == 2]
dq = deque(v)
e = [(i, j) for i in range(N) for j in range(M) if Map[i][j] == 0]
cases = list(combinations(e, 3))
ans = []
for case in cases:
    m = copy.deepcopy(Map)
    q = copy.deepcopy(dq)
    for i, j in case:
        m[i][j] = 1
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < N and 0 <= y < M and m[x][y] == 0:
                m[x][y] = 2
                q.append((x, y))
    ans.append(sum(row.count(0) for row in m))
print(max(ans))