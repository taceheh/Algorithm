# 첫번째 줄에 n
# 다움 줄부터 n개의 줄에 걸쳐 한 줄에 하나의 정보가 주어지는데 그 정보는 유형1, 2중 하나

# 유형 1 a: 학생 번호가 양의 정수 a인 학생 1명이 학교 식당에 도착하여 식당 입구의 맨 뒤에 줄을 서기 시작한다.
# 유형 2: 식사 1인분이 준비되어 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 시작한다.

# 출력 : 첫번째 정보부터 n번째 정보까지 순서대로 처리한 다음 식당 입구에 줄을 서서 대기하는 학생수가 최대가 되었던 순간의 학생수와
# 이때 식당 입구의 맨뒤에 대기중인 학생의 번호를 빈칸을 사이에 두고 순서대로 출력
# 대기하는 학생 수가 최대인 경우가 여러번이라면 맨 뒤에 줄 서 있는 학생의 번호가 가장 작은 경우를 출력

import sys
from collections import deque

n = int(sys.stdin.readline())
line = deque()
max_line=0
line_num=0
for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    if a[0]==1:
        line.append(a[1])

        # 최댓값 찾는 로직 
        if len(line)>max_line:
            max_line=len(line)
            line_num= line[-1]
        elif len(line)== max_line:
            if line_num>line[-1]:
                line_num = line[-1]
    elif a[0]==2:
        line.popleft()


print(max_line,end=" ")
print(line_num)