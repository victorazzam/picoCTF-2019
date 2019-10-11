x, y, z = 0, 0, {}
for i in range(256):
    z[chr(x) + chr(y)] = chr(i)
    x = (x + 16) % 256
    if x < 10:
        y += 1

flag = ""
z["\xff\x06"] = "o" # weird odd case

# from pprint import pprint
# pprint(z)
# print(z["\xff\x06"])

for i in "54321":
    with open(f"Item0{i}_cp.bmp", "rb") as f:
        a = f.read()[2019:2139]
        b = "".join(bin(x)[-1] for x in a)
        c = "".join(chr(int(b[x:x+8][::-1], 2)) for x in range(0, 120, 8))
        for j in range(0, 15, 3):
            # print(flag, "\n", repr(c), len(c))
            flag += c[j]
            try:
                flag += z[c[j+1:j+3]]
            except KeyError:
                flag += chr(ord(z[chr(ord(c[j+1])+1)+c[j+2]])-1)

print(flag)
