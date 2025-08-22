def insertion(arr):

    for i in range(1, len(arr)):
        j = i -1
        temp = arr[i]

        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

    return arr



arr1 = [5,3,2,0,2,1,-6,4]
arr2 = [5]

arr3 = [-9,-11]

print(insertion(arr1))
print(insertion(arr2))
print(insertion(arr3))