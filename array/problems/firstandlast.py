def find(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1 
        elif arr[mid] > target:
            high = mid - 1
        else:
            return (low, high)
    return False 


def searchRange(arr, target):

    result = [-1,-1]
    first = last = None
    test = find(arr, target)
    if test:
        flag = False
        start, end = test
        while start <= end:
            if flag == False and arr[start] == target:
                first = last = start 
                flag = True
            elif arr[start] == target:
                if last < start:
                    last = start 
            start += 1
        result[0] = first
        result[1] = last 
    return result 



arr = [1,1,1,1,1,1,1]

print(searchRange(arr, 1))

