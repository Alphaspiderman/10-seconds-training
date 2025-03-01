#
# Find count of vowels and consonants in a string without relational operators
# Preferred to do in C


def solve(string: str):
    string = string.lower()
    vowels = (
        string.count("a")
        + string.count("e")
        + string.count("i")
        + string.count("o")
        + string.count("u")
    )
