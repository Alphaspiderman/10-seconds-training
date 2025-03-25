#
# In a String, that is like A3B2C1D1A7B1
# Compress the string to A10B3C1D1


def solve(s: str):
    n = len(s)
    i, j = 0, 1
    mapping = {}
    while j < n:
        if s[i].isalpha():
            j = i + 1
            while j < n and s[j].isdigit():
                j += 1
            mapping[s[i]] = int(s[i + 1 : j]) + mapping.get(s[i], 0)
            i = j
        else:
            i += 1

    return "".join([f"{k}{v}" for k, v in mapping.items()])


s = "A3B2C1D1A7B1"
print(solve(s))
