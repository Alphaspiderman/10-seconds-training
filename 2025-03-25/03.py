#
# Sort a string in O(n) time complexity


def solve(s: str):
    n = len(s)
    count = {}
    for i in range(n):
        c = count.get(s[i], 0)
        count[s[i]] = c + 1
    ans = ""
    for i in range(26):
        letter = chr(ord("a") + i)
        ans += letter * count.get(letter, 0)
    return ans


arr = ["banana", "racecar"]
for s in arr:
    print(f"{s} -> {solve(s)}")
