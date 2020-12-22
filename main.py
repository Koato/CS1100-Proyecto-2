import sys
import os
import copy
from Funciones import *

matriz_alumnos = [[201910512,"jose diaz", 11,11,12,13,11,15,12,16,14],
[202019214,"eduardo lujan", 17,11,12,13,11,15,12,16,14],
[201920918,"luis casanova", 18,11,12,13,11,15,12,16,14],
[202023412,"fernando gutierrez",11,20,12,13,11,15,12,16,14],
[201920912,"mauricio castro",11,11,12,13,11,15,12,16,14],
[201812153,"carlos quispe", 11,11,12,13,20,12,12,16,14],
[201919812,"victor peña", 11,11,7,13,11,9,12,16,11],
[201820123,"mark ventura", 16,17,17,19,17,15,16,17,19],
[202015612,"juan mendoza", 20,11,12,13,14,15,12,16,14],
[201910912, "carlos justino", 12,13,12,16,20,12,10,11,12],
[201920913, "miguel villarubia", 11, 18, 19, 16, 20, 20, 11, 14, 13],
[202019812, "tony vicente", 12,20,18,16,20,12,10,16,15],
[201820198, "francis escalante", 15,19,15,16,20,12,10,19,12],
[201913467, "lidia zegarra", 13,13,12,15,20,20,19,13,17],
];

def notas_formulas(opcion,nota_escogida):
	reopcion=0
	if(nota_escogida==1):
		reopcion=2
	elif(nota_escogida==2):
		reopcion=3
	elif(nota_escogida==3):
		reopcion=4
	elif(nota_escogida==4):
		reopcion=5
	elif(nota_escogida==5):
		reopcion=6
	elif(nota_escogida==6):
		reopcion=7
	elif(nota_escogida==7):
		reopcion=8
	elif(nota_escogida==8):
		reopcion=9
	elif(nota_escogida==9):
		reopcion=10

	if(opcion==1):
		return nota_max(matriz_alumnos,reopcion)
	elif(opcion==2):
		return nota_min(matriz_alumnos,reopcion)
	elif(opcion==3):
		return promedio(matriz_alumnos,reopcion)
	elif(opcion==4):
		return moda(matriz_alumnos,reopcion)
	elif(opcion==5):
		return desviacion_media(matriz_alumnos,reopcion)
	elif(opcion==6):
		return varianza(matriz_alumnos,reopcion)
	elif(opcion==7):
		return desviacion_standard(matriz_alumnos,reopcion)

def submenu():
	print('\n')
	while(True):
		print("1. La nota maxima y la cantidad de alumnos que la obtuvieron.")
		print("2. La nota minima y la cantidad de alumnos que la obtuvieron.")
		print("3. La Media o el promedio.")
		print("4. La moda o frecuencia.")
		print("5. La desviacion respecto de la media.")
		print("6. La varianza.")
		print("7. La desviacion standard.")
		print("8. Salir")
		print(' ')
		opcion=int(input("Digite una opcion :"))
		if(opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5 or opcion==6 or opcion==7):
			print("\n1. E1.")
			print("2. C1.")
			print("3. C2.")
			print("4. PC1.")
			print("5. PC2.")
			print("6. PC3.")
			print("7. PC4.")
			print("8. P1.")
			print("9. P2.")
			print(" ")
			nota_escogida=int(input("Ahora escoja una nota : "))
			notas_formulas(opcion,nota_escogida)		

		elif(opcion==8):
			break
		else:
			print("\nError, digite solo una de esta opciones .")

def opcion_3():
	nueva_matriz=[]
	for i in range(len(matriz_alumnos)):
		nota_final=0
		lista=[]
		count=0
		for j in matriz_alumnos[i]:
			if(count==0 or count==1):
				lista.append(j)
			elif(count==2):
				nota_final = nota_final + float(j*0.4)
			elif(count==3 or count==4):
				nota_final = nota_final + float(j*0.04)
			elif(count==5 or count==6 or count==7 or count==8):
				nota_final = nota_final + float(j*0.09)
			elif(count==9 or count==11):
				nota_final = nota_final + float(j*0.08)
			count=count+1
		lista.append(nota_final)
		nueva_matriz.append(lista)


	for i in range(len(nueva_matriz)):
		cont=0
		for j in nueva_matriz[i]:
			if(cont==2):
				print("%.2f" %j)
			else:
				print(j, end = '')
				print("   ", end = '')
			cont=cont+1
	print('\n')

