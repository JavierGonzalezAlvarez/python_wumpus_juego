#importamos numeros aleatorios
import random
#importamos sistema
import sys

class clase_Cuadrante:
    #Clase que contiene las conexiones dentro de la grilla y me dice donde está el cazador
    #Inicalizamos los atributos de la clase con init
    def __init__(self, **kwargs):
        self.i = 0  #casilla de salida inicial        
        #Lista con los movimientos a donde podemos ir
        self.conectamos_con = []        
        #Control del teclado
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    #Pasamos el objeto a string
    def __str__(self):
        return str(self.i)

    def casilla_anexa(self, variable_recibir_lista):
        if variable_recibir_lista not in self.conectamos_con:
            self.conectamos_con.append(variable_recibir_lista)

    def donde_estamos(self):       
        #Matriz. Para que el jugador vea la grilla
        print("----------------------------")
        matriz = [[16,15,14,13], [9,10,11,12], [8, 7, 6, 5], [1, 2, 3, 4]]
        for a in range(4):
            for b in range(4):
                print(matriz[a][b], end=' ')
            print()
        #
        print("----------------------------")
        print("DISPONES DE 10 FLECHAS.")
        print("OPCIONES:")
        print("----------------------------")
        print ("MOVER, SALIR, DISPARAR")
        print("----------------------------")
        print("Estas en la casilla {} y puedes ir a la casilla {}".format(self.i, self.conectamos_con))

    def removimiento_connect(self, variable_recibir_listas):
        if variable_recibir_listas in self.conectamos_con:
            self.conectamos_con.removimiento(variable_recibir_listas)
 
    def conexion_valida(self, variable_recibir_lista):
        return variable_recibir_lista in self.conectamos_con
    
class clase_Actores():
    def __init__(self, **kwargs):
        #empezamos en 0
        self.localizacion = 0
        #teclado
        for key, value in kwargs.items():
            setattr(self, key, value)

    def movimiento(self, a_new_localizacion):
        if a_new_localizacion.i in self.localizacion.conectamos_con or a_new_localizacion == self.localizacion:
            self.localizacion = a_new_localizacion
            return True
        else:
            return False

    def validar_movimiento(self, a_new_localizacion):
        return a_new_localizacion.i in self.localizacion.conectamos_con or a_new_localizacion == self.localizacion
                
    def get_localizacion(self):
        return self.localizacion.i
 
    def alcanzado(self, a_room):
        return self.localizacion == a_room

#------------------------------------------------------------------
def crear_Cuadrante():
    for ii in range(16):
        #Creamos los cuadrantes. Llamada a la clase y atributo casilla
        lista_Cuadrante.append(clase_Cuadrante(i = ii + 1))          
    #iniciamos los objetos (enumerate) posicionandolos dentro de una lista
    for  x, celda in enumerate(lista_Cuadrante):
        #------------------------------------------------------------
        #Casillas para avanzar/girar derecha/girar izquierda        
        #------------------------------------------------------------
        #Cada posicion puede: avanzar, girar derecha y girar izquierda
        #Se añade a una lista
        if x == 0: 
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +7].i)            
        if x == 8:    
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +7].i)            
        if x == 1:
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +5].i)            
        if x == 9:                
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +5].i)            
        if x == 2:
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +3].i)            
        if x == 10:    
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +3].i)            
        if x == 3:
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 11:    
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +1].i)                 
#--------------------------------
        if x == 7:
            #Girar a la izquierda         
            celda.casilla_anexa(lista_Cuadrante[x -7].i)                      
        if x == 15:    
            #Girar a la izquierda         
            celda.casilla_anexa(lista_Cuadrante[x -7].i)                      
        if x == 6:
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x -5].i)            
        if x == 14:    
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x -5].i)            
        if x == 5:
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -3].i)            
        if x == 13:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -3].i)            
        if x == 4:
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -1].i)            
        if x == 12:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -1].i)                 
#--------------------------------
        if x == 7:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 6:    
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x +3].i)            
        if x == 5:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x +5].i)            
        if x == 4:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x +7].i)            
#--------------------------------
        if x == 11:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -7].i)            
        if x == 10:    
            #Girar a la izquierda
            celda.casilla_anexa(lista_Cuadrante[x -5].i)            
        if x == 9:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -3].i)           
        if x == 8:    
            #Girar a la derecha
            celda.casilla_anexa(lista_Cuadrante[x -1].i)            
#------------------------------------------------------
        if x == 0:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 1:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 2:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 4:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 5:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 6:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 8:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 9:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 10:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 12:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
        if x == 13:    
            #Avanzar 1 casilla
            celda.casilla_anexa(lista_Cuadrante[x +1].i)            
