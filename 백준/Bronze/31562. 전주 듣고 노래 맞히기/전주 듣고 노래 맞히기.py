# 전주 듣고 노래 맞히기
# 정환이 음을 아는 노래의 개수 N
# 정환이 맞히기를 시도할 노래의 개수 M

# 두 번째 줄부터 n개의 줄에 걸쳐 노래 제목의 길이 T, 노래 제목 S, 해당 노래에서 처음 등장하는 일곱개의 음이름이 공백으로 구분되어 주어짐

# N+2번째 줄부터 M개의 줄에 걸쳐 정환이 맞히기를 시도할 첫 세 음의 음이름이 공백으로 구분되어 주어짐


# 정환이 맞히기를 시도할 각 노래에 대하여 프로그램에 저장된 노래와 첫 세 음이 동일한 노래가 하나만 있다면 해당 노래의 제목을, 두 개 이상이면 ?을, 없다면 !을 한 줄에 하나씩 출력

n,m = map(int, input().split())
songList={}
result=[]

for _ in range(n):
    temp = input().split()
    code =  " ".join(temp[2:5])
    if code not in songList:
        songList[code]=[temp[1]]
    else :
        songList[code].append(temp[1])

for _ in range(m):
    ans = input()
    if ans in songList:
        if len(songList[ans])==1:
            result.append(songList[ans])
        elif  len(songList[ans])>1: 
              result.append("?")
            
    else:
        result.append("!")

for r in result:
    print(*r)
