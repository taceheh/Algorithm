s = int(input())

str_list =[]
for _ in range(s):
    num , char = input().split()
    # str_list.append({int(num):list(char)})
    char = list(char)
    new_str=""
    for i in range(len(char)):
        new_str+=char[i]*int(num)
    str_list.append(new_str)

for str in str_list:
    print(str)