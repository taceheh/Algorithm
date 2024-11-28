str = input()
str_set=set()

for i in range(len(str)):
    for j in range(i,len(str)):
        str_set.add(str[i:j+1])
    # else:
    #     str_list.append(str[0:i+1])
# print(str_list)
# print(len(str))
print(len(str_set))

