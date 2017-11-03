#Programa para sumar dos numeros

#while True: 
#	try:
#		valor = int(input("Introducir numero 1: "))
#		print('ok')
#		break
#	except ValueError:
#		print('Veste a la mierda')
 

while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except NameError:
         print("Oops!  That was no valid number.  Try again...")