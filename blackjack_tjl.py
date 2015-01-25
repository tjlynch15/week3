#blackjack.py
import time
import random

def build_deck():

    suit = ['\u2660', '\u2663', '\u2665', '\u2666']
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
             value = value + eval(card[:-1])
    return value


def card_value(card):
    if card[0] == 'J' or card[0] == 'K' or card[0] =='Q':
        value = 10
    elif card[0] == 'A':
        value = 11
    else:
        value = eval(card[:-1])
    return value   
        

def play_game():
    
    #PLAYER HAND

    print()
    deck = shuffle()   
    hand = []

    hand = [deck.pop(0), deck.pop(0)]
    print('Your hand: ', ''.join(hand))
    print()

    dealer_hand = [deck.pop(0), deck.pop(0)]
    print('Dealer hand: ', ''.join(dealer_hand[0]), 'X')
    print()

    value = hand_value(hand)
    dealer_value = hand_value(dealer_hand)

    if value == 21:
        print('Blackjack! You win!')

    elif value < 21:    
        answer = input("Do you want another card? (y or n) " )
      
        while answer == "y" and hand_value(hand) < 21:
            print()
            hand.append(deck.pop(0))
            print('Your hand: ', ''.join(hand))
            #print(hand_value(hand))
            print()
            if hand_value(hand) < 21:
                answer = input("Do you want another card? (y or n) " ) 

        value = hand_value(hand)

        ace_count =  ''.join(hand).count('A')  
        while value > 21 and ace_count != 0:
        
            #print('number of aces', ace_count)
           
            value = value - 10
            ace_count = ace_count - 1

            if value < 21:
                answer = input("Do you want another card? (y or n) " )
                if answer == "y":
                    hand.append(deck.pop(0))
                    print()
                    print('Your hand: ', ''.join(hand))
                    value = value + card_value(hand[-1])
                    if card_value(hand[-1]) == 11:
                        ace_count = ace_count + 1
                    print('hand value', value)
                    print()
                    if value < 21:
                        answer = input("Do you want another card? (y or n) " ) 

            #print('hand value', value)

        

        if  value == 21:
            print('Blackjack! You win!')

        elif value > 21:
            print('You busted! You lose!')

        else:
            print('You have: ', value)

    print()



    #DEALER HAND

    if value < 21:

        time.sleep(4)
        print('Dealer hand: ', ''.join(dealer_hand))
        time.sleep(4)

    
        while hand_value(dealer_hand) <= 17:
            print("Dealer takes another card" )
            print()
            time.sleep(4)
            dealer_hand.append(deck.pop(0))
            print('Dealer hand: ', ''.join(dealer_hand))
            print()
    
        dealer_value = hand_value(dealer_hand)

        ace_count =  ''.join(dealer_hand).count('A')  
        while dealer_value > 21 and ace_count != 0:
                    
            #print('number of aces', ace_count)
           
            dealer_value = dealer_value - 10
            ace_count = ace_count - 1

            while dealer_value <= 17:
                print("Dealer takes another card" )
                print()
                time.sleep(4)
                dealer_hand.append(deck.pop(0))
                print('Dealer hand: ', ''.join(dealer_hand))
                dealer_value = dealer_value + card_value(dealer_hand[-1])
                if card_value(dealer_hand[-1]) == 11:
                    ace_count = ace_count + 1
                print('Dealer hand value', dealer_value)
                print()
                 

            #print('Dealer hand value ', dealer_value)

      
        print('Dealer has: ', dealer_value)   
       
        if  dealer_value == 21:
            print('Dealer has blackjack. Dealer wins.')

        elif dealer_value > 21:
            print('Dealer busted! You win!')

        elif value > dealer_value:
            print('You win!')

        elif value == dealer_value:
            print('Tie. Nobody wins.')   

        else:
            print('Dealer wins.')

    
        
def main():

    play_game()
    print()
    answer = input("Do you want to play again? (y or n): ")
    while answer == "y":
        print()
        play_game()
        print()
        answer = input("Do you want to play again? (y or n): ") 
   



if __name__ == '__main__':
    main()
