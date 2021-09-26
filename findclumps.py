from typing import Pattern


def FindClumps(Text, k, L, t):
    Patterns = []
    n = len(Text)
    for i in range(n-k+1):
        Window = Text[i:L]
        freqMap = FrequencyMap(Window, k)
        for key in freqMap:
            if freqMap[key] >= t:
                if key not in Patterns:
                    Patterns.append(key)
    return Patterns

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern] += 1
        else:
            freq[Pattern] = 1
    return freq

print(FindClumps('', 9, 500, 3))