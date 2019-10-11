#!/usr/bin/env python3

'''
• This was a pain to reverse.
• Used sample input to figure out each char is encoded into 2 bytes.
• Brute force character by character.
• The ending was a nightmare - enumerate first 22, then go right to left. Trust me.
• Luckily I could use the script from the previous iteration, with a few tweaks.

Flag: picoCTF{t1m3f1i350000000000044f90727}

'''

import os, sys

target = "ba a3 ae bb 8a 3a ab 8e aa 3a eb b8 ea 8e aa e2 ea e8 ea b8 ea b8 ea b8 ea b8 ea b8 ea b8 ea b8 ea b8 ea b8 ea b8 ea b8 ba e8 ba e8 ea a2 ee ee 3a ae 3a ba 2e ba e3 ab a0"
vals = bytes.fromhex(target.replace(" ", ""))
chars = "abcdefghijklmnopqrstuvwxyz0123456789 "
ch = "0123456789abcdef"
pre, x = "t1m3f1i350000000000044{}0727", 56

try:
    #while len(pre) < 28:
    for iii in ' ':
        #for i in ch:
            #for j in ch:
                #for k in chars:
                #p = pre + i + j # + k
        for p in (i + j for i in ch for j in ch):
                p = pre.format(p)
                print(p, end="\r")
                sys.stdout.flush()
                with open("flag.txt", "w") as f:
                    f.write(f"{p:28}")
                os.popen("./mystery 1>&2 2>/dev/null").read()
                with open("output", "rb") as f:
                    a = f.read()
                #if len(vals) != len(a):
                #    print(vals,"\n",a)
                #    input()
                if vals[-12:] == a[-12:]:
                    exit("\nDONE" + p)
                """
                if vals[:x] == a[:x]:
                    exit("\nDone: " + pre + p)
                """
                '''
                pre += i
                x += 2
                print("\n" + pre, x)
                break
                '''
                #ui = input(f"\nContinue? {i} & {j}")
                #if ui == "skip":
                #    break
                #elif ui == "ok":
                #    pre += i
                #    x += 1
                #    input(f"Continue with pre={pre} and x={x}")
except KeyboardInterrupt:
    print(p)