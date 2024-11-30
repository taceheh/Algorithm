import sys
t = int(sys.stdin.readline())
result= []

for _ in range(t):
    dict ={}
    sum =1
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, type =sys.stdin.readline().split()
        # 종류가 딕셔너리에 없으면 추가
        if type in dict:
            dict[type].append(name)
        # 있으면 이름만 추가
        else:
            dict[type]=[name]
    
    for v in dict :
        # 선택하지 않을 경우도 포함해야하니까 +1
        sum*=len(dict[v])+1
    # 아무것도 선택하지 않을 경우를 빼야하니까 -1
    result.append(sum-1)

for r in result:
    print(r)