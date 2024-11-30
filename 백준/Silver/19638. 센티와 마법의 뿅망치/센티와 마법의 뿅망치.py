from heapq import heappop, heappush,heapify,heapreplace

# 순서대로 주민수, 센티의 키, 사용할 수 있는 뿅망치 횟수
n, centi, cnt = map(int, input().split())

min_cnt =0

# 최대힙 사용하기 위해서 음수화
heap=[]
for _ in range(n):
    heappush(heap,-int(input()))


for i in range(cnt):
    if -heap[0] ==1 or -heap[0] < centi:
        break
    else: 
        # heapq.heapreplace(힙배열, 7)
        #해당 힙에서 가장 작은 원소를 팝한 후 원소를 푸시

        ## 이렇게 하니까 값이 미묘하게 차이가남 
        # 이중 마이너스의 의미????
        heapreplace(heap,-(-heap[0]//2))
        min_cnt+=1


if centi<=-heap[0]:
    print("NO")
    print(-heap[0])
else:
    print("YES")
    print(min_cnt)
