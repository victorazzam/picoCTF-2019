from gmpy2 import invert

c = 2205316413931134031074603746928247799030155221252519872649651160278476902145087143487410518148797849017656369316341655241171591967799156330520717647775870050832989405039500714403825189288474886866683126666398914647066914847128627018357093
e = 3

def get_m(C):

    # Find length of m = C ^ (1/e)
    m = "1" + "".join("0" for x in range(len(str(C))) if pow(int("1" + "0" * x), e) < C)

    # Enumerate m = C ^ (1/e)
    for y in range(len(m)):
        M = m[:y], m[y+1:]
        for x in range(1, 10):
            tmp = int(str(x).join(M))
            if tmp ** e < C:
                m = str(x).join(M)
            elif tmp ** e > C:
                m = str(x - 1).join(M)
                break
            else:
                return tmp

m = get_m(c)
print(bytes.fromhex(hex(m)[2:]).decode())

# picoCTF{n33d_a_lArg3r_e_6eb35d6d}
