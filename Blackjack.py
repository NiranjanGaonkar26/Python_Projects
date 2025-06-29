import random

suits = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three': 3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards_list = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards_list.append(card)
    
    def shuffle_deck(self):
        random.shuffle(self.cards_list)
    
    def draw_card(self):
        return self.cards_list.pop()        


class Player:
    def __init__(self, name, card1, card2):
        self.name = name
        self.balance = 500
        self.hand = [card1, card2]
    
    def place_bet(self, amount):
        if amount > self.balance:
            print("Sorry, insufficient balance to play the game")
            return False
        else:
            self.bet = amount
            self.balance -= amount
            return True
    
    def hit(self, card):
        self.hand.append(card)
    
    def display_hand(self):
        print("Your current hand")
        for card in self.hand:
            print(card, end = ", ")
        print()
    
    def hand_sum(self):
        total = 0
        for card in self.hand:
            total += card.value
        
        return total
        
    def check_bust(self):
        return self.hand_sum() > 21
    
    def player_win(self):
        win_amount = 2 * self.bet
        print(f"\nCongratulations!!!, you win {win_amount}")
        self.balance += win_amount

class Dealer:
    def __init__(self, card1, card2):
        self.hand = [card1, card2]
    
    def hit(self, card):
        self.hand.append(card)
    
    def display_hand(self, player_stand_flag):
        print("\nDealer's current Hand")
        if player_stand_flag:
            for card in self.hand:
                print(card, end = ", ")
        else:
            print("#", end = ", ")
            for card in self.hand[1:]:
                print(card, end = ", ")
        print()
        
    def hand_sum(self):
        total = 0
        for card in self.hand:
            total += card.value
        
        return total
    
    def check_bust(self):
        return self.hand_sum() > 21


def play_Blackjack():
    game_on = True

    while game_on:
        play_game = input("GAME ON? y or n")
        if play_game.lower() != 'y' and play_game.lower() != 'n':
            break
        if play_game.lower() == 'n':
            break
        
        deck = Deck()
        deck.shuffle_deck()

        card1 = deck.draw_card()
        card2 = deck.draw_card()
        player = Player('Josh', card1, card2)

        card3 = deck.draw_card()
        card4 = deck.draw_card()
        dealer = Dealer(card3, card4)
        
        current = 'Player'
        try:
            amount = int(input("Please place your bet amount"))
        except:
            print("Please enter a valid amount")

        if player.place_bet(amount) == False:
            continue

        if player.hand_sum() == 21:
            player.display_hand()
            player.player_win()
            continue
        
        print("Your Turn\n")
        
        while current == 'Player':
            player.display_hand()
            dealer.display_hand(False)
            player_option = input("What do you want to do? Type Hit or Stand")
            
            if player_option.lower() != 'hit' and player_option.lower() != 'stand':
                print("Invalid answer")
                continue
            
            if player_option.lower() == 'stand':
                current = 'Dealer'
            
            else:
                card = deck.draw_card()
                print(f"\nYou have drawn a {card}\n")
                
                player.hit(card)
                player.display_hand()
                
                if player.check_bust():
                    print("\nYou loose, better luck next time")
                    # game_on = False
                    # break
                    current = 'Play Again'
                
                elif player.hand_sum() == 21:
                    player.player_win()
                    # game_on = False
                    # break
                    current = 'Play Again'
        
        if current == 'Dealer':
            print("\nDealer's Turn")
            while dealer.hand_sum() < 17:
                dealer.display_hand(True)
                card = deck.draw_card()
                dealer.hit(card)
            
            if dealer.check_bust():
                dealer.display_hand(True)
                player.player_win()
                
            elif dealer.hand_sum() > player.hand_sum():
                dealer.display_hand(True)
                print("You loose, better luck next time")
                
            else:
                dealer.display_hand(True)
                player.player_win()

if __name__ == '__main__':
    play_Blackjack()




