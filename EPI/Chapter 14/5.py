def NOT_intersect(A,B):
    if list(A)[0] <= list(B)[0] and list(B)[1] >= list(A)[0]:
        return False
    else:
        return True

input=[{-4,-1},{0,2},{3,6},{7,9},{11,12},{14,7}]
set_1 = {1,8}
result =[]
for i in input:
    print(result)
    if set_1.intersection(i) == set() and NOT_intersect(i,set_1) :
        result.append(i)
    else:
        set_1 = set([i[0],])

set_1 = sorted(set_1)
print(set_1)
# v = [set_1[0],set_1[-1]]
# result.append(set(v))
# print(result)
