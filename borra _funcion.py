def suma(hasta):
    resultado = 0
    for x in range(1, hasta+1):
        resultado += x
    return resultado
    
def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo+1):
        resultado += i*i
    return resultado
    
print(suma(100))
print(sumaTodosLosCuadrados(3))
            