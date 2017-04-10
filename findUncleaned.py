import re
import sys
import os

def isDone(theFile):
    file = open(theFile, 'r+') #Open file in read mode
    try:
        allTheXML = file.read() #Put it all in a variable
        file.close() #Close access to file

        regexp = re.compile(r'<.*?>')

        if regexp.search(allTheXML) is not None:
            os.rename(theFile, "../unclean/"+theFile)
    except UnicodeDecodeError as ude:
         print("FOUND A FUBAR UNICODE CHARACTER -- DELETING FILE")
         os.remove(sys.argv[1])


theTarget = sys.argv[1]
isDone(theTarget)
