#Swapping bits
# Note : x&(x-1) -> clears the last set bit of x
# Note : x&~(x-1) -> extracts the last set bit of x

# x = int(input())
# i,j = map(int,input().split())) # indices to swap

#Brute Force
def swap(x,i,j):
    bit1=  (x>>i)&1
    bit2=  (x>>j)&1

    n = bit1 ^ bit2

    n = n<<i | n<<j

    print(n^x)

# swap(5,0,1)

#optimised
def flip(x,i,j):
    # check if bit at i and j are different otherwise swapping not reqd
    if x>>i&1 != x>>j&1:
        #create a mask
        mask  = 1<<i | 1<<j
        print(mask^x)

flip(5,0,1)
