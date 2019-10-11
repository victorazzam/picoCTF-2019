data = []

for i in "54321":
    with open(f"Item0{i}_cp.bmp", "rb") as f:
        a = f.read()[2019:2139]
        b = "".join(bin(x)[-1] for x in a)
        c = "".join(b[x:x+8][::-1] for x in range(0, 120, 8))
        data.append(c)
        print(" ".join(bytes.fromhex(hex(int(c, 2))[2:])[::3].decode()), end=" ")

print()

for i in data:
    print([x for x in bytes.fromhex(hex(int(i, 2))[2:])])
