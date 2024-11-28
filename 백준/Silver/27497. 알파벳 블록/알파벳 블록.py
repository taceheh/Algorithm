## 문제 분석
# 문자열 만들기 게임
# 첫번째줄에는 버튼을 누를 횟수를 입력
# 1번 버튼 : 맨 뒤에 블록 추가
# 2번 버튼 : 맨 앞에 블록 추가
# 3번 버튼 : 가장 나중에 추가된 블록 제거

# 버튼을 누른 횟수만큼 버튼의 숫자와 추가할 문자를 띄어쓰기로 구분하여 입력한다
# 3번은 문자를 입력할 필요가 없고 빈문자열일 경우 0을 출력한다

from collections import deque
import sys

n = int(input())
deq = deque()
li =[]

for _ in range(n):
    s = list(map(str, sys.stdin.readline().split()))
    num = int(s[0])

    if num==1:
        deq.append(s[1])
        # 뒤에 추가했을경우, true
        li.append(True)
    elif num==2:
        deq.appendleft(s[1])
        # 앞에 추가했을경우, false
        li.append(False)
    elif num == 3:  # 가장 나중에 추가된 블록 제거
        if li:  # li가 비어 있지 않을 때만 처리
            p = li.pop()  # 추가된 위치 기록을 가져옴
            if p:  # 뒤에서 추가된 경우
                deq.pop()
            else:  # 앞에서 추가된 경우
                deq.popleft()

if deq:
    print("".join(deq))
else:
    print(0)