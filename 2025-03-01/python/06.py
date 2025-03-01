#
# Print the number of consecutive occurrences of a char in a string


def solve(string: str):
    i = 0
    while i < len(string):
        fast = 0
        char = string[i]
        while i + fast < len(string) and string[i + fast] == char:
            fast += 1
        print(f"{char}:{fast}")
        i += fast


txt = "aabbbccaadaae"
print(txt)
solve(txt)
