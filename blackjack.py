import random

deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

card_values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

def calculate_hand(hand):
    total_value = sum(card_values[card] for card in hand)
    if 'A' in hand and total_value > 21:
        total_value -= 10
    return total_value

def deal_card():
    return deck.pop()

def play_game():
    random.shuffle(deck)

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    print("Your hand: ", player_hand, "total value ==>", calculate_hand(player_hand))
    print(f"Dealer's hand: ['{dealer_hand[0]}' '?']")

    while True:
        action = input("Do you want to hit or stand (h or s) ? ")
        if action.lower() == 'h':
            player_hand.append(deal_card())
            print("Your hand: ", player_hand, "total value ==>", calculate_hand(player_hand))
            print(f"Dealer's hand: ['{dealer_hand[0]}' '?']")
        
        if calculate_hand(player_hand) > 21:
            print("Total card value exceeds 21. You lose!")
            break
        elif calculate_hand(player_hand) == 21:
            print("You win!")
        
        elif action.lower() == 's':
            break
        else:
            print("Invalid action, please enter 'h' or 's'")

    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    print("Dealer's hand: ", dealer_hand)
    
    if calculate_hand(dealer_hand) > 21:
        print("Dealer's total card value exceeds 21. You win!")
    
    elif calculate_hand(player_hand) == 21:
        print("You lose!")
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)
    
    if 21 > player_total > dealer_total:
        print("You win!")
    elif 21 > dealer_total > player_total:
        print("Dealer won!")
    elif player_total == dealer_total and player_total > 17:
        print("Draw!")


play_game()
