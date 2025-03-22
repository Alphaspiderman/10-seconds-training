#
# Trapping Rainwater Problem
# Given n integers representing an elevation map where the width of each bar is 1
# Compute how much water it can trap after raining.


def solve(arr: list):
    n = len(arr)
    left = [0] * n
    right = [0] * n
    water = 0

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])

    for i in range(n):
        water += min(left[i], right[i]) - arr[i]

    return water

arr = [5, 0, 3, 4, 6]
out = solve(arr)
print(f"Amount of water trapped: {out}")