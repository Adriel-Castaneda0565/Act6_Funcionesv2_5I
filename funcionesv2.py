print("Mas sobre funciones")
#Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def resta_ab(a,b):
    r=a-b
    return r

def mult_ab(a,b):
    m=a*b
    return m

def div_ab(a,b):
    d=a/b
    return d

#Llamada a funciones
print("\nCalculando suma")
n1=int(input("Ingresa el primer numero: "))
n2=int(input("Ingresa el segundo numero: "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")

print("\nCalculando resta")
n3=int(input("Ingresa el primer numero: "))
n4=int(input("Ingresa el primer numero: "))
resta=resta_ab(n3,n4)
print(f"La suma de {n3} + {n4} es: {resta}")

print("\nCalculando multiplicacion")
n5=int(input("Ingresa el primer numero: "))
n6=int(input("Ingresa el primer numero: "))
multi=mult_ab(n5,n6)
print(f"La suma de {n5} + {n6} es: {multi}")

print("\nCalculando division")
n7=int(input("Ingresa el primer numero: "))
n8=int(input("Ingresa el primer numero: "))
div=div_ab(n7,n8)
print(f"La suma de {n7} + {n8} es: {div}")
