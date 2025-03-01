#
# In a list of strings, if same strings occur next to each other, remove
# Return leftover strings


def solve(arr: list[str]):
    idx = 1
    while idx < len(arr):
        if arr[idx] == arr[idx - 1]:
            arr.pop(idx)
            arr.pop(idx - 1)
            idx -= 1
        else:
            idx += 1
    return arr


arr = ["ab", "bc", "cd", "cd", "bc", "de"]
print(arr)
print(solve(arr))
