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




# Question: Please draw "number_of_cards" cards from deck "deck_id" and return the value of "cards"
#
# Example response from deckofcardsapi.com when drawing a card
#
# {
#     "cards": [
#         {
#             "code": "QH",
#             "image": "https://deckofcardsapi.com/static/img/QH.png",
#             "images": {
#                 "png": "https://deckofcardsapi.com/static/img/QH.png",
#                 "svg": "https://deckofcardsapi.com/static/img/QH.svg"
#             },
#             "suit": "HEARTS",
#             "value": "QUEEN"
#         }
#     ],
#     "deck_id": "vg290ja1bftp",
#     "remaining": 50,
#     "success": true
# }

# This function should call the Deck of Cards API and return the cards drawn
def draw_cards(deck_id, number_of_cards):
    raise Exception("Please write this function!")