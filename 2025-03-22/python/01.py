#
# In an array, there is an element only occouring once
# Other elements occour multiple times
# Find that element in O(n) time


def solve(arr: list):
    counter = {}
    for c in arr:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    for k, v in counter.items():
        if v == 1:
            return k


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
out = solve(arr)
print(f"Element occouring only once: {out}")

# Trainer Comment - Use a sliding window to solve this problem (IDK WHY!)