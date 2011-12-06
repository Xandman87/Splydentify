#!/bin/bash

if [ "$1" == -regen ]
then
	./Quotients.py

	./scorecalc.py markov_pos.json train_pos.txt > train_pos.json
	./scorecalc.py markov_neg.json train_neg.txt > train_neg.json

	./scorecalc.py markov_pos.json test_pos.txt > test_pos.json
	./scorecalc.py markov_neg.json test_neg.txt > test_neg.json
fi

./plotMarkov.py train_pos.json train_neg.json

./decide.py 2.25
