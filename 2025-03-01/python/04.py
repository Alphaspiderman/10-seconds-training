#
# For a given array and a range
# From the range, add a number to the array to maximize the LCM
# Return the number


def hcf(a: int, b: int):
    h = min(a, b)
    while h != 0:
        if a % h == 0 and b % h == 0:
            return h
        h -= 1
    return 1


def solve(arr: list[int], upper: int):
    arr_lcm = arr[0]
    for val in arr[1:]:
        arr_lcm = arr_lcm * val // hcf(arr_lcm, val)
    soln = 1
    soln_val = arr_lcm * 1 // hcf(arr_lcm, 1)
    for i in range(upper + 1):
        i_val = arr_lcm * i // hcf(arr_lcm, i)
        if i_val >= soln_val:
            soln = i
            soln_val = i_val
    return soln


arr = [5, 2, 3, 4]
print(arr)
print(solve(arr, 9))
