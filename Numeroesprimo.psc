Algoritmo numeroesprimo
	//definimos variables
    definir Num, divisor, contador como entero
	//colocamos valores
    divisor = 1
    contador = 0
    
    //se le pide al usuario ingresar el número
    Escribir("Por favor, ingrese el número:")
    Leer Num
    //empezamos  con la selectiva si, para descartar las excepciones que son el 2 y números negativos
    Si Num == 2 Entonces
        Escribir("2 Tiene una peculiaridad: es el único número par que es primo :D")
			Sino Si Num <= 1 Entonces;
			Escribir(" Tiene una peculiaridad: al no ser mayor a 1, no es primo :(.")
		Sino
			//mientras para calcular si no se cumple las anteriores con la selectiva para ver los casos y asi terminar con la secuencia
			Mientras divisor <= Num Hacer
				Si Num % divisor == 0 Entonces;
                contador = contador + 1
				Fin Si
				divisor = divisor + 1
				Si contador > 3 Entonces;
				Fin Si
					Si divisor >= 101 Entonces;
            Fin Si
		Fin Mientras
       //el si para determinar si es primo o no con las siguientes condiciones 
        Si contador == 2 Entonces;
            Escribir "El número ", Num, " SI es primo";
        Fin Si
        Si contador >= 3 Entonces;
            Escribir "El número ingresado que es: ", Num, " NO es primo "
        Fin Si
    Fin Si
FinSi

FinAlgoritmo
