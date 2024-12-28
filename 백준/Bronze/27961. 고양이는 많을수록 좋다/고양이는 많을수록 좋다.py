# boj 27861 : 고양이는 많을수록 좋다

# 입력 : 키우기를 원하는 고양이의 수 n
# 출력 : n마리의 고양이를 들일 수 있는 최소의 행동 횟수
import sys
input = sys.stdin.readline

n = int(input())
cat = 1 # 초기 고양이의 수
cnt =0 # 행동횟수

if n==0:
    print(0)
elif n ==1:
    print(1)
else: 
    while cat !=n:
        if cat>= n-cat:
            cat+=n-cat
            cnt+=1
        else:
            cat = cat+cat
            cnt +=1
    print(cnt+1)