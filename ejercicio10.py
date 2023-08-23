def main():
    mensaje = """
    Lista de Compra
    1) Agregar articulo y precio
    2) Finalizar
    """
    print(mensaje)
    listaCompra = {}
    precioTotal = 0
    opcion = int(input("Ingrese una opción: "))
    while opcion != 2:
        if opcion == 1:
            cantArti = int(input("¿Cuántos articulos desea comprar?: "))
            totalArti = 0
            while totalArti != cantArti:
                articulo = input("Ingrese articulo: ")
                precio = int(input("Ingrese precio del articulo: "))
                precioTotal = precioTotal + precio 
                totalArti = totalArti + 1
                listaCompra[articulo] = precio
            listaCompra['Total'] = precioTotal
            print(listaCompra)
        opcion = int(input("Ingrese una opción: "))
    

if __name__ == '__main__':
    main()