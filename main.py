import sys

################# Definicion de instrucciones ##############

instrucciones_total = ["L.D", "MUL.D", "SUB.D", "S.D", "ADD.D"]

############################################################

archivo = "/Users/vdek/Desktop/Algoritmos Arqui/Codigo.asm"

instrucciones = []

estaciones = [[], [], [], [], [], [], []]   # Estaciones posibles 7

operaciones = ["L.D","MUL.D", "SUB.D","S.D","ADD.D"]

estado_instruccion = []

# Declaracion de Registros
registros = {'F0': 0, 'F1': 1, 'F2': 2,'F3': 3, 'F4': 4, 'F5': 5,'F6': 6, 'F7': 7, 'F8': 8, 'F9': 9,
             'R0': 0, 'R1': 1, 'R2': 2,'R3': 3, 'R4': 4, 'R5': 5,'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9,
             'G0': 0, 'G1': 1, 'G2': 2,'G3': 3, 'G4': 4, 'G5': 5,'G6': 6, 'G7': 7, 'G8': 8, 'G9': 9}

memoria = []

i = 0
while(i<50):
    memoria.append(i)
    i += 1



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
        estacion.append( instrucciones[i][2] )    # Vj
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



matriz_oper_resultados = []
# Guardado de operadores resultado
i = 0
while(i<len(instrucciones)):
    operando = instrucciones[i][1] 
    nombre = estaciones[i][0]
    val = []
    val.append(nombre)
    val.append(operando)
    matriz_oper_resultados.append(val)
    i += 1
    



# Deteccion de riesgos 1
i = 0
j = 0
while(i<len(instrucciones)):
    instru = instrucciones[i]
    estacion = estaciones[i]
        
    # Iteracion interna
    while(j<len(instrucciones)):
        #print(instru, instrucciones[j])
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
    elif(len(estaciones[i]) > 6):
        estaciones[i].pop()
    i += 1





# # Deteccion de riesgos 2
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


# # Insercion de 0 en caso de no darse la condicion
i = 0
while(i<len(estaciones)):
    if(len(estaciones[i]) == 6):
        estaciones[i].append(0)
    elif(len(estaciones[i]) > 7):
        estaciones[i].pop()
    i += 1




# # Deteccion de riesgos 3
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






# # Insercion de 0 en caso de no darse la condicion
i = 0
while(i<len(estaciones)):
    if(len(estaciones[i]) == 7):
        estaciones[i].append(0)
    elif(len(estaciones[i]) > 8):
        estaciones[i].pop()
    i += 1



# # Agregar indice para operacion
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
    if((estaciones[i][4] and estaciones[i][5] and estaciones[i][6]) == 0):
        estaciones[i].append(0)
    else:
        estaciones[i].append(1)
    i += 1


# Llenar estado de instruccion
i = 0
while(i<len(estaciones)):
    val = []
    val.append(estaciones[i][0])
    estado_instruccion.append(val)
    i += 1



# Cambiar estado de instrucciones a Issue
i = 0
while(i < 7):
    estado_instruccion[i].append("Issue")
    i += 1



# Incluir 0 a todos los estados
i = 0
while(i < len(estado_instruccion)):
    estado_instruccion[i].append(0)
    i += 1






# Pasar las instrucciones sin riesgo a Exe
i = 0
while(i < 7):
    if(estaciones[i][9] == 0):
        estado_instruccion[i][1] = "Exe"   
    i += 1




def checkFinished():
    j = 0
    flag = False
    while(j < len(estado_instruccion)):
        if(estado_instruccion[j][2] == 1 and len(terminadas) == len(estado_instruccion)):
            flag = True
        else:
            flag = False
        j += 1
    
    if(flag == True):
        return True
    else:
        return False


def getInstruccion(id):
    i = 0
    while(i < len(instrucciones)):
        if(instrucciones[i][0] == id):
            return instrucciones[i]
        i += 1
    return -1           # No encontrado
    


def noExe():
    n = 0
    flag = False
    #print(estado_instruccion)
    while(n<len(estado_instruccion)):
        if(estado_instruccion[n][1] == "Exe"):
            flag = True
        n += 1
    
    if(flag == True):
        return True
    else:
        return False

temporales = []         
terminadas = []         # Arreglo que contiene el nombre de las instrucciones que ya fueron ejecutadas



def updateEstado_instruccion():

    k = 0
    while(k < len(estado_instruccion)):
        if(estado_instruccion[k][2] == 0):              # Si la instruccion aun no ha sido ejecutada
            nombre_instruccion = estado_instruccion[k][0]           # Nombre con el cual busco en las estaciones para revisar si resolvi la dependencia
            #print("Evaluando ", nombre_instruccion)
            l = 0
            while(l < len(estaciones)):
                
                if(nombre_instruccion == estaciones[l][0]):     # Cuando encuentro la instruccion

                    # Si todas las dependencias estan contenidas dentro de la lista de terminadas significa que puedo pasarla a Exe
                    if( (estaciones[l][5] in terminadas or estaciones[l][5] == 0) and (estaciones[l][6] in terminadas or estaciones[l][6] == 0) and (estaciones[l][7] in terminadas or estaciones[l][7] == 0) ):   

                        estado_instruccion[k][1] = "Exe"
                        estado_instruccion[k][2] = 1


                l += 1

        k += 1





