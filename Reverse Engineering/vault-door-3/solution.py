def check(p):
    b = [0] * 32
    i = 0
    while i < 8:
            b[i] = p[i]
            i += 1
    while i < 16:
            b[i] = p[23-i]
            i += 1
    while i < 32:
            b[i] = p[46-i]
            i += 2
    i = 31
    while i >= 17:
            b[i] = p[i]
            i -= 2
    return "".join(b)

test = "abcdefghijklmnopqrstuvwxyzABCDEF"
result = check(test)
a = "jU5t_a_sna_3lpm1eg34a_u_4_m4ra40"
b = [0] * 32
for y, i in enumerate(result):
    b[test.find(i)] = a[y]

print("picoCTF{" + "".join(b) + "}")

# picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_a43ae0}
