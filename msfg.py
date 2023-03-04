#/opt/homebrew/bin/python3
# pylint: disable=C0301

"""
Module for scraping usefull info off of the scryfall 
REST API when invoked as a module, versus a library

Author: Contrastellar (Gabriella Agathon)
2023
"""

import os
import json
import argparse
import requests
import grab_cards


def json_parse(obj):
    """
    Return a string object of the json passed in via obj
    """
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

PAGENUM = 1
MODULE_DESCRIPTION = "Script to pull card info from api.scryfall.com based on specific set"

def main():
    """
    main, allowing this to be invoked as a module from the command line.
    """
    parser = argparse.ArgumentParser(description=MODULE_DESCRIPTION)

    parser.add_argument('set', metavar='set',
                        help="3-5 letter/number ID that dictates which set to pull from")
    parser.add_argument('-c', '--cards',
                        help="grab card names associated with specific IDs",
                        action='store_true', default=True)
    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity', action='store_true')

    # Parse arguments
    args = parser.parse_args()
    user_set = str(args.set)
    pull_card_info = bool(args.cards)

    if bool(args.verbose):
        print("Outputting verbosely\n"+os.path.abspath(os.path.dirname( __file__ )))

    # Used to verify that the two sets are actually identical.
    card_set_url = "https://api.scryfall.com/sets/" + user_set

    card_list_url = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ user_set +"&unique=prints&page=" + str(PAGENUM)

    set_data = requests.get(card_set_url, timeout=10000)
    response_data = requests.get(card_list_url, timeout=10000)

    if bool(args.verbose):
        print("Set URL  =   " + str(card_set_url))

    if bool(args.verbose):
        print("Card URL =   " + str(card_list_url))

    if bool(args.verbose):
        print("Response code: " + str(response_data.status_code) + "\n")

    parsed_set_file = json.loads(json_parse(set_data.json()))
    parsed_card_file = json.loads(json_parse(response_data.json()))

    if bool(args.verbose):
        print("Card set from the set search ...  ? -> " + parsed_set_file['name'])

    set_name_from_search = parsed_set_file['name']
    set_name_from_card = parsed_card_file['data'][0]['set_name']

    if bool(args.verbose):
        print("Are strings the same?")
        if set_name_from_card == set_name_from_search:
            print("Yes!")

        else:
            print("No! Exiting!")
            print("\n\n")
            return

    if bool(args.verbose) :
        print("Total cards --   " + str(parsed_card_file["total_cards"]))

        print("\n\n--!-- Does output have \"next page\"?")
        print(parsed_card_file['has_more'])

    # Declare MasterOutput for modification in the following blocks.
    master_output = None

    if pull_card_info :
        master_output = grab_cards.GrabCards(UserSet=user_set,
                                           ResponseData=response_data, PageNum=1,
                                           VerboseSetting=bool(args.verbose))
        # Serializing json
        output_object = json.dumps(master_output, indent=4)

        # Writing to sample.json
        with open("output/" + set_name_from_search +
                    "_card_name_info.json", "w", encoding="UTF8") as outfile:
            outfile.write(output_object)

if __name__ == "__main__":
    main()
