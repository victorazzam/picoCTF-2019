a = [106, 85, 53, 116, 95, 52, 95, 98]
b = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
c = [0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o141, 0o64]
d = ['0', '8', 'b', 'c', '3', 'c', 'f', 'c']
print("picoCTF{" + "".join(map(chr, a + b + c)) + "".join(d) + "}")
# picoCTF{jU5t_4_bUnCh_0f_bYt3s_a408bc3cfc}
