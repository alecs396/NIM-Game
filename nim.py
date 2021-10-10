"""The nim module contains the classes for playing the Nim strategy game.

Author(s):  Matt Manley
"""
import random


class Game:
    """A period of turn-based play ending in a definate result. The 
    responsibility of Game is to control the sequence of play.
    
    Stereotype: Controller
    """
    def play(self):
        board = Board()
        official = Official()
        players = []
        _next = 0
        
        official.register(players)
        while not board.is_solved():
            official.display(board)
            player = players[_next]
            player.make_move(board)	
            official.check(board, player)
            _next = (_next + 1) % len(players)


class Player:
    """A person taking part in a game. The responsibility of Player is to make 
    moves and keep track of their identity.
    
    Stereotype: Information Holder
    """
    def __init__(self, _id, name):
        self._id = _id
        self._name = name
    
    def get_id(self, _id):
        return _id
    
    def get_name(self, _name):
        return _name

    def make_move(self, board):
        print(f"{self._name}'s turn:")
        pile = int(input(f"What pile to remove from? "))
        stones = int(input(f"How many stones to remove? "))
        move = (pile, stones)
        board.update(move)

    
class Board:
    """A designated area for playing a game. The responsibility of Board is 
    to keep track of the items in play.
    
    Stereotype: Information Holder
    """
    def __init__(self):
        self._items = []
        piles = random.randint(2, 5)
        for n in range(piles):
            stones = random.randint(1, 9)
            self._items.append(stones)
    
    def get_items(self):
        return self._items
    
    def is_solved(self):
        completed = [0] * len(self._items)
        return self._items == completed

    def update(self, move):
        pile, stones = move
        pile = pile - 1
        self._items[pile] -= stones

class Official:
    """A person who officiates in a game. The responsibility of Official is to 
    perform special duties including: check if there's a winner, display the 
    board and register players.
    
    Stereotype: Service Provider
    """
    def check(self, board, player):
        if board.is_solved():
            name = player.get_name()
            print(f"\n{name} won!")

    def display(self, board):
        items = board.get_items()
        text =  "\n--------------------"
        for pile, stones in enumerate(items):
            pile = pile + 1
            text += (f"\n{pile}: " + "O " * stones)
        text += "\n--------------------"
        print(text)

    def register(self, players):
        for i in range(2):
            _id = i + 1
            name = input(f"Player {_id} name: ")
            player = Player(_id, name)
            players.append(player)

    
if __name__ == "__main__":
    game = Game()
    game.play()