def main():
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese una letra: ")
    cont = 0
    for letter in palabra:
        if letter == letra:
            cont = cont + 1
    print(f"La letra {letra} aparece {cont} veces en la palabra {palabra}")
    
if __name__ == '__main__':
    main()