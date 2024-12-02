# 세준세비

import sys
t= int(sys.stdin.readline())

for _ in range(t):
    input() # 줄바꿈으로 구분
    n, m=map(int,sys.stdin.readline().split())
    sejun =sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    sebi=sorted(list(map(int, sys.stdin.readline().split())),reverse=True)

    while sejun and sebi:
        if sejun[-1]>= sebi[-1]:
            sebi.pop()
        elif sebi[-1]> sejun[-1]:
            sejun.pop()
    
    if sebi:
        print("B")
    elif sejun:
        print("S")
    else:
        print("C")