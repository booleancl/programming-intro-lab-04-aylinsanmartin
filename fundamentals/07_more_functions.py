# Podemos crear nuestras propias funciones 
# Lo hacemos con la palabra especial "def" y el cuerpo 
# La funcion debe ir correctamente identado

def chuchuwa(inst):
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("chuchuwa chuchuwa chuchuwa wa wa!")
    print("atención!, compañia:")
    print(inst)

print(chuchuwa)
print(type(chuchuwa))

# el llamado de la función 
chuchuwa("Mano hacia el frente")
chuchuwa("Hombros hacia atras")

# Las funciones deben llamarse o ejecutarse con los mismos parámetros que se definió
result = chuchuwa("lengua afuera")

# Si la funcion no tiene un valor de retorno, nos entregará "none", que es para representar: "nada"
print(result)





