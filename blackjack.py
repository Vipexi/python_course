#! /usr/bin/python3

import numpy as np
import random
import os


def make_a_new_deck():
    deck_of_cards = [i for i in range(52)] #make a deck that has 52 cards in it
    for i in range(13): #13 cards for each suit
        for y in range(4): #4 suits
            if i <10: #make every card over 10 equal to 10
                deck_of_cards[i+y*13] = i+1
            elif i >= 10:
                deck_of_cards[i+y*13] = 10
    random.shuffle(deck_of_cards)
    return deck_of_cards

def draw_card(deck):
    #print(len(deck))
    card = deck.pop()
    #print(len(deck))
    return card

def calculate_hand(hand): # takes a list as argument, returns int as sum of cards.
    sum_of_hand = sum(hand)
    if sum_of_hand <= 11:
        for i in range(len(hand)):
            if hand[i] == 1:
                hand[i] = 11
                break
    
    elif sum_of_hand > 21:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i] = 1
                break
    sum_of_hand = sum(hand)
    return sum_of_hand
    
    
def print_hands(dealer_hand_local, player_hand_local):
    print("Dealer has", dealer_hand_local)
    print("Player has", player_hand_local)

def ask_if_player_wants_card(player_hand_now):
    question = "you have now " + str(player_hand_now)+", do you want another card?"
    answer_local =input(question)
    return answer_local

def ask_if_player_wants_to_split(player_hand_now):
    question = "you have now " + str(player_hand_now)+", do you want to split your hand?"
    answer_local = input(question)
    return answer_local

def ask_how_many_credits_player_wants():
    while True:
        try:
            local_answer = int(input("How many credits do you want (5-100) use?"))
            if local_answer >= 5 and local_answer <=100:
                return local_answer
        except:
            print("not a valid answer, try again")

"""def write_to_file(winner,game_ended):
    file_to_write.write(f"winner,{winner},game_ended,{game_ended}player hand,{player_hand},dealer hand,{dealer_hand}\n")
        try:
            file_to_write = open(filename,"a")
        except:
            print("can not open file")"""

if __name__ == "__main__":

    player_credits = ask_how_many_credits_player_wants()

    while True:
        deck = make_a_new_deck()
        dealer_hand = []
        player_hands = [[]]
        dealer_hand.append(draw_card(deck))
        player_hands[0].append(draw_card(deck))
        player_hands[0].append(draw_card(deck))
        print(deck)
        if player_hands[0][0] == player_hands[0][1]:
            if ask_if_player_wants_to_split(player_hands[0]) =="yes":
                player_hands.append([])
                player_hands[1].append(player_hands[0]).pop()
                player_hands[0].append(draw_card(deck))
                player_hands[1].append(draw_card(deck))
        
        for i in range(len(player_hands)):        
            while True:
                print_hands(dealer_hand,player_hands[i])
                answer = ask_if_player_wants_card(player_hands[i])
                if answer == "yes":
                    player_hands[i].append(draw_card(deck))
                    
                    if calculate_hand(player_hands[i]) > 21:
                        break
                elif answer == "no":
                    break
        
        hands_went_over = []
        for i in range(len(player_hands)):
            print_hands(dealer_hand, player_hands)
            if calculate_hand(player_hands[i]) > 21:
                print("you went over, you lose the hand")
                hands_went_over.append(True)
            else:
                hands_went_over.append(False)

        if all(hands_went_over) == True:
            print("you lose all hands")

        elif calculate_hand(dealer_hand) < 16:
            while calculate_hand(dealer_hand) < 16:
                dealer_hand.append(draw_card(deck))
                print("dealer takes a card")
                print(dealer_hand, player_hands)

            if calculate_hand(dealer_hand) > 21:
                print("dealer went over you win")
            
            else:
                for i in range(len(player_hands)):
                    if calculate_hand(dealer_hand) >= calculate_hand(player_hands[i]):
                        print("Dealer wins the hand!")
                    else:
                        print("Player wins the hand!")
        
        new_game = input("Do you want a new game, press enter. If you want to end type: no ")
        if new_game == "no":
            break


    
"""while True:
    print_hands(dealer_hand,player_hand)
    if calculate_hand(player_hand) > 21:
        print("you went over, you lose")
        #write_to_file(0,1)
        break
    elif calculate_hand(dealer_hand) < 16:
        dealer_hand.append(draw_card(deck))
        
    elif calculate_hand(dealer_hand) > 21:
        print("dealer went over, you win")
        #write_to_file(1,0)
        break
        
    elif calculate_hand(dealer_hand) >= calculate_hand(player_hand):
        print("Dealer wins!")
        #write_to_file(0,2)
        break
    else:
        print("Player wins!")
        #write_to_file(1,3)
        break
    
    new_game = input("Do you want a new game, press enter. If you want to end type: no ")

if new_game == "no":
    break"""
    
#file_to_write.write(f("player hand {player_hand} dealer hand {dealer_hand}\n")

                
                

