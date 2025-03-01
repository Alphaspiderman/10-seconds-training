#
# In any row, last of prev is first
# Sum of prev + one above = curr
# Return - IDK, mat or final val


def solve(n):
    soln = []
    last = 1
    for i in range(n + 1):
        lst = [last]
        val = last
        for j in range(1, i):
            val = lst[j - 1] + soln[i - 1][j - 1]
            lst.append(val)
        last = val
        soln.append(lst)

    _ = soln.pop(0)
    return soln


out = solve(int(input("N:")))
print(out)
