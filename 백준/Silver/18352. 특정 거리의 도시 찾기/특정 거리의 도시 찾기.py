'''
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
'''
from collections import deque
import sys

n,m,k,x = map(int,sys.stdin.readline().split())

city = [[] for _ in range(n+1)]
visited = [False] *(n+1)

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    city[a].append(b)




def bfs(start):
    visited[start]=True
    queue= deque([(start,0)])
    result=[]

    while queue:
        node,distance = queue.popleft()
        if distance==k:
            result.append(node)
        elif distance<k:
            for c in city[node]:
                if visited[c]==False:
                    visited[c] = True
                    queue.append((c,distance+1))
    
    if result:
        for r in sorted(result):
            print(r)
    else:
        print(-1)


bfs(x)