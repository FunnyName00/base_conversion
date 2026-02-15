
def binTo10(number):
    final = 0
    number = str(number)
    sum = 0 
    for i in range(len(number)):
        final += int(number[len(number)-i-1])*(2**i)
        print(number[i], " += " , int(number[i])*(2**i), " ",i)
    return final

def decimaloBinary(number):
    temp = []
    while number >=1:
        temp.append(number % 2)
        number = number // 2
    temp.reverse()
    return temp

print(binTo10(11011110))  #-> 222  
print(decimaloBinary(222))  #-> 11011110
