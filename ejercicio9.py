def palabraLarga(list):
    nuevoLargo = 0
    for i in range(len(list)):
        largo = len(list[i])
        if largo > nuevoLargo:
            nuevoLargo = largo
            masLargo = list[i]
    return masLargo

def main():
    cantPalabras = int(input("¿Cuántos palabras desea agregar?: "))
    lista = []
    while(len(lista) != cantPalabras):
        palabra = input("Ingrese palabra: ")
        lista.append(palabra)
    print(lista)
    largo = palabraLarga(lista)
    print(f"La palabra más larga de la lista es {largo}")
    
    
if __name__ == '__main__':
    main()