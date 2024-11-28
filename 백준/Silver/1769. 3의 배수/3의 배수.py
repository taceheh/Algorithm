
num = list(input())
cnt = 0

# 각 자릿수가 한자리 이상일 때 반복
while len(num)>1:
    cnt+=1
    num =sum(map(int,num))
    num = list(str(num))
if int(num[0]) %3 ==0:
    print(cnt)
    print("YES")
else : 
    print(cnt)
    print("NO")