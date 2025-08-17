class DoubleListError(Exception):

    def __init__(self,message):
        super().__init__(message)



class InvalidOperationError(DoubleListError):

    def __init__(self,message):
        super().__init__(message)
