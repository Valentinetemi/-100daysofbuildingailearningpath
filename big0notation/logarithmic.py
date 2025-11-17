def binary_search(arr, target):
    low =0 # this is should be the first element in the array
    high = len(arr) - 1 #this should be the last element in the array
    steps =0 # this is the number of guesses, so it will keep track of the number of guess
    
    while low <= high:
        mid = (low + high) //2
        steps +=1
        
        if arr[mid] ==  target:
            return mid, steps
        
        elif arr[mid] < target:
            low = mid + 1 #it should move to the right to search for the target
            
        else:
            high = mid -1 #it should move back to the left hand side to search for the target
            
    return mid, steps

arr = [1, 5, 7, 20, 90, 40, 55]
target = 90

position, steps = binary_search(arr, target)
print(f"Target {target} found after {steps} steps") 