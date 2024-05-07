import random

class DiceGame:
    
    def __init__(self, points):
        self.points = points
    
    def play():

        roll_user = random.randint(1,7)
        roll_CPU = random.randint(1,7)
        
        print(f'Your dice: {roll_user}')
        print(f'CPU dice: {roll_CPU}')
        
        if roll_user > roll_CPU:
            print('You win this round.')
            DiceGame.points += 1
            
    
    