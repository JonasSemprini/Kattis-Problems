s = str(input())
check = s.split("COV")
print(check)
for i in check:
    if str(i) == s:
        print("Ekki veikur!")
        break
    print("Veikur!")
    break

