n = int(input())
stack=[]

for _ in range(n):
    stack.append(reversed(input().split()))

for i in range(n):
    print(f"Case #{i+1}: ",end="")
    print(*stack[i])