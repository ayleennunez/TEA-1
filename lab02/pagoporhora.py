# Tendencias e Innovacion en Tecnologia Agricola (TEA)
horas = input("numero de horas trabajadas? ")
valorPorhora = input("valor por hora? ")

# se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# calculando el valor total de las horas trabajadas
total=int(horas)*float(valorPorhora)
print(total)