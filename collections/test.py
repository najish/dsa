"""
    collections module in python has number of useful classes that provide fast implementation of storing collections



    modules:
        - namedtuple: factory function for creating tuple subclasses with named fields
        - deque: like list container with fast appends pops on either end
        - ChainMap: 
        - Counter
        - OrderDict
        - defaultdict
        - UserDict
        - UserList
        - UserString
"""
from collections import deque
import time

# List front pop
lst = list(range(10_0000))
start = time.time()
while lst:
    lst.pop(0)
print("List pop(0):", time.time() - start)

# Deque popleft
dq = deque(range(10_0000))
start = time.time()
while dq:
    dq.popleft()
print("Deque popleft():", time.time() - start)





