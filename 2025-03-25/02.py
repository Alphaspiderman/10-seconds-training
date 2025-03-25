#
# Convert Excel sheet column to number
# A = 1, Z = 26, AA = 27


def solve(s: str):
    n = len(s)
    ans = 0
    for i in range(n):
        ans = ans * 26 + ord(s[i]) - ord("A") + 1
    return ans


arr = ["A", "Z", "AA", "AB", "ZY"]
for s in arr:
    print(f"{s} = {solve(s)}")
