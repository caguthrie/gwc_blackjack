# coding=utf-8
suits = {
    "CLUBS": "♣",
    "DIAMONDS": "♦",
    "HEARTS": "♥",
    "SPADES": "♠"
}

def print_table(cards, show_all_dealer_cards):
    if show_all_dealer_cards:
        card_names = list(map(lambda card: get_card_name(card), cards["dealer"]))

        print("Dealer has:\n{dealers_cards} \n(Total: {total})\n".format(
            dealers_cards="\n".join(card_names),
            total=get_total(cards["dealer"])
        ))
    else:
        print("\nDealer is showing:\n{card}\n\n".format(
            card=get_card_name(cards["dealer"][0])
        ))
    
    card_names = list(map(lambda card: get_card_name(card), cards["player"]))
    
    print("You have:\n{players_cards}\n(Total: {total})\n".format(
        players_cards="\n".join(card_names),
        total=get_total(cards["player"])
    ))
    

def get_card_name(card):
    return "{value} {suit}".format(
        value=card["value"],
        suit=suits[card["suit"]]
    )

def get_total(cards):
    value = 0
    
    # Add up all cards
    for card in cards:
        if card["value"] == "JACK" or card["value"] == "QUEEN" or card["value"] == "KING":
            value += 10
        elif card["value"] == "ACE":
            value += 11
        else:
            value += int(card["value"])
            
    # Special case, handle aces because they can be 1 or 11. If total is greater than 21, try to reduce
    if value > 21:
        for card in cards:
            if card["value"] == "ACE":
                value -= 10 # 11 - 1 is 10
                if value <= 21:
                    break
    
    return value