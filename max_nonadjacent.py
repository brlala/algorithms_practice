# Maximum of non-adjacent sum
data = [4, 6, 100, 2, 3, 8]  # this should return 112


def max_nonadjacent_sum(data):
    incl = 0
    excl = 0

    for i in data:
        # current exclude will be previous include if larger else maintain
        new_excl = excl if excl > incl else incl

        # include
        incl = excl + i
        excl = new_excl

    return max(excl, incl)


print(max_nonadjacent_sum(data))
