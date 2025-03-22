#
# In an array, move all 0's to the end of the array
# Time complexity should be O(n), and space complexity should be O(1)

def solve(arr: list):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    return arr

arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
out = solve(arr)
print(f"Array with 0's at the end: {out}")