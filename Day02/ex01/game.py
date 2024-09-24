from collections import Counter
import random

class Player:
    def __init__(self):
        self.last_response = None
    
    def cooperate(self):
        return 1
    
    def cheat(self):
        return 0
    
    def strategy(self, opponent):
        raise NotImplementedError

class Cheater(Player):
    def strategy(self, opponent):
        return self.cheat()

class Cooperator(Player):
    def strategy(self, opponent):
        return self.cooperate()

class Copycat(Player):
    def strategy(self, opponent):
        if opponent.last_response is None:
            return self.cooperate()
        return opponent.last_response

class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.grudged = False
    
    def strategy(self, opponent):
        if self.grudged:
            return self.cheat()
        if opponent.last_response == self.cheat():
            self.grudged = True
            return self.cheat()
        return self.cooperate()

class Detective(Player):
    def __init__(self):
        super().__init__()
        self.moves = [1, 0, 1, 1]  
        self.index = 0
        self.copycat_mode = False  
        self.detected_cheat = False  
    
    def strategy(self, opponent):
        # First four moves (predefined)
        if self.index < 4:
            move = self.moves[self.index]
            self.index += 1
            if opponent.last_response == self.cheat():  
                self.detected_cheat = True
            return move
        
        if self.detected_cheat:
            if opponent.last_response is None:
                return self.cooperate()
            return opponent.last_response
        else:
            return self.cheat()

class ForgivingCopycat(Player):
    def strategy(self, opponent):
        if opponent.last_response is None:
            return self.cooperate()
        if opponent.last_response == self.cheat() and random.random() < 0.1:
            return self.cooperate()
        return opponent.last_response

# Game class
class Game:
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
    
    def play(self, player1, player2):
        for _ in range(self.matches):
            response1 = player1.strategy(player2)
            response2 = player2.strategy(player1)
            
            player1.last_response = response1
            player2.last_response = response2
            
            if response1 == response2 == 1:
                self.registry[player1.__class__.__name__] += 2
                self.registry[player2.__class__.__name__] += 2
            elif response1 == 0:
                self.registry[player1.__class__.__name__] += 3
                self.registry[player2.__class__.__name__] -= 1
            elif response2 == 0:
                self.registry[player1.__class__.__name__] -= 1
                self.registry[player2.__class__.__name__] += 3
    
    def top3(self):
        print(self.registry.most_common(6))

game = Game()
players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective(), ForgivingCopycat()]

for i in range(len(players)):
    for j in range(i + 1, len(players)):
        print(f"{players[i].__class__.__name__} vs {players[j].__class__.__name__}")
        game.play(players[i], players[j])

game.top3()
