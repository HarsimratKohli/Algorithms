#Dutch Flag
A=[4, 5, 3, 7, 2]
pivot =A[0]

def q_sort(A,pivot):
    smaller = equal = 0
    larger = len(A)

    while (equal < larger):

        if A[equal] <pivot:
            A[smaller],A[equal] = A[equal],A[smaller]
            smaller+=1
            equal +=1


        elif A[equal] ==pivot:
            equal+=1
        else:
            larger -=1
            A[larger],A[equal] = A[equal],A[larger]

    print(A)
    print('equal:',equal)

q_sort(A,pivot)
