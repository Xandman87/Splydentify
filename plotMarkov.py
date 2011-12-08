#!/usr/bin/python

import sys
import json
from pylab import *

class PlotMarkov():

    def __init__(self, filename1, filename2):

        self.filename1 = filename1
        self.filename2 = filename2

        f = open(self.filename1, 'r')
        self.values1 = json.loads(f.read())

        g = open(self.filename2, 'r')
        self.values2 = json.loads(g.read())

    def plot(self):

#        labels = [][]

        for vals, ax_f, label, color in (
			(self.values1, lambda: subplot(1,1,1), "pos", 'r'),
			(self.values2, lambda: twinx()       , "neg", 'b')):

            args = {
                "label"       : label,
		"facecolor"   : color,
		"bins"        : 100,
                "range"       : (-7,7),
		"alpha"       : 0.5,
#               "log"         : True,
#		"histtype"    : "step",
            }

            ax = ax_f()
 
#            labels[ hist(vals, **args) ] = label
            hist(vals, **args)

            ax.legend(loc=0)

#        legend(labels.keys(), labels.values())
#        legend()

#        title('Markov Chain Scores')

#        title(self.filename1 + " | " + self.filename2)

#        ax.set_ylim(0, 10000)

#        ax.set_xlabel('score')
#        ax.set_ylabel('count')

        show()

if __name__ == '__main__':
    pm = PlotMarkov(sys.argv[1], sys.argv[2])
    pm.plot()
