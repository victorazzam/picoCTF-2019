# https://www.chaoswebs.net/snow10
# https://medium.com/@SimpleDynamics/plaintext-steganography-on-the-web-c0af4ece9f58

with open("whitepages.txt", "rb") as f:
    a = f.read()

b = a.replace(b"\xe2\x80\x83", b"0").replace(b" ", b"1").decode()
c = int(b, 2)
d = "0" + hex(c)[2:]

print(bytes.fromhex(d).decode())

# picoCTF{not_all_spaces_are_created_equal_0696a7c2dfa36b081b44603b8aa78efd}
