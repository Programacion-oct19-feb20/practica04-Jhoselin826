"""
  @autor:Jhoselin826
  nombre:ejercicio6.py
  descripción: ...

  Jhoselin Guachizaca -- 17
  Su suma de notas es: 30
  su promedio es: 15
"""

nombre = input("Ingrese su nombre: ")

edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de su nota 1: ")
nota2 = input("Ingrese el valor de su nota 2: ")

suma = int(nota1) + int(nota2);
promedio = int(suma) / 2

print("%s -- %s\nSu suma de notas es %s\nSu promedio es %s" % 
	(nombre , edad, suma, promedio))