# print("\n")
# k = 0
# while(k < len(estado_instruccion)):
#     print(estado_instruccion[k])
#     k += 1

while(checkFinished() == False):


    if(noExe() == False):                # Si ya no tengo instrucciones en Exe

        # print("\n")
        # k = 0
        # while(k < len(estado_instruccion)):
        #     print(estado_instruccion[k])
        #     k += 1


        updateEstado_instruccion()


        # print("\n")
        # k = 0
        # while(k < len(estado_instruccion)):
        #     print(estado_instruccion[k])
        #     k += 1

    
    # Proceso de llenado de temporales en Exe
    i = 0
    while(i < len(estado_instruccion)):
        #print(estaciones[i], estado_instruccion[i])
        if(estado_instruccion[i][1] == "Exe" and estaciones[i][-2] == 1):      # Add 
            val = []
            val.append(estaciones[i][0])
            val.append( int(registros[estaciones[i][3]])  + int(registros[estaciones[i][4]]) ) 
            val.append(estaciones[i][-2])

            temporales.append(val)

        elif(estado_instruccion[i][1] == "Exe" and estaciones[i][-2] == 2):     # Sub
            #print(estado_instruccion[i])
            #print(estaciones[i])

            val = []
            val.append(estaciones[i][0])
            res = int(registros[estaciones[i][3]]) - int(registros[estaciones[i][4]])

            #print(res, registros[estaciones[i][3]], registros[estaciones[i][4]])
            val.append( res )   
            val.append(estaciones[i][-2])

            temporales.append(val)

        elif(estado_instruccion[i][1] == "Exe" and estaciones[i][-2] == 3):     # Mul
            #print(estado_instruccion[i])
            #print(estaciones[i])

            val = []
            val.append(estaciones[i][0])
            res = int(registros[estaciones[i][3]]) * int(registros[estaciones[i][4]])

            #print(res, registros[estaciones[i][3]], registros[estaciones[i][4]])
            val.append( res )   
            val.append(estaciones[i][-2])

            temporales.append(val)

        elif(estado_instruccion[i][1] == "Exe" and estaciones[i][-2] == 4):     # STORE

            val = []
            val.append(estaciones[i][0])
            val.append( int(instrucciones[i][2]) + registros[str(instrucciones[i][3])] )  # (0 + Valor R1)
            val.append(estaciones[i][-2])

            temporales.append(val)

        elif(estado_instruccion[i][1] == "Exe" and estaciones[i][-2] == 5):     # LOAD  

            val = []
            val.append(estaciones[i][0])
            val.append( int(instrucciones[i][2]) + registros[str(instrucciones[i][3])] )  # (0 + Valor R1)
            val.append(estaciones[i][-2])

            temporales.append(val)
      

        i += 1

    i = 0
    while(i < len(estado_instruccion)):
        
        if(estado_instruccion[i][1] == "Exe"):
            estado_instruccion[i][1] = "Write"
        i += 1


    #print(temporales)

    i = 0
    while(i < len(temporales)):
        
        instruccion = temporales[i][0]
        resultado = temporales[i][1]
        operacion = temporales[i][2]
        nombre_operador_resultado = -1

        

        n = 0
        while(n<len(matriz_oper_resultados)):
            if(matriz_oper_resultados[n][0] == instruccion):
                nombre_operador_resultado = matriz_oper_resultados[n][1]
                break
            n += 1

        
        if(nombre_operador_resultado == -1):
            print("Error 3")
        

        print("WB numero:",i,"instruccion: ", instruccion, "operacion:", operacion, "resultado exe:", resultado, "Registro de guardado:", nombre_operador_resultado)
        
        if(operacion == 1 or operacion ==  2 or operacion ==  3):             # ADD #SUB #MUL
            registros[nombre_operador_resultado] = resultado
        elif(operacion == 4):           # STORE
            memoria[resultado] = registros[nombre_operador_resultado]
        elif(operacion == 5):           # LOAD
            registros[nombre_operador_resultado] = memoria[resultado]

        i += 1



    n = 0
    while(n < len(estado_instruccion)):
        if(estado_instruccion[n][1] == "Write"):
            estado_instruccion[n][1] = "Done"
            estado_instruccion[n][2] = 1
            terminadas.append(estado_instruccion[n][0])
        n += 1
    
    temporales = []
    





print("\n")
k = 0
while(k < len(estado_instruccion)):
    print(estado_instruccion[k])
    k += 1


print("\n")
print("Valores finales de los registros")
print("Valor de F0:", registros["F0"])
print("Valor de F2:", registros["F2"])
print("Valor de F4:", registros["F4"])
print("Valor de F6:", registros["F6"])
print("Valor de F8:", registros["F8"])
print("Valor de F10:", registros["F10"])
print("Valor de Memoria[1]:", memoria[1])