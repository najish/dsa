from re import S


def happyNumber(n):

    while n != 1:
        length = 0
        number = n 

        while number != 0:
            length += 1
            number = number // 10
        
        number = n
        while length != 0:
            digit = number % length

    return True