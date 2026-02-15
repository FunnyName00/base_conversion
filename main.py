
def binTo10(number):
    """
    Function to convert from a binary int -> decimal int
    
    :param number: int
    """

    final = 0
    number = str(number)
     
    for i in range(len(number)):
        final += int(number[len(number)-i-1])*(2**i)

    return final

def decimalToBinary(number):
    """
    Function to convert from a decimal int -> binary int
    
    :param number: int
    """
    try:
        temp = []
        while number >=1:
            temp.append(number % 2)
            number = number // 2
        temp.reverse()
        
        return lstToInt(temp)
    
    except TypeError:
        return -1
def lstToInt(lst):
    """
    Makes a integer by concatenating elements of lst
    (Not a sum)
    
    :param lst: List
    """

    try:
        final = ""
        for i in range(len(lst)):
            final+=str(lst[i])

        return int(final)
    except:
        return -1
