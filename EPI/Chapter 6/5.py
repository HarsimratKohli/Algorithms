A =[2,3,5,5,7,11,11,11,13]
write_index =0
for i in range(0,len(A)-1):
    if A[i]!=A[i+1]:
        A[write_index] =A[i]
        write_index+=1
A[write_index] = A[len(A)-1]
write_index += 1
print(write_index)
print(A)
