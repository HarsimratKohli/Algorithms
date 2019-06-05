hashTable =['0','1',"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

def phone_Mneomic_helper(number,curr_digit,output,n):
    if curr_digit == n:
        print(output)
        return

    for i in range( len(hashTable[int(number[curr_digit])]) ):
        # print(hashTable[number[curr_digit]])
        output[curr_digit] = hashTable[int(number[curr_digit])][i]
        phone_Mneomic_helper(number, curr_digit+1, output, n)

        if (number[curr_digit] == 0 or number[curr_digit] == 1):
            return

def phone_Mneomic(phone_number):
    n=len(phone_number)
    result=[0 for i in range(n+1)]
    phone_Mneomic_helper(phone_number,0,result,n)

phone_Mneomic('22')
