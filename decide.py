#!/usr/bin/python

import json



import sys

co = float(sys.argv[1])



pos = json.load(open("test_pos.json"))
neg = json.load(open("test_neg.json"))

nposplice, npos = len(filter(lambda v: v >= co, pos)), len(pos)
nnegsplice, nneg = len(filter(lambda v: v >= co, neg)), len(neg)

print "splice sites in pos: %d / %d" % (nposplice, npos)
print "splice sites in neg: %d / %d" % (nnegsplice, nneg)

sensivity = float(nposplice) / (nposplice + (npos - nposplice))

specifity = float(nneg - nnegsplice) / ((nneg - nnegsplice) + nnegsplice)

print "specifity: %f\nsensivity: %f" % (sensivity, specifity)
