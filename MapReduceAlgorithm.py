#!/usr/bin/env python
import json
import sys


init_state = 'null'
init_count = 0
init_score = 0

with open('./prueba_mapper.txt') as data:

    for line in data:
    #for line in sys.stdin:
        #try:
            #item = json.loads(line) #Carga de un JSON
        #except: pass

        #try:

            state, score = line.split(',')
            state = str(state)
            score = int(score)
            print('inicial', state, score)
            if state == init_state:
                init_score = init_score + score
                init_count = init_count + 1

            else:
                if init_state == 'null':
                    init_state = state
                    init_score = score
                    init_count = 1
                else:
                    total_score = init_score/init_count
                    print '%s%s%d' % (str(init_state), ',', total_score)
                    init_state = state
                    init_count = 1
                    init_score = score


        #except: pass
