#Reverse Polish Expression

inp_string = '+12-3'
l = list(inp_string)

while l:
    ans=-1
    for i in l:
        if i =='+' or i =='-' or i =='*' or i =='/':
            sign = i
            l.pop(0)

            y=l.pop(0)
            x=l.pop(0)
            if sign =="+":
                res=int(y)+int(x)
            if sign =="-":
                res=int(y)-int(x)
            if sign =="*":
                res=int(y)*int(x)
            if sign =="/":
                res=int(y)/int(x)

            l.insert(1,str(res))
            # print(l)
        else:
            ans=l.pop(0)
    print(ans)
