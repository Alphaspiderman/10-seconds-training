#
# In a String, where numbers are separated by alphabets
# Find the sum of all numbers


def solve(s: str):
    n = len(s)
    ans = 0
    num = 0
    for i in range(n):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        else:
            ans += num
            num = 0
    ans += num
    return ans

s = "A212B51C12"
print(solve(s))