from api_consumer import draw_cards
from display import get_total

def deal_cards(deck_id):
    cards = {
        'player': [],
        'dealer': []
    }
    
    cards['player'].append(draw_cards(deck_id, 1)[0])
    cards['dealer'].append(draw_cards(deck_id, 1)[0])
    cards['player'].append(draw_cards(deck_id, 1)[0])
    cards['dealer'].append(draw_cards(deck_id, 1)[0])
    
    return cards

def dealer_hit(deck_id, cards):
    while get_total(cards['dealer']) < 17:
        cards['dealer'].append(draw_cards(deck_id, 1)[0])