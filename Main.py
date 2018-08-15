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
    print("Failed to retrieve evironment variables:\nWATSON_USER\nWATSON_PASS\n\nSet them using values of your Watson API username and password.")
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
        print('Failed to retrieve file' + er.strerror)

logOutput = '{\n\t"document_sentiment": {'
logOutput += '\n\t\t"polarity": {},'.format(TextBlob(doc).polarity)
logOutput += '\n\t\t"subjectivity": {}'.format(TextBlob(doc).subjectivity)
logOutput += '\n\t},\n'
print("Successfully retrieved document sentiment...")


try:
    content_type = 'application/json'
    logOutput += json.dumps(tone_analyzer.tone({"text": doc}, content_type, False), indent=4)[1:-2] + ",\n"
except WatsonApiException as er:
    print("Failed to retrieve document tone.\n Status code " + str(er.code) + ": " + er.message)
    exit()
print("Successfully retrieved document tone...")

#LexSig#

corpus = []

invaldocs = 0

try:
    os.chdir("corpus")
    for file in glob.glob("*.txt"):
        try:
            temp = open(file, "r")
            corpus.append(TextBlob(temp.read()))
        except UnicodeDecodeError as er:
            invaldocs += 1
except IOError as er:
    print("Failed to access corpus.")
    exit()

print("Successfully accessed corpus with {} invalid documents...".format(invaldocs))

doc = TextBlob(doc)
logOutput += '\n\t"lexical_signature": {\n\t\t"tf-idf": [\n\t\t\t{'
scores = {word: tfidf(word, doc, corpus) for word in doc.words}
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
comma = 0
for word, score in sorted_words[:5]:
    comma+=1;
    out = '\n\t\t\t\t"{}": {}'
    if comma < 5:
        out += ","
    logOutput += out.format(word, round(score, 5))
logOutput += "\n\t\t\t}\n\t\t]\n\t}\n}"
print("Successfully calculated lexical signature...")

#print(logOutput)
