# 줄세우기 문제

# ex) 줄 선 5명의 번호를 차례로 매긴다면
#     1   2   3   4   5
#    (0   1   1   3   2  만큼 앞으로 이동)


#     1   2   3   4   5   >> 1번 학생 이동 없음
#     2   1   3   4   5   >> 2번 학생 앞으로 한 칸 이동
#     2   3   1   4   5   >> 3번 학생 앞으로 한 칸 이동
#     4   2   3   1   5   >> 4번 학생 앞으로 세 칸 이동
#     4   2   5   3   1   >> 5번 학생 앞으로 두 칸 이동


n = int(input())
forward_num = list(map(int,input().split()))

# range는 연속된 숫자를 생성
student = list(range(1,n+1))
#    (0   1   1   3   2  만큼 앞으로 이동)
for i in range(n):
    num = forward_num[i]
    # print(num)

    student.insert(i - num, student.pop(i))
    # print(student)
    # print()

print(*student, sep=" ")