import requests

API_BASE_URL = "http://deckofcardsapi.com/api"

def shuffle():
    response = requests.get("{api}/deck/new/shuffle/?deck_count=1".format(
        api=API_BASE_URL
    ))
    deck_details = response.json()
    if response.status_code == 200 and deck_details["success"] == True:
        return deck_details["deck_id"]
    else:
        raise Exception("Trouble shuffling the deck!")
    
def draw_cards(deck_id, number_of_cards):
    response = requests.get("{api}/deck/{deck_id}/draw/?count={number_of_cards}".format(
        api=API_BASE_URL,
        deck_id=deck_id,
        number_of_cards=number_of_cards
    ))
    draw_details = response.json()
    if response.status_code == 200 and draw_details["success"] == True:
        return draw_details["cards"]
    else:
        raise Exception("Error drawing cards (greasy fingers maybe)!")