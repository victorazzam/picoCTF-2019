with open("encoded.bmp", "rb") as f:
    data = f.read()[723:]

f, p = "", 0

for i in range(100):
    if i % 2:
        p += 1
    else:
        for j in range(8):
            f += bin(data[p])[-1]
            p += 1

F = "".join(f[i:i+8][::-1] for i in range(0, len(f), 8))
print(bytes.fromhex(hex(int(F, 2))[2:]).decode())

# picoCTF{4n0th3r_L5b_pr0bl3m_0000000000000aa9faea3}
