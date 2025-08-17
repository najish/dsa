from ds.linkedlist.Error.DoubleListError import InvalidOperationError


class DoubleList:

    class Node:

        def __init__(self,data):
            self.data = data
            self.prev = self.next = None


    def __init__(self):
        self.head = None 
        self.length = 0


    # insertion

    def insertAtFirst(self,data):
        try:
            node = self.Node(data)
            current = self.head 

            if current is None:
                self.head = node
            else:
                next = current.next
                current.prev = node 
                node.next = current 
                self.head = node 
            self.length += 1
        except InvalidOperationError as e:
            print(f"invalid oprationsdfaslfa: {e}")
        except Exception as e:
            print(f"Exception: {e.__traceback__}")

    def insertAtLast(self,data):
        try:
            node = self.Node(data)
            if self.head is None:
                self.head = node 
                self.length += 1
                return
            current = self.head 
            while current.next is not None:
                prev = current 
                current = current.next
            current.next = node 
            node.prev = current 
            self.length += 1
        except Exception as e:
            print(f"exception: {e}")

    
    # dundder method

    def __len__(self):
        return self.length 


    # printList 

    def printList(self):
        try:
            if self.length == 0:
                raise InvalidOperationError('Invalid Operation: Operation not allowed with current state')
            current = self.head 
            while current is not None:
                print(f"{current.data} ", end=' ')
                current = current.next
            print()
        except InvalidOperationError as e:
            print(f"Cannot print the List operation is Invalid")



if __name__ == "__main__":
    list = DoubleList()
    list.insertAtFirst(10)
    list.insertAtFirst(20)
    list.insertAtFirst(20)
    list.insertAtFirst(20)
    list.insertAtFirst(20)
    list.printList()
    print(len(list))
