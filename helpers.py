from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    # TODO
    # Takes a and b and puts them into a set while splitting them
    lineA = set(a.split("\n"))
    lineB = set(b.split("\n"))
    # Returns lineA and lineB into a list and uses intersection method which sifts out the elements found in both sets.
    return list(lineA.intersection(lineB))


def sentences(a, b):
    """Return sentences in both a and b"""
    # TODO
    # Sets a and b and utilizes sent_tokenize in order to seperate out the sentences
    sentenceA = set(sent_tokenize(a))
    sentenceB = set(sent_tokenize(b))
    # Returns sentenceA and sentenceB into a list while again utilizing the intersection method 
    return list(sentenceA.intersection(sentenceB))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    # TODO
    # Set a and b and get the substring of a and b from index to but not including the index + n and include helper function
    substringA = set(a[i:i+n] for i in range(len(a)-(n-1)))
    substringB = set(b[i:i+n] for i in range(len(b)-(n-1)))
    return list(substringA.intersection(substringB))
