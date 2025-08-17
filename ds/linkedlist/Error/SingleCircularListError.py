class SingleCircularListError(Exception):

    def __init__(self, message):
        super().__init__(message)




class NotValidOperationError(SingleCircularListError):

    def __init__(self,message):
        super().__init__(message)