#! /usr/bin/python3

import random

class Bj_game:

    def __init__(self, game_type):
        self.game_type = game_type

    def make_a_new_deck(self):
        deck_of_cards = [i for i in range(52)]
        for i in range(13):
            for y in range(4):
                if i <10:
                    deck_of_cards[i+y*13] = i+1
                elif i >= 10:
                    deck_of_cards[i+y*13] = 10
        random.shuffle(deck_of_cards)
        return deck_of_cards

    def draw_card(self, deck):
        
        #print(len(deck))
        card = deck.pop()
        #print(len(deck))
        return card

    def calculate_hand(self, hand):
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
        
    def print_hands(self, dealer_hand_local, player_hand_local):
        if self.game_type == "cmd":
            print("Dealer has", dealer_hand_local)
            print("Player has", player_hand_local)
        elif self.game_type == "ai":
            pass
        #elif not a command line game
    def ask_if_player_wants_card(self, player_hand_now):
        if self.game_type == "cmd":
            question = "you have now " + str(player_hand_now)+", do you want another card?"
            answer_local =input(question)
            return answer_local
        elif self.game_type =="ai":
            return "no"
        #elif not a command line game
    def ask_if_player_wants_to_split(self, player_hand_now):
        if self.game_type == "cmd":
            question = "you have cards " + str(player_hand_now)+", do you want to split our hand?"
            answer_local = input(question)
            return answer_local
        elif self.game_type =="ai":
            return "no"
        #elif not a command line game

    def info_to_player(self, message):
        if self.game =="cmd":
            print(message)
        elif self.game_type == "ai":
            pass

    def ask_if_player_want_a_new_game(self):
        if self.game_type == "cmd":
            answer = input("Do you want new game, press enter. If you want to end type:no ")
            return answer
        elif self.game_type =="ai":
            return "no"

    def game(self):
        while True:
            deck = self.make_a_new_deck()
            dealer_hand = []
            player_hands = [[]]
            dealer_hand.append(self.draw_card(deck))
            player_hands[0].append(self.draw_card(deck))
            player_hands[0].append(self.draw_card(deck))
            if player_hands[0][0] == player_hands[0][1]:
                if self.ask_if_player_wants_to_split(player_hands[0]) == "yes":
                    player_hands.append([])
                    player_hands[1].append(player_hands[0].pop())
                    player_hands[0].append(self.draw_card(deck))
                    player_hands[1].append(self.draw_card(deck))

            for i in range(len(player_hands)):
                while True:
                    self.print_hands(dealer_hand,player_hands[i])
                    answer = self.ask_if_player_wants_card(player_hands[i])
                    if answer == "yes":
                        player_hands[i].append(self.draw_card(deck))
                        
                        if self.calculate_hand(player_hands[i]) > 21:
                            break
                    elif answer == "no":
                        break
            

            hands_went_over = []
            for i in range(len(player_hands)):
                self.print_hands(dealer_hand,player_hands)
                
                if self.calculate_hand(player_hands[i]) > 21:
                    self.info_to_player("you went over, you lose the hand")
                    hands_went_over.append(True)
                else: 
                    hands_went_over.append(False)

            if all(hands_went_over) == True:
                self.info_to_player("you lose all hands")   
                

            elif self.calculate_hand(dealer_hand) < 16:
                while self.calculate_hand(dealer_hand) < 16:
                    dealer_hand.append(self.draw_card(deck))
                    self.info_to_player("dealer takes a card")
                    self.print_hands(dealer_hand,player_hands)
                    
                if self.calculate_hand(dealer_hand) > 21:
                    self.info_to_player("dealer went over, you win")
                else:
                    for i in range(len(player_hands)):
                        if self.calculate_hand(dealer_hand) >= self.calculate_hand(player_hands[i]):
                            self.info_to_player("Dealer wins the hand!")
                        else:
                            self.info_to_player("Player wins the hand!")
            new_game = self.ask_if_player_want_a_new_game()
            if new_game == "no":
                break

if __name__ == "__main__":
    play_game = Bj_game("cmd")
    play_game.game()


