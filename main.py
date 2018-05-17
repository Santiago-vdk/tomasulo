import sys

################# Definicion de instrucciones ##############

instrucciones_total = ["L.D", "MUL.D", "SUB.D", "S.D", "ADD.D"]

############################################################

archivo = "/Users/vdek/Desktop/Algoritmos Arqui/Codigo.asm"

instrucciones = []

estaciones = [[], [], [], [], [], [], []]   # Estaciones posibles 10

memoria = []

operaciones = ["L.D","MUL.D", "SUB.D","S.D","ADD.D"]

# Declaracion de Registros
registros = {'F0': 0, 'F1': 0, 'F2': 0,'F3': 0, 'F4': 0, 'F5': 0,'F6': 0, 'F7': 0, 'F8': 0, 'F9': 0,
             'R0': 0, 'R1': 0, 'R2': 0,'R3': 0, 'R4': 0, 'R5': 0,'R6': 0, 'R7': 0, 'R8': 0, 'R9': 0,
             'G0': 0, 'G1': 0, 'G2': 0,'G3': 0, 'G4': 0, 'G5': 0,'G6': 0, 'G7': 0, 'G8': 0, 'G9': 0}




def extraerOperandos(line, i):
    line = line.split(" ")
    line[-1] = line[-1].replace("\n","")
    return line


# Parseo en tuplas y lista de instrucciones
with open(archivo) as file:
    i = 0
    for l in file:
        instrucciones.append(extraerOperandos(l, i))
        i += 1



# Itero sobre las estaciones para llenarlas
i = 0
while(i<len(estaciones)):
    if(i >= len(instrucciones)):
        break
    estacion = []
    estacion.append(instrucciones[i][0])    # Name
    estacion.append(1)                      # Busy
    estacion.append(instrucciones[i][0])    # OP
    
    if(instrucciones[i][0] == "L.D" or instrucciones[i][0] == "S.D"):
        estacion.append( instrucciones[i][1] )    # Vj
        estacion.append(int(instrucciones[i][2]) + registros[ str(instrucciones[i][3]) ])       # Vk
    else:
        estacion.append( instrucciones[i][1] )    # Vj
        estacion.append(instrucciones[i][3] )     # Vk

    estacion.append(0)
    estaciones[i] = estacion                # Push estacion
    i += 1



# Enumeracion de instrucciones repetidas
i = 0
j = 0
k = 0
while(i<len(instrucciones)):
    instru = instrucciones[i]   # Extraigo la instruccion para compararla con las demas
    
    # Iteracion interna
    while(j<len(instrucciones)):
        
        if(instrucciones[j][0] == instru[0]):       # Comparacion de nombres
            estaciones[j][-1] = instru[0] + str(k)
            k += 1
        j += 1

    j = 0
    k = 0
    i += 1


# Ajuste de nombres
i = 0
while(i<len(instrucciones)):
    estaciones[i][0] = estaciones[i].pop()
    i += 1



# Deteccion de riesgos 1
i = 0
j = 0

while(i<len(instrucciones)):
    instru = instrucciones[i]
    estacion = estaciones[i]
    
    # Iteracion interna
    while(j<len(instrucciones)):
        if(instru != instrucciones[j]):     # Si la instruccion que estoy evaluando no es la misma
            
            if(instru[1] == instrucciones[j][2]):         # Comparar resultado con primer operando Qj
                # Hay riesgo
                estaciones[j].append(estacion[0])
        j += 1
    j = 0
    i += 1


# Insercion de 0 en caso de no darse la condicion
i = 0
while(i<len(estaciones)):
    if(len(estaciones[i]) == 5):
        estaciones[i].append(0)
    i += 1





# Deteccion de riesgos 2
i = 0
j = 0

while(i<len(instrucciones)):
    instru = instrucciones[i]
    estacion = estaciones[i]
    
    # Iteracion interna
    while(j<len(instrucciones)):
        if(instru != instrucciones[j]):     # Si la instruccion que estoy evaluando no es la misma
            
            if(instru[1] == instrucciones[j][3]):         # Comparar resultado con segundo operando Qk 
                # Hay riesgo
                estaciones[j].append(estacion[0])
        j += 1
    j = 0
    i += 1


# Insercion de 0 en caso de no darse la condicion
i = 0
while(i<len(estaciones)):
    if(len(estaciones[i]) == 6):
        estaciones[i].append(0)
    i += 1




# Deteccion de riesgos 3
i = 0
j = 0

while(i<len(instrucciones)):
    instru = instrucciones[i]
    estacion = estaciones[i]
    
    # Iteracion interna
    while(j<len(instrucciones)):
        if(instru != instrucciones[j]):     # Si la instruccion que estoy evaluando no es la misma
            
            if(instru[1] == instrucciones[j][1]):         # Comparar resultado con resultado Rout 
                # Hay riesgo
                estaciones[j].append(estacion[0])
        j += 1
    j = 0
    i += 1


# Insercion de 0 en caso de no darse la condicion
i = 0
while(i<len(estaciones)):
    if(len(estaciones[i]) == 7):
        estaciones[i].append(0)
    i += 1

# Agregar indice para operacion
i = 0
while(i<len(estaciones)):
    if(estaciones[i][2] in operaciones):
        if(estaciones[i][2] == "L.D"):
            estaciones[i].append(5)
        elif(estaciones[i][2] == "MUL.D"):
            estaciones[i].append(3)
        elif(estaciones[i][2] == "SUB.D"):
            estaciones[i].append(2)
        elif(estaciones[i][2] == "S.D"):
            estaciones[i].append(4)
        elif(estaciones[i][2] == "ADD.D"):
            estaciones[i].append(1)
        else:
            print("Error")
    i += 1


# Bandera de riesgo 
i = 0
while(i<len(estaciones)):
    if((estaciones[i][4] and estaciones[i][4] and estaciones[i][4]) == 0):
        estaciones[i].append(0)
    else:
        estaciones[i].append(1)
    i += 1


print("\n")
k = 0
while(k<len(estaciones)):
    print(estaciones[k])
    k += 1