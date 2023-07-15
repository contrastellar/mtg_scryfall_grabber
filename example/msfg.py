#/opt/homebrew/bin/python3
# pylint: disable=C0301
# pylint: disable=C0303
# pylint: disable=R0913
# pylint: disable=R0914
# pylint: disable=R0133
# pylint: disable=R0124
"""
Example implementation of the mtg_scryfall_grabber module from @contrastellar
https://pypi.org/project/mtg-scryfall-grabber/

Author: Contrastellar (Gabriella Agathon)
2023
"""

import os
import json
import time
import argparse
import requests
import mtg_scryfall_grabber

def merge(dict1, dict2) -> dict:
    """Merge two dictionaries together"""
    return dict1.update(dict2)

def json_parse(obj) -> str:
    """
    Return a string object of the json passed in via obj
    """
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

def file_name_creation(user_set, pull_card_info, pull_price_info) -> str:
    """
    Create a filename to be used during the output process
    """
    file_name = ""
    file_name += user_set
    if pull_card_info :
        file_name += "_name"
    if pull_price_info :
        file_name += "_price"
    file_name += "_"
    file_name += str(int(time.time()))

    return file_name

# Consts
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
                        action='store_true', 
                        default=False)
    parser.add_argument('-p', '--price',
                        help="grab card price associated with collector number",
                        action='store_true',
                        default=False
                        )
    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity', 
                        action='store_true',
                        default=False)

    # Parse arguments
    args = parser.parse_args()
    user_set = str(args.set)
    pull_card_info = bool(args.cards)
    pull_price_info = bool(args.price)

    if bool(args.verbose):
        print("Outputting verbosely\n"+os.path.abspath(os.path.dirname( __file__ )))
        print(args)

    # Used to verify that the two sets are actually identical.
    card_set_url = "https://api.scryfall.com/sets/" + user_set

    card_list_url = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ user_set +"&unique=prints&page=" + str(PAGENUM)

    set_data = requests.get(card_set_url, timeout=10000)
    response_data = requests.get(card_list_url, timeout=10000)

    if bool(args.verbose):
        print("Set URL  =   " + str(card_set_url))
        print("Card URL =   " + str(card_list_url))
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

    # it is assumend that pull_card_info is always true
    # calling the flag is for brevity/old code that I don't
    # feel like getting rid of
    master_output = mtg_scryfall_grabber.grab_cards(user_set=user_set,
                                           response_data=response_data, page_num=1,
                                           verbose_setting=bool(args.verbose), name=pull_card_info, prices=pull_price_info)

    # Serializing json, this happens regardless of pull_card_info or any other state
    output_object = json.dumps(master_output, indent=4)

    path = "output"
    does_exist = os.path.exists(path=path)
    if not does_exist:
        os.makedirs(path)

    # Create Filename based on arguments
    file_name = file_name_creation(user_set=user_set, pull_card_info=pull_card_info, pull_price_info=pull_price_info)

    # Writing to sample.json
    with open("output/" + file_name + ".json", "w", encoding="UTF8") as outfile:
        outfile.write(output_object)

if __name__ == "__main__":
    main()
