#Realice un programa en Python que al crear un diccionario que tenga 5 registros de la poblacion de cada pais, 
# realice una busqueda del mismo y me muestre en la pantalla el pais y la poblacion del mismo. Puede agregar los paises y numero de población que ud desee. 
# Debe validar que al ingresar un pais que no este registrado en el diccionario, enviar un mensaje que no esta registrado dicho pais.
import msvcrt
paises ={
    "Honduras":"8,000,000",
    "China":"1200,000,000",
    "Canada":"300,000,000",
    "Mexico":"150,000,000",
    "Panama":"5,000,000"
}

buscar=input("Introduce el nombre de un pais: ")
print("Resultado: ",paises.get(buscar,"Este pais no esta registrado"))

msvcrt.getch()