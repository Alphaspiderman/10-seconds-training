#
# Make an array in such a way that 2 +ve can be together, 2 -ve can be together, a +ve and a -ve together should be removed
# Return an array of leftover numbers


def solve(arr: list[int]):
    idx = 1
    while idx < len(arr):
        if (arr[idx] > 0 and arr[idx - 1] > 0) or (arr[idx] < 0 and arr[idx - 1] < 0):
            idx += 1
        else:
            arr.pop(idx)
            arr.pop(idx - 1)
            idx -= 1
    return arr


arr = [5, 2, 7, -5, 3, -6, -7, 4]
print(arr)
print(solve(arr))
