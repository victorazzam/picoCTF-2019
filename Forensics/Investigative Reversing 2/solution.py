with open("encoded.bmp", "rb") as f:
    a = f.read()

def proc(offset):
    vals1 = "".join(f"{x:08b}"[-1] for x in a[offset:offset+400])
    vals2 = "".join(vals1[i:i+8][::-1] for i in range(0, 400, 8))
    return "".join(chr(int(vals2[x:x+8], 2)) for x in range(0, 400, 8))

print("".join(chr(ord(x) + 5) for x in proc(2000)))