#--------------------------------------------------------------------
def crear_actores(lista_Cuadrante_1):
    lista_actores = []
    #creamos numeros aleatorios con 6 celdas, una para cada actor
    numeros_aleatorios = random.sample(lista_Cuadrante_1, 6)
    #asignamos los cuadrantes que hay en la lista a los numeros aleatorios
    for celda in numeros_aleatorios:
        #añadimos a la lista
        lista_actores.append(clase_Actores(localizacion = celda))
    return lista_actores
#--------------------------------------------------------------------
#Empezamos creando una lceldasta para las Cuadrante
lista_Cuadrante = []
#--------------------------------------------------------------------
#llamada a un metodo
crear_Cuadrante()
#--------------------------------------------------------------------
#Creamos los clase_clase_actores y los metemos dentro del cuadrante/celda
wumpus, cazador, pozo_1, pozo_2, pozo_3, oro = crear_actores(lista_Cuadrante)
#--------------------------------------------------------------------
#Establceer armas
flechas = 10
#--------------------------------------------------------------------
while True:
    #indicamos donde estamos, y no salimos hasta realizar una acción
    cazador.localizacion.donde_estamos()
    if cazador.localizacion.i == 4:
        print("Percibo un un choque y no puedes avanzar. DEBES GIRAR!")
    if cazador.localizacion.i == 12:
        print("Percibo un un choque y no puedes avanzar. DEBES GIRAR!")    
    if cazador.localizacion.i == 13:
        print("Percibo un un choque y no puedes avanzar. DEBES GIRAR!")    
    if cazador.localizacion.i == 16:
        print("Percibo un un choque y no puedes avanzar. DEBES GIRAR!")    
    if cazador.localizacion.i == 8:
        print("Percibo un un choque y no puedes avanzar. DEBES GIRAR!")    
    if cazador.localizacion.i == 1:
        print("Percibo un un choque y no puedes avanzar. DEBES GIRAR!")        
    
    #Recorremos las casillas para comprobar donde estan los actores
    for Cuadrante_1 in cazador.localizacion.conectamos_con:
        #Verificamos con un if para comprobar donde están los actores
        if wumpus.localizacion.i == Cuadrante_1:
            #Si no quieres saber donde está el actor comenta la siguiente linea.
            print("wumpus esta en la casilla:", wumpus.localizacion.i)
            print("Percibo un hedor!")
        if pozo_1.localizacion.i == Cuadrante_1:
            #Si no quieres saber donde está el actor comenta la siguiente linea.
            print("hay un pozo(el 1) en la casilla:", pozo_1.localizacion.i)
            print("Percibo una brisa fresca!")
        if pozo_2.localizacion.i == Cuadrante_1:
            #Si no quieres saber donde está el actor comenta la siguiente linea.
            print("hay un pozo(el 2) en la casilla:", pozo_2.localizacion.i)
            print("Percibo una brisa fresca!")
        if pozo_3.localizacion.i == Cuadrante_1:
            #Si no quieres saber donde está el actor comenta la siguiente linea.
            print("hay un pozo(el 3) en la casilla:", pozo_3.localizacion.i)
            print("Percibo una brisa fresca!")            
        if oro.localizacion.i == Cuadrante_1:
            #Si no quieres saber donde está el actor comenta la siguiente linea.
            print("hay oro en la casilla:", pozo_3.localizacion.i)
            print("Percibo su brillo maravilloso!")                
    
    teclear = input("\n")
    tecla = teclear.split(' ')
    frase = tecla[0].upper()

    if len(tecla) > 1:
        try:
            movimiento = lista_Cuadrante[int(tecla[1]) -1]
        except:
            print("\n Error")
            continue
    else:
        movimiento = cazador.localizacion

    if frase == 'SALIR' or  frase == 'salir':
        print("\nHasta otra")
        sys.exit()

    elif frase == 'MOVER' or frase == 'mover':
        if cazador.movimiento(movimiento):
            if cazador.localizacion == wumpus.localizacion:
                print("Estás en la casilla con el wunpus")                
        else:
            print("\n **No puedes avanzar")
            continue

    elif frase == 'DISPARAR' or frase == 'disparar':
        if cazador.validar_movimiento(movimiento):            
            if wumpus.localizacion == movimiento:
                print("\n Le has dado al wumpus.\n")
                sys.exit()
        else:
            print("\n** Para de tirar a las paredes")

        flechas -= 1
        if flechas == 0:
            print("\n Te quedan {} \n".format(flechas))
            print("\n Ya no tienes fechas- Game over\n")
            sys.exit()
   
    else:
        print("\n Teclea una de las opciones correctas")
        continue

    if cazador.localizacion == wumpus.localizacion:
        print("wunpus te ha pillado. Game over\n")
        sys.exit()    

    elif cazador.localizacion == pozo_1.localizacion or cazador.localizacion == pozo_2.localizacion or cazador.localizacion == pozo_3.localizacion:
        print("Has caido en el pozo. Game over\n")
        sys.exit()

    else: # Seguimos cazando
        pass