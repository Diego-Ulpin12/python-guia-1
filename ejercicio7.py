def main():
    num_factorial = int(input("Ingrese el número: "))
    val_ant = 1
    val_sig = 2
    while (val_sig <= num_factorial):
        factorial = val_ant * val_sig
        val_ant = factorial
        val_sig = val_sig + 1
    print(f"El factorial de {num_factorial} es {factorial}")
    
if __name__ == '__main__':
    main()