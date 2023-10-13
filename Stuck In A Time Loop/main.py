def echo(word, n):
    for i in range(1, n + 1):
        print(f"{i} {word}")


word = "Abracadabra"
n = int(input())
echo(word, n)
