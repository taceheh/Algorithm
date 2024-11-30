# 크리스마스 선물
# 아이들과 거점지를 방문한 횟수 n
# n줄의 데이터를 입력받을 예정
# 0이면 아이들을 만난 것이고
# 0이 아니라면 첫째로 거점지에서 몇개의 선물을 충전할 것인지 그리고 그 선물들의 가치를 입력받는다
# 만난 아이들에게 차례대로 가치높은 선물을 주면된다
# 만약 줄 선물이 없다면 -1을 출력
import sys 
from heapq import heapify,heappop,heappush

n = int(sys.stdin.readline())
heap=[]
result=[]

for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    # print(temp)
    a = temp[0]
    value = temp[1:]
    for v in value: 
        heappush(heap,-v)
    
    if a ==0:
        if heap:
            result.append(-heappop(heap))
        else:
            result.append(-1)

for r in result:
    print(r)