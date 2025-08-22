def linear_search(arr,target):
    for item in arr:
        if item == target:
            return True
    return False 



def rec_linear_search(arr,index, target):
    if index < 0:
        return False
    
    if arr[index] == target:
        return True
    
    return rec_linear_search(arr, index - 1, target)






arr = [1,2,4,3,1]



print(linear_search(arr, 4))
print(linear_search(arr, 2))
print(linear_search(arr, 1))
print(linear_search(arr,-6))




print(rec_linear_search(arr,4,4))
print(rec_linear_search(arr,4,2))
print(rec_linear_search(arr,4,1))
print(rec_linear_search(arr,4,-6))
