from collections import deque

# 입력
row, col = map(int, input().split())
area = [list(input()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

# 이동 방향
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 전체 양과 늑대의 수를 누적할 변수
total_v, total_k = 0, 0

# BFS 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    v, k = 0, 0  # 현재 영역의 늑대(v)와 양(k) 개수

    while queue:
        cx, cy = queue.popleft()
        
        # 현재 위치의 양/늑대 수 갱신
        if area[cx][cy] == "v":
            v += 1
        elif area[cx][cy] == "k":
            k += 1

        # 이동 가능한 방향 탐색
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and area[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return v, k

# 전체 영역 탐색
for i in range(row):
    for j in range(col):
        if not visited[i][j] and area[i][j] != '#' and area[i][j] != '.':
            # 새로운 울타리 영역 탐색 시작
            v, k = bfs(i, j)
            # 조건에 따라 살아남은 양/늑대 누적
            if v >= k:
                total_v += v
            else:
                total_k += k

print(total_k, total_v)
