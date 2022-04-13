# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:04:47 2021

@author: Vipul Kumar
"""

from abc import ABC, abstractmethod
from random import shuffle
import sys

class Player(ABC):

    def __init__(self, name, playerType):
        '''
        Subclass of player class defining methods for Human players

        Parameters
        ----------
        name : String
            Name to be associated with human player instance

        Attributes
        -------
        name: Name to be associated with human player instance
        hand: Set of cards associated with current player instance
        playerType: Type of player instance "human", "computer" or "deaer"

        '''
        self.name = name
        self.hand = []
        self.playerType = playerType
        
    def getType(self):
        '''
        Get the type of player - Human, Computer or Dealer

        Returns
        -------
        String
            self.playerType - Returns the type of player instance

        '''
        return self.playerType
    
    def getName(self):
        '''
        Get the name of player

        Returns
        -------
        String
            self.name - Returns the name of player instance

        '''
        return self.name
    
    def score(self):
        '''
        Calculates the current score for the player instance based on hand

        Returns
        -------
        current_score : Int
            Value of current hand of layer instance

        '''
        current_score = 0 
        ace_cards = []
        for card in self.hand:
            if card.getRank() == 'A':
                ace_cards.append(card)
            else:
                current_score += card.value(current_score)
        for card in ace_cards:
            current_score += card.value(current_score)
        return current_score
    
    def add_card(self,card):
        '''
        Adds card to the hand of player

        Parameters
        ----------
        card : Object of class Card
            Card object having attributes 'rank' and 'suit'

        Returns
        -------
        None.

        '''
        self.hand.append(card)
        
    def show_hand(self):
        '''
        Prints the current hand of player instance

        '''
        for card in self.hand:
            print(card)
            
    def refreshHand(self):
        '''
        
        Empty hand of player for new round.

        '''
        self.hand = []
               
    @abstractmethod
    def action(self):
        pass

class HumanPlayer(Player):

    def __init__(self, name):
        
        '''
        Calls super class constructor to set attributes for human player

        Parameters
        ----------
        name : String
            Name to be associated with human player instance

        Attributes
        -------
        name: Name to be associated with human player instance
        hand: Set of cards associated with current player instance
        type: Type of player instance "human", "computer" or "deaer"

        '''

        super().__init__(name, "human")            
            
    def action(self):
        '''
        Method used to check if the human player wants to 'hit' or 'stand'
        on their turn

        Raises
        ------
        ValueError
            If the input by the player is other than 'hit' or 'stand'
            ValueError is raised

        Returns
        -------
        answer : String
            Input by the player

        '''
        while True:
            try:
                print("\n", self.getName(),"Do you want to hit or stand?")
                answer = input()
                if answer == "hit" or answer == "stand":
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter 'hit' or 'stand'")
        return answer
        
    
class ComputerPlayer(Player):
    
    def __init__(self, name):
        
        '''
        Calls super class constructor to set attributes for computer player

        Parameters
        ----------
        name : String
            Name to be associated with computer player instance

        Attributes
        -------
        name: Name to be associated with computer player instance
        hand: Set of cards associated with current player instance
        type: Type of player instance "human", "computer" or "deaer"

        '''

        super().__init__(name, "computer")  
        
            
            
    def action(self):
        '''
        Define cation for computer player

        Returns
        -------
        str
                returns either 'hit' or 'stand' based on current score of
                the computer player

        '''
        if self.score()<17:
            return "hit"
        else:
            return "stand"

        
class Dealer(Player):
    
    def __init__(self, name):
        
        '''
        Calls super class constructor to set attributes for the dealer

        Parameters
        ----------
        name : String
            Name to be associated with dealer instance

        Attributes
        -------
        name: Name to be associated with dealer instance
        hand: Set of cards associated with current player instance
        type: Type of player instance "human", "computer" or "deaer"

        '''

        super().__init__(name, "dealer")             
            
    def action(self):
        '''
        Define action for dealer

        Returns
        -------
        str
                returns either 'hit' or 'stand' based on current score of
                the dealer

        '''
        if self.score()<17:
            return "hit"
        else:
            return "stand"
        
    def show_one_card(self):
        '''
        Prints just one card out of dealer's cards'

        Returns
        -------
        Card object
            First card dealt to dealer

        '''
        return self.hand[0]
        
        
class Card:
    def __init__(self, rank, suit):
        '''
        Card class defines the behavior of a playing card

        Parameters
        ----------
        rank : String
            Rank of the card
        suit : String
            suit of the card

        Attributes
        -------
        rank : Rank of the card
        suit : Suit of the card

        '''
        self.rank = rank
        self.suit = suit
    def getRank(self):
        '''
        get method to get the rank of card instance

        Returns
        -------
        String
            Rank of the card instance

        '''
        return self.rank
    
    def __repr__(self):

        return "Card(rank='{}', suit='{}')".format(self.rank, self.suit)
    def __eq__(self, other):
        try:
            return self.rank == other.rank and self.suit == other.suit
        except AttributeError:
            return False
        
    def value(self, current_score):
        '''
        This method calculates the value of a card as per the rules of black
        jack game

        Parameters
        ----------
        current_score : Int
            Score calculated as per the value of preceeding cards. Used 
            to determine value of Ace

        Returns
        -------
        Int
            Value of current card

        '''

        if self.rank in ['2', '3', '4', '5', '6' , '7', '8', '9', '10']:
            return int(self.rank)
        elif self.rank in ['J', 'Q', 'K']:
            return 10 
        else:
            if current_score<=10:
                return 11
            else:
                return 1
    
class Deck():
    
    def __init__(self):
        '''
        Deck class defines the behavior of card deck

        Attributes
        -------
        _cards : The deck of all 52 cards

        '''
        ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
        suits = ['spades', 'diamonds', 'clubs', 'hearts']
        self._cards = [Card(rank, suit) for suit in suits for rank in ranks]
        
    
    def deal_card(self):
        '''
        Deals the top card from the deck

        Returns
        -------
        Card object
            Top card from the deck

        '''
        return self._cards.pop(0)
    
        
    def shuffle(self):
        '''
        Shufles the deck of card


        '''
        shuffle(self._cards)
        
    def size(self):
        '''
        Method to find the number of cards left in the deck

        Returns
        -------
        int
            Number of cards in the deck

        '''
        return len(self._cards)
        


        
    
class Game():
    
    def __init__(self, num_human=1, num_computer=1):
        '''
        Game class controls the gameplay of Blackjack

        Parameters
        ----------
        num_human : int, optional
            Number of human players passed. The default is 1.
        num_computer : int, optional
            Number of human players passed. The default is 1.

        Attributes
        -------
        num_human_player : Number of human players
        num_computer_player : Number of computer players

        '''
        self.num_human_player = num_human
        self.num_computer_player = num_computer
        
        
    def play(self):
        '''
        Method that deines the gameplay.

        Raises
        ------
        IndexError
            Error raised when deck is empty, a message is displayed and
            the game exits.
        ValueError
            Error is raised when the user input does not match the required
            keywords.


        '''

        players = []
        for player in range(0,self.num_human_player):
            name = input("Provide player "+ str(player+1)+" name:")
            players.append(HumanPlayer(name))
            
            
        for player in range(0,self.num_computer_player):
            name = "Computer Player " + str(player + 1)
            players.append(ComputerPlayer(name))
            
        players.append(Dealer("Dealer"))
        
            
        play_a_round = True
        
        while(play_a_round):
            for player in players:
                player.refreshHand()
            deck = Deck()
            deck.shuffle()
            active_players = players[:]
            max = 0
            winner = []
            
            for i in range(0,2):               
                for player in players:
                    try:
                        if deck.size() > 0:
                            card = deck.deal_card()
                        else:
                            raise IndexError
                    except IndexError:
                        sys.exit("\nNo more cards left: game has ended")
                        
                    player.add_card(card)
            
            print("\nCards dealt are as follows:")
            for player in players:
                if player.getName() != "Dealer":
                    print("\n",player.getName())
                    player.show_hand()
                else:
                    print("\n", player.getName())
                    print(player.show_one_card())
                    print("Card 2 is face down")
            

                    
            for player in players:
                while (True):
                    if player.getName() == "Dealer":
                        print("\n",player.getName())
                        player.show_hand()
                    action = player.action()
                    if action == 'hit':
                        print("\n", player.getName(),"has decided to hit.")
                        try:
                            if deck.size() > 0:
                                card = deck.deal_card()
                            else:
                                raise IndexError
                        except IndexError:
                            sys.exit("\nNo more cards left: game has ended")
                        player.add_card(card)
                        print("\n",player.getName(),"cards:")
                        player.show_hand()
                    if player.score()>21:
                        print("\n",player.getName(), 
                              ": bust, you are out of game")
                        active_players.remove(player)
                        break
                    if action == 'stand':
                        print("\n", player.getName(),"has decided to stand.")
                        break
                        

            for player in active_players:
                if player.score()>max:
                    max = player.score()
                    winner = [player]
                elif player.score() == max:
                    winner.append(player)
                else:
                    continue
            
            print("\nFinal hands and scores are as follows:")
            for player in players:
                print("\n",player.getName())
                player.show_hand()
                print("Score:",player.score(),"\n")
                
                
                
            print("Winner of this round:")
            if len(winner)>0:
                for player in winner:
                    print(player.getName())
            else:
                print("This round does not have a winner")
                
            

            
            for player in players:
                if player.getType() == "human":
                    print("\n",player.getName(),
                          " : Do you want to play another round?")                
                    while True:
                        try:
                            answer = input("Please enter 'yes' or 'no':")
                            if answer == "yes" or answer == "no":
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Please enter 'yes' or 'no':")
                if answer == 'no':
                    play_a_round = False
                    print("End of game")
                    break
                        
                
if __name__ == "__main__":
    g = Game()
    g.play()             
                    
                
                
                
                    
                    
                    
                        
                        
                    
                

                    
                

                    
                    

                    
            
            
            
        
        
    