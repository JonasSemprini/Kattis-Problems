def board(size):
    if size == 1:
        return f"first"
    elif size % 2 == 0:
        return f"second"
    else:
        return f"first"


n = int(input())
print(board(n))
