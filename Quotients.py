#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
Created on Thu Dec 01 11:48:00 2011

@author: Xandman-mini
"""

import json

class Quotients:

    # dictionaries carrying counts and frequencies
    counts = {}
    freqs = {}

    # init a Quotients
    #
    def __init__(self, name):
        self.name = name
        for ltr in 'acgt':
            self.counts[ltr] = 0
            for ltr2 in 'atgc':
                self.counts[ltr+ltr2] = 0

    # Based on the data found in file,
    # create a json-file holding relativ frequencies
    #
    def makeJson(self, file):
        for line in file:
            if(line[0] != '>'):
                self.count(line.strip(' \t\r\n'))
        self.calcQuotients()
        self.storeJson()
            
    # counts occurences of motifs
    #
    def count(self, line):
        last = ''
        for ltr in line:
            self.counts[last+ltr] += 1
            last = ltr

    # calculates relativ frequencys of motifs and stores them in dictionary        
    #
    def calcQuotients(self):

        # tsum : transition class (count) sum
        #
        # v- sum of all one-letter transitions
        #
        tsum = sum(self.counts[ltr] for ltr in 'acgt')

        for ltr in 'acgt':

            self.freqs[ltr] = float(self.counts[ltr]) / tsum

            # v- sum of all 2-letter transitions starting with ltr
            #
            tsum2 = sum(self.counts[ltr+ltr2] for ltr2 in 'acgt')

            for ltr2 in 'acgt':

                self.freqs[ltr+ltr2] = float(self.counts[ltr+ltr2]) / tsum2

    # save the json file
    #
    def storeJson(self):
        json.dump(self.freqs, open(self.name,'w'))

if __name__ == "__main__":

    # open training files
    #
    pos = open('train_pos.txt', 'r')  
    neg = open('train_neg.txt', 'r')       

    # create Quotients and save frequencies       
    Quotients('markov_pos.json').makeJson(pos)
    Quotients('markov_neg.json').makeJson(neg)
