"""
======================================================
* 문제
  임무는 어떤 문자열이 주어졌을 때,
  괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것

  문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류
  << 균형을 이루는 조건 >>
  모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
  모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
  모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
  모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
  짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.

* 입력
  각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"),
  대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.

* 출력
  각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
* 예제 입력
  So when I die (the [first] I will see in (heaven) is a score list).
  [ first in ] ( first out ).
  Half Moon tonight (At least it is better than no Moon at all].
  A rope may form )( a trail in a maze.
  Help( I[m being held prisoner in a fortune cookie factory)].
  ([ (([( [ ] ) ( ) (( ))] )) ]).
   .
  .

* 예제 출력
  yes
  yes
  no
  no
  no
  yes
  yes
======================================================

* 문제 분석
  1. *(), []
  2. 균형 (), [] << 짝이 맞는지 확인하는 작업이 필요할 것 같아요
  3. 안에 있는 문자열들은 삭제하고 (),[]만 추출해서 비교해야될 것 같아요
  4. 자료구조는 스택으로 문자열이 섞이지 않고 비교할 수 있도록 할 수 있을꺼같아요.
  5. 3번 문제와 비슷한 문제.
  6. 괄호가 없는경우는 yes 출력
* 의사 결정

* 코드 구현
"""

while True:
    # 입력 값
    string = input()
    # print(string)
    # print(len(string))
    if (string == "."):
        break
    pair = []
    stack = []

    for i in range(len(string)):
        ## string에서 괄호만 추출해서 pair 배열에 추가
        if string[i] == "(" or string[i] == ")" or string[i] == "[" or string[i] == "]":
            pair.append(string[i])

    for p in pair:
        # print(p)
        ## 스택이 비어있으면
        if not len(stack):
            # append i번째 요소
            stack.append(p)
            # print(*stack)
        elif stack[-1] != p: ###
            if stack[-1] =="(" and p ==")" :
                stack.pop()
            elif stack[-1] =="[" and p=="]":
                stack.pop()
            # stack.pop()
            else:
                stack.append(p)
            # print(*stack)

        else:
            stack.append(p)
            # print(*stack)

    if not stack:
        print("yes")
    else:
        print("no")
    # print(stack)
    # print(pair)

# ['a', 'f', 's', 'd', 'f', 'd', ]
# string = "afsfsdfsdf"
#           0123456789