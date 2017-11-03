#Operadores de comparacion
# Igual ==
# Distinto !=
# Mayor que >
# Mayor o igual que >=
# Menor o igual que <=
# Menor que <

variable = 1

if(variable == 1):
	#Condicion es cierta
	print('condicion es verdadera')
else:
	#Condicion no es cierta
	print('la condicion es falsa')

variable = 2
if (variable < 1):
	print(variable, ' es menos que 1')
elif (variable == 2):
	print (variable, 'es igual a 2')
else:
	pritn ('caca')


print("")
print("")

# Operadores logicos
# la condicion es cierta and 
# al menos una condicion es cierta or
# la condicion no es cierta not
var1 = 1
var2 = 1
var3 = 3

if (var1 == var2 and var1 < var3):
	print('dos condicionnes son verdadero')

if not (var2 > var3):
	print ('la condicion esta negada')


# Operador membership
# Comprueban valores en strings, lists y tuples
# El valor es encontrado in 
# El valor no es encontrado not in

lista = ['bromis', 'in', 'the', 'air']

if ("bromis" in lista):
	print("Ha aparecido bromis en la lista")
else: 
	print('No ha aparecicho')




