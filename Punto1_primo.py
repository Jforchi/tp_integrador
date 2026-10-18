#Solicitud de Nro:
def es_primo(numero):
    primo = True
    if numero < 2:
        primo = False  #Los números menores a 2 no son primos
    for i in range(2, numero):
        if numero % i == 0:  #Si la división es exacta, no es primo.
            primo = False
    return primo 

numero = int(input("Numero a verificar: "))
print("Numero ingresado", numero)

if es_primo(numero):
    print ("es nro. primo")
else:
    print ("No es nro. primo")