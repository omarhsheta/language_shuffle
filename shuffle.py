def shuffle(s, t, result=None, string=''):
    """This function computes all the possible combinations between strings 's' and 't'
       and returns the set of all possible combinations of those two strings."""
    if result == None:
        result = set()
    if len(s) == 0:
        result.add(string+t)
        return result
    elif len(t) == 0:
        result.add(string+s)
        return result
    else:
        first = shuffle(s[1:], t, string=string+s[0])
        second = shuffle(s, t[1:], string=string+t[0])
        union = first.union(second)
        return union

def shuffle_language(A, B):
    """Works the same way as the previous function, but iterates through the languages A and B.
       Meaning, that every language contains at least one string, and the function will provide
       every possible combinations of the strings of languages A and B"""
    if len(A) == 0:
        return A
    elif len(B) == 0:
        return B
    else:
        result = set()
        for x in A:
            for y in B:
                result = result.union(shuffle(x, y))
        return result

print(sorted(shuffle_language({'abc'}, {'abc'})))
