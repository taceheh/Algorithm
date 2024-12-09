'''
바이러스

입력 : vertex -> 컴퓨터의 수
       edge -> 연결되어 있는 컴퓨터 쌍의 수
       a, b -> 연결되어 있는 컴퓨터 쌍 a, b

       1번 컴퓨터가 바이러스에 걸렸을 때 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수
'''

import sys
from collections import deque

vertex = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

# 안되는 이유
# 빈리스트 하나만 만들어짐
# tree = [[]* (vertex+1)]
tree = [[] for _ in range(vertex+1)]
visited =[False]* (vertex+1)

for _ in range(edge):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(start):
    visited[start]=True
    queue = deque([start])
    cnt =0

    while queue :
        x = queue.popleft()

        for t in tree[x]:
            if not visited[t]:
                visited[t]=True
                queue.append(t)
                cnt+=1
    print(cnt)


bfs(1)
