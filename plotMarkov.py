#!/usr/bin/python

import sys, json, pylab

class PlotMarkov():

    def __init__(self, pos_scores, neg_scores):

        self.pos_scores = json.load(open(pos_scores, 'r'))
        self.neg_scores = json.load(open(neg_scores, 'r'))

    def plot(self):

        ax = None

        for vals, ax_fun, color, label, leg_loc in (
			(self.pos_scores, pylab.axes,  'r', 'Positive Scores', 'upper right'),
			(self.neg_scores, pylab.twinx, 'b', 'Negative Scores', 'upper left' )):

            ax = ax_fun()
            ax.hist(vals,
		bins        = 100,            # number of bins
#                range       = (-7,7),         # x-axis range (important! so all bins have the same width)
                label       = label,          # legend label
		facecolor   = color,          # bins color
		alpha       = 0.5,            # bins alpha value (semi-transparent to see hidden/overlapping bins)
#               log         = True,           # logarhitmic y-axis
#		histtype    = "step",         # different histogram tipes - default is "bins"
            )
            ax.legend(loc=leg_loc)            # position label - supply loc=... to make sure they're not overlapping

        ax.set_title('Markov Chain Scores')

#        ax.set_ylim(0, 10000)

        ax.set_xlabel('score')
        ax.set_ylabel('count')

        pylab.show()

if __name__ == '__main__':

    pm = PlotMarkov(sys.argv[1], sys.argv[2])
    pm.plot()
