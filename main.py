
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

def decimaloBinary(number):
    """
    Function to convert from a decimal int -> binary int
    
    :param number: int
    """

    temp = []
    while number >=1:
        temp.append(number % 2)
        number = number // 2
    temp.reverse()
    
    return lstToInt(temp)

def lstToInt(lst):
    """
    Makes a integer by concatenating elements of lst
    (Not a sum)
    
    :param lst: List
    """
    final = ""
    for i in range(len(lst)):
        final+=str(lst[i])

    return int(final)

print(binTo10(11011110))  #-> 222  
print(decimaloBinary(222))  #-> 11011110
