def binary_search(arr, target):
    left = 0 # this is the first element of the array, and we will start our searching from here.
    right =  len(arr) - 1 # this is the last element of the array. and we make it minus one because python index start from 0
    
    steps = 0 # this is the number of guess we will use to find the target
    
    while left <= right:
        mid = (left + right) // 2
        steps += 1
        
        if arr[mid] == target:
            print(f"Found the target {target} at step {steps}")
            return mid, steps
        
        elif arr[mid ] < target:
            left =  mid + 1 # we are saying that the target is not in the left side of the array
            print("  Target Not found on the left side of the array")
            
        else: 
            right =  mid - 1 # we are saying that the target is not in the right side of the array
            print("Target Not Found On The Right Side Of The Array")
            
    print(f"Target {target} Was Not Found In The Array after {steps} steps.")
    return -1, steps 

#Test

array = [34,56,78,90]
target = 56

postion, steps = binary_search(array,target)

print(f"The target {target} was found at position : {postion}")
print(f"It took {steps} steps to find the target.")