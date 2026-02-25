#Crear un programa que solicite al usuario su nombre y pinte un mensaje de bienvenida. 
nombre = input("Por favor, introduce tu nombre: ")
print(f"¡Bienvenido, {nombre}!")
# Crear un programa que solicite al usuario su color favorito y diga si es un color cálido o frío.
color_favorito = input("¿Cuál es tu color favorito? ")
if color_favorito.lower() in ["rojo", "naranja", "amarillo", "rosa", "morado", "violeta", "magenta", "fucsia", "carmesí", "coral", "salmon", "terracota", "marrón", "dorado", "cobre"]:
    print(f"{color_favorito} es un color cálido.")
elif color_favorito.lower() in ["azul", "verde", "turquesa", "celeste", "cian", "gris", "esmeralda", "jade", "menta", "oliva"]:
    print(f"{color_favorito} es un color frío.")
else: print(f"No tengo información sobre el color que has indicado como  {color_favorito}.")