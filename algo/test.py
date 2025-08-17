def return_list(number):

    if number == 0:
        return []

    return [number] + return_list(number-1)


def return_list2(number):
    if number == 0:
        return []
    
    return return_list(number-1) + [number]


def return_list3(number):
    if number == 0:
        return []
    return [].append(return_list3(number-1)) 




x = list()
y = set()
z = dict()
t = tuple()
p = object()
print(type(x))
print(type(y))
print(type(z))
print(type(p))
print(type(t))


print(return_list(5))
print(return_list2(5))
print(return_list3(5))