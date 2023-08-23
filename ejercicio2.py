def centiPul(centimetros):
    equivalencia = 0.393701
    return (centimetros*equivalencia)/1

def metroKilo(metros):
    equivalencia = 0.001
    return (metros*equivalencia)/1
    
def onzGram(onzas):
    equivalencia = 28.3495
    return (onzas*equivalencia)/1
    
def milKilo(millas):
    equivalencia = 1.60934
    return (millas*equivalencia)/1
    
def celFah(celsius):
    return (celsius*(9/5))+32

def main():
    mensaje = """
    Transformador de Unidades
    1) Centimetros->Pulgadas
    2) Metros->Kilometros
    3) Onzas->Gramos
    4) Millas->Kilometros
    5) Celsius->Fahrenheit
    6) Salir
    """
    print(mensaje)
    opcion = int(input("Ingrese una opción: "))
    while opcion != 6:
        valor1 = float(input("Ingrese el valor a transformar: "))
        if opcion == 1:
            resultado = centiPul(valor1)
        elif opcion == 2:
            resultado = metroKilo(valor1)
        elif opcion == 3:
            resultado = onzGram(valor1)
        elif opcion == 4:
            resultado = milKilo(valor1)
        elif opcion == 5:
            resultado = celFah(valor1)
        else:
            resultado = ""
            print("La opción ingresada no es válida")
        print(f"El resultado de la operación es: {resultado}")
        print(mensaje)
        opcion = int(input("Ingrese una opción: "))


if __name__ == "__main__":
    main()