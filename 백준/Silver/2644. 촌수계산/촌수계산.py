'''
부모와 자식 사이 : 1촌
할아버지와 손자 : 2촌
나와 아버지의 형제들 : 3촌

첫째 줄에는 전체 사람의 수 n이 주어지고, 
둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

x(부모) y(자식)

각 사람의 부모는 최대 한 명만 주어진다.

목표
두번째 줄에서 입력받은 x와 y가 몇촌관계인지 구하는 문제

** SUDO CODE 
1 BFS < -  
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람의 수 n
a,b = map(int,input().split()) # 정점 a,b : 둘의 거리는
m = int(input()) # 부모-자식 관계의 수 m 

graph = [[] for _ in range(n+1)]

for i in range(1,m+1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)

# 촌수의 거리는? 
# distance = 1
res=[0]*(n+1)
# [0 0 0 0 0 0 0 0 0 0]

def bfs(start):
    global distance
    queue = deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()

        for g in graph[v]:
            if not visited[g]:
                queue.append(g)
                #distance+=1 
                res[g]=res[v]+1
                # print(res)
                visited[g] = True

bfs(a)

if res[b]>0:
    print(res[b])
else:
    print(-1)