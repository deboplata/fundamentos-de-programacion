#El numero es primo?

#Se definen las variables

Num = int
divisor = int
contador = int
continuar = str

#se declaran las variables

divisor = 1
contador = 0
continuar = "SI"


#pedir al usurio ingresar el número

Num =int(input("Por favor, ingrese el número: "))

#Condiconal if/elif(si) para interpretar los casos en el cual el usuario ingrese 2 o algun número negativo.

if Num == 2:
    print("2 Tiene una peculiaridad: es el único número par que es primo :D")
elif Num <= 1:
    print(" Tiene una peculiaridad: al no ser mayor a 1,  no es primo :(." )

#En caso de que no se cumpla el si, el algoritmo poondra a prueba el condicional else(si no).
else:

#El ciclo while, mientras que el número divisor(comienza en uno), al ser dividido con Num (que seria el dividendo) no de como residuo 0, se le sumaruná  número al divisor.
#Ejemplo: Si antes el divisor era 1, ahora pasa a ser 2, si aún no se logra que el residuo de 0, pasara a 3, hasta lograr que el residuo de 0.


    while divisor <= Num:

#Este condicional es el que informa al algoritmo si encuentra algún divisor, sumándole uno a la variable "contador"(su valor inicial es 0).

        if Num % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1

#En caso de que el contador llegue a ser mayor a 3, automáticamente se considera al número como NO primo y el programa termina.

        if contador >3:
            break
        if divisor >= 101:
            print("El número ingresado SI es primo")
            break

#En caso de que el número sea primo, solo tendrá dos divisores
    
    
    if contador == 2:
        print("El número ", Num, " SI es primo")

#En caso de que el número tenga 3 o más divisores, hace que este automáticamente deje de ser un número primo

    if contador >= 3:
        print("El número ingresado que es:", Num, "NO es primo")
