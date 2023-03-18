import random

def get_card_value(card):
    if card == 'A':
        return 11
    elif card in ['K', 'Q', 'J']:
        return 10
    else:
        return int(card)

def get_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        card_value = get_card_value(card)
        value += card_value
        if card == 'A':
            num_aces += 1
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1
    return value

def get_new_deck():
    deck = []
    for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        deck.append(rank)
    random.shuffle(deck)
    return deck

def play_game():
    deck = get_new_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    print(f"Player's hand: {player_hand}, value: {get_hand_value(player_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]}")
    while get_hand_value(player_hand) <= 21:
        action = input("Do you want to hit or stand? ")
        if action.lower() == "hit":
            player_hand.append(deck.pop())
            print(f"Player's hand: {player_hand}, value: {get_hand_value(player_hand)}")
        else:
            break
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"Player's hand: {player_hand}, value: {get_hand_value(player_hand)}")
    print(f"Dealer's hand: {dealer_hand}, value: {get_hand_value(dealer_hand)}")
    if get_hand_value(player_hand) > 21:
        print("You lose.")
    elif get_hand_value(dealer_hand) > 21:
        print("You win!")
    elif get_hand_value(player_hand) > get_hand_value(dealer_hand):
        print("You win!")
    elif get_hand_value(player_hand) < get_hand_value(dealer_hand):
        print("You lose.")
    else:
        print("Draw.")

play_game()
