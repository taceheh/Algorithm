'''
백준 2108 통계학

단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

num=[]
dict={}

for _ in range(n):
    x = int(sys.stdin.readline())
    num.append(x)
    if x in dict :
        dict[x]+=1
    else : 
        dict[x]=1


# 산술평균
print(round(sum(num)/n))

# 중앙값
num.sort()
print(num[len(num)//2])

# 최빈값
max_num = max(dict.values())
modes = [key for key, value in dict.items() if value == max_num]

modes.sort()
if len(modes)>1:
    print(modes[1])
else: 
    print(modes[0])

# 최댓값- 최솟값
print(max(num)-min(num))