'''
백준 1012 유기농 배추

입력 : t -> 테스트 케이스
       m,n,k -> 배추밭의 가로길이, 세로길이, 배추 개수
       k줄 -> 배추의 위치
'''

import sys
from collections import deque

t = int(sys.stdin.readline())  # 테스트 케이스 개수
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상하좌우 방향 벡터

# BFS 함수 정의
def bfs(x, y, m, n):
    queue = deque([(x, y)])
    visited[y][x] = True  

    while queue:
        x1, y1 = queue.popleft()
        for dx, dy in d:
            nx, ny = x1 + dx, y1 + dy 
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny))

for _ in range(t):

    m, n, k = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]


    for _ in range(k):
        w, h = map(int, sys.stdin.readline().split())
        graph[h][w] = 1  # h가 행(세로), w가 열(가로)

    cnt = 0
    for i in range(n):  # 세로 (y 방향)
        for j in range(m):  # 가로 (x 방향)
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(j, i, m, n)  
                cnt += 1  

    print(cnt)
