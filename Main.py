import json
import math
import glob, os
from textblob import TextBlob
from watson_developer_cloud import ToneAnalyzerV3, WatsonException, WatsonApiException


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

print(TextBlob(doc).sentiment)

try:
    content_type = 'application/json'
    print(json.dumps(tone_analyzer.tone({"text": doc}, content_type), indent=4))
except WatsonApiException as er:
    print("Your Watson API keys are invalid")
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
if invaldocs > 0:
    print("{} invalid documents in corpus.".format(invaldocs))

doc = TextBlob(doc)
print("Top words in document")
scores = {word: tfidf(word, doc, corpus) for word in doc.words}
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for word, score in sorted_words[:5]:
    print("\t{} - TF-IDF: {}".format(word, round(score, 5)))
