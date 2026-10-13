
PRECIO_ENTRADA = 7

edad = int(input("Dame tu edad"))

precioFinal = PRECIO_ENTRADA
if edad < 5:
    precioFinal = PRECIO_ENTRADA * 0.4
elif edad < 60:
    precioFinal = PRECIO_ENTRADA * 0.45

print("El precio final es: ${:.2f}".format(precioFinal)*)
