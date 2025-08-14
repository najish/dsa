from tkinter import NO


class BinaryTree:

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def add(self, data, root = None):

        if root is None:
            root = self.root 

        if root is None:
            self.root = self.Node(data)
            return self.root 
        elif root.data > data:
            if root.left is None:
                root.left = self.Node(data)
            else:
                root.left = self.add(data, root.left)
        elif root.data < data:
            if root.right is None:
                root.right = self.Node(data)
            else:
                root.right = self.add(data, root.right)
        return root
    

    
    def remove(self,data, root=None):

        if root is None:
            root = self.root
        if root is None:
            return None
        elif root.data > data:
            if root.left is None:
                return None
            else:
                root.left = self.remove(data, root.left)
        elif root.data < data:
            root.right = self.remove(data, root.right)
        else:

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left 
            else:

                current = root.right 
                prev = None
                while current is not None:
                    prev = current 
                    current = current.left
                
                current.right = self.remove(prev.data, root.right)

        return root     



            


    

        

