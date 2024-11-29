## 민균이의 비밀번호
## 입력받은 숫자만큼 단어를 입력받고
## 그 단어중에는 민균이의 비밀번호에 해당되는 문자열과 비밀번호가 뒤집힌 문자열이 존재한다.

n = int(input())
pw ={}
result=""
for _ in range(n):
    word = input()
    # 만약 단어가 딕셔너리에 있거나
    # 뒤집은 단어가 딕셔너리에 있다면?
    if word not in pw :
        if word[::-1] in pw:
            result=word
        else:
            pw[word]=word
    if result =="" and word==word[::-1]:
         result=word
print(len(result),result[len(result)//2])