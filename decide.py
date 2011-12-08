#!/usr/bin/python

import sys, math, json

def try_cutoff(cut_off, show_info = False):

    # calculate True/False Positives/Negatives
    #
    pos = json.load(open("scores_pos.json"))
    neg = json.load(open("scores_neg.json"))
    npos = len(pos)
    nneg = len(neg)

    TP = len(filter(lambda v: v >= cut_off, pos))
    FP = len(filter(lambda v: v >= cut_off, neg))
    FN = npos - TP
    TN = nneg - FP

    # calculate the Matheaws Correlation Coefficiant
    #
    # --> http://en.wikipedia.org/w/index.php?title=Matthews_correlation_coefficient&oldid=424752995
    #
    # Quotes from the article:
    #  - "\text{MCC} = \frac{ TP \times TN - FP \times FN } {\sqrt{ (TP + FP) ( TP + FN ) ( TN + FP ) ( TN + FN ) } }"
    #  - "If any of the four sums in the denominator is zero, the denominator can be arbitrarily set to one."
    #
    denom = (TP + FP) * ( TP + FN ) * ( TN + FP ) * ( TN + FN )
    mcc = float( TP * TN - FP * FN ) / math.sqrt( denom or 1 )

    # show specifity, sensitivity, etc.
    #
    if show_info:
        print "Cut-Off Value:", cut_off
#        print " splice sites in pos: %d / %d" % (TP, npos)
#        print " splice sites in neg: %d / %d" % (FP, nneg)
        print " specifity:", float(TN) / (TN + FP)
        print " sensitivity:", float(TP) / (TP + FN)
        print " Matthews correlation coefficient:", mcc

    return mcc


def decide():

    mccs = {}       # dictionary of "cut-off values" and "mathew correlation coefficients"
    step = 0.1      # scan granularity - lower granularity => more tries
    upper = 6       # score range to scan
    lower = -6

    # a range generator that works with float values
    #
    def frange(low, high, step):
        for i in range(int(abs(high - low) / step + 1)):
            yield low + i * step

    # get the Mathews cc for all cut-off values
    #
    # FIXME: we're currently using one cpu core only
    # FIXME: this brute-force algorithm to find the maximum
    #        could probably be improved to work much quicker...
    #        e.g. binary search, if there are no local maximas, that is,
    #        the derivative of mcc = f(cut-off) has only one root (nullstelle)
    #        EDT: there seem to be local maximas!
    #             therefore a different approach would be needed
    #
    for co in frange(lower, upper, step):
#        print "trying...", co,
        mccs[co] = try_cutoff(co)
#        print " -> ", mccs[co]

    # find the maximum Mathews cc
    #
    _max = max(mccs.values())

    # extract all (most probably just one!) cut-off values
    # that yielded the maximum Mathews cc
    #
    max_cutoffs = filter(lambda co: mccs[co] == _max, mccs)

    # display some information about those cut-off values
    #
    for co in max_cutoffs:
        try_cutoff(co, show_info = True)

if __name__ == "__main__":

    decide()
