#
# Find largest even-odd subarray
# Return length
def even_odd(a, b):
    return (a % 2 == 1 and b % 2 == 0) or (a % 2 == 0 and b % 2 == 1)


def solve(arr: list[int]):
    l, r = 0, 0
    length = 0
    while r < len(arr):
        if l == r:
            if not even_odd(arr[l], arr[l + 1]):
                l += 1
            r += 1
        else:
            if even_odd(arr[r - 1], arr[r]):
                r += 1
            else:
                length = r - l
                l = r

    return max(length, r - l)


arr = [1, 2, 3, 4, 5, 6, 10, 1, 2, 10, 9, 1, 2, 3, 4, 5, 6, 7]
print(arr)
# print([i % 2 == 0 for i in arr])
print(solve(arr))
