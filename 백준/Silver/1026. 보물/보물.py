import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int,sys.stdin.readline().split())))
b = list(map(int,sys.stdin.readline().split()))

sum=0
# b(2, 4, 5, 3, 1)
for i in range(n):
    sum+=a.pop()*b.pop(b.index(min(b)))
print(sum)