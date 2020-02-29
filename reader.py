import os
import json
import glob
contents=[]
for file in glob.glob('*.json'):
	files = open(file, 'r')
	data=json.load(files)
	contents.append(data)
print(contents)
import json
import glob
import numpy
from scipy.stats import chisquare
contents=[]
outputs=[]
for file in glob.glob('*.json'):
	files = open(file, 'r')
	data=json.load(files)
	contents.append(data)
for w in range(len(contents)):
    for x in range(len(contents)):
        if x==w:
            continue
        elif contents[x]['article']['title']==contents[w]['article']['title']:
            continue
        else:
            test=[]
            count=0
            for c in list(contents[w][signature].keys()):
                for d in list(contents[x][signature].keys()):
                    if c==d:
                        count++
                    else:
                        continue
                    if count>=3:
                        for y in range(len(contents[w]['tone'])):
                            for z in range(len(contents[x]['tone'])):
                                    if contents[w]['tone'][y]['tone_id']==contents[x]['tone'][z]['tone_id']:
                                            outputs.append(chisquare([contents[w]['tone'][y]['score'], contents[x]['tone'][z]['score']]))
print(outputs)
