from typing import Pattern

def ReverseCompliment(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

def Reverse(Pattern):
    rev = ''
    for char in Pattern:
        rev = char + rev
    return rev

def Complement(Pattern):
    bp = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    comp = ''
    for base in Pattern:
        comp += bp.get(base)
    return comp

print(ReverseCompliment(' '))
