"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for value in items:
        count = 0
        for val in items:
            if str(value) == str(val):
                count += 1
        frequencies[str(value)] = count

    return frequencies
