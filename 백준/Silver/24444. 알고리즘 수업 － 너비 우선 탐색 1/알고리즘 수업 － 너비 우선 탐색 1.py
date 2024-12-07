import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())

'''
n+1로 하는 이유
문제에서 노드 번호는 항상 1 이상이기 때문에
0번 인덱스는 쓰이지 않아도 1번노드의 인접 노드 graph[1]로 바로 접근 가능하기 때문 
-> 편의성 때문에 
[
[],
[],
[],
[],
[],
[]
]
'''


graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, len(graph)):
    graph[i].sort()

def BFS(start):
    queue = deque([start])
    visited = [False]*(N+1)
    result = [0]*(N+1) # result[idx]는 idx노드를 방문한 순서 값을 의미함
    cnt = 1 # 방문 순서 값
    
    while queue:
        cnt_node = queue.popleft()

        if visited[cnt_node] :
            continue
        
        visited[cnt_node] = True
        
        # 방문 순서 값 저장
        result[cnt_node] = cnt
        cnt += 1
        
        # 아직 방문 이력 없으면(=스택에서 뽑은 적 없으면)
        # 스택에 싹 다 집어 넣기
        for adj_node in graph[cnt_node]:
            if not visited[adj_node]:
                queue.append(adj_node)
    
    return result

result = BFS(R)
    
print(*result[1:], sep="\n")
