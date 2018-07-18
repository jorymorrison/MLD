import json
import glob, os
from textblob import TextBlob
from watson_developer_cloud import ToneAnalyzerV3

def fileContents(name):
    return open(name, "r").read()


def termFrequency(document):
    temp = {}
    tfb = len(TextBlob(document).words)

    for word in TextBlob(document).words:
        if len(temp) != 0 and word in temp:
            temp[word] += 1;
        else:
            temp[word] = 1;

    for term in temp:
        temp[term] = float(temp[term]) / float(tfb)

    return temp

try:
    keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
    print(keys)
except KeyError as er:
    print("Missing evironment variables:\nWATSON_USER\nWATSON_PASS\n\nSet them using values of your Watson API username and password.")
    exit()


try:
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        username='',
        password=''
    )
except OSError as er:
    print("git gud")



filefound = False
while filefound == False:
    try:
        filefound = True
        filename = input("Enter a file name and extension: ")
        doc = fileContents(filename)
    except IOError as er:
        filefound = False
        print(er.strerror + "'. Check for correct spelling and/or location.")


print(TextBlob(doc).sentiment)


#content_type = 'application/json'
#print(tone_analyzer.tone({"text": doc}, content_type))

#LexSig#

corpus = []

os.chdir("corpus")
for file in glob.glob("*.txt"):
    temp = open(file, "r")
    corpus.append(temp.read())

termfreq = termFrequency(doc)

tfidf = {}

'''for term in termfreq.keys():
    idfb = 0
    for document in corpus:
        print(document[290:300])
        for word in TextBlob(document).words:
            if word == term:
                idfb += 1
                break

    tfidf[term] = float(termfreq[term])/(float(len(corpus))/float(idfb))

print(tfidf)'''













