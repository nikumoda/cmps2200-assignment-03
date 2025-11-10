from main import *

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

# ADDED FOR ALIGNMENT DIST
def test_alignment_distance():
    for S, T in test_cases:
        aS, aT = fast_align_MED(S, T)
        dist = sum(1 for x, y in zip(aS, aT) if x == '-' or y == '-')
        assert dist == fast_MED(S, T)

