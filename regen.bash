#!/bin/bash

if [ "$1" == -regen ]
then
	./Quotients.py

	./scorecalc.py markov_pos.json markov_neg.json test_pos.txt > scores_pos.json
	./scorecalc.py markov_pos.json markov_neg.json test_neg.txt > scores_neg.json
fi

./plotMarkov.py scores_pos.json scores_neg.json

#./decide.py 2.25
