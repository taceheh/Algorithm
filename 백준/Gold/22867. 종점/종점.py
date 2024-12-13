'''
boj 22867  종점

문제 분석 : 주행을 마치고 버스들이 종점의 들어왔다가 나가는 시간을 보고, 버스 정비 공간이 최소 몇 개가 필요한지 계산하기

입력 : t -> 테스트 케이스
      a, b -> 버스가 종점에 들어오는 시간, 나가는 시간

출력 : 최소로 필요한 버스 정비공간수
'''

import sys
input = sys.stdin.readline

# 입력 처리
n = int(input())
events = []

# 시간 데이터 변환하고 리스트에 추가
for _ in range(n):
    arrive, depart = input().strip().split()
    
    # 도착 시간 변환
    h, m, s, ms = map(int, [arrive[:2], arrive[3:5], arrive[6:8], arrive[9:]])
    arrive_time = ms + s * 1000 + m * 60000 + h * 3600000
    events.append([arrive_time, 1])  # 도착 
    
    # 출발 시간 변환
    h, m, s, ms = map(int, [depart[:2], depart[3:5], depart[6:8], depart[9:]])
    depart_time = ms + s * 1000 + m * 60000 + h * 3600000
    events.append([depart_time, -1])  # 출발 

events.sort()

# 정비 공간 계산
max_buses = 0
current_buses = 0

for event in events:
    if event[1] == 1:  # 도착
        current_buses += 1
        max_buses = max(max_buses, current_buses)
    else:  # 출발
        current_buses -= 1

print(max_buses)
