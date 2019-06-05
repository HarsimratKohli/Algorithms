import heapq
A = [1,0,3,5,2,0,1]
L=[]
H=[]
for i in A:
    # print("L:",L,"& H:",H)

    if L==[]: #min heap is empty
        heapq.heappush(L,i)
    else:
        if i >= L[0]: # L[0] = top element of minHeap
            heapq.heappush(L,i)
        else:
            heapq.heappush(H,i*-1)

    if len(L) > len(H) + 1:
            heapq.heappush(H,-1*heapq.heappop(L))
            # heapq.heappop(L)
    elif len(H) > len(L):
            heapq.heappush(L,heapq.heappop(H)*-1)
            # heapq.heappop(H)


    if len(L)==len(H):
        print("Median :",0.5*(L[0]+(-1*H[0])))
    else:
        print("Median :",L[0])
