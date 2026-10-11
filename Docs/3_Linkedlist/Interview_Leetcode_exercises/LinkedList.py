from Node import Node


class Linkedlist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        # Empty list then head and tail point to the new_node:
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # Update the pointer first and then add the new_node:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        # Iniciar variables apuntando al primer nodo. Temp irá al último nodo y pre al penúltimo
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        # El final ahora es el penultimo nodo y el puntero no apunta a nada
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Si teniamos un elemento y lo hemos quitado, se asocia el inicio y final a nada:
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
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
        # Sin elementos:
        if self.length == 0:
            return None
        # 1 o más elementos. Se obtiene el primer elemento y el puntero del siguiente
        temp = self.head
        self.head = self.head.next
        # Quitamos el puntero y decrementa la longitud
        temp.next = None
        self.length -= 1
        # Si habia un elemento y ahora no hay, el final apunta a None
        if self.length == 0:
            self.tail = None
        return temp

    # El metodo devuelve None si el indice es invalido. Devuelve el nodo si el nodo es correcto
    def get(self, index):
        if index < 0 or self.length <= index:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    # Se obtiene el nodo None o valido y se asigna el valor. Sobreescribe el valor del nodo.
    # Devuelve True si hizo la operacion correctamente y False si get devolvio None
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # Controlar nodo invalido:
        if index < 0 or self.length < index:
            return False
        # Insertar al principio de la lista:
        if index == 0:
            return self.prepend(value)
        # Insertar al final de la lista:
        if index == self.length:
            return self.append(value)

        # Generar el nodo y apuntar a la posicion previa a la insercion para cambiar el puntero
        new_node = Node(value)
        temp = self.get(index - 1)
        if temp:
            # Primero se asocia el puntero del nuevo nodo hacia el siguiente elemento de la lista antes de insertar el nodo en la lista
            new_node.next = temp.next
            # En la lista original, el elemento apunta al nuevo nodo.
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or self.length <= index:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # Elemento anterior para sobreescribir su puntero al siguiente nodo
        prev = self.get(index - 1)
        temp = prev.next
        # Movemos el puntero del previo al siguiente:
        prev.next = temp.next
        # Deshabilitamos la conexion entre el puntero del elemento a borrar y el siguiente:
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

    def find_middle_node(self):
        """
            Devuelve el nodo que está en el medio de la lista.

            Idea: usamos dos punteros que recorren la lista a distinta velocidad.
              - slow (lento): avanza 1 nodo por vuelta.
              - fast (rápido): avanza 2 nodos por vuelta.
            Cuando el rápido llega al final, el lento va justo por la mitad,
            porque ha recorrido la mitad de camino.

            Ejemplo con 10 -> 20 -> 30 -> 40 -> 50:
              inicio:   slow=10, fast=10
              vuelta 1: slow=20, fast=30
              vuelta 2: slow=30, fast=50   (fast.next es None, el bucle termina)
              resultado: 30 (el nodo del medio)

            Si la lista tiene un número PAR de nodos, hay dos nodos centrales
            y este método devuelve el segundo.
            Ejemplo: 10 -> 20 -> 30 -> 40 devuelve 30.

            Si la lista está vacía (head es None), devuelve None.

            Coste: O(n), una sola pasada por la lista.
        """
        # Los dos punteros empiezan en el primer nodo
        slow = self.head
        fast = self.head

        # Seguimos mientras el rápido pueda dar sus dos pasos:
        #   - "fast" no debe ser None (lista vacía o ya se salió de la lista)
        #   - "fast.next" no debe ser None (si lo es, fast está en el último nodo
        #     y no puede avanzar dos veces; además evitamos un AttributeError)
        while fast and fast.next is not None:
            slow = slow.next  # el lento avanza 1 paso
            fast = fast.next.next  # el rápido avanza 2 pasos

        # Cuando el rápido termina, el lento está en el medio
        return slow

    def has_loop(self):
        """
        Comprueba si la lista tiene un ciclo (un bucle infinito).

        Un ciclo ocurre cuando algún nodo apunta de vuelta a un nodo anterior,
        de modo que nunca se llega a None. Ejemplo:
            10 -> 20 -> 30 -> 40
                         ^      |
                         |______|   (el 40 apunta otra vez al 30)

        Idea (algoritmo de la tortuga y la liebre, de Floyd):
          - slow (lento) avanza 1 nodo por vuelta.
          - fast (rápido) avanza 2 nodos por vuelta.
        Si NO hay ciclo, el rápido llega al final (None) y el bucle termina.
        Si SÍ hay ciclo, ambos entran en él y dan vueltas; como el rápido
        gana terreno en cada vuelta, tarde o temprano alcanza al lento
        y los dos apuntan al mismo nodo.

        Devuelve:
            True  si hay un ciclo.
            False si no lo hay (incluida una lista vacía).

        Coste: O(n) en tiempo y O(1) en memoria (no guarda nodos visitados).
        """
        # Los dos punteros empiezan en el primer nodo
        slow = self.head
        fast = self.head

        # Mismas condiciones que en find_middle_node: el rápido necesita
        # poder dar dos pasos sin salirse de la lista
        while fast and fast.next is not None:
            slow = slow.next  # el lento avanza 1 paso
            fast = fast.next.next  # el rápido avanza 2 pasos

            # Si los dos apuntan al MISMO nodo, se han encontrado dentro de un ciclo.
            # (Se comparan nodos, no valores: dos nodos distintos pueden tener el
            # mismo dato sin que haya ciclo.)
            if slow == fast:
                return True

        # El rápido llegó al final de la lista: no hay ciclo
        return False

    def remove_duplicates(self):
        """
        Elimina de la lista los nodos con valores repetidos.
        Se queda con la PRIMERA aparición de cada valor y borra las demás.

        Idea: usamos dos punteros.
          - current (actual): el nodo que estamos "protegiendo". Su valor es el
            que vamos a buscar repetido más adelante.
          - runner (corredor): recorre el resto de la lista buscando nodos con el
            mismo valor que current. Siempre mira al nodo SIGUIENTE (runner.next),
            porque para borrar un nodo hay que estar parado en el anterior.

        Ejemplo con 10 -> 20 -> 10 -> 30 -> 20:
          current=10: runner encuentra el segundo 10 y lo borra
                      resultado parcial: 10 -> 20 -> 30 -> 20
          current=20: runner encuentra el segundo 20 y lo borra
                      resultado parcial: 10 -> 20 -> 30
          current=30: no hay nada más que revisar
          resultado final: 10 -> 20 -> 30

        No devuelve nada: modifica la lista directamente.

        Coste: O(n al cuadrado) en tiempo, porque para cada nodo recorremos el
        resto de la lista. Usa O(1) de memoria extra.
        """
        # Empezamos en el primer nodo
        current = self.head

        # Bucle externo: cada nodo de la lista tendrá su turno como "current"
        while current:
            # El corredor arranca en el mismo nodo que current
            runner = current

            # Bucle interno: revisamos todos los nodos que vienen después de current.
            # Paramos cuando runner está en el último nodo (runner.next es None)
            while runner.next:
                if current.value == runner.next.value:
                    # Valor repetido: nos saltamos el nodo siguiente.
                    # Ahora runner apunta al nodo que estaba DESPUÉS del repetido,
                    # y el nodo repetido queda fuera de la lista.
                    runner.next = runner.next.next
                    self.length -= 1
                    # Importante: aquí runner NO avanza, porque el nuevo
                    # runner.next podría ser otro repetido.
                else:
                    # No es repetido: avanzamos el corredor un paso
                    runner = runner.next

            # Terminamos con current: pasamos al siguiente nodo
            current = current.next

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num

    def partition_list(self, value):
        """
        Reordena la lista para que todos los nodos con valor MENOR que `value`
        queden al principio, y los nodos con valor IGUAL O MAYOR queden después.
        El orden original se mantiene dentro de cada grupo.

        Idea: en vez de mover nodos uno a uno, construimos DOS listas pequeñas
        y al final las unimos:
          - lista 1: los nodos menores que value.
          - lista 2: los nodos iguales o mayores que value.
        Recorremos la lista original una sola vez y enganchamos cada nodo
        al final de la lista que le corresponde.

        Ejemplo con 3 -> 8 -> 5 -> 10 -> 2 -> 1  y  value = 5:
          lista 1 (menores que 5):       3 -> 2 -> 1
          lista 2 (iguales o mayores):   8 -> 5 -> 10
          unimos lista 1 + lista 2:      3 -> 2 -> 1 -> 8 -> 5 -> 10

        No devuelve nada: modifica la lista directamente.
        Si la lista está vacía, devuelve None y no hace nada.

        Coste: O(n), una sola pasada, y O(1) de memoria extra
        (no se crean nodos nuevos, salvo los dos auxiliares).
        """
        # Lista vacía: no hay nada que reordenar
        if self.length == 0:
            return None

        # Nodos "falsos" (dummy) que sirven de punto de partida de cada lista.
        # Su valor (0) da igual: nunca formarán parte del resultado final.
        # Nos evitan tener que tratar aparte el caso de "la lista aún está vacía".
        dummy1 = Node(0)  # empieza la lista de los menores que value
        dummy2 = Node(0)  # empieza la lista de los iguales o mayores

        # prev1 y prev2 apuntan al ÚLTIMO nodo de cada lista (donde se engancha el siguiente)
        prev1 = dummy1
        prev2 = dummy2

        # Recorremos la lista original desde el primer nodo
        current = self.head
        while current is not None:
            if current.value < value:
                # Va a la lista 1: se engancha al final y ese pasa a ser el último
                prev1.next = current
                prev1 = current
            else:
                # Va a la lista 2: se engancha al final y ese pasa a ser el último
                prev2.next = current
                prev2 = current

            current = current.next  # <-- AÑADIDO: sin esta línea el bucle es infinito

        # El último nodo de la lista 2 tiene que apuntar a None.
        # Si no, podría seguir apuntando a un nodo de la lista 1 y se formaría un ciclo.
        prev2.next = None

        # Unimos las listas: el final de la lista 1 apunta al inicio de la lista 2
        # (dummy2.next es el primer nodo real de la lista 2, no el dummy)
        prev1.next = dummy2.next

        # El nuevo primer nodo es el primero de la lista 1 (dummy1.next, no el dummy).
        # Si no hay menores, dummy1.next ya es el primero de la lista 2, y funciona igual.
        self.head = dummy1.next

