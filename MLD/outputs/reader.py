import os
import json
import glob
contents=[]
for file in glob.glob('*.json'):
	files = open(file, 'r')
	data=json.load(files)
	contents.append(data)
print(contents)
