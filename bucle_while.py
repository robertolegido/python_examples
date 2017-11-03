# Bucles mientras la condicion dada es cierta
# Recorrer los elementos de array y tuples!!

contador = 0
final = 5

while (contador < final):
	print('El valor del contador es:', contador)
	#contador = contador + 1
	contador += 1

# Condiciones
print('Condicione en bucle')
print('')

while (contador < final):
	print('El valor del contador es:', contador)
	#contador = contador + 1
	contador += 1
else: 
	print('El valor de contador:' , contador, 'no es menor que: ', final)


# Breaks
print('Breaks')
print('')
start = 1 
end = 5

while (start < end):
	print('El valor de start es: ', start)
	if (start==2): 
		print('Si el valor de start es 2 para')
		break
	start += 1


# Recorrer los elementos
print('Elementos de array')
index = 0
lista = [7, 8, 9, 10, 'ja ja']

while (index < len(lista)):
	print('El valor de elemento en la posicion ', index, ' de la lista es: ', lista[index])
	index += 1
