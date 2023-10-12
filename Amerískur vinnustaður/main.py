field_l = 0.09144


def length(n):
    road = n * field_l
    return f"{road}"


n = int(input())
print(length(n))
