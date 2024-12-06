# 입력 
# k : 레벨
# 상근이가 방문한 빌딩의 번호가 들어간 순서대로


# 출력 형태를 보니까 마지막에 저장한 부모 노드가 제일 첫 번째로 나옴
# dfs : 스택 구조 사용

k = int(input())

visited=list(map(int,input().split()))
tree=[[] for _ in range(k)]
# print(node)
# 가운데를 기준으로 반으로 나누고


def dfs(node,level):
    mid = len(node)//2
    tree[level].append(node[mid])

    if len(node)==1:
        return
    
    dfs(node[0:mid],level+1)
    dfs(node[mid+1:],level+1)


dfs(visited,0)

for t in tree:
    print(*t)