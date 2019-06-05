#Finding duplicate and missing number
A=[5,3,0,3,1,2]
duplicate = missing = -1

miss_XOR_dup=0
for i in range(len(A)):
    miss_XOR_dup ^= i^A[i]

differ_bit = miss_XOR_dup &(~(miss_XOR_dup-1))

miss_or_dup=0
for i in range(len(A)):
    if i & differ_bit:
        miss_or_dup ^= i
    if A[i] & differ_bit:
        miss_or_dup ^= A[i]

#miss_or_dup is either missing or dup
flag=True
for i in A:
    if i == miss_or_dup:
        flag=False
        duplicate=miss_or_dup
        missing=miss_or_dup^miss_XOR_dup

if flag:
    duplicate=miss_or_dup^miss_XOR_dup
    missing=miss_or_dup

print('Missing: ',missing)
print('Duplicate: ',duplicate)
