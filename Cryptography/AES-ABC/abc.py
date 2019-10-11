from Crypto.Cipher import AES
import os
import sys
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def to_bytes(n):
    s_n = hex(n)[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2:
        s_n = '0' + s_n
    decoded = s_n.decode('hex')
    pad = len(decoded) % BLOCK_SIZE
    if pad: 
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded

def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n')+1:]

def parse_header_ppm(f):
    data = f.read()
    header = ""
    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i
    return header, data

def pad(pt):
    padding = BLOCK_SIZE - len(pt) % BLOCK_SIZE
    return pt + (chr(padding) * padding)

def aes_abc_encrypt(pt):
    cipher = AES.new(sys.argv[2], AES.MODE_ECB)
    ct = cipher.encrypt(pad(pt))

    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]
    iv = os.urandom(16)
    blocks.insert(0, iv)
    
    for i in range(len(blocks) - 1):
        prev_blk = int(blocks[i].encode('hex'), 16)
        curr_blk = int(blocks[i+1].encode('hex'), 16)

        n_curr_blk = (prev_blk + curr_blk) % UMAX
        blocks[i+1] = to_bytes(n_curr_blk)

    ct_abc = "".join(blocks) 
    return iv, ct_abc, ct

if __name__ == "__main__":
    with open(sys.argv[1], 'rb') as f:
        header, data = parse_header_ppm(f)
    iv, c_img, ct = aes_abc_encrypt(data)
    with open(sys.argv[1] + ".enc2", 'wb') as fw:
        fw.write(header)
        fw.write(c_img)

'''
Trying to understand the AES-ABC algorithm:
• First block is the IV
• Second block is itself + IV (modulo UMAX)
• Third block is itself + second block (modulo UMAX)
• Etc

    iv
c1  iv+c1
c2  iv+c1+c2
c3  iv+c1+c2+c3

lim = 10
    5
e1  5+2     7    -5 =2
e2  7+4     1    -7 =4 mod lim
e3  1+6     7    -1 =6
'''
