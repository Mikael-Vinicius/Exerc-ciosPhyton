list = [30, 20, 50, 70, 20]

def media(numbers): 
    total = 0
    for number in numbers: 
        total += number

    return total / len(numbers)
        


print(media(list))