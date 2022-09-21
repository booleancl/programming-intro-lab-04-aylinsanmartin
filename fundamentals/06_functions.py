# una función es un grupo de sentencias con un nombre que realizan una computación.
# primero uno define una función y luego se "llama" o "ejecuta" esa función 

# python viene con muchas funciones para usar.
# Solo hay que llamarlas o ejecutarlas.
print("hola pao")

# La mayoria de las funciones entregan un vaLor , es decir , nos devuelven el resultado. ejemplo:

str_num = '32'
real_num = int(str_num) #esta función trasnforma a enteros 
print(type(str_num))

float_num = 3.9999
int_num = int(float_num)
print(int_num)

# la siguiente línea es un error
# int("hola inmundo")

print(float('32')) # Esta función entrega un float 
print(str(3.1415)) # Esta función entrega un str

# composición de funciones: anidar funciones 

print(srt(3.1415))
