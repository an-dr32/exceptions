import os
import sys

try:
    #pedir al usuario que ingrese dos numeros
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    # Realizar la division
    resultado = num1 / num2

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else: 
    # Este bloque se ejecutara si no se produjo ninguna excepcion
    print(f"El resultado de la division es: {resultado}")

finally:
    print("Gracias por usar la calculadora.")
    
    #Reiniciar o cerrar el programa
    restart = input("\nDeseas hacer otra division? [y/n] > ")

    if restart == "y":
        #Primero importar las librerias os y sys, 
        #sys.executable: ejecutable de python, 
        #os.path.abspath(__file__): el archivo de python que estas ejecutando, 
        #*sys.argv: argumento restante
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    else:
        print("\nAdios...")
        sys.exit(0)