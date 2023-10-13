data = [int(input()) for _ in range(abs(int(input())))]
for n in data:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
