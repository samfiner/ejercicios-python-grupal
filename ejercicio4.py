import math
Radio=float(input('Ingrese el radio del circulo: '))
if Radio>=0:
    area=math.pi*Radio**2
    print("El area del circculo es: ",area, "metros cuadrados")
else:
    print ("El radio introducido no es correcto")
