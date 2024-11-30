from heapq import heappop,heappush
import sys
result =[]
heap=[]

n = int(sys.stdin.readline().strip())

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num >0 :
        heappush(heap,num)
    elif num ==0:
        if heap: result.append(heappop(heap))
        else : result.append(0)

for r in result :
    print(r)