def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def siguientePrimo(n):
    if esPrimo(n):
        i = 1
        while esPrimo(n + i) == False:
            i = i + 1
        return n + i
    else:
        return "No es primo"

print( siguientePrimo(13) )