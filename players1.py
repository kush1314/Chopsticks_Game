class Player:
    def __init__(self, name, opponent=None):
        self.name = name
        self.opponent = opponent
        self.leftHand = 1  # The player's right and left hands will start with 1
        self.rightHand = 1
    
    def is_out(self):
        return self.leftHand == 0 and self.rightHand == 0  # Determines if the player is out
    
    def get_status(self):  # Prints the status of each player
        left_status = f'Left Hand: {self.leftHand}' if self.leftHand > 0 else 'Left Hand is out'
        right_status = f'Right Hand: {self.rightHand}' if self.rightHand > 0 else 'Right Hand is out'
        return f'{left_status}, {right_status}'
    
    def win(self):
        if self.is_out(): 
            return f'{self.name} has won!'
    
    def attack_On_Right_With_Left(self):
        if self.opponent.rightHand > 0:
            self.opponent.rightHand = (self.opponent.rightHand + self.leftHand) % 5
            if self.opponent.rightHand == 0:
                print(f"{self.opponent.name}'s Right Hand is out!")

    def attack_On_Right_With_Right(self):
        if self.opponent.rightHand > 0:
            self.opponent.rightHand = (self.opponent.rightHand + self.rightHand) % 5
            if self.opponent.rightHand == 0:
                print(f"{self.opponent.name}'s Right Hand is out!")

    def attack_On_Left_With_Right(self):
        if self.opponent.leftHand > 0:
            self.opponent.leftHand = (self.opponent.leftHand + self.rightHand) % 5
            if self.opponent.leftHand == 0:
                print(f"{self.opponent.name}'s Left Hand is out!")
    
    def attack_On_Left_With_Left(self):
        if self.opponent.leftHand > 0:
            self.opponent.leftHand = (self.opponent.leftHand + self.leftHand) % 5
            if self.opponent.leftHand == 0:
                print(f"{self.opponent.name}'s Left Hand is out!")

    def split(self):
        splits = input('How do you want to split? Give the numbers in order from right hand to left hand. Ex: 12 ')
        if splits == '11':
            self.leftHand = 1
            self.rightHand = 1
        elif splits == '21':
            self.leftHand = 2
            self.rightHand = 1
        elif splits == '12':
            self.leftHand = 1
            self.rightHand = 2
        elif splits == '22':
            self.leftHand = 2
            self.rightHand = 2
        elif splits == '31':
            self.leftHand = 3
            self.rightHand = 1
        elif splits == '13':
            self.leftHand = 1
            self.rightHand = 3
        elif splits == '14':
            self.leftHand = 1
            self.rightHand = 4
        elif splits == '41':
            self.leftHand = 4
            self.rightHand = 1
        elif splits == '23':
            self.leftHand = 2
            self.rightHand = 3 
        elif splits == '32':
            self.leftHand = 3
            self.rightHand = 2
        elif splits == '02':
            self.leftHand = 0
            self.rightHand = 2
        elif splits == '20':
            self.leftHand = 2
            self.rightHand = 0 
        elif splits == '03':
            self.leftHand = 0
            self.rightHand = 3
        elif splits == '30':
            self.leftHand = 3
            self.rightHand = 0
        elif splits == '04':
            self.leftHand = 0
            self.rightHand = 4
        elif splits == '40':
            self.leftHand = 4
            self.rightHand = 0

def main():
    print('Welcome to chopsticks!')
    name1 = input('What is player 1\'s name? ')
    name2 = input('What is player 2\'s name? ')
    player1 = Player(name1)
    player2 = Player(name2, player1)
    player1.opponent = player2
    current_player = player1

    while not player1.is_out() and not player2.is_out():
        print(f'The status of {current_player.name} is: {current_player.get_status()}')
        rules = input(f'It\'s now {current_player.name}\'s turn. Pick a move: 1. Left hand to right hand, 2. Right hand to right hand, 3. Right hand to left hand, 4. Left hand to left hand, 5. Split ')

        if rules == '1':
            current_player.attack_On_Right_With_Left()
        elif rules == '2':
            current_player.attack_On_Right_With_Right()
        elif rules == '3':
            current_player.attack_On_Left_With_Right()
        elif rules == '4':
            current_player.attack_On_Left_With_Left()
        elif rules == '5':
            current_player.split()
        
        if player1.is_out() or player2.is_out():
            break
        
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    if player1.is_out():
        print(f'{player2.name} wins!')
    elif player2.is_out():
        print(f'{player1.name} wins!')

if __name__ == "__main__":
    main()
