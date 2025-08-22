from ctypes.wintypes import tagRECT


def binarySearch(arr,target):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return True
    return False


def rec_binarySearch(arr, low, high, target):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            return rec_binarySearch(arr, mid + 1, high, target)
        elif arr[mid] > target:
            return rec_binarySearch(arr, low , mid - 1, target)
        else:
            return True
    return False        
    

arr = [1,2,3,4,5,6]

print(binarySearch)

print(binarySearch(arr, -1))
print(binarySearch(arr, 0))
print(binarySearch(arr, 1))
print(binarySearch(arr, 2))
print(binarySearch(arr, 3))
print(binarySearch(arr, 4))
print(binarySearch(arr, 5))
print(binarySearch(arr, 6))
print(binarySearch(arr, 7))

print('------------------')

print(rec_binarySearch(arr,0, 5, -1))
print(rec_binarySearch(arr,0, 5, 0))
print(rec_binarySearch(arr,0, 5, 1))
print(rec_binarySearch(arr,0, 5, 2))
print(rec_binarySearch(arr,0, 5, 3))
print(rec_binarySearch(arr,0, 5, 4))
print(rec_binarySearch(arr,0, 5, 5))
print(rec_binarySearch(arr,0, 5, 6))
print(rec_binarySearch(arr,0, 5, 7))


