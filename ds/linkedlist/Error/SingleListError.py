
class SingleListError(Exception):

    def __init__(self,message='SingleListError'):
        super().__init__(message)

    
class InvalidIndexError(SingleListError):
    def __init__(self, index):
        super().__init__('invalid index error')
        print(f"Index value is invalid: {index}")
    


class EmptySingleListError(SingleListError):

    def __init__(self):
        super().__init__('The linked list is empty')
    


class InvalidOperationSingleListError(SingleListError):
    def __init__(self, message):
        super().__init__(f'Invalid Operation: {message}')

    
class NodeNotFoundError(SingleListError):
    def __init__(self,message):
        super().__init__(message)