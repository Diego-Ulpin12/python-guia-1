def main():
    num_prim = int(input("Ingrese el número: "))
    cont = 0
    for n in range(2, num_prim):
        if num_prim % n == 0:
            cont = cont + 1 
            print(f"{n} es divisor")  
    if cont > 0:
        print(f'El número {num_prim} no es primo')
    else:
        print(f"El número {num_prim} es primo")
    
if __name__ == '__main__':
    main()