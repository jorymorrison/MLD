# MLD Article Analysis

[![CircleCI](https://circleci.com/gh/jorymorrison/MLD/tree/master.svg?style=svg)](https://circleci.com/gh/jorymorrison/MLD/tree/master)

MLD, pronounced Mold, is a command line based application that uses natural language processing (NLP) techniques to analyze the tone, sentiment, and lexical signature of a news article of a user-inputted URL. 

# Disclaimer 
The project is developed and maintained by students as part of Jory Morrison's mentorship program for secondary education students. There is no affiliation, endorsement, ownership, or sponsorship with or by any commercial or non-commercial entity. Ownership of this repository should not be construed as contribution or creation of intellectual property; please reference commit history for attribution of intellectual property origin.

# License
[Apache 2.0 License](https://choosealicense.com/licenses/apache-2.0/) applies

# Notes
As of September 2019 this project is being actively maintained. It is currently in a limited-functioning state due to changes in the Watson SDK. Please reference [issues](https://github.com/jorymorrison/MLD/issues)

This project uses the [IBM Watson Tone Analyzer API](https://www.ibm.com/watson/services/tone-analyzer/), which requires an IMB Creative Cloud account.

# Prerequisites
* Python 3.67
* PIP3
* GCC
* [An IBM Creative Cloud Account](https://console.bluemix.net/registration/?target=/catalog/%3fcategory=watson&cm_mmc=Earned-_-Watson+Core+-+Platform-_-WW_WW-_-intercom&cm_mmca1=000000OF&cm_mmca2=10000409&&cm_mc_uid=27843925725315299422843&cm_mc_sid_50200000=54807401535555236296&cm_mc_sid_52640000=27596621535555236301)

# Cloning the Project
To clone this project, use the following command:
```
$ git clone https://github.com/jorymorrison/MLD.git
```
### Installing Requirements
Use these commands to install all required dependencies:
```
$ cd MLD
$ pip install -r requirements.txt
```

# Basic Usage
Once a URL to a news article is inputted, the program will process the article's text and output the sentiment in terms of polarity and subjectivity, the tone, and five key words that make up the article's lexical signature.

```
Enter the URL of a news article as the first argument when calling in command line:https://abcnews.go.com/Politics/john-mccain-memorials-start-longtime-senators-body-lying/story?id=57472926
Retrieving satus code...Successfully retrieved status code: 200
Successfully retrieved representation.
Creating results file...
Successfully created results file at: /home/libbymadren/MLD\'John McCain will always have our back': Politicians pay tribute to the late senator-2018-08-29 19:47:37.537351.txt
Successfully wrote retrieval status to results file.
Successfully wrote retrieval to results file.
Successfully retrieved document sentiment.
Successfully retrieved document tone.
Successfully accessed corpus with 2 invalid documents.
Successfully calculated lexical signature.
Successfully wrote output to results file.
Exiting program...
```
The article's title, body text, and all output results are submitted to a results txt folder found in the repository.

### Obtaining Watson API Keys

The first time this program runs, the program will search for Watson API keys. If none are found, you will be instructed to set your Watson username and password. 

To access the Watson API Keys, log into your IBM Creative Cloud Account and locate the [Tone Analyzer](https://console.bluemix.net/catalog/services/tone-analyzer?hideTours=true&cm_mmc=-_-Watson+Core_Watson+Core+-+Platform-_-WW_WW-_-wdc-ref&cm_mmca1=000000OF&cm_mmca2=10000409) page. Click *Create,* and a username and password will be generated for you. Copy these and set them in the application by either editing the ` config.conf ` file, or by setting environmental variables:
```
$ export WATSON_USER="apikey"
$ export WATSON_PASS=<apikey-url>
```

# Output Synopsis
### Json Schema:
```
{
    "article": {
        "body": <body-text>,
		"date": <date>,
        "title": <title>,
        "url": <url>
    },
    "sentiment": {
        "polarity": <value 0-1>,
        "subjectivity": <value 0-1>
    },
    "signature": {
        <most frequent>: <value 0-1>,
        <most frequent>: <value 0-1>,
        <most frequent>: <value 0-1>,
        <most frequent>: <value 0-1>,
        <most frequent>: <value 0-1>
    },
    "tone": {
		<tone>: <value 0-1>,
		<tone>: <value 0-1>,
		<tone>: <value 0-1>,
		<tone>: <value 0-1>,
		<tone>: <value 0-1>,
		<tone>: <value 0-1>
	}
}
```

### Sentiment:
**Polarity:** Scale -1 - 1 (-1 being very negative, 0 being neutral, 1 being very positive)

**Subjectivity:** Scale 0 - 1 (0 is very objective, 1 is very subjective)

### Tone:
Tonal scores are displayed on a scale from 0.5 - 1, with lower scores indicating emotions less present in the document, and higher scores indicating emotions that are likely perceived in the content. Scores higher than 0.75 should be consider very emotional.
For in depth documentation on the IBM Watson Tonal Analyzer go to: https://console.bluemix.net/docs/services/tone-analyzer/using-tone.html#using-the-general-purpose-endpoint

### Lexical Signature:
Lexical signature is represented by the top 5 words in a document according to Term Frequency / Inverse Document Frequency (TF-IDF). 
For in depth documentation of how TF-IDF is calculated go to: https://http//www.tfidf.com
Output is formatted in key-value pairs of a word and its TF-IDF score.
