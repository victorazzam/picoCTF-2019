#!/usr/bin/env python3

'''
Slowly stepping through 'pre' one char at a time until: picoCTF{encodediaqnbuxqzb}

'''

import os, sys

target = "8e 8e ba 3b b8 ea 23 a8 a2 e3 ba e3 a3 aa 2b 8e ae 3b ae 3b a8 ea 80"
vals = bytes.fromhex(target.replace(" ", ""))
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
pre, x = "ENCODEDIAQNBUXQZ", 23
z = 0

try:
    for i in chars:
        p = pre + i
        print(p, end="\r")
        sys.stdout.flush()
        with open("flag.txt", "w") as f:
            f.write(f"{p:17}")
        os.popen("./mystery 1>&2 2>/dev/null").read()
        with open("output", "rb") as f:
            a = f.read()
        if vals[:x] == a[:x]:
            ui = input(f"\nContinue? {i}") # {i} & {j}
            if ui == "skip":
                z = 1
                break
            elif ui == "ok":
                pre += i
                x += 1
                input(f"Continue with pre={pre} and x={x}")
        if z:
            z = 0
            break
except KeyboardInterrupt:
    print(p)
