with open("cattos.jpg", "rb") as f, open("kitters.jpg", "rb") as g:
    a, b = f.read(), g.read()

for x, y in zip(a, b):
    if x != y:
        print(chr(x), end="")

print()

# One-liner:
# print("".join(chr(x) for x, y in zip(a, b) if x != y))
