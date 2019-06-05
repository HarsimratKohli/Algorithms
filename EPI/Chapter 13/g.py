#code
# T = int(input())
T=1

for q in range(T):
    # N,E = map(int,input().split())
    N=42
    E=468
    # A = list(map(int,input().split()))
    A = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]

    curr_sum=A[0]
    start=0
    i=1
    while i<=N:

        while curr_sum > E and start <= i-1:
            curr_sum -= A[start]
            start +=1

        if curr_sum == E:
            print(start+1,i)

        if i < N:
            curr_sum+=A[i]
        i+=1
