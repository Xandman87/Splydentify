#!/usr/bin/python

import sys

from Quotients import Quotients

import scorecalc

from plotMarkov import PlotMarkov

import decide

from threading import Thread

def splice_detect(recalc = True):

    if recalc:
        Quotients('markov_pos.json').makeJson(open('train_pos.txt', 'r'))
        Quotients('markov_neg.json').makeJson(open('train_neg.txt', 'r'))

        orig_out = sys.stdout
        sys.stdout = open('scores_pos.json', 'w')
        scorecalc.main('markov_pos.json', 'markov_neg.json', 'test_pos.txt')
        sys.stdout = open('scores_neg.json', 'w')
        scorecalc.main('markov_pos.json', 'markov_neg.json', 'test_neg.txt')
        sys.stdout = orig_out


    pm = PlotMarkov('scores_pos.json', 'scores_neg.json')

    Thread(target = pm.plot).start()

    decide.decide()

if __name__ == "__main__":

    splice_detect()
