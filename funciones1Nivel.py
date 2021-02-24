def normal(x): #ojo!! la x solo funciona en el ámbito de la funcion(linea 1 y 2)
    return x

def cuadrado(x): #ojo!! la x solo funciona en el ámbito de la funcion(linea 4 y 5)
    return x * x

#vamos a utilizar una función(f), como parámetro de entrada
def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i) #a resultado le sumo la aplicacion de la funcion (f) sobre i
    return resultado

print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))