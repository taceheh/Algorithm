n = int(input())

fruits = {"BANANA":0,
          "PLUM":0,
          "STRAWBERRY":0,
          "LIME":0}

for _ in range(n):
    f, num = map(str,input().split())
    fruits[f]+=int(num)

if 5 in fruits.values():
    print("YES")
else:
    print("NO")
