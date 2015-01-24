#blackjack.py

import random

def build_deck():

    suit = ['C', 'S', 'D', 'H']
    value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']

    deck = []
    for letter in suit:
        for number in value:
            deck.append(number + letter)
    return deck


def shuffle():

    deck = build_deck()
    random.shuffle(deck)
    return deck

def hand_value(cards):
 
    value = 0
    for card in cards:
        if card[0] == 'J' or card[0] == 'K' or card[0] =='Q':
            value = value + 10
        elif card[0] == 'A':
            value = value + 11
        else:
             value = value + eval(card[0])
    return value
        

def main():

    #PLAYER HAND

    print()
    deck = shuffle()   
    hand = []

    hand = [deck.pop(0), deck.pop(0)]
    print('Your hand: ', hand)

    if hand_value(hand) == 21:
        print('Blackjack! You win!')

    answer = input("Do you want another card? (y or n) " )
    print()
    while answer == "y" and hand_value(hand) < 21:
        hand.append(deck.pop(0))
        print('Your hand: ', hand)
        print(hand_value(hand))
        if hand_value(hand) < 21:
            answer = input("Do you want another card? (y or n) " ) 
        print()
       
    if  hand_value(hand) == 21:
        print('Blackjack! You win!')

    elif hand_value(hand) > 21:
        print('You busted! You lose!')

    else:
        print('You have ', hand_value(hand))

    print()



    #DEALER HAND

    if hand_value(hand) < 21:

        dealer_hand = [deck.pop(0), deck.pop(0)]
        print('Dealer hand: ', dealer_hand)

    
        while hand_value(dealer_hand) < 18:
            print("Dealer takes another card" )
            print()
            dealer_hand.append(deck.pop(0))
            print('Dealer hand: ', dealer_hand)
            print(hand_value(dealer_hand))
    
       
        if  hand_value(dealer_hand) == 21:
            print('Dealer has 21. Dealer wins')

        elif hand_value(dealer_hand) > 21:
            print('Dealer busted! You win!')

        elif hand_value(hand) > hand_value(dealer_hand):
            print('You win')

        else:
            print('Dealer wins.')

    print()



if __name__ == '__main__':
    main()
