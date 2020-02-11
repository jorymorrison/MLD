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
            count = 0
            for p in range(5):
                for q in range(p,5,1):
                    if contents[x]['lexical_signature'].keys()[p]==contents[w]['lexical_signature'].keys()[p]:
                        count+=1
            if count>=4:
                test=[]
                for y in range(len(contents[w]['tone'])):
                    for z in range(len(contents[x]['tone'])):
                        if contents[w]['tone'][y]['tone_id']==contents[x]['tone'][z]['tone_id']:
                            outputs.append(chisquare([contents[w]['tone'][y]['score'], contents[x]['tone'][z]['score']]))
print(outputs)
