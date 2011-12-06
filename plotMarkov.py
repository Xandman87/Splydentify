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
        ax1 = subplot(111)
        hist(self.values1, 50, facecolor='y', alpha=0.5)
        
        ax2 = twinx()
        hist(self.values2, 50, facecolor='r', alpha=0.5)
        
        title('Title')
        ax1.set_ylabel('y_label1')
        ax2.set_ylabel('y_label2')
        ax1.set_xlabel('xLabel')

        show()

if __name__ == '__main__':
    pm = PlotMarkov(str(sys.argv[1]), str(sys.argv[2]))
    pm.plot()
