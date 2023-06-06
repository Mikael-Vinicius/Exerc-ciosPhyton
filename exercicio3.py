def somaRecursiva(number): 
    if(number == 0): 
        return 0
    else: 
        return number + somaRecursiva(number - 1)
    
print(somaRecursiva(4))