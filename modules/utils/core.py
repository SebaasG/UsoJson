import os 
import json
MY_DATABASE = ''

def newFile(*param):
    with open(MY_DATABASE, 'w') as wf:
        json.dump(param[0], wf, indent= 4)


def readFile (): 
    with open(MY_DATABASE, 'r') as rf:
        return json.load(rf)
    
def addData(*param):
    with open(MY_DATABASE, 'r+') as frw:
        json.dump(param[0],frw, indent= 2)

def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(readFile())
    else:
        if(len(param)):
            newFile(data[0])