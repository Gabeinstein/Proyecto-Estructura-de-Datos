# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:51:01 2022
@author: cesar
"""

from __future__ import division



#Creacion de dias---------------------
dia = 1
class Node: #dia del calendario 
    

    def __init__(self):

        self.next_node = None  #orden estandar de los dias 1-30    

        global dia 
        
          
        if(dia == 31):
            dia = 1
        self.dia = dia   #cada coneccion de un nodo va aumentando el numero de dia 
        dia +=1
         # la siguiente vez que creo un nodo sera uno mas arriba 

        self.nombre_invitado = None #una variable string que serivira para agrupar todos los nodos que contengan dicho nombre 
        self.numero_invitados = None #agrupar nodos que contengan mismo lugar 
        self.lugar = None  #una variable string que serivira para agrupar todos los nodos que contengan dicho nombre
        self.evento = None #familiar, social, academicas 


        
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        

    #def crear_evento():
        #numero de invitados
        #nombre de invitado 
        #lugar
        #fecha (prioridad por fecha mas cercana) Stack en linked list     
    #SETS   
    def set_nombre_invitado(self, nombre):
        self.nombre_invitado = nombre

    def set_numero_invitados(self, numero_invitados):
        self.numero_invitados = numero_invitados
    
    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_evento(self, evento):
        self.evento = evento


    #GETS 
    def get_nombre_invitado(self):
        return self.nombre_invitado

    def get_numero_invitados(self):
        return self.numero_invitados
    
    def get_Lugar(self):
        return self.lugar

    def get_tipo_evento(self):
        return self.evento    

    def get_dia(self):
        return self.dia
    #imprimir informacion del dia
    def informacion_dia(self):
        print("Nombre del invitado: ",self.nombre_invitado)
        print("Numero de Invitados: ",self.numero_invitados)
        print("Lugar: ",self.lugar)
        print("Tipo de Evento: ",self.evento)

#Creacion de meses---------------------
mes = 1 
class Singly_linked_list: 
    """
    Implementation of a singly linked list
    """
    def __init__(self, ):
   
        global mes      
        if(mes == 12):
            mes = 1
        self.mes = mes  #meses desde 1-12
        mes +=1
        self.head_node = None
        self.next_List = None #sirve para conectar mes 1, con mes 2, con mes 3 etc  porque cada mes es una linked list de 30 nodos 
        self.next_node = None
        self.fecha = []
        
        
        for i in range(1,31):    
            self.fecha.append (Node())     #una single linked list crea 30 nodos y los conecta automaticamente
            if(i > 1):
               self.fecha[i-2].set_next_node (self.fecha[i-1])
        self.head_node = self.fecha[0]       


    def set_next_List(self, next_List): 
        self.next_List = next_List

    def list_traversed(self):
        node = self.head_node
        while node:
            if node.nombre_invitado is not None:
                print("Dia: ",node.dia)
                #imprimir informacion de cada dia
                node.informacion_dia()
                print("---------------")
            node = node.next_node
    def evento_dia(self,dia):
        node = self.head_node
        while node:
            if(dia==node.dia):
                node.informacion_dia()
                return None
            node = node.next_node       



class Singly_linked_list(Singly_linked_list):


    def insert_head(self, new_node):
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)
        
    def insert_middle(self, new_node, value):
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)


#Creacion del año---------------------
fecha_mes = []  #<----Arreglo donde se guardan meses
def año(): 

    
    for i in range(1,14):
        fecha_mes.append( Singly_linked_list())   #un año crea 12 single linked list conectadas en otra linked list
        if(i > 1):
           fecha_mes[i-2].set_next_List(fecha_mes[i-1])
          

def regresar_tabla(clave):
    return eventos_favoritos[clave]

#Creacion de funciones de agrupacion o de busqueda---------------------

#Creacion de eventos por dia
def ingreso_evento(mes,dia,nombre_invitado, numero_invitados, lugar, evento):
    if mes>12 or mes<=0:
        print("El mes que escogio no existe")
        return None
    i=1
    fecha_evento=fecha_mes[mes-1].head_node
    while i<=dia:
        if fecha_evento.dia==dia:
            fecha_evento.set_nombre_invitado(nombre_invitado)
            fecha_evento.set_numero_invitados(numero_invitados)
            fecha_evento.set_lugar(lugar)
            fecha_evento.set_evento(evento)
            #Ingreso Eventos Hash
            if fecha_evento.evento in eventos_favoritos:#Se valida que no exista la clave del hashtable
                eventos_favoritos[fecha_evento.evento]=eventos_favoritos[fecha_evento.evento]+1
            else:
                eventos_favoritos[fecha_evento.evento]=1 #Ingreso datos en HashTable
            #Ingreso Invitados Hash 
            if fecha_evento.nombre_invitado in invitado_favoritos:#Se valida que no exista la clave del hashtable
                invitado_favoritos[fecha_evento.nombre_invitado]=invitado_favoritos[fecha_evento.nombre_invitado]+1
            else:
                invitado_favoritos[fecha_evento.nombre_invitado]=1 #Ingreso datos en HashTable
            #Ingreso Lugares Hash
            if fecha_evento.lugar in lugares_favoritos:#Se valida que no exista la clave del hashtable
                lugares_favoritos[fecha_evento.lugar]=lugares_favoritos[fecha_evento.lugar]+1
            else:
                lugares_favoritos[fecha_evento.lugar]=1 #Ingreso datos en HashTable
            return None
        fecha_evento=fecha_evento.next_node
        i+=1

#Eliminacion de eventos por dia
def eliminar_evento(mes,dia):
    if mes>12 or mes<=0:
        print("El mes que escogio no existe")
        return None
    i=1
    fecha_evento=fecha_mes[mes-1].head_node
    while i<=dia:
        if fecha_evento.dia==dia:
            if(fecha_evento.nombre_invitado==None):
                print("No existe evento en ese dia")
                return None
            
            #Ingreso Eventos Hash
            if eventos_favoritos[fecha_evento.evento]>1:#Se valida que no exista la clave del hashtable
                eventos_favoritos[fecha_evento.evento]=eventos_favoritos[fecha_evento.evento]-1
            else:
                del eventos_favoritos[fecha_evento.evento] #Ingreso datos en HashTable
            #Ingreso Invitados Hash 
            if invitado_favoritos[fecha_evento.nombre_invitado]>1:#Se valida que no exista la clave del hashtable
                invitado_favoritos[fecha_evento.nombre_invitado]=invitado_favoritos[fecha_evento.nombre_invitado]-1
            else:
                del invitado_favoritos[fecha_evento.nombre_invitado] #Ingreso datos en HashTable
            #Ingreso Lugares Hash
            if lugares_favoritos[fecha_evento.lugar]>1:#Se valida que no exista la clave del hashtable
                lugares_favoritos[fecha_evento.lugar]=lugares_favoritos[fecha_evento.lugar]-1
            else:
                del lugares_favoritos[fecha_evento.lugar] #Ingreso datos en HashTable
            fecha_evento.set_nombre_invitado(None)
            fecha_evento.set_numero_invitados(None)
            fecha_evento.set_lugar(None)
            fecha_evento.set_evento(None)
            return None
        fecha_evento=fecha_evento.next_node
        i+=1


#Funcion para mostrar un dia en especifico        
def mostrar_evento(mes,dia):
    print("Mes:",mes)
    print("Dia:",dia)
    fecha_mes[mes].evento_dia(dia)

#Funcion para ver el eveto que mas se repite
def evento_recurrente():
    tipo_evento=""
    repetido=1
    for x in eventos_favoritos:
        if eventos_favoritos[x]>repetido:
            tipo_evento=x
            repetido=eventos_favoritos[x]
    print("Su evento mas recurrente es: ", tipo_evento, " , este evento se repite ",repetido, " veces al año.")

def invitado_recurrente():
    invitado=""
    repetido=1
    for x in invitado_favoritos:
        if invitado_favoritos[x]>repetido:
            invitado=x
            repetido=invitado_favoritos[x]
    print("Su invitado mas recurrente es: ", invitado, " , este invitado a estado en ",repetido, "de sus eventos al año.")
def lugar_recurrente():
    lugar=""
    repetido=1
    for x in lugares_favoritos:
        if lugares_favoritos[x]>repetido:
            lugar=x
            repetido=lugares_favoritos[x]
    print("Su lugar mas recurrente es: ", lugar, " , ha tenido ",repetido, "eventos al año en este lugar.")


#Busqueda de eventos      
def search_by_event(year, event):
    cevent = 0
    times = 0
    for month in year:
        node = month.head_node
        while node:
            if(node.evento == event):
                times +=1
                print("Dia: " + str(node.dia) + "|| Mes: " + str(cevent+1) + "||  Evento: " + str(node.evento))
            node = node.next_node
        cevent += 1
    
    if times > 0:
        print("Para la búsqueda de ", str(event)," se tiene un total de ", times, " eventos encontrados")
        print("-------------------")
    else:
        print("No se encontraron eventos relacionados con la búsqueda de ",event)
        print("-------------------")
#Busqueda de lugares    
def search_by_place(year, place):
    clugar = 0
    times = 0
    for month in year:
        node = month.head_node
        while node:
            if(node.lugar == place):
                times +=1
                print("Dia: " + str(node.dia) + "|| Mes: " + str(clugar+1) + "||  Lugar: " + str(node.lugar))
            node = node.next_node
        clugar += 1
        
    if times>0:
        print("Para la búsqueda de ", str(place)," se tiene un total de ", times, " eventos encontrados")
        print("-------------------")
    else:
        print("No se encontraron eventos relacionados con la búsqueda de ",place)
        print("-------------------")
#Busqueda de invitados 
def search_by_host(year, host):
    chost = 0
    times = 0
    for month in year:
        node = month.head_node
        while node:
            if(node.nombre_invitado == host):
                times +=1
                print("Dia: " + str(node.dia) + "|| Mes: " + str(chost+1) + "||  Evento: " + str(node.nombre_invitado))
            node = node.next_node
        chost += 1
        
    if times>0:
        print("Para la búsqueda de ", str(host)," se tiene un total de ", times, " eventos encontrados")
        print("-------------------")
    else:
        print("No se encontraron eventos relacionados con la búsqueda de ",host)
        print("-------------------")


def imprimir_año():
    for i in range(0,12):
        print("-------------------")
        print("MES ", i+1)
        fecha_mes[i].list_traversed()



eventos_favoritos={} #HashTable donde se guardan tipos de eventos
invitado_favoritos={} #HashTable donde se guardan invitados
lugares_favoritos={} #HashTable donde se guardan lugares

año() #Creacion del año


#prueba de ingreso de datos
ingreso_evento(2,11,"Jose",22,"USFQ","Graduacion")
ingreso_evento(2,12,"Jose",25,"USFQ","Premiacion")
ingreso_evento(1,20,"Jose",12,"Casa","Familiar")
ingreso_evento(6,5,"Jose",5,"Cine","Social")
ingreso_evento(1,11,"Pedro",22,"Casa","Familiar")
ingreso_evento(2,2,"Jose",25,"Empresa","Laboral")
ingreso_evento(1,19,"Maria",22,"Restaurante","Familiar")
ingreso_evento(2,14,"Jose",25,"Empresa","Laboral")
#prueba eliminacion evento
eliminar_evento(2,2)

print("-------------------")
evento_recurrente() #muestra el evento que mas se repite
invitado_recurrente() #muestra el invitado que mas se repite
lugar_recurrente() #muestra el lugar que mas se repite
#print("Mes 2")
#fecha_mes[1].list_traversed() #Calendario mes 2
print("-------------------")
print(invitado_favoritos)
print(eventos_favoritos)
    
print("-------------------")
    
search_by_event(fecha_mes, "Laboral")
search_by_event(fecha_mes, "dd")
search_by_host(fecha_mes, "Jose")
search_by_place(fecha_mes, "Empresa")

print("-------------------")
fecha_mes[0].list_traversed()

