class DoubleCircularList:

    class Node:
        def __init__(self,data):
            self.data = data
            self.prev = self.next = None

    def __init__(self):
        self.head = None
        self.length = 0
        