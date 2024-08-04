# class dice and a method roll dice

from random import randint

class Dice():
    def __init__(self, sides = 6):
    
       self.sides = sides

    def roll_dice(self, num):
        self.num = num
        if self.sides == 6:
            self.num  = num
            for n in range(self.num):
                print(f'Random numbers between 1 and {self.sides} is {randint(1,self.sides)}')
        elif self.sides == 10: 
            for n in range(self.num):
                print(f'Random numbers between 1 and {self.sides} is {randint(1,self.sides)}')
        elif self.sides == 20: 
            for n in range(self.num):
                print(f'Random numbers between 1 and {self.sides} is {randint(1,self.sides)}')


# class instance

dice = Dice(6)
print ('Dice of 6 sides:')
dice.roll_dice(10)

dice2 = Dice(10)
print('Dice of 10 sides:')
dice2.roll_dice(10)

dice3 = Dice(20)
print('Dice of 20 sides')
dice3.roll_dice(20)