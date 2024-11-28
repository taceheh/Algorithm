n = int(input())
employee_name = {}

for i in range(n * 4):
    temp_list = list(map(str, input().split()))

    # 근무자 이름 처리
    for li in temp_list:
        if li == "-":  # '-'는 건너뛰기
            continue

        # 이름이 처음 등장하면 0으로 초기화
        if li not in employee_name:
            employee_name[li] = 0

        # 근무 시간을 더해줌
        if i % 4 == 0 or i % 4 == 2:  # 08:00~12:00, 18:00~22:00 -> 4시간
            employee_name[li] += 4
        elif i % 4 == 1:  # 12:00~18:00 -> 6시간
            employee_name[li] += 6
        elif i % 4 == 3:  # 22:00~08:00 -> 10시간
            employee_name[li] += 10

# 모든 근무 시간이 동일한지 확인
if employee_name:
    max_hours = max(employee_name.values())
    min_hours = min(employee_name.values())
    if max_hours - min_hours <= 12:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")  # 아무도 근무하지 않는 경우
