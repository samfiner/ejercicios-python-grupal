diccionario={"cereza":1.35, "ganabana":0.80, "uva":0.85, "pera":0.70}
f=input("ingrese el nombre de la fruta: ")
if(f in diccionario):
    p=float(input("dijite cuantos kilos desea comprar: "))
    total=p*diccionario[f]
    print(" el Total de su compra es: ",total)
else:
    print("En el momento su fruta de seleccion no esta disponible")
