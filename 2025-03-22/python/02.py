#
# In an array, find the largest sum of a contiguous subarray


def solve(arr: list):
    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current

    return max_global

arr = [-2, 5, -4, 7, 2, -1]
out = solve(arr)
print(f"Largest sum of a contiguous subarray: {out}")
