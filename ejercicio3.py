palabra = (input("Escriba una palabra: "))
contador=0
for i in palabra:
    if((contador%2) == 0):
        print(i)
        contador = 0
    contador+=1
    

