#!/usr/bin/python
#-*- Coding: utf-8 -*-

nota1 = float(raw_input("Nota de Primer Corte:" ))

nota2 = float(raw_input("Nota de Segundo Corte: "))

nota3 = float(raw_input("Nota de Tercer Corte: "))

promedio = (float(nota1) + float(nota2) + float(nota3)) / 3

print ""
print "Su Promedio es de: " , ("%.2f" % promedio)

print ""
if promedio >= 3:
    print "Aprovado"
else:
    print "Suspendido"
