'''
백준 1697 숨바꼭질

동생의 위치 k 
수빈이의 위치 x

걸었을 때 x+1
순간이동 2*x

입력 : n, k -> 수빈이의 위치, 동생의 위치

출력 : 4
'''
import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())

visited = [False]*100001


def bfs(start,end):
    queue = deque([(start,0)])
    visited[start] = True

    while queue:
        x,cnt= queue.popleft()
        # d=[x+1,2*x,x-1]

        if x==end:
            return cnt
        

        for nx in (x+1,2*x,x-1):
            if 0<= nx < 100001 and not visited[nx]:
                visited[nx]=True
                queue.append((nx,cnt+1))

print(bfs(n,k))