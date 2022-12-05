from __future__ import division




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
        self.numero_invitado = numero_invitados
    
    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_lugar(self, evento):
        self.lugar = evento


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
            print(node.dia)
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

     #ordenar por nombre de invitado      
     #    mostrar todos los nodos donde aparezcan "Juan" 

     #ordenar por lugar 
     #    mostrar todos los nodos con parametro lugar "universidad"

     #ordenar por tematicas
     #     mostrar todos los nodos con tematica "social" 

     #ordenar por mes 
     # mostrar solamente los eventos del mes "enero"
           

fecha_mes = []  #<----
def año(): 

    
    for i in range(1,14):
        fecha_mes.append( Singly_linked_list())   #un año crea 12 single linked list conectadas en otra linked list
        if(i > 1):
           fecha_mes[i-2].set_next_List(fecha_mes[i-1])
          







#12 linked list de 30 nodos 
#encontrar interseccion de un valor string dentro de 2 listas diferentes 

#list2 = Singly_linked_list(m2) # una linked list representa 1 mes con 30 nodos o dias  


#node1.

#año()
#fecha_mes[1].list_traversed()



año()

for i in range(1,13):
    print(" ")
    print("MES ", i )
    fecha_mes[i].list_traversed()


#REUSMEN
#al crear una linked list, estoy creando 30 nodos y conectandolos en la linked list 
#La funcion año() crea 12 linked list que a su vez estan conectadas 
#hace falta hacer una funcion dentro de año() para que se pueda buscar un valor identico dentro de los nodos de las 12 linked list 