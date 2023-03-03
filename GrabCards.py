#/opt/homebrew/bin/python3
"""
Utility script in order to pull complete card sets from Scryfall

Author: Contrastellar (Gabriella Agathon)
"""


import json
import time
import requests

def Merge(dict1, dict2):
    """Merge two dictionaries together"""
    return dict1.update(dict2)

def jsonParse(obj):
    """ Return a string object of the json passed in via obj"""
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

def GrabCards(UserSet, ResponseData, PageNum, VerboseSetting):
    """
        Grabs all cards from a user defined set @UserSet
    """
    parsedCardFile = json.loads(jsonParse(ResponseData.json()))

    masterOutput = {}
    output = {}
    i = 0
    for d in parsedCardFile['data']:
        output[i+1] = {}
        output[i+1][0] = d["name"]
        i = i + 1
        Merge(masterOutput, output)

    # Sleeps are used to not get blocked by the API
    time.sleep(0.25)

    # Now, can go into the "has more"
    hasNext = parsedCardFile['has_more']

    while(hasNext):

        PageNum += 1
        cardListURL = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ UserSet +"&unique=prints&page=" + str(PageNum)

        responseData = requests.get(cardListURL, timeout=10000)
        if VerboseSetting:
            print("Card URL =   " + str(cardListURL))
        if VerboseSetting:
            print("Response code: " + str(responseData.status_code) + "\n")

        parsedCardFile = json.loads(jsonParse(responseData.json()))
        hasNext = parsedCardFile['has_more']
        output2 = {}

        for d in parsedCardFile['data']:
            output2[i+1] = {}
            output2[i+1][0] = d["name"]
            i = i + 1
            Merge(masterOutput, output2)

        time.sleep(0.25)

    return masterOutput

def GrabPrices(UserSet, ResponseData, PageNum, VerboseSetting):
    """
        Grabs all prices for the collectors numbers as defined in the set @UserSet
    """
    parsedCardFile = json.loads(jsonParse(ResponseData.json()))

    masterOutput = {}
    output = {}
    i = 0
    for d in parsedCardFile['data']:
        output[i+1] = {}
        output[i+1][1] = d["prices"]
        i = i + 1
        Merge(masterOutput, output)

    # Sleeps are used to not get blocked by the API
    time.sleep(1)

    # Now, can go into the "has more"
    hasNext = parsedCardFile['has_more']

    while(hasNext):

        PageNum += 1
        cardListURL = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ UserSet +"&unique=prints&page=" + str(PageNum)

        responseData = requests.get(cardListURL, timeout=10000)
        if VerboseSetting:
            print("Card URL =   " + str(cardListURL))
        if VerboseSetting:
            print("Response code: " + str(responseData.status_code) + "\n")

        parsedCardFile = json.loads(jsonParse(responseData.json()))
        hasNext = parsedCardFile['has_more']
        output2 = {}

        for d in parsedCardFile['data']:
            output2[i+1] = {}
            output2[i+1] = d["name"]
            i = i + 1
            Merge(masterOutput, output2)

        time.sleep(1)

    return masterOutput
