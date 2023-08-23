import random

def main():
    num_azar = random.randint(1,100)
    numero = int(input("Ingrese número: "))
    while(numero != num_azar):
        if numero > num_azar:
            print(f"El número {numero} ingresado esta por encima del número generado")
        elif numero < num_azar:
            print(f"El número {numero} ingresado esta por debajo del número generado")
        numero = int(input("Ingrese número: "))
    print(f"El número {numero} es igual al número generado")

if __name__ == '__main__':
    main()