def find_kth_from_end(ll, k):
    """
    Devuelve el nodo que está en la posición k contando desde el FINAL
    de la lista. Con k = 1 devuelve el último nodo, con k = 2 el penúltimo, etc.

    Parámetros:
        ll: la lista enlazada (un objeto Linkedlist). Se usa ll.head.
        k: posición contando desde el final (empieza en 1).

    Devuelve:
        El nodo encontrado, o None si k es mayor que el tamaño de la lista,
        si k es 0 o negativo, o si la lista está vacía.

    Idea: usamos dos punteros separados por una distancia fija de k nodos.
      1) Adelantamos "fast" k pasos, mientras "slow" se queda en el inicio.
      2) Avanzamos los dos a la vez, de uno en uno.
      3) Cuando "fast" se sale de la lista (None), "slow" está justo en
         el nodo que buscamos, porque siempre iba k nodos por detrás.

    Ejemplo con 1 -> 2 -> 3 -> 4 -> 5  y  k = 2  (queremos el 4):
      tras adelantar fast k pasos:  slow=1, fast=3
      vuelta 1: slow=2, fast=4
      vuelta 2: slow=3, fast=5
      vuelta 3: slow=4, fast=None   (fast se salió, el bucle termina)
      resultado: 4

    Ventaja: no hace falta saber el tamaño de la lista ni recorrerla dos
    veces. Coste: O(n) en tiempo y O(1) en memoria.
    """
    # Los dos punteros empiezan en el primer nodo
    slow = ll.head
    fast = ll.head

    # Paso 1: adelantamos "fast" k nodos
    for _ in range(k):
        # Si nos quedamos sin nodos antes de dar los k pasos,
        # la lista es más corta que k: esa posición no existe
        if fast is None:
            return None
        fast = fast.next

    # Paso 2: avanzamos los dos punteros a la vez hasta que "fast" se salga
    # de la lista. Como "slow" va k nodos por detrás, queda en el nodo buscado.
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow