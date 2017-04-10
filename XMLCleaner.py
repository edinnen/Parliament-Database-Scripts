# -*- coding: utf-8 -*-
import re
from collections import deque
import inflect
import sys
from unidecode import unidecode as ud
from num2words import num2words

contractions = {
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he has",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how has",
"I'd": "I would",
"I'd've": "I would have",
"I'll": "I will",
"I'll've": "I will have",
"I'm": "I am",
"I've": "I have",
"isn't": "is not",
"it'd": "it had",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she had",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that had",
"that'd've": "that would have",
"that's": "that has",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when has",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who has",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}

#Find contractions and return the expanded form
contRe = re.compile('(%s)' % '|'.join(contractions.keys()))
def expandContraction(s, contractions_dict=contractions):
    def replace(match):
        return contractions_dict[match.group(0)]
    return contRe.sub(replace, s)

#Converts numbers to ENGLISH words
def numToWord(match):
    num = float(match.group(0))
    inflector = inflect.engine()
    return inflector.number_to_words(num)

def numToFRWord(match):
    num = int(match.group(0))
    return num2words(num, lang='fr')

#Tokenizes based on capital letters
## i.e. BigDumbLongString -> Big Dumb Long String
def tokenizer(match):
    theThing = match.group(0)
    pattern = r'([A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]{2,}(?=[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]|$)|[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ](?=[a-zàâçéèêëîïôûùüÿñæœ]|$))'
    chunks = deque(re.split(pattern, theThing))

    result = []
    while len(chunks):
      buf = chunks.popleft()
      if len(buf) == 0:
        continue
      if re.match(r'^[A-Z]$', buf) and len(chunks):
        buf += chunks.popleft()
      result.append(buf)

    return ' '.join(result)

#Cleaning function
def doTheClean(theFile):
    file = open(theFile, 'r+') #Open file in read mode
    try:
        allTheHTML = file.read() #Put it all in a variable
        file.close() #Close access to file
    except UnicodeDecodeError as ude:
        print("FOUND A FUBAR UNICODE CHARACTER -- DELETING FILE")
        os.remove(sys.argv[1])

    #Set output to all between <HansardBody>...</HansardBody>
    tmp = re.search("<HansardBody>([\s\S]*)<\/HansardBody>", allTheHTML)
    out = tmp.group(0)

    out = re.sub("(\b(Mr|Hon|Monsieur|M|Madame|Mme|Mademoiselle|Mlle|mr|hon|monsieur|m|madame|mme|mademoiselle|mmle)s?\.*\s+[A-zàâçéèêëîïôûùüÿñæœÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]+\s*[A-zàâçéèêëîïôûùüÿñæœÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]*\s*[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ][a-zàâçéèêëîïôûùüÿñæœ]*|\b(Mr|Hon|Monsieur|M|Madame|Mme|Mademoiselle|Mlle|mr|hon|monsieur|m|madame|mme|mademoiselle|mmle)s?\.*\s+[A-zàâçéèêëîïôûùüÿñæœÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]+|[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]{1}[a-zàâçéèêëîïôûùüÿñæœ]+\s+[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ][a-zàâçéèêëîïôûùüÿñæœ]+(\s+[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ][a-zàâçéèêëîïôûùüÿñæœ]+)*)", "", out) #Delete all names, but keep proper nouns
    out = re.sub("<style>([\s\S]*)<\/style>", "", out) #Remove anything between/including <style> tags
    out = re.sub("<script.*>([\s\S]*)<\/script>", "", out)
    out = re.sub("'s\b", "", out)
    out = re.sub("&nbsp", "", out) #Removes &nbsp
    out = re.sub("<.*?>", "", out) #Anything between <...>
    out = re.sub("\[.*?\]", "", out) #Any [...]
    out = re.sub("\(.*?\)", "", out) #Any (...)
    out = re.sub("[1-9]+", numToFRWord, out) #Any change any int to words
    out = re.sub("point zero", "", out) #Any 'point zero'
        out = re.sub("[a-zàâçéèêëîïôûùüÿñæœ]+[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]{2}[a-zàâçéèêëîïôûùüÿñæœ]*", tokenizer, out) #Matches mixed case strings (i.e. C[hattersMr]) and passes to the tokenizer function
    out = out.lower() #Converts to lowercase
    out = re.sub("[!\"#$%&\(\)\.\*\+,\/:;«»—<=>\?@\\\^_`\{\}~]", " ", out) #Any special char
    #out = re.sub("[^a-zàâçéèêëîïôûùüÿñæœA-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ\s]", "", out) #Anything that isn't whitespace or letters
    out = re.sub("\t", "", out) #Tabs - I think this is redundant now due to final operation
    out = re.sub("[A-ZÀÂÇÉÈÊËÎÏÔÛÙÜŸÑÆŒ]{2,}", "", out)
    out = re.sub("\w*html", "", out) #Removes any word + html - Think I found some of these in the initial browse through
    out = re.sub("0+", "", out) #Removes strings of zeros
    out = re.sub("\n{2,}", "\n", out) #Replaces two or more \n's with one - I think redundant
    out = re.sub("\|", "", out) #Removes random pipe characters
    out = ' '.join(out.split()) #Compresses by splitting everything and rejoining with " "

    #Write the file
    file = open(theFile, 'w')
    file.truncate()
    file.write(out)
    file.close()

theTarget = sys.argv[1]
doTheClean(theTarget)
