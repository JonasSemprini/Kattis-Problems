x = int(input())
N = int(input())
i = 0
data = 0
while i < N:
    num = int(input())
    data += x - num
    i = i + 1

data = data + x

print(data)
