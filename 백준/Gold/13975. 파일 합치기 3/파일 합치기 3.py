import sys
import heapq
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())

    page = list(map(int,sys.stdin.readline().split()))
    heapq.heapify(page)
    min_price =0
    while len(page)>1:
        pair_price = heapq.heappop(page)+heapq.heappop(page)
        min_price+=pair_price
        heapq.heappush(page,pair_price)
        pair_price=0
    print(min_price)
