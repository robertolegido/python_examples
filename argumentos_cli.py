import sys

print('Modulo importado sys')
print('')
print("Los argmentos son: ", sys.argv)

print('')
print('Nombre del script en ejecucion: ', sys.argv[0])

print('\n\nsuma de parametros\n\n')
numero1 = sys.argv[1]
numero2 = sys.argv[2]

try:
	numero1 = float(numero1)
	numero2 = float(numero2)
	total = numero2 + numero1
	print("La suma es: ", total)
except (NameError, ValueError, IndexError):
    print("Oops!  No has introducido dos numeros.  Prueba otra vez...")



