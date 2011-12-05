#!/usr/bin/env python2

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
        figure(0)
        hist(self.values1, 50, normed=1, facecolor='y', alpha=0.5)
        figure(1)
        hist(self.values2, 50, normed=1, facecolor='b', alpha=0.5)
        title('Title')
        xlabel('x_label')
        ylabel('yLabel')
        show()

if __name__ == '__main__':
    pm = PlotMarkov(str(sys.argv[1]), str(sys.argv[2]))
    pm.plot()
