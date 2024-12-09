'''
Bucket Brigade

문제는 10x10 크기의 농장의 격자에서 "버킷 브리게이드"를 만들기 위한 최소 cow 수를 구하는 문제입니다. 버킷 브리게이드는 호수(Lake)와 헛간(Barn) 사이에 물통을 전달하는 경로를 만들기 위해 cow들이 필요한 최소한의 '.' 지점들을 차지해야 한다는 조건을 만족해야 합니다.

주요 조건:
B: 헛간(Barn) 위치.
L: 호수(Lake) 위치.
R: 바위(Rock) 위치. 이곳은 cow들이 지나갈 수 없다.
.: cow가 올 수 있는 빈 칸. 여기서 최소 cow들이 채워져야 합니다.

경로의 조건:
물통은 북, 남, 동, 서 방향으로만 이동할 수 있습니다.
호수 근처의 cow는 물통을 받을 수 있고, 헛간 근처의 cow는 물통을 던질 수 있습니다.
바위가 있는 곳은 cow가 지나갈 수 없으므로 경로에서 제외됩니다.

목표:
호수에서 물을 받아서 헛간에 물을 전달하는 경로를 만들 때, 최소한의 '.' 지점에 cow를 배치하여 경로를 형성해야 합니다.
헛간과 호수가 인접해 있지 않다는 보장이 있습니다.
해결하려는 문제:
이 문제는 호수(L)와 헛간(B) 사이의 최단 경로를 구하는 문제로, 빈 칸 ('.')에 cow들을 배치하여 두 지점 사이에 경로를 만들기 위한 최소 cow 수를 구하는 것입니다.
'''
import sys
from collections import deque

# 10x10 농장 그리드 입력
farm = [list(sys.stdin.readline().strip()) for _ in range(10)]
visited = [[False for _ in range(10)] for _ in range(10)]

# 이동 방향 (하, 우, 상, 좌)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# BFS 탐색 함수
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y, 0)])  # (x, y, cnt)
    visited[start_x][start_y] = True  # 시작 지점 방문 처리

    while queue:
        x, y, cnt = queue.popleft()

        # 호수(Lake) 지점에 도달했을 때
        if farm[x][y] == "L":
            return cnt  # 바로 cnt 값을 반환하여 종료

        # 네 방향으로 이동
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            # 범위 내에 있고, 방문하지 않았고, 바위가 아니면
            if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and farm[nx][ny] != "R":
                visited[nx][ny] = True
                # 빈 칸일 경우 카운트 증가
                if farm[nx][ny] == ".":
                    queue.append((nx, ny, cnt + 1))
                else:
                    queue.append((nx, ny, cnt))

# 헛간(Barn) 위치 찾기
for i in range(10):
    for j in range(10):
        if farm[i][j] == "B":
            print(bfs(i, j))
            break
