"""
Write an algorithms that generates all permutations of the string 
'abcdefghklmnopqrstuvwxyz0123456789'

As it's permutation, order is important.

ref. https://brilliant.org/wiki/permutations-with-repetition/
"""
import itertools


def print_all_perms(input):
    print("\nPrinting all permutations for {}".format(input))
    for i, x in enumerate(itertools.permutations(input)):
        print ("perm[{}] = {}".format(i + 1, "".join(x)))


print_all_perms(list("123"))
