#
# For a given number, return the sum of the 3rd, 4th digit without using extra variables
# Preferred to do in C


def solve(num: int):
    return int(str(num)[2]) + int(str(num)[3])


num = 5321641
print(num)
print(solve(num))
