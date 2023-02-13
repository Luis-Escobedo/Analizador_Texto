print("==========================")
print(" Analizador de textos")
print("==========================")

texto = input("Ingresa un texto: \n\t").lower()

letra1=input("Ahora Ingresa una letra: \n").lower()
letra2=input("Ahora Ingresa otra letra: \n").lower()
letra3=input("Ahora Ingresa otra letra: \n").lower()
mi_lista=[]
mi_lista.append(letra1)
mi_lista.append(letra2)
mi_lista.append(letra3)

print("\nInciando Programa.......\n")

print("====== 1.- Cuantas veces aparece cada letra en el texto =======")
print(f"\nAparecen {texto.count(letra1)} veces la letra {letra1}")
print(f"\nAparecen {texto.count(letra2)} veces la letra {letra2}")
print(f"\nAparecen {texto.count(letra3)} veces la letra {letra3}")

print("\n\n====== 2.- Cuantas palabras tiene el texto =======")
print(f"\nCantidad de palabras {len(texto)}")

print("\n\n====== 3.- Cual es la primera y ultima letra =======")
print(f"\nLa primera letra es {texto[0]} y la ultima letra es {texto[-1]}")

print("\n\n====== 4.- Invertir el Texto  =======")
print(f"\n {texto[::-1]}")
print("\n Se remplaza los espacions por Guines medios -")
lista = texto.split()
e = "-".join(lista)
print(e)
print("\n\n====== 5.- En el texto esta la palabra Python  =======")
valor = "python" in texto

print(f"\n El texto python esta? \nTrue - SI \n False - NO :\n\t{valor}")

print("======= Gracias Por Utilizar el Programa ============")
