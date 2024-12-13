'''
boj 22252 정보상인 호석

문제 분석 : 고릴라 상인에게 정보를 사는 문제

입력 : t -> 테스트 케이스의 개수
      1 name k c1 c2 ... ck ->  1로 시작하는 경우, 고릴라의 이름, 정보의 개수, 정보별 가치들
      2 name b -> 호석이가 구매하려는 고릴라의 이름, 정보의 개수 b
      
출력 : 호석이가 얻게되는 정보 가치의 총합


이때 고릴라가 가진 정보들 중 가장 비싼 b개를 구매하고 고릴라가 가진 정보가 b개 이하면 가진 모든 정보를 구매함

의사결정코드
1) 테스트 케이스 입력받기
2) 테스트 케이스 만큼 반복문
3) 1일 경우, 딕셔너리에 저장
4) 2일 경우, 해당 고릴라에게 정보구매(큰값부터)
5) 정보 구매시 총합에 누적
'''
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

t = int(input())
gorilla_dict = defaultdict(list)
total_value = 0

for _ in range(t):
    query = input().split()
    command = int(query[0])

    if command == 1:
        # 고릴라가 정보를 얻는 경우
        name = query[1]
        k = int(query[2])
        values = list(map(int, query[3:3 + k]))
        # 고릴라의 정보 리스트를 max-heap 형태로 관리
        for value in values:
            heapq.heappush(gorilla_dict[name], -value)

    elif command == 2:
        # 고릴라에게 정보를 구매하는 경우
        name = query[1]
        b = int(query[2])
        if name in gorilla_dict:
            for _ in range(b):
                if gorilla_dict[name]:
                    # 가장 높은 값을 pop하여 total_value에 추가
                    total_value += -heapq.heappop(gorilla_dict[name])
                else:
                    break

print(total_value)
