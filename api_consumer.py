import requests

API_BASE_URL = "http://deckofcardsapi.com/api"

# This function should shuffle a deck and return a deck_id from the Deck of Cards API
def shuffle():

    new_deck = requests.get(API_BASE_URL + "/deck/new/shuffle/?deck_count=1")

    # if this was a successful request:
    if new_deck.status_code == 200:
        return new_deck.json().get("deck_id")
    else:
        raise Exception("Trouble shuffling the deck!")




# This function should call the Deck of Cards API and return the cards drawn
def draw_cards(deck_id, number_of_cards):
    url = API_BASE_URL + "/deck/" + deck_id + "/draw/?count=" + str(number_of_cards)
    cards = requests.get(url)

    # if this was a successful request:
    if cards.status_code == 200:
        return cards.json().get("cards")
    else:
        raise Exception("Error drawing cards (greasy fingers maybe)!")