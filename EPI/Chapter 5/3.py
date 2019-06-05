precomputed_reverse={}

def preProcess():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            for g in range(2):
                                for h in range(2):
                                    for i in range(2):
                                        for j in range(2):
                                            for k in range(2):
                                                for l in range(2):
                                                    for m in range(2):
                                                        for n in range(2):
                                                            for o in range(2):
                                                                for p in range(2):
                                                                    s=[]
                                                                    s.append(a)
                                                                    s.append(b)
                                                                    s.append(c)
                                                                    s.append(d)
                                                                    s.append(e)
                                                                    s.append(f)
                                                                    s.append(g)
                                                                    s.append(h)
                                                                    s.append(i)
                                                                    s.append(j)
                                                                    s.append(k)
                                                                    s.append(l)
                                                                    s.append(m)
                                                                    s.append(n)
                                                                    s.append(o)
                                                                    s.append(p)
                                                                    r = ''.join(str(q) for q in s)
                                                                    r = int(r,2)
                                                                    s.reverse()
                                                                    # print(o)
                                                                    val = int(''.join(str(x) for x in s))
                                                                    # print(val)
                                                                    precomputed_reverse[r]= val

def reverseBit(x):
    x=int(x)
    wordSize= 16
    bitMask= 0xFFFF
    print(precomputed_reverse[1])
    return precomputed_reverse[x & bitMask] << (3*wordSize)    | precomputed_reverse[(x >> wordSize) & bitMask ] << (2*wordSize)    |  precomputed_reverse[(x >> (2*wordSize)) & bitMask ] << wordSize    | precomputed_reverse[(x >> (3*wordSize)) & bitMask ]

preProcess()
# print(precomputed_reverse)
print(reverseBit(1))
