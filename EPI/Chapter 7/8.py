#
# def LookAndSay(n):
#     if (n == 1):
#         return "1"
#     if (n == 2):
#         return "11"
#     # Initialize previous term
#     s = "11"
#     for i in range(3, n + 1):
#         s += '$'
#         l = len(s)
#         cnt = 1
#         tmp = ""
#         for j in range(1 , l):
#             if (s[j] != s[j - 1]):
#                 tmp += str(cnt)+s[j - 1]
#                 cnt = 1
#             else:
#                 cnt += 1
#         s = tmpA
#     return s
def LookAndSay(n):
    if n==1:
        return '1'
    if n==2:
        return '11'
    s='11'
    for i in range(3,n+1):
        s+='@'
        l=len(s)
        count=1
        tmp=''
        for j in range(1,l):
            if s[j]!=s[j-1]:
                tmp += str(count)+s[j-1]
                count=1
            else:
                count+=1
        s=tmp
    return s

for i in range(1,10):
    print(LookAndSay(i))