def notaValida(n):
    if n.isdigit():
        n = int(n)
        print("Ingrese una nota valida :")
        print("\n")
        if 0 < n < 21:
            n = int(n)
            return n
        n = -1
        return n
    else:
        print("Ingrese una nota valida :")
        print("\n")
        n = -1
        return n

def opcion_2():
	lista=[]
	E1, C1, C2, PC1, PC2, PC3, PC4, P1, P2 = -1, -1, -1, -1, -1, -1, -1, -1, -1
	print("\n")
	lista.append(input("Agregue el codigo :"))
	lista.append(input("Agregue el nombre :"))
	while E1 < 0 or E1 > 20:
		E1 = input("Agregue la nota de E1 :")
		E1 = notaValida(E1)
		if E1 != -1:
			lista.append(E1)
	while C1 < 0 or C1 > 20:
		C1 = input("Agregue la nota de C1 :")
		C1 = notaValida(C1)
		if C1 != -1:
			lista.append(C1)
	while C2 < 0 or C2 > 20:
		C2 = input("Agregue la nota de C2 :")
		C2 = notaValida(C2)
		if C2 != -1:
			lista.append(C2)
	while PC1 < 0 or PC1 > 20:
		PC1 = input("Agregue la nota de PC1 :")
		PC1 = notaValida(PC1)
		if PC1 != -1:
			lista.append(PC1)
	while PC2 < 0 or PC2 > 20:
		PC2 = input("Agregue la nota de PC2 :")
		PC2 = notaValida(PC2)
		if PC2 != -1:
			lista.append(PC2)
	while PC3 < 0 or PC3 > 20:
		PC3 = input("Agregue la nota de PC3 :")
		PC3 = notaValida(PC3)
		if PC3 != -1:
			lista.append(PC3)
	while PC4 < 0 or PC4 > 20:
		PC4 = input("Agregue la nota de PC4 :")
		PC4 = notaValida(PC4)
		if PC4 != -1:
			lista.append(PC4)
	while P1 < 0 or P1 > 20:
		P1 = input("Agregue la nota de P1 :")
		P1 = notaValida(P1)
		if P1 != -1:
			lista.append(P1)
	while P2 < 0 or P2 > 20:
		P2 = input("Agregue la nota de P2 :")
		P2 = notaValida(P2)
		if P2 != -1:
			lista.append(P2)
	matriz_alumnos.append(lista)
	print("")
	print("Alumno agregado con exito!")
	print("\n")


def opcion_1(matriz):
	for i in range(11):
		if(i==0):
			print("codigo   ", end = '')
		elif(i==1):
			print("   nombre   ", end = '')
		elif(i==2):
			print("   E1      ", end = '')
		elif(i==3):
			print("    C1      ", end = '')
		elif(i==4):
			print("    C2      ", end = '')
		elif(i==5):
			print("    PC1     ", end = '')
		elif(i==6):
			print("    PC2     ", end = '')
		elif(i==7):
			print("    PC3     ", end = '')
		elif(i==8):
			print("    PC4     ", end = '')
		elif(i==9):
			print("    P1      ", end = '')
		elif(i==10):
			print("    P2 ",)
	for i in range(len(matriz)):
		for j in matriz[i]:
			print(j, end = '')
			for k in range(12 - len(str(j))):
				print(' ', end = '')
		print('')
	print("\n")

def opcion_5(matriz):
	file = open("alumnos.txt", "w", encoding = "utf-8")
	file.write("Código Nombre Apellido 9 notas" + os.linesep)
	for i in range(len(matriz)):
		for j in matriz[i]:
			file.write(str(j).title() + ' ')
		file.write("\n")
	file.close()

