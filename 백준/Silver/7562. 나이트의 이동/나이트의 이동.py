from collections import deque

t = int(input())


d = [(-2,1),(-1,2),(1,2),(2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

def bfs(w,start,end,ex,ey):
    visited=[[False]*w for _ in range(w)]
    # 현재 좌표와 이동 횟수
    queue = deque([(start,end,0)])
    visited[start][end] = True

    while queue:
        # queue에 횟수까지 넣어주는 이유는 이동단계를 추적하기 위해서임
        x, y,cnt = queue.popleft()
        if x==ex and y==ey:
            print(cnt)
            break

        for dx, dy in d :
            nx, ny = x+dx, y+dy
            if 0<=nx< w and 0<=ny<w and not visited[nx][ny]:
                visited[nx][ny]=True
                queue.append((nx,ny,cnt+1))





for _ in range(t):
    width = int(input())
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    bfs(width,start_x,start_y,end_x,end_y)