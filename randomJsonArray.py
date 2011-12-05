#!/usr/bin/env python2

import json
import sys
import random


def randomToJson(a, b):
    
    randomNum = []
    for i in range(500):
        # create a random number and save it in the list
        randomNum.append(random.uniform(a, b))
    
    values = json.dumps(randomNum, ensure_ascii=False)
    
    if len(sys.argv) == 1:
        filename = str(raw_input("Bitte geben sie einen Dateinamen ein: "))
    else:
        filename = sys.argv[1]
    
    if filename.find('.json') == -1:
        filename = filename + '.json'


    f = open(filename, 'a')
    f.write(values)
    f.close()

    return filename

filename = randomToJson(35, 100)

print "Done...\tsaved random Numbers in the file: " + filename 
