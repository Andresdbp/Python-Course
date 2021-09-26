def PatternMatching(Pattern, Genome):
    positions = []
    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        if Pattern == Genome[i:i+k]:
            positions.append(i)
    return positions

data = PatternMatching('AA','AAACATAGGATCAAC')

print(*data, sep=' ')