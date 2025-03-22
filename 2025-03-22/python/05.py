#
# In an array, find the equilibrium point
# Equilibrium point is an index where the sum of elements at before is equal to the sum of after


def solve(arr: list):
    n = len(arr)
    left_sum = 0
    total_sum = sum(arr)

    for i in range(n):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]

    return -1


arr = [5, 2, 10, 3, 4]
out = solve(arr)
print(f"Equilibrium Index: {out}")
print(f"Element at Equilibrium Index: {arr[out]}")
