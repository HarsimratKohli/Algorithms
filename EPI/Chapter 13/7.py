class SubArray :

    def __init__(self,start,end):
        self.start = start
        self.end = end

def findSmallestSubArrayCoveringSet(paragraph,keywords):

    keywordToCover = dict()

    for string in keywords:
        if string not in keywordToCover.keys():
            keywordToCover[string] = 1
        else:
            keywordToCover[string] += 1

    # print(keywordToCover)

    result = SubArray(-1,-1)
    remainingToCover = len(keywords)

    # print(remainingToCover)


    left = right = 0
    while right < len(paragraph):
        right +=1
        word = paragraph[right]
        keywordCount = keywordToCover.get(word)

        # print(keywordCount)

        if keywordCount :
            keywordToCover[word] = keywordCount-1
            if keywordCount >=0:
                remainingToCover -= 1

        while remainingToCover==0:
            if (result.start == -1 and result.end ==-1) or right -left < result.end -result.start:
                result.start = left
                result.end = right

            word = paragraph[left]
            keywordCount = keywordToCover.get(word)
            if keywordCount :
                keywordToCover[word] += keywordCount+1
                if keywordCount >0:
                    remainingToCover +=1
            left +=1

        print(keywordToCover)

    return result

paragraph ='hello there how are you'.split()
keywords = set('hello there'.split())
res =findSmallestSubArrayCoveringSet(paragraph,keywords)
print(res.start,res.end)
