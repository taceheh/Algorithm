# 좌표 압축

# 입력 형태
# 5
# 2 4 -10 4 -9

# 출력 형태 
# 2 3 0 3 1

import sys

n = int(sys.stdin.readline())

x = list(map(int,sys.stdin.readline().split()))
x_sorted = sorted(set(x))

org = dict(zip(x_sorted,range(len(x_sorted))))

for xx in x:
    print(org[xx],end=" ")