#
# In a String, A is Bitwise AND, B is Bitwise OR, C is Bitwise XOR, we only have 0 and 1
# Find the result of the expression


def solve(s: str):
    n = len(s)
    ans = int(s[0])
    for i in range(1, n):
        if s[i].isdigit():
            num = int(s[i])
            if s[i - 1] == "A":
                ans &= num
            elif s[i - 1] == "B":
                ans |= num
            elif s[i - 1] == "C":
                ans ^= num
    return ans


arr = ["1A1", "0A1", "1A0B1C1"]
for s in arr:
    print(f"{s} -> {solve(s)}")
