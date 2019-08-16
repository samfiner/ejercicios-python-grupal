diccionario={}
palabra=input("dijite la palabra, seguido de dos puntos coloque su significado")
par=palabra.split(":")
llave=par[0]
valor=par[1]
diccionario.update({llave:valor})
print(diccionario)

