import os
import json
import glob
import datetime
import numpy
from scipy.stats import chisquare
date = str(datetime.datetime.now())
path = os.path.split(os.path.abspath(__file__))[0] + '/comparison-' + date + ".json"
results = open(path, 'a+')
contents=[]
outputs=[]
for file in glob.glob('outputs/*.json'):
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
            for c in list(contents[w]['signature'].keys()):
                for d in list(contents[x]['signature'].keys()):
                    if c==d:
                        count+=1
                    else:
                        continue
                    if count>=3:
                        for y in range(len(contents[w]['tone'])):
                            for z in range(len(contents[x]['tone'])):
                                    if contents[w]['tone'][y]['tone_id']==contents[x]['tone'][z]['tone_id']:
                                            outputs.append({'comparison' : [contents[w]['article']['title'],contents[x]['article']['title']],'results' : chisquare([contents[w]['tone'][y]['score'], contents[x]['tone'][z]['score']])})

output=json.dumps(outputs, indent=4, sort_keys=True)
results.write(output)
