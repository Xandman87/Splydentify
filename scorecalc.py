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

def score(pos_probs, neg_probs, seq):
    score = 1
    lastletter = ""
    for letter in seq:
        score *= pos_probs[lastletter+letter]/neg_probs[lastletter+letter]
        lastletter=letter
    return log(score, 2)

def main(pos_probs, neg_probs, data):
    import json
    pos_probs = json.load(open(pos_probs))
    neg_probs = json.load(open(neg_probs))
    scores = []
    from Bio import SeqIO
    for seq in SeqIO.parse(data, "fasta"):
        scores.append(score(pos_probs, neg_probs, seq))
    from sys import stdout
    json.dump(scores, stdout)

if __name__ == "__main__":
    from sys import argv
    main(argv[1], argv[2], argv[3])

