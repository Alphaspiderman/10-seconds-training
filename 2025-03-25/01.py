#
# In an array, find the majority element
# Basically an element that appears more than n/2 times

def solve(arr: list):
    n = len(arr)
    count = 1
    majority = arr[0]
    for i in range(1, n):
        if arr[i] == majority:
            count += 1
        else:
            count -= 1
            if count == 0:
                majority = arr[i]
                count = 1
    count = 0
    for i in range(n):
        if arr[i] == majority:
            count += 1
    if count > n // 2:
        return majority
    return -1


arr = [5, 3, 5, 5, 8]
print(solve(arr))
