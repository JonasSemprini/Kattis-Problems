def echo(word, typ):
    if typ == "Echo":
        return (word + " ") * 3


word = str(input().strip())

typ = "Echo"

print(echo(word, typ))
