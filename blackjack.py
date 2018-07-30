from api_consumer import shuffle
from game_actions import deal_cards, draw_cards, dealer_hit
from display import print_table, get_total

deck_id = shuffle()

# Get initial set of cards
cards = deal_cards(deck_id)

while True:
    
    print_table(cards, False)
    
    # Ask user what action they want to take
    input = raw_input("Do you want to hit (h) or stand (s)?\n")
    print("\n")
    if len(input) == 0:
        continue
        
    # Process user input
    if input.lower()[0] == "h":
        cards['player'].append(draw_cards(deck_id, 1)[0])
        
        # Repeat if the total is less than or equal to 21
        if get_total(cards["player"]) <= 21:
            continue
    elif input.lower()[0] != "s":
        continue


    # See if the user has busted
    if get_total(cards["player"]) > 21:
        print_table(cards, True)
        print("\nSorry, you have busted.\n")
    else:
        # Dealer draws card(s) if necessary
        dealer_hit(deck_id, cards)
        print_table(cards, True)
        
        # Print game results
        if get_total(cards["dealer"]) > 21:
            print ("\nDealer busts, you win!\n")
        elif get_total(cards["player"]) > get_total(cards["dealer"]):
            print("\nYou win!\n")
        elif get_total(cards["player"]) < get_total(cards["dealer"]):
            print("\nYou lost\n")
        elif get_total(cards["player"]) == get_total(cards["dealer"]):
            print("\nYou pushed\n")


    play_again = raw_input("Do you want to play again (y/n)?")
    if len(play_again) == 0 or play_again.lower()[0] == "y":
        deck_id = shuffle()
        cards = deal_cards(deck_id)
        continue
    else:
        break
        
    
    
    