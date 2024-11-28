# 문제분석
# 특정 명령어를 입력하면 그에 맞는 동작이 수행됨
# 띄어쓰기를 기준으로 단어가 1개가 들어올 수도 있고, 2개가 들어올 수도 있음
# for문안에서 list로 새로 입력받기

# queue문제이지만 deque를 queue처럼 활용
# 양방향 출입이 아니라 선입선출 방식으로

from collections import deque
n = int(input())
que = deque()
arr =[]

for i in range(n) :
    a = list(map(str,input().split()))

    cmd=a[0]
    
    if cmd=="push":
        que.append(a[1])
    elif cmd=="pop":
        if len(que)==0:
            arr.append(-1)
        else:
            arr.append(que.popleft())
    elif cmd=="size":
        arr.append(len(que))
    elif cmd=="empty":
        if len(que)==0:
            arr.append(1)
        else:
            arr.append(0)
    elif cmd== "front":
        if len(que)==0:
            arr.append(-1)
        else : 
            arr.append(que[0])
    elif cmd== "back":
        if len(que)==0:
            arr.append(-1)
        else : 
            arr.append(que[-1])


for item in arr :
    print(item)

