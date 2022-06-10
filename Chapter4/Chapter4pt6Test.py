numArray = [7, 13, 27, 48, 56000000, 49000] 
def divisible_by_7(numArray):
    return_values = []
    for x in numArray:
        if (x % 7 == 0):
            return_values.append(True) 
        else:
            return_values.append(False)     

    return return_values
print(divisible_by_7(numArray))
