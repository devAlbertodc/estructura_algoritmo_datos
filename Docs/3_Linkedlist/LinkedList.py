from Node import Node

class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)

        #Empty list then head and tail point to the new_node:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            #Update the pointer first and then add the new_node:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        #Iniciar variables apuntando al primer nodo. Temp irá al último nodo y pre al penúltimo
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        #El final ahora es el penultimo nodo y el puntero no apunta a nada
        self.tail = pre
        self.tail.next = None
        self.length -=1
        #Si teniamos un elemento y lo hemos quitado, se asocia el inicio y final a nada:
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        #Sin elementos:
        if self.length == 0:
            return None
        #1 o más elementos. Se obtiene el primer elemento y el puntero del siguiente
        temp = self.head
        self.head = self.head.next
        #Quitamos el puntero y decrementa la longitud
        temp.next = None
        self.length -= 1
        #Si habia un elemento y ahora no hay, el final apunta a None
        if self.length == 0:
            self.tail = None
        return temp

    #El metodo devuelve None si el indice es invalido. Devuelve el nodo si el nodo es correcto
    def get(self,index):
        if index < 0 or self.length <= index:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    # Se obtiene el nodo None o valido y se asigna el valor. Sobreescribe el valor del nodo.
    # Devuelve True si hizo la operacion correctamente y False si get devolvio None
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        #Controlar nodo invalido:
        if index < 0 or self.length < index:
            return False
        #Insertar al principio de la lista:
        if index == 0:
            return self.prepend(value)
        #Insertar al final de la lista:
        if index == self.length:
            return self.append(value)

        #Generar el nodo y apuntar a la posicion previa a la insercion para cambiar el puntero
        new_node = Node(value)
        temp = self.get(index-1)
        if temp:
            #Primero se asocia el puntero del nuevo nodo hacia el siguiente elemento de la lista antes de insertar el nodo en la lista
            new_node.next = temp.next
            #En la lista original, el elemento apunta al nuevo nodo.
            temp.next = new_node
            self.length += 1
            return True

    def remove(self,index):
        if index < 0 or self.length <= index:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        #Elemento anterior para sobreescribir su puntero al siguiente nodo
        prev = self.get(index - 1)
        temp = prev.next
        #Movemos el puntero del previo al siguiente:
        prev.next = temp.next
        #Deshabilitamos la conexion entre el puntero del elemento a borrar y el siguiente:
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # Se obtiene el primer nodo temporal:
        temp = self.head
        # Intercambiar inicio y fin:
        self.head = self.tail
        self.tail = temp
        # Generar el puntero posterior a cada nodo (el anterior no por si la lista tiene 0 elementos):
        before = None
        # Iteracion a traves de la lista para cambiar la direccion de los punteros
        for _ in range(self.length):
            after = temp.next  # 1) guardo el siguiente
            temp.next = before  # 2) invierto el puntero
            before = temp  # 3) avanzo before
            temp = after  # 4) avanzo temp
        return True