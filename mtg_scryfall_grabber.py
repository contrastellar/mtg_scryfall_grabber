#/opt/homebrew/bin/python3
# pylint: disable=C0301
# pylint: disable=C0303
# pylint: disable=R0913
"""
Utility script in order to pull complete card sets from Scryfall

Author: Contrastellar (Gabriella Agathon)
"""


import json
import time
import requests

def merge(dict1, dict2) -> dict:
    """
        Merge two dictionaries together
    """
    return dict1.update(dict2)

def json_parse(obj) -> str:
    """
        Return a string object of the json passed in via obj
    """
    text = json.dumps(obj, sort_keys=True, indent=3)
    return text

def grab_cards(user_set, response_data, page_num, verbose_setting, name, prices) -> dict:
    """
        Grabs all cards from a user defined set @UserSet
    """
    parsed_card_file = json.loads(json_parse(response_data.json()))
    master_output = {}
    output = {}

    i = 0
    for data in parsed_card_file['data']:
        # For future -- this can be cleaned up so that it doesn't use a long if chain to determine what data to include
        output[i+1] = {}
        if name:
            output[i+1]["Card Name"] = data["name"]

        if prices:
            output[i+1]["Price"] = data["prices"]

        i = i + 1
        merge(master_output, output)

    # Sleeps are used to not get blocked by the API
    time.sleep(0.25)

    # Now, can go into the "has more"
    has_next = parsed_card_file['has_more']

    while has_next:
        # Repeat same function as above, except for every page after.
        page_num += 1
        card_list_url = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ user_set +"&unique=prints&page=" + str(page_num)

        response_data = requests.get(card_list_url, timeout=10000)
        if verbose_setting:
            print("Card URL =   " + str(card_list_url))
            print("Response code: " + str(response_data.status_code) + "\n")

        parsed_card_file = json.loads(json_parse(response_data.json()))
        has_next = parsed_card_file['has_more']
        output2 = {}

        for data in parsed_card_file['data']:
            output2[i+1] = {}
            if name:
                output2[i+1]["Card Name"] = data["name"]

            if prices:
                output2[i+1]["Price"] = data["prices"]

            i = i + 1
            merge(master_output, output2)

        time.sleep(0.25)

    # Return the master_output dictionary, so it can be parsed.
    return master_output
