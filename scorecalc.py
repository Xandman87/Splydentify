#!/usr/bin/python
#
# scorecalc.py - calculate transition scores
#
# Copyright (C) 2011  Patrick Pfeifer

"""

usage: scorecalc.py frequencies.json data.txt

  based on the transition frequencies in scores.json,
  calculate the scores of all sequences found in data.txt

  the result is printed on standard output

"""
from math import log

def score(seq, freqs):
    score = 1
    lastletter = ""
    for letter in seq:
        score *= freqs[lastletter+letter]
        lastletter=letter
    score /= 0.25**len(seq)
    return log(score)/log(2)

def main(frequencies, data):
    import json
    freqs = json.load(open(frequencies))
    scores = []
    from Bio import SeqIO
    for seq in SeqIO.parse(data, "fasta"):
        scores.append(score(seq, freqs))
    from sys import stdout
    json.dump(scores, stdout)

if __name__ == "__main__":
    from sys import argv
    main(argv[1], argv[2])

