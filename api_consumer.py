import requests

API_BASE_URL = "http://deckofcardsapi.com/api"

# This function should shuffle a deck and return a deck_id from the Deck of Cards API
def shuffle():
    
    # TODO: Make HTTP request here to shuffle a new deck
    
    # TODO: if this was a successful request ...:
        return json_parsed_data["deck_id"]
    # else:
        raise Exception("Trouble shuffling the deck!")

# This function should call the Deck of Cards API
def draw_cards(deck_id, number_of_cards):
    
    # TODO: Make HTTP request here to draw {number_of_cards} cards from deck with id {deck_id}

    # TODO: if this was a successful request ...:
        return json_parsed_data["cards"]
    # else:
        raise Exception("Error drawing cards (greasy fingers maybe)!")