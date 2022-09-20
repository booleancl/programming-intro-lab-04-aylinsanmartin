# Tenemos expresiones que se pueden evaluar con termino booleano 
# ó dicótomicos
# Ejemplo

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales , por ejemplo 

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False 

gaby_age = 30
paola_age = 30

# Estas siguientes intrucciones las podriamos leer como:
# "Sí(if) el resultado de is_adult ejecutada con la variable gaby_age
# es verdadero , entonces el programa imprime'¿Quieres una cerveza'
# de otro modo (else) imprime'cantemos chuchuwa?" 

if is_adult(paola_age):
    print("¿Quieres una cerveza?")
else:
    print("cantemos chuchuwa")

# elif es una abreviacion "else it" nos permite seguir evaluando expresiones. Podemos tener tantos como nesesitemos 
if paola_age > gaby_age:
    print("Paola es mayor que Gaby")
elif paola_age < gaby_age:
    print("Paola es menor que Gaby")
else:
    print("Tienen la misma edad")