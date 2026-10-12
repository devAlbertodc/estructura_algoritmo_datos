from LinkedList import Linkedlist

'''my_linked_list = Linkedlist(10)
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.print_list()
my_linked_list.pop()
print()
my_linked_list.pop_first()
my_linked_list.print_list()

my_linked_list.append(30)
my_linked_list.append(40)
my_linked_list.append(50)'''

my_linked_list = Linkedlist(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.reverse_between(1,3)
#my_linked_list.print_list()

print(my_linked_list.get_lowest_value())