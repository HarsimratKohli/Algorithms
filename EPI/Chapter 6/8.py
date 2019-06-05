def Generate_primes(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0] = is_prime[1] = False

    for i in range(2,n+1):
        if is_prime[i] == True:
            #Seive
            for j in range(2*i,n+1,i):
                is_prime[j]=False

    return(is_prime)

res=Generate_primes(50)
for index,val in enumerate(res):
    if val ==True:
        print(index)
