#Mastermind game
#
#Rules:
#The codebreaker tries to guess the pattern, in both order and number.
#Once placed, the codemaker provides feedback:
#- "red peg" means a digit belongs to the solution and it's placed the right position
#- "white peg" means a digit belongs to the solution but is not the right position.
#
#If there are duplicate digits in the guess, they cannot all be awarded a correct/incorrect unless they correspond to the same number of duplicate digits in the hidden code.
#For example, if the hidden code is 1 1 2 2 and the player guesses 1 1 1 2, the game will award two red pegs for the two 1s,
#nothing for the third 1 as there is not a third 1 in the code, and a "correct" for the 2.
#No indication is given of the fact that the code also includes a second 2.


import random


def get_random_combination():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
    return random.sample(colors, 8)[:4]

  
def get_player_guess():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
    while True:
        guesses = input(f"Enter your four guesses separated by a space ({', '.join(colors)}): ").lower().split()
        if len(guesses) == 4 and all(color in colors for color in guesses) and len(set(guesses)) == 4:
            return guesses
        print("Invalid input. Please enter four unique colors from the available options.")

        
def count_matches(solution, guesses):
    correct = sum(solution[i] == guesses[i] for i in range(4))
    incorrect = sum(min(guesses.count(color), solution.count(color)) for color in set(guesses)) - correct
    return correct, incorrect

  
def play_combination_game():
    solution = get_random_combination()
    turns = 0

    while True:
        turns += 1
        guesses = get_player_guess()
        correct, incorrect = count_matches(solution, guesses)

        if correct == 4:
            print(guesses, "is correct. You win.")
            print("It took you", turns, "turns to solve it.")
            break
        else:
            print("red pegs:", correct, "white pegs:", incorrect)

            
if __name__ == "__main__":
    play_combination_game()
