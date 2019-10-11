# This recovers the original (AES-ECB encrypted) file.
# It needs to be decrypted by finding the 128-bit key.
# But not really, you can kind of see the flag anyway.
# Flag: picoCTF{d0Nt_r0ll_yoUr_0wN_aES}

with open("body.enc.ppm.backup", "rb") as f:
	a = f.read()

header = a[:16]    # PPM header, never changes: P6 1895 820 255
data = a[16:]      # File contents
iv = a[16:32]      # Random IV, doesn't affect anything
lim = 256 ** 16    # Modulus

# Bytes to number
def b2n(x):
	return int("".join(f"{i:02x}" for i in x), 16)

# Number to bytes
def n2b(x):
	x = hex(x)[2:]
	z = bytes.fromhex(len(x) % 2 * "0" + x)
	while len(z) != 16:
		z = b"\x00" + z
	return z

result = b""

# Deconstruct the file
for i in range(16, len(data), 16):
	prev = data[i-16:i]
	curr = data[i:i+16]
	encr = (b2n(curr) - b2n(prev)) % lim
	result += n2b(encr)

# Write resulting data into output file
with open("body-enc.ppm", "wb") as f:
	f.write(header)
	f.write(result)
