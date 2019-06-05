#Intro : count no. of 1's in a integer
def count(x):
    c=0
    while(x):
        c += x&1
        x>>=1
    print(c)


# 1. Parity : check if no. of bits are odd (ouput = 1) or even(output =0)

#Brute Force : O(n)
def Parity(x):
    res = 0
    while(x):
        res ^=(x&1)
        x=x>>1
    print(res)

#optimised : Remove Lowest set bit
def

Parity(1)
