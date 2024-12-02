
# 팀명 정하기

import sys
# 차례로 해결한 문제의 개수, 입학 연도, 성씨씨
first_char = []
year=[]
info={}
for _ in range(3):
    p,y,s = sys.stdin.readline().split()
    year.append(str(int(y)%100))

    if p not in info:
        info[int(p)]=s[0]

reversed_info = sorted(info,reverse=True)
print("".join(sorted(year)))
for item in reversed_info:
    print(info[item],end="")
