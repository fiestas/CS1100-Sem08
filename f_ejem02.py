# definir varias funciones

def suma_cuadrados(N):
    suma = 0
    for i in range(1, N + 1):
       suma += i * i  #   suma=suma+i*i
    return suma

def main():
    a=int(input("ingrese un valor: "))
    print("la suma de cuadrados hasta %d es: %f"%(a,suma_cuadrados(a)))


if (__name__== "__main__"):
    main()