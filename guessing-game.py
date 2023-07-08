from random import choice
def guessingGame():
    random_num = choice(range(100))
    is_over = False
    count_guess = 0 
    def game(num):
        # when we want to modify variables from the enclosing scope within a nested function, we have to declare them nonlocal
        nonlocal is_over, count_guess
        if is_over: return "The game is over, you already won!"
        count_guess += 1
        if num > random_num: 
            return f"{num} is too high"
        elif num < random_num:
            return f"{num} is too low"
        else:
            is_over = True
            return f"You win! Found {num} in {count_guess} guesses"
    return game

game = guessingGame()
game(5)
game(90)
game(77)
game(66)