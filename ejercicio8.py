def areaCirculo (pi,radio):
    return pi * (radio ** 2)

def volumenCilindro(pi, altura, radio):
    area_circulo = areaCirculo(pi, radio)
    return area_circulo * altura

def main():    
    radio = int(input("Ingrese el radio del circulo: "))
    altura = int(input("Ingrese altura del cilindro: "))
    pi = 3.14
    area = areaCirculo(pi,radio)
    volumen = volumenCilindro(pi, altura, radio)
    print(f'El area del circulo es de {area} y el volumen del cilindro es de {volumen}')
    
if __name__ == '__main__':
    main()