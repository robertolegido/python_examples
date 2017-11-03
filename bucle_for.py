#El bucle for 
# Range
start = 0
end = 10

print("")
print("Bucle incremental con un indice")
for i in range (start, end):
	print('El valor de indice es: ', i)


#Tuples
print("")
print("Recorrer un array/tuples")

nombres = ('Harry', 'ouh yeah')
for z in range (len(nombres)):
	print ('El valor de la posicion, ', z,' del tuple es: ', nombres[z])

#Otra forma alternativa
print('')
contador = 0
for z in nombres:
	print('El valor de la posicion, ', contador ,'es: ', z)
	contador = contador + 1

#Anadir una condicion
print('')
print('Incluir una condicion')
for w in range(len(nombres)):
	print('El contenido es: ', nombres[w])
else:
	print('Ya no hay mas')

#Diccionarios
dic = {1:"esto", 2:"es", 3:"una prueba"}
for clave,valor in dic.items():
	print('la clave es: ', clave, 'con valor: ', valor)
