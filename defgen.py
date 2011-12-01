#!/usr/bin/python
#
# defgen.py - generate a json file with default transition prabailities for all 20 - 0.25
# 
# Copyright (C) 2011  Patrick Pfeifer

freqs = {}
letters = "acgt"
for l in letters:
	freqs[l] = 0.25
	for l2 in letters:
		freqs[l + l2] = 0.25

import json
from sys import stdout

json.dump(freqs, stdout)
