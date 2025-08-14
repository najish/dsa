from venv import create


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None

    def __init__(self):
        self.head = None
        

    def printList(self):

        head = self.head 
        while head is not None:
            print(f"{head.data} -> ", end='')
            head = head.next
        print('null')

    

    def addHead(self, data):
        head = self.head 
        node = self.Node(data)
        node.next = head 
        self.head = node 

    def addTail(self,data):
        head = self.head
        if head is None:
            self.head = self.Node(data)
        else:
            while head.next is not None:
                head = head.next
            head.next = self.Node(data)
    

    def get_number(self, head):
        if head is None:
            return 0
        return self.get_number(head.next) * 10 + head.data 




def printList(head):
    if head is None:
        return None
    print(f"{head.data} ->", end='')
    printList(head.next)




list = LinkedList()
list.addTail(6)
list.addTail(8)
list.addTail(7)
list.printList()


list2 = LinkedList()
list2.addTail(6)
list2.addTail(8)
list2.addTail(7)

number1 = list.get_number(list.head)
number2 = list2.get_number(list2.head)

print(number1 + number2)

