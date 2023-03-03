import os, requests, json, argparse
import GrabCards

def Merge(dict1, dict2):
    return(dict1.update(dict2))

# Return a string object of the json passed in via obj
def jsonParse(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

def main():

    # Current dir the script is running in, can be useful for debugging
    script_dir = os.path.abspath(os.path.dirname( __file__ ))

    description = "Script to pull card info from api.scryfall.com based on specific set"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('set', metavar='set', help="3-5 letter/number ID that dictates which set to pull from") #set to pull card data from
    parser.add_argument('-c', '--cards', help="grab card names associated with specific IDs", action='store_true')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')

    # Parse arguments
    args = parser.parse_args()
    verboseSetting = bool(args.verbose)
    userSet = str(args.set)
    pullCardInfo = bool(args.cards)
    pageNum = 1

    if(verboseSetting): print("Outputting verbosely\n"+script_dir)

    # Used to verify that the two sets are actually identical.
    cardSetURL = "https://api.scryfall.com/sets/" + userSet

    cardListURL = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ userSet +"&unique=prints&page=" + str(pageNum)

    setData = requests.get(cardSetURL)
    responseData = requests.get(cardListURL)

    if(verboseSetting): print("Set URL  =   " + str(cardSetURL))
    if(verboseSetting): print("Card URL =   " + str(cardListURL))

    if(verboseSetting): print("Response code: " + str(responseData.status_code) + "\n")

    parsedSetFile = json.loads(jsonParse(setData.json()))
    parsedCardFile = json.loads(jsonParse(responseData.json()))

    if(verboseSetting): print("Card set from the set search ...  ? -> " + parsedSetFile['name'])
    if(verboseSetting): print("Card set from the card ID    ... " + parsedCardFile["data"][0]["collector_number"] + "? -> "+ parsedCardFile['data'][0]['set_name'])

    setNameFromSearch = parsedSetFile['name']
    setNameFromCard = parsedCardFile['data'][0]['set_name']

    if(verboseSetting):
        print("Are strings the same?")
        if(setNameFromCard == setNameFromSearch):
            print("Yes!")
            
        else:
            print("No! Exiting!")
            print("\n\n")
            return -1

    """
        At this point, we can pretty much get on with it
    """
    if(verboseSetting):
        print("Total cards --   " + str(parsedCardFile["total_cards"]))

        print("\n\n--!-- Does output have \"next page\"?")
        print(parsedCardFile['has_more'])

    if(pullCardInfo):
        MasterOutput = GrabCards.GrabCards(UserSet=userSet, ResponseData=responseData, PageNum=pageNum, VerboseSetting=verboseSetting)
        # Serializing json
        outputObject = json.dumps(MasterOutput, indent=4)
    
        # Writing to sample.json
        with open("output/" + setNameFromSearch + "_card_name_info.json", "w") as outfile:
            outfile.write(outputObject)

if __name__ == "__main__":
    main()
