# 완전 이진 트리의 노드 수는 2^k-1
# k = 레벨

# k = 10 
# node = 2**k -1

t = int(input())



for _ in range(t):
    a,b = map(int, input().split())
    

    while True:
        if a==b:
            print(a*10)
            break

        if a>b:
            a=a//2
        else:
            b=b//2
