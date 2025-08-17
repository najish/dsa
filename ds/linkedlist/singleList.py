'''
OPERATION:
    INSERTION:
        AT HEAD, AT TAIL, AT POSITION
    DELETE:
        FIRST OCCURENCE, AT POSITION
    SEARCHING:
        CONTAINS

        
'''

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from ds.linkedlist.Error import SingleListError
from ds.linkedlist.Error.SingleListError import InvalidIndexError, EmptySingleListError, InvalidOperationSingleListError, NodeNotFoundError


class SingleList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0

    # dunder methods
    def __len__(self):
        return self.length
    
    # insertion
    def insertAtFirst(self,data):
        node = self.Node(data)
        node.next = self.head 
        self.head = node
        self.length += 1            


    def insertAtLast(self, data):
        head = self.head
        if head is None:
            self.head = self.Node(data)
        else:
            current = head 
            while current.next is not None:
                current = current.next
            current.next = self.Node(data)
        self.length += 1


    def insertAtPosition(self, index, data):
        try:
            if index < 0:
                raise InvalidIndexError(index)
            
            prev = next = None
            current = self.head 
            currentIndex = -1 
            while current is not None:
                currentIndex += 1
                if currentIndex == index:
                    node = self.Node(data)
                    if prev is None:
                        node.next = self.head 
                        self.head = node 
                    else:
                        prev.next = node
                        node.next = current 
                prev = current 
                current = current.next 
            self.length += 1


        except InvalidIndexError as e:
            print(f"Invalid Index: {e}") 

    # deletion
    def deleteAtFirst(self):
        try:
            if self.head is None:
                raise EmptySingleListError()

            self.head = self.head.next 
            self.length -= 1
        except EmptySingleListError as e:
            print(f"Empty Deletion Error")

    def deleteAtLast(self):
        try:
            if self.head is None:
                raise EmptySingleListError()
            current = self.head 
            prev = None
            while current.next is not None:
                prev = current
                current = current.next 
            if prev is None:
                self.head = None
            else:
                prev.next = None
            self.length -= 1
        except EmptySingleListError as e:
            pass 

    def deleteAtPosition(self,index):
        try:
            if self.length == 0 or index < 0:
                raise EmptySingleListError()
            
            current = self.head 
            currentIndex = -1
            prev = next = None
            while current is not None:
                currentIndex += 1
                if currentIndex == index:
                    if prev is None:
                        self.head = self.head.next 
                    else:
                        prev.next = current.next
                    break
                prev = current 
                current = current.next

        except EmptySingleListError as e:
            print(f"Cannot perform delete operation list is already empty: {e}")
        
    # search the value in SingeList

    def __contains__(self,data):
        try:
            if self.length == 0:
                raise EmptySingleListError()
            current = self.head 

            while current is not None:
                if current.data == data:
                    return True
                current = current.next 
            return False 
        except EmptySingleListError as e:
            print(f'cannot perform the contains operation')

    def getNode(self,data):
        try:
            if self.length == 0:
                raise InvalidOperationSingleListError('getNode')
            current = self.head 

            while current is not None:
                if current.data == data:
                    return current
                current = current.next 
            raise NodeNotFoundError('Node is not present')
        except EmptySingleListError as e:
            print(f"Invalid operation")
        except NodeNotFoundError as e:
            print(f"Node not found")
        except InvalidOperationSingleListError as e:
            print(f"Invalid Operation {e}")


    # print the list 

    def printList(self):
        current = self.head 
        while current is not None:
            if current.next is None:
                print(f"{current.data}->nulll",end='')
            else:
                print(f"{current.data}->",end='')
            current = current.next 
        print()

if __name__ == "__main__":
    list = SingleList()
    list.insertAtFirst(10) 
    list.insertAtFirst(10) 
    list.insertAtFirst(10)
    list.insertAtLast(20)
    list.insertAtLast(50)
    list.printList()
    x = SingleList()
    node = list.getNode(20)
    print(node.data)