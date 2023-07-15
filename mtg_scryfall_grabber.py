#/opt/homebrew/bin/python3
# pylint: disable=C0301
# pylint: disable=C0303
# pylint: disable=R0913
# pylint: disable=R0133
# pylint: disable=R0124
"""
Library to pull card sets from scryfall

Author: Contrastellar (Gabriella Agathon)
"""


import json
import time
import requests

def test_dict_merge() -> None:
    """
        Test the merge function
    """
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    dict_expected = {'c': 4, 'a': 10, 'b': 8, 'd': 6}
    merge(dict1=dict1, dict2=dict2)

    assert dict1 == dict_expected

def test_json_parse() -> None:
    """
        Test the json parse function
    """
    user_set: str = "ONE"
    card_set_url = "https://api.scryfall.com/sets/" + user_set

    obj = requests.get(card_set_url, timeout=10000)
    output = json.loads(json_parse(obj=obj.json()))

    #Expected dictionary
    expected_dict: dict = {"arena_code": "one",
                           "card_count": 479,
                           "code": "one",
                           "digital": False,
                           "foil_only": False,
                           "icon_svg_uri": "https://svgs.scryfall.io/sets/one.svg?1688961600",
                           "id": "04bef644-343f-4230-95ee-255f29aa67a2",
                           "mtgo_code": "one",
                           "name": "Phyrexia: All Will Be One",
                           "nonfoil_only": False,
                           "object": "set",
                           "printed_size": 271,
                           "released_at": "2023-02-03",
                           "scryfall_uri": "https://scryfall.com/sets/one",
                           "search_uri": "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3Aone&unique=prints",
                           "set_type": "expansion",
                           "tcgplayer_id": 17684,
                           "uri": "https://api.scryfall.com/sets/04bef644-343f-4230-95ee-255f29aa67a2"}
    
    assert output == expected_dict

def test_grab_cards() -> None:
    """
        Test the grab cards function
    """
    user_set = "TMUL"
    page_num = 1
    card_list_url = "https://api.scryfall.com/cards/search?include_extras=true&include_variations=true&order=set&q=e%3A"+ user_set +"&unique=prints&page=" + str(page_num)
    response_data = requests.get(card_list_url, timeout=10000)
    verbose_setting = False
    name = True
    prices = True
    output: dict = grab_cards(user_set=user_set, response_data=response_data, 
                              page_num=1, verbose_setting=verbose_setting,
                              name=name, prices=prices)
    print(str(output))
    expected_output: dict = {1: {'Card Name': 'Phyrexian Myr', 'Price': {'eur': None, 'eur_foil': None, 'tix': None, 'usd': None, 'usd_etched': None, 'usd_foil': None}}, 2: {'Card Name': 'Elemental', 'Price': {'eur': None, 'eur_foil': None, 'tix': None, 'usd': None, 'usd_etched': None, 'usd_foil': None}}}
    
    assert output == expected_output

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

def grab_cards(user_set: str, response_data: dict, page_num: int, verbose_setting: bool, name: bool, prices: bool) -> dict:
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
