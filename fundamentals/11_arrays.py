# Los arreglos(listas) son una ESTRUCTURA DE DATOS FUNDAMENTAL 
# que permite agrupar valores , separados por coma 

first_array = ['sacar la basura', 'peinarse', 'dormir','secar la ropa']

# En python el primer elemento de un arreglo tiene posición (índice) 0
print(first_array[0])
print(first_array[1])
print(first_array[2])
print(first_array[3])
# no existe el elemento con indice 4 y python da un error 
# print(first_array[4])

# podemos saber el largo de un arreglo o lista con una función pre definida len()

print(len(first_array))

# además , podemos agregar elementos al final de arreglo con el método append 
first_array.append('comer')
first_array.append('dormir')

# Podemos indicar la posicion del nuevo elemento a agregar con isert 
first_array.insert(0,'levantarse')


# Podemos imprimir la lista completa 
print(first_array)
