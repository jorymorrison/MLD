import json
import math
import glob, os
from textblob import TextBlob
from watson_developer_cloud import ToneAnalyzerV3, WatsonApiException


def fileContents(name):
    return open(name, "r").read()


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

try:
    keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
except KeyError as er:
    print("Missing evironment variables:\nWATSON_USER\nWATSON_PASS\n\nSet them using values of your Watson API username and password.")
    exit()


tone_analyzer = ToneAnalyzerV3(
   version='2017-09-21',
   username=keys[0],
   password=keys[1]
)

filefound = False
while filefound == False:
    try:
        filefound = True
        filename = input("Enter a file name and extension: ")
        doc = fileContents(filename)
    except IOError as er:
        filefound = False
        print(er.strerror + ". Check for correct spelling and/or location.")

print('{\n\t"document_sentiment": {')
print('\t\t"polarity": {},'.format(TextBlob(doc).polarity))
print('\t\t"subjectivity": {}'.format(TextBlob(doc).subjectivity))
print('\t},')


try:
    content_type = 'application/json'
    print(json.dumps(tone_analyzer.tone({"text": doc}, content_type, False), indent=4)[1:-2] + ",\n")
except WatsonApiException as er:
    print("Method failed with status code " + str(er.code) + ": " + er.message)
    exit()


#LexSig#

corpus = []

invaldocs = 0

os.chdir("corpus")
for file in glob.glob("*.txt"):
    try:
        temp = open(file, "r")
        corpus.append(TextBlob(temp.read()))
    except UnicodeDecodeError as er:
        invaldocs += 1
#if invaldocs > 0:
    #print("{} invalid documents in corpus.".format(invaldocs))

doc = TextBlob(doc)
print('\t"lexical_signature": {\n\t\t"tf-idf": [\n\t\t\t{')
scores = {word: tfidf(word, doc, corpus) for word in doc.words}
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
comma = 0
for word, score in sorted_words[:5]:
    comma+=1;
    out = '\t\t\t\t"{}": {}'
    if comma < 5:
        out += ","
    print(out.format(word, round(score, 5)))
print("\t\t\t}\n\t\t]\n\t}\n}")
