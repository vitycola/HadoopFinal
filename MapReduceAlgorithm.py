#!/usr/bin/env python
import sys


init_state = 'null'
init_count = 0
init_score = 0

#with open('./prueba_mapper.txt') as data:

    #for line in data:
for line in sys.stdin:

        #try:

        state, score = line.split(',')
        state = str(state)
        score = int(score)


        if state == init_state:
            #print('inicial', state, score)
            init_score = init_score + score
            init_count = init_count + 1

        else:
            if init_state == 'null':
                init_state = state
                init_score = score
                init_count = 1
            else:
                total_score = round(float(init_score)/float(init_count),3)
                print '%s%s%s' % (str(init_state), ',', total_score)
                init_state = state
                init_count = 1
                init_score = score

if init_state == state:
    print '%s%s%s' % (str(init_state), ',', total_score)


        #except: pass
