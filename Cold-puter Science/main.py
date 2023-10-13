def count_temp(temp):
    count = 0
    for t in temp:
        if int(t) < 0:
            count += 1
    return count


tmp = int(input())
numbers = input().split()
print(count_temp(numbers))
