from .Error.SingleCircularListError import NotValidOperationError
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))



class SingleCircularList:

    class Node:
        def __init__(self,data):
            self.data = data 
            self.next = None


    def __init__(self):
        self.head = None
        self.length = 0

    
    # insertion

    def insertAtFirst(self,data):
        try:
            node = self.Node(data)
            if self.head is None:
                self.head = node 
            else:
                pass

            
        except Exception as e:
            pass 

    def insertAtLast(self,data):
        pass 

    def insertAtIndex(self,index,data):
        pass 

    def insertAtMiddle(self,data):
        pass 


    # Traversal

    def printList(self):
        try:
            if self.length == 0:
                raise NotValidOperationError('Operation: ') 
            current = self.head 

            while current is not None:
                print(f"{current.data} ",end=' ')
                current = current.next 
        except NotValidOperationError as e:
            print(f"Invalid Operation: {e}")



if __name__ == "__main__":
    print(sys.path)
    list = SingleCircularList()

    list.printList()