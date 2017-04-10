import sys
import os

def countLines(fname):
    try:
        out = sum(1 for line in open(fname)) #Add one for each \n
        return out

    except UnicodeDecodeError as ude:
        print("FOUND A FUBAR UNICODE CHARACTER -- DELETING FILE")
        os.remove(sys.argv[1])

numLines = countLines(sys.argv[1])
if numLines < 500:
    os.remove(sys.argv[1]) #Delete file
    print("Deleted: " + sys.argv[1])
    pass
