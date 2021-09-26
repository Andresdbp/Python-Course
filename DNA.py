from collections import Counter
counter = Counter()
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
for nt in seq:
    counter[nt] += 1
print(counter)
