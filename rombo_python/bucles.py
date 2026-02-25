# Crea un programa que pinte un rombo de asteriscos con un número de filas indicado por el usuario.
numero = int(input("Introduce el número de filas de la parte superior para el rombo de asteriscos: "))
# Parte superior
# i comienza en 0 y va hasta numero-1, lo que nos da el número correcto de filas para la parte superior del rombo
# i es el número de fila actual, comenzando desde 0 y es el número de filas que se pintan en la parte superior del rombo.
# En cada iteración de i, se pintan tantos espacios como el número de filas menos i menos 1, y luego se pintan tantos asteriscos como el doble de i más 1.
# Primera vuelta del bucle: i=0, numero=5, se pintan 4 espacios y 1 asterisco.
# Segunda vuelta del bucle: i=1, numero=5, se pintan 3 espacios y 3 asteriscos.
# Tercera vuelta del bucle: i=2, numero=5, se pintan 2 espacios y 5 asteriscos.
# Cuarta vuelta del bucle: i=3, numero=5, se pintan 1 espacio y 7 asteriscos.
# Quinta vuelta del bucle: i=4, numero=5, se pintan 0 espacios y 9 asteriscos.
# El bucle interno con la variable j se encarga de imprimir los espacios necesarios antes de los asteriscos, y el bucle interno con la variable k se encarga de imprimir los asteriscos.
# j comienza en 0 y va hasta numero - i - 1, lo que nos da el número correcto de espacios para cada fila. Por tanto, en la primera vuelta del bucle, se imprimen (numero - i -1)= (5 -0 -1 )= 
# 4 espacios (cuando i=0), luego 3 espacios (cuando i=1), luego 2 espacios (cuando i=2), luego 1 espacio (cuando i=3) y finalmente 0 espacios (cuando i=4).
# k comienza en 0 y va hasta 2 * i + 1, 
# (2 * 0 + 1) cuando i = 0. Por tanto, en la primera vuelta del bucle, se imprimen (2 * i + 1) = (2 * 0 + 1) = 1 asterisco (cuando i=0), luego 3 asteriscos (cuando i=1), luego 5 asteriscos (cuando i=2), luego 7 asteriscos (cuando i=3) y finalmente 9 asteriscos (cuando i=4).

for i in range(numero):
    # Espacios
    for j in range(numero - i - 1):
        print(" ", end="")
        
    # Asteriscos (ahora usamos k)
    for k in range(2 * i + 1):
        print("*", end="")
        
    print()

# Parte inferior
# La variable i comienza valiendo el valor de numero - 2 y va disminuyendo hasta llegar a -1 (excluyendo -1). Esto se hace para pintar la parte inferior del rombo, que tiene una fila menos que la parte superior.
# En cada iteración de i, se pintan tantos espacios como el número de filas menos i menos 1, y luego se pintan tantos asteriscos como el doble de i más 1.
# Los tres argumentos de range()
#El primer argumento, numero - 2, es el valor inicial. Si el usuario ingresó 5, esta expresión evalúa a 5 -2 = 3. El bucle comenzará desde este número.
#El segundo argumento, -1, es el valor de parada (exclusivo). El bucle continuará mientras el valor sea mayor que -1, pero nunca alcanzará el -1 mismo. Esto es fundamental en Python: el valor de parada siempre se excluye del rango.
#El tercer argumento, -1, es el valor de incremento. El bucle irá decrementando i en 1 en cada iteración. Al inicio i vale numero - 2 por tanto vale 5 -2 = 3, y se ira decrementando en cada iteración: 3, luego 2, luego 1, luego 0, y finalmente -1 (en este punto el bucle se detiene porque -1 no es mayor que -1) y ahi ya no pinta nada más porque ha llegado al valor de parada.

for i in range(numero - 2, -1, -1):
    # Espacios
    for j in range(numero - i - 1):
        print(" ", end="")
        
    # Asteriscos (usamos k también aquí)
    for k in range(2 * i + 1):
        print("*", end="")
        
    print()