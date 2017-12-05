# Jake McGhee
# Lab 14

import os

def getTextFromFile(fileName):
    # Get the programs working directory - see https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    directory = os.path.dirname(__file__) 
    
    # Make full path name
    path = directory + "\\" + fileName
    
    
    # Open the file if it exists - see https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python
    if os.path.exists(path):
        file = open(path, "rt")
        return file.read()
    # Manually select file if not found
    else:
        print "File not found\nPlease select " + fileName
        file = open(pickAFile(), "rt")
        return file.read()

# ---------- Part I ----------

def countWords():
    article = getArticle("eggs.txt")
    article = article.replace('?', '')
    article = article.replace('!', '')
    article = article.replace('-', ' ')
    
    print "Total Words = %s" % wordCountTotal(article) # print total words
    printDictionairy(wordCountIndividual(article))
    

def wordCountTotal(text):
    return len(text.split())

def wordCountIndividual(text):
    text = text.split()
    words = {}
    for word in text:
        word = word.title()
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words
    
def printDictionairy(dict):
    sortedDictionary = sorted(dict)
    for key in sortedDictionary:
        print "%s: %s" % (key, dict[key])

        
# ---------- Part II ----------
        
def getHeadlines():
    print getTextFromFile("webpage.html")
    