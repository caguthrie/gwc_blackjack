import requests

API_BASE_URL = "http://deckofcardsapi.com/api"

# This function should shuffle a deck and return a deck_id from the Deck of Cards API
def shuffle():

    newDeck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    
    # if this was a successful request:
    if newDeck.status_code == 200:
        return newDeck.json().get("deck_id")
    else:
        raise Exception("Trouble shuffling the deck!")




# This function should call the Deck of Cards API and return the cards drawn
def draw_cards(deck_id, number_of_cards):    
    url = "https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=" + str(number_of_cards)
    cards = requests.get(url)

    # if this was a successful request:
    if cards.status_code == 200:
        return cards.json().get("cards")
    else:
        raise Exception("Error drawing cards (greasy fingers maybe)!")