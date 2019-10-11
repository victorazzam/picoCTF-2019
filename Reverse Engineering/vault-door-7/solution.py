import struct
a = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293046, 926180660, 862348336]
print("picoCTF{" + b"".join(struct.pack("I", x)[::-1] for x in a).decode() + "}")
# picoCTF{A_b1t_0f_b1t_sh1fTiNg_6674e43fd0}
