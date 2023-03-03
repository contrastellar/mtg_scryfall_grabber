#/opt/homebrew/bin/python3

# Utility script in order to pull complete card sets from Scryfall

import os, requests, json, argparse, time

def Merge(dict1, dict2):
    return(dict1.update(dict2))

# Return a string object of the json passed in via obj
def jsonParse(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

# Returns the complete JSONList
def GrabCards(UserSet, CardSetURL, CardListURL, SetData, ResponseData, pageNum, verboseSetting):

    parsedSetFile = json.loads(jsonParse(SetData.json()))
    parsedCardFile = json.loads(jsonParse(ResponseData.json()))

    masterOutput = {}
    output = {}
    i = 0
    for d in parsedCardFile['data']:
        output[i+1] = d["name"]
        i = i + 1
        Merge(masterOutput, output)
    
    # Sleeps are used to not get blocked by the API
    time.sleep(1)

    # Now, can go into the "has more"
    hasNext = parsedCardFile['has_more']

    while(hasNext):

        pageNum += 1
        cardListURL = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ UserSet +"&unique=prints&page=" + str(pageNum)

        responseData = requests.get(cardListURL)
        if(verboseSetting): print("Card URL =   " + str(cardListURL))
        if(verboseSetting): print("Response code: " + str(responseData.status_code) + "\n")
        parsedCardFile = json.loads(jsonParse(responseData.json()))
        hasNext = parsedCardFile['has_more']
        output2 = {}

        for d in parsedCardFile['data']:
            output2[i+1] = d["name"]
            i = i + 1
            Merge(masterOutput, output2)

        time.sleep(1)

    return masterOutput