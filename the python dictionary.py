import json
from difflib import get_close_matches

data = json.load(open("C:\\Users\\mar_k\\Downloads\\data.json"))

def search(word):
    # make sure to lower the word to lowercase
    word = word.lower()
    if word in data :
        return data[word]
    # in case the word itself was a title in the data dictionary
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data :
        return data[word.title()]
    elif len(get_close_matches(word,data.keys()))!=0:
        word2= get_close_matches(word,data.keys())
        print("did you mean {} instead".format(word2[0]))
        get = input("y/n")
        if get =="y":
            return data[word2[0]]
        else:
            print("sorry this word is not found in the dictionary")
    else:
        print ("word not in the dictionary")


word = input("enter the word you want to search for ?")
out = search(word)
# in some dictionaries the word has multiple meanings so make sure to display them all
if type(out)== list:
    for meaning in out :
        print (meaning)
else:
    print(out)