#!/usr/bin/python

# -*- encoding: utf-8 -*-

"""
Created on Thu Dec 01 11:48:00 2011

@author: Xandman-mini
"""

import json

class Quotients:

    # dictionaries carrying counts and frequencies
    counts = []
    freqs = []

    seq_len = 7

    # init a Quotients
    #
    def __init__(self, name):
        self.name = name

        new_dict = {}
        for ltr in 'acgt':
            new_dict[ltr] = 1
        self.counts.insert(0, new_dict)

        for idx in range(1, self.seq_len):
            new_dict = {}
            for ltr in 'acgt':
                for ltr2 in 'atgc':
                    new_dict[ltr+ltr2] = 1
            self.counts.insert(idx, new_dict)

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
        for idx, ltr in enumerate(line):
            self.counts[idx][last+ltr] += 1
            last = ltr

    # calculates relativ frequencys of motifs and stores them in dictionary        
    #
    def calcQuotients(self):


        for idx in range(self.seq_len):

            tsum = sum(self.counts[idx].values())

            new_freqs = {}
            for key in self.counts[idx]:
                new_freqs[key] = float(self.counts[idx][key]) / tsum

            self.freqs.insert(idx, new_freqs)
            
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
