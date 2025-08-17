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
        self.length = 0
        

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
        self.length += 1

    def addTail(self,data):
        head = self.head
        if head is None:
            self.head = self.Node(data)
        else:
            while head.next is not None:
                head = head.next
            head.next = self.Node(data)
        self.length += 1

    def get_number(self, head):
        if head is None:
            return 0
        return self.get_number(head.next) * 10 + head.data 
    
    


    def remove_node(self,data):
        head = self.head 

        if self.length == 0:
            return 

        if head is None:
            return 
        
        current = head 
        prev = next = None

        while current is not None:
            next = current.next 
            if current.data == data:
                if prev is None:
                    self.head = current.next 
                else:
                    prev.next = next
            current = current.next 

        self.length -= 1

                
    def __len__(self):
        return self.length


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

print(len(list2))


