#   this file is for different keywords that are available to us in python

#   True, False and None

def checkEven(num) : 
    return num%2==0     #   True if even False when not even

def isNone(val) :
    if val is None : 
        return True
    else : 
        return False


if __name__ == "__main__" :
    #   you can ignore this section will be explained in a different section
    valu = None
    print(isNone(valu))