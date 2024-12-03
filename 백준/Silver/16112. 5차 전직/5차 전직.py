# n : 아케인 스톤 (받아야할 아케인스톤 수?)
# k : 활성화 시킬 수 있는 아케인스톤의 최대 수
import sys
n,k = map(int, sys.stdin.readline().split())


# i 번째 퀘스트를 진행하면 ai의 경험치와 i번째 아케인 스톤이 주어짐
# 퀘스트로 얻는 경험치도 사냥으로 얻는 것과 똑같은 경험치이기 때문에 i번째 퀘스트의 보상 경험치를 받을 때 활성화되어 있던 아케인 스톤에는 ai의 경험치가 추가됨

# 경험치를 최대로 받으려면 아케인 스톤을 다 활성화 한 후에 최대 경험치인 퀘스트를 깨야함

a = sorted(list(map(int, sys.stdin.readline().split())))
cnt_active_stone =0
point=0
for i in range(n):
    # 만약 현재 활성화된 스톤이 활성화할 수 있는 스톤의 개수보다 작다면
    if k>cnt_active_stone:
        # 활성화할 아케인 스톤 +1
        cnt_active_stone+=1
        point-=a[i]
    point+=a[i]*cnt_active_stone

print(point)
