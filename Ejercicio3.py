texto = input("Ingrese un texto de su preferencia: ")
texto = texto.lower()# caracteres del texto en minusculas
letra1 = input("Ingrese primera letras de su eleccion:  ")
letra1 = letra1.lower()#caracter letra1 en minuscula
letra2 = input("Ingrese la segunda letras de su eleccion:  ")
letra2 = letra2.lower()#caracter letra2 en minuscula
letra3 = input("Ingrese primera letras de su eleccion:  ")
letra3 = letra3.lower()#caracter letra3 en minuscula
# Primer Punto
print(f"La letra: {letra1} se encuentra " , texto.count(letra1), "veces")
print(f"La letra: {letra2} se encuentra " , texto.count(letra2), "veces")
print(f"La letra: {letra3} se encuentra " , texto.count(letra3), "veces")
listaLetras = []
listaLetras.append(letra1)
listaLetras.append(letra2)
listaLetras.append(letra3)
print(listaLetras)
divisionLetras = [texto.split()]
print(len(texto))

for index, item in enumerate(texto):
    print([index, '::', item])

# Quinto punto
if(texto.find('python') == 0):
    print("La palabra python si se encuentra ene el texo")
else:
    print("La palabra python no se encuentra en el texto")