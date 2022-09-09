import time

# Es perfectamente posible llamar una función dentro de otra 
# Lo hicimos cuando calculamos en volumen de un cilindro 

# Pero también es perfectamente posible que una función se llame a si misma 
# Esto es una técnica muy poderosa para ciertos problemas 

# función conteo regresivo
# Es una función que se llama a si mismo 
def countdown(number):
    if number <= 0:
        print("KABUMM")
    else:
        print(number)
        time.sleep(0.5)
        countdown(number - 1)
countdown(5)


def super_sum(number):
    if number <= 0:
        return number 
    else:
        return number + super_sum(number - 1)

print(super_sum(3))


# Recursion infinita , sin condición de salida 
# para nada útil, pero entretenida
def infinite():
    infinite()



    



















