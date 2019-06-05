import enum
import sys
limit = sys.float_info.max
# Square Root of a Real Number

class Ordering(enum.Enum):
    SMALLER =0
    EQUAL =1
    LARGER =2


def Square_Root(x):
    if x <1.0:
        left = x
        right = 1.0
    else:
        left = 1.0
        right = x

    # print(Compare(left,right))
    while (Compare(left,right)!=Ordering['SMALLER']):
        mid = left + 0.5*(right-left)
        print('Mid:',mid)
        mid_square = mid*mid

        if (Compare(mid_square,x)==Ordering['EQUAL']):
            return mid
        elif (Compare(mid_square,x)==Ordering['LARGER']):
            right = mid
        else:
            left = mid
    return left

def Compare(a,b):

    print("a: ",a," and b: ",b)
    diff = (a-b)/b
    print('diff :', diff)
    print(float('inf'))
    if diff < -limit:
        return Ordering['SMALLER']
    elif diff > limit:
        return Ordering['LARGER']
    else:
        return Ordering['EQUAL']

x=float(input())
print(Square_Root(x))
