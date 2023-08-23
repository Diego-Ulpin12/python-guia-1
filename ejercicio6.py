def main():
    menu = """
    1)Ingresar palabras
    2)Salir
    """
    print(menu)
    opcion = int(input("¿Que opción escogera?: "))
    while opcion != 2:
        palabra = input("Ingrese palabra: ")
        print(palabra[::-1])
        print(menu)
        opcion = int(input("¿Desea continuar?: "))
    
if __name__ == '__main__':
    main()