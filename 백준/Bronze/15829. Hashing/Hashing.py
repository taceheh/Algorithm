# Hashing
import string

alphabet = {}
result=0
M = 1234567891

for index, char in enumerate(string.ascii_lowercase, start=1):
    alphabet[char] = index


n = int(input())
st=list(input())

for i in range(n):
    # print(alphabet[st[i]])
    result+=alphabet[st[i]]*31**i

print(result%M)


