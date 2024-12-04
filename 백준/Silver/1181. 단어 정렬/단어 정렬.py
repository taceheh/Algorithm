import sys

n = int(sys.stdin.readline())
word = {}

for _ in range(n):
    w = sys.stdin.readline().strip()
    if len(w) in word:
        word[len(w)].add(w)  # 이미 존재하는 세트에 문자열 추가
    else:
        word[len(w)] = {w}  # 새로운 세트로 초기화

for item in sorted(word):  # 키(문자열 길이) 기준 정렬
    print("\n".join(sorted(word[item])))  # 세트를 정렬 후 줄바꿈으로 출력
