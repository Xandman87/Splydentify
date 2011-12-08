#!/usr/bin/python

import sys, math, json

def try_cutoff(cutoff, show=False):

    cut_off = float(cutoff)

    pos = json.load(open("scores_pos.json"))
    neg = json.load(open("scores_neg.json"))

    TP, npos = len(filter(lambda v: v >= cut_off, pos)), len(pos)
    FP, nneg = len(filter(lambda v: v >= cut_off, neg)), len(neg)

    FN = npos - TP
    TN = nneg - FP

    denom = (TP + FP) * ( TP + FN ) * ( TN + FP ) * ( TN + FN )

    if denom == 0:
        denom = 1

    mcc = float( TP * TN - FP * FN ) / math.sqrt( denom )

    if show:
        print "splice sites in pos: %d / %d" % (TP, npos)
        print "splice sites in neg: %d / %d" % (FP, nneg)

        sensivity = float(TP) / (TP + FN)

        specifity = float(TN) / (TN + FP)

        print "specifity: %f\nsensivity: %f" % (sensivity, specifity)


        print "Matthews correlation coefficient:", mcc

    return mcc


def decide():
    mccs = {}

    for i in range(100):

       co = -6 + i * (12. / 50)

       mccs[co] = try_cutoff(co)

    mx = max(mccs.values())
    maxmccs = filter(lambda keyvalue: keyvalue[1] == mx, mccs.iteritems())

    for key, val in maxmccs:

        try_cutoff(key, show=True)


if __name__ == "__main__":

    decide()
