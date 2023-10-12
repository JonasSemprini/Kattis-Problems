start = 2022


def years(n, k):
    if k == 0:
        return start
    new_years = n / k
    if n % k != 0:
        return round(start + new_years + 1)
    return round(start + new_years)


n = int(input())
k = int(input())