def opcion_6():
	archivo = open('alumnos.txt', 'r', encoding = "utf-8")
	archivo.__next__()
	archivo.__next__()
	for linea in archivo.readlines():
		lista = []
		x = linea.split(" ")
		lista.append(int(x[0]))
		lista.append('' + x[1] + " " + x[2] + '')
		lista.append(int(x[3]))
		lista.append(int(x[4]))
		lista.append(int(x[5]))
		lista.append(int(x[6]))
		lista.append(int(x[7]))
		lista.append(int(x[8]))
		lista.append(int(x[9]))
		lista.append(int(x[10]))
		lista.append(int(x[11]))
		matriz_alumnos.append(lista)
	archivo.close()

def opcion_7():
	lista = obtener_ponderado()
	for f in range(len(lista)):
		for actual in range(len(lista) - 1):
			siguiente_elemento = actual + 1
			if lista[actual].split(" ")[2] > lista[siguiente_elemento].split(" ")[2]:
				lista[siguiente_elemento], lista[actual] = lista[actual], lista[siguiente_elemento]
	file = open("promedios.txt", "w", encoding = "utf-8")
	file.write("Nombre Apellido Promedio ponderado" + os.linesep)
	for i in reversed(range(len(lista))):
		file.write(str(lista[i]).title() + "\n")
	file.close()

def obtener_ponderado():
	matriz_alumnos_copia = copy.deepcopy(matriz_alumnos)
	lista = []
	for i in range(len(matriz_alumnos_copia)):
		matriz_alumnos_copia[i].pop(0)
		matriz_alumnos_copia[i].pop(0)
		posicion = 0
		nota = 0
		for j in matriz_alumnos_copia[i]:
			if posicion == 0:
				nota += j * 0.4
			elif posicion == 1 or posicion == 2:
				nota += j * 0.04
			elif posicion == 3 or posicion == 4 or posicion == 5 or posicion == 6:
				nota += j * 0.09
			elif posicion == 7 or posicion == 8:
				nota += j * 0.08
			posicion += 1
		lista.append(matriz_alumnos[i][1] + ' ' + str(round(nota, 2)))
	return lista

def opcion_8():
	print("1. E1.")
	print("2. C1.")
	print("3. C2.")
	print("4. PC1.")
	print("5. PC2.")
	print("6. PC3.")
	print("7. PC4.")
	print("8. P1.")
	print("9. P2.")
	print(" ")
	nota_escogida=int(input("Indique el rubro de evaluación : "))
	
	file = open("analisis.txt", "w", encoding = "utf-8")
	file.write("Nombre del rubro de evaluación: " + str(nota_escogida) + "\n")
	file.write(notas_formulas(1, nota_escogida) + "\n")
	file.write(notas_formulas(2, nota_escogida) + "\n")
	file.write(notas_formulas(3, nota_escogida) + "\n")
	file.write(notas_formulas(4, nota_escogida) + "\n")
	file.write(notas_formulas(5, nota_escogida) + "\n")
	file.write(notas_formulas(6, nota_escogida) + "\n")
	file.write(notas_formulas(7, nota_escogida) + os.linesep)
	file.close()

def menu():
	opcion=0
	while(True):
		print("1.Mostrar la base de los alumnos registrados.")
		print("2.Agregar la informacion de un alumno.")
		print("3.Mostrar el promedio de todos los alumnos.")
		print("4.Submenu de notas.")
		print("5.Grabar en archivo.")
		print("6.Leer información del archivo.")
		print("7.Reporte.")
		print("8.Reporte de análisis de un rubro de evaluación.")
		print("9.Salir.")
		print("\n")
		opcion=input("Digita la opcion : ")
		if opcion.isdigit():
			opcion = int(opcion)
			if(opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 
			or opcion == 5 or opcion == 6 or opcion == 7 or opcion == 8):
				if(opcion == 1):
					opcion_1(matriz_alumnos)
				elif(opcion == 2):
					opcion_2()
				elif(opcion == 3):
					opcion_3()
				elif(opcion == 4):
					submenu()
				elif(opcion == 5):
					opcion_5(matriz_alumnos)
				elif(opcion == 6):
					opcion_6()
				elif(opcion == 7):
					opcion_7()
				elif(opcion == 8):
					opcion_8()
			elif(opcion == 9):
				sys.exit(1)
			else:
				print("Digite de nuevo una de la opciones")
				print("\n")
		else:
			print("Digite de nuevo una de la opciones")
			print("\n")

menu()