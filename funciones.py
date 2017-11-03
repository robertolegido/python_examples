def saludo():
	#print('hola holita')
	return('Hola holita ')

print(saludo())

#Funcion con un argumento
def escribir(cadena):
	return(cadena)

print(escribir('caca'))

#Funcion de varios argumentos
print('\n\n')
def restar(numero1, numero2):
	try:
		num1=float(numero1)
		num2=float(numero2)
		resta = num1 - num2
		return(resta)
	except (ValueError, NameError):
		print('No has puesto numeros')

print('Ejemplo resta')
a=input("Numero 1: ")
b=input("Numero 1: ")
print(restar(a,b))