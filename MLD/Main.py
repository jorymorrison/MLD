import json, sys, math, glob, os, datetime, platform, argparse
import urllib
from textblob import TextBlob
from goose3 import Goose
from goose3.configuration import Configuration
from watson_developer_cloud import ToneAnalyzerV3, WatsonApiException
import nltk
import ssl	

#parser = argparse.ArgumentParser()
#parser.add_argument("url")
#args = parser.parse_args()

class bcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

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
    
def jsonOut(title, body, url, date, sentiment="error", signature="error", tone=['error']):
        
    article= {'title' : title, 'date' : date, 'url' : url, 'body' : body}
    final={'article' : article, 'sentiment' : sentiment, 'signature' : signature, 'tone' : tone}
    output=json.dumps(final, indent=4, sort_keys=True)

    sys.stdout.write(bcolors.ENDC + '\nSuccessfully created results file at: ' + path + "\n")
    results.write(output)

def calc(url):
    try:	
        _create_unverified_https_context = ssl._create_unverified_context	
    except AttributeError:	
        pass	
    else:	
        ssl._create_default_https_context = _create_unverified_https_context	

    nltk.download('punkt')

    try:
        sys.stdout.write(bcolors.ENDC + "Searching for configuration file 'config.conf'...")
        sys.stdout.flush()
        file = open ("config.conf", "r")
        keys = file.readlines()
        keys = [keys[0][12:].split("\n")[0], keys[1][12:]]
        sys.stdout.write(bcolors.ENDC + "\rSuccessfully found configuration file 'config.conf'.\n")
        sys.stdout.flush()

        sys.stdout.write(bcolors.ENDC + "Extracting keys from 'config.conf'...")
        sys.stdout.flush()
        if keys[0] == "" or keys[1] == "":
            sys.stdout.write(bcolors.WARNING + "\rFailed to extract keys from 'config.conf', missing values.\n")
            sys.stdout.flush()
            try:
                sys.stdout.write(bcolors.ENDC + "Retrieving environmental variables...")
                sys.stdout.flush()
                keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
                sys.stdout.write(bcolors.ENDC + "\rSuccessfully retrieved environmental variables.\n")
                sys.stdout.flush()
                if keys[0] == "" or keys[1] == "":
                    sys.stdout.write(bcolors.WARNING + "WARNING: environmental variables missing values!\n")
                    sys.stdout.flush()

            except KeyError as er:
                sys.stdout.write(bcolors.WARNING + "\rFailed to find environmental variables.\n")
                sys.stdout.flush()
                sys.stdout.write(bcolors.FAIL + "Please access the config or evironment variables:\nWATSON_USER\nWATSON_PASS\n\nSet them using values of your Watson API username and password.\nExiting program...\n" + bcolors.ENDC)
                sys.stdout.flush()
                exit()
        else:
            sys.stdout.write(bcolors.ENDC + "\rSuccessfully extracted keys from 'config.conf'.\n")
            sys.stdout.flush()

    except IOError as er:
        sys.stderr.write(bcolors.WARNING + "\rFailed to find 'config.conf'. " + er.strerror + ".\n")
        try:
            sys.stdout.write(bcolors.ENDC + "Retrieving environmental variables...")
            sys.stdout.flush()
            keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
            sys.stdout.write(bcolors.ENDC + "\rSuccessfully retrieved environmental variables.\n")
            sys.stdout.flush()
            if keys[0] == "" or keys[1] == "":
                sys.stderr.write(bcolors.WARNING + "WARNING: environmental variables missing values!\n")

        except KeyError as er:
            sys.stdout.write(bcolors.WARNING + "\rFailed to find environmental variables.\n")
            sys.stdout.flush()
            sys.stdout.write(bcolors.ENDC + "Generating config file 'config.conf'...")
            sys.stdout.flush()
            file = open("config.conf", "w")
            file.write("watson_user=\nwatson_pass=")
            sys.stdout.write(bcolors.ENDC + "\rSuccessfully generated configuration file 'config.conf'.\n")
            sys.stdout.write(bcolors.FAIL + "Please access the config or evironment variables:\nWATSON_USER\nWATSON_PASS\n\nSet them using values of your Watson API username and password.\nExiting program...\n" + bcolors.ENDC)
            sys.stdout.flush()
            exit()
    #
    #
    #


    tone_analyzer = ToneAnalyzerV3(
       version='2017-09-21',
       url='https://gateway.watsonplatform.net/tone-analyzer/api',
       username=keys[0],
       password=keys[1]
    )

    #url = input("Input a url: ")
    #url = input('Enter the URL of a news article:')
    url = url.replace(' ','')

    try:
         sys.stdout.write("Retrieving satus code...")
         page = urllib.request.urlopen(url, data=None)

    # error thrown if the status code is bad
    except urllib.error.HTTPError as e:
         sys.stdout.write(bcolors.ENDC + '\rSuccessfully retrieved status code: ' + e.getcode() + "\n")
         sys.stdout.write(bcolors.FAIL + 'Failed to retrieve representation.\nExiting program...\n' + bcolors.ENDC)
         exit()

    # error thrown if the URL is bad
    except (urllib.error.URLError, ValueError):
         sys.stdout.write(bcolors.FAIL + '\rFailed to retrieve status code.\nExiting program...\n' + bcolors.txt)
         exit()

    scode = str(page.getcode())

    sys.stdout.write(bcolors.ENDC + 'Successfully retrieved status code: ' + scode + "\n")
    sys.stdout.write(bcolors.ENDC + 'Successfully retrieved representation.\n')

    #
    #
    #

    g = Goose()
    # g.config.known_context_patterns = {'attr': 'class', 'value': 'l-container'}
    article = g.extract(url=url)
    # article.strict = False
    titletext = (article.title)
    bodytext = article.cleaned_text
    #print(bodytext)
    bodytext = bodytext.replace('"', "'")
    bodytext = bodytext.replace('\n', '   ')
    doc = bodytext #input one
    date = str(datetime.datetime.now()) #input two

    sys.stdout.write(bcolors.ENDC + "Creating results file...")
    if platform.system() == "Windows":
            path = os.path.split(os.path.abspath(__file__))[0] + "\\outputs\\" + titletext + '-' + date + ".json"
    else:
            path = os.path.split(os.path.abspath(__file__))[0] + "/outputs/" + titletext + '-' + date + ".json"
    results = open(path, 'a+')

    #results.write('Status Code: ' + scode)

    #sys.stdout.write('Successfully wrote retrieval status to results file.\n')

    #serialized = '{\n   "article": {\n   "title": "' + titletext + '",\n   "time": "' + date + '",\n   "url": "' + url + '",\n   },'

    #results.write(serialized)

    #sys.stdout.write('Successfully wrote retrieval to results file.\n')

    #sys.stdout.write("Retrieving document senitment... 0%")
    #sys.stdout.flush()
    sentiment={}
    #output = '\t"document_sentiment": {'
    #sentiment.append('"polarity": {},'.format(TextBlob(doc).polarity))
    sentiment.update({'polarity' : TextBlob(doc).polarity})
    #print(TextBlob(doc).polarity)
    #output += '\n\t\t"polarity": {},'.format(TextBlob(doc).polarity)
    #sys.stdout.write("\rRetrieving document senitment... 50%")
    #sys.stdout.flush()
    #output += '\n\t\t"subjectivity": {}'.format(TextBlob(doc).subjectivity)
    #sentiment.append('"subjectivity": {}'.format(TextBlob(doc).subjectivity))
    sentiment.update({'subjectivity' : TextBlob(doc).subjectivity})
    #print(TextBlob(doc).subjectivity)
    #sys.stdout.write("\rRetrieving document senitment... 100%")
    #sys.stdout.flush()
    #output += '\n\t},\n'
    #sys.stdout.write("\rSuccessfully retrieved document sentiment.\n")

    #sys.stdout.write("Retrieving document tone...")
    #sys.stdout.flush()


    #
    #
    #


    try:
        content_type = 'application/json'
        #logOutput = json.dumps(tone_analyzer.tone({"text": doc}, content_type, False), indent=4)[1:-2] + ",\n"
        logOutput = tone_analyzer.tone({"text": doc}, content_type, True)['document_tone']['tones']
    except WatsonApiException as er:
        sys.stderr.write("\rFailed to retrieve document tone.\n Status code " + str(er.code) + ": " + er.message)
        exit()
    sys.stdout.write("\rSuccessfully retrieved document tone.\n")

    #print(logOutput)
    #print("test")
    #print(tone_analyzer.tone({"text": doc}, content_type, False)['document_tone']['tones'])
    #LexSig#

    corpus = []

    invaldocs = 0

    sys.stdout.write("Accessing corpus...")
    try:
        os.chdir("corpus")
        for file in glob.glob("*.txt"):
            try:
                temp = open(file, "r")
                corpus.append(TextBlob(temp.read()))
            except UnicodeDecodeError as er:
                invaldocs += 1
    except IOError as er:
        sys.stderr.write("\rFailed to access corpus.")
        exit()

    sys.stdout.write("\rSuccessfully accessed corpus with {} invalid documents.\n".format(invaldocs))

    percent = 0
    sys.stdout.write("Calculating lexical signature... %d%%" % percent)
    sys.stdout.flush()
    doc = TextBlob(doc)
    percent += 12.5
    sys.stdout.write("\rCalculating lexical signature... %d%%" % percent)
    sys.stdout.flush()
    #output += '\n\t"lexical_signature": {\n\t\t"tf-idf": [\n\t\t\t{'
    scores = {word: tfidf(word, doc, corpus) for word in doc.words}
    percent += 12.5
    sys.stdout.write("\rCalculating lexical signature... %d%%" % percent)
    sys.stdout.flush()
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    percent += 12.5
    sys.stdout.write("\rCalculating lexical signature... %d%%" % percent)
    sys.stdout.flush()
    comma = 0
    signature={}
    for word, score in sorted_words[:5]:
        comma+=1;
        out = '"{}": {}'
        if comma < 5:
            out += ","
        signature.update({word : score})
        #signature.append(out.format(word, round(score, 5)))
        percent += 12.5
        sys.stdout.write("\rCalculating lexical signature... %d%%" % percent)
        sys.stdout.flush()
    #output += "\n\t\t\t}\n\t\t]\n\t}\n}"
    sys.stdout.write("\rSuccessfully calculated lexical signature.\n")
    jsonOut(titletext, bodytext, url, date, sentiment, signature, logOutput)
    #results.write(output)
    #sys.stdout.write("Successfully wrote output to results file.\nExiting program...\n" + bcolors.ENDC)
    exit()
