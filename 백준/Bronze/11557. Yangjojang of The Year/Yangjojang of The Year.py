

import sys
# 테스트케이스
t = int(sys.stdin.readline())
result=[]

for _ in range(t):
    # 학교의 숫자 정수 
    n = int(sys.stdin.readline())
    # 학교명과 술소비량을 담을 딕셔너리 선언
    univercity ={}
    first_uni = ""
    max_amount=0
    for _ in range(n):
        name,amount = sys.stdin.readline().split()
        if name not in univercity:
            univercity[name]= int(amount)
        else :
            univercity[name]+=int(amount)
            
        if int(amount)>max_amount:
            max_amount=int(amount)
            first_uni= name
    print(first_uni)
