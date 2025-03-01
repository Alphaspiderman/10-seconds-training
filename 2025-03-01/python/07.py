#
# Find value of max(arr[j]-arr[i]) where i < j


def solve(arr: list[int]):
    max_map = {len(arr): arr[-1]}
    for i in range(len(arr) - 1, -1, -1):
        max_map[i] = max(max_map[i + 1], arr[i])
    print(max_map)
    soln = 0
    for idx, val in enumerate(arr):
        soln = max(soln, max_map[idx] - val)
    return soln


arr = [7, 2, 12, 15, 10, 14]
print(arr)
print(solve(arr))
