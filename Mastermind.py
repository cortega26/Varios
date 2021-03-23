#Mastermind game
#
#Rules:
#The codebreaker tries to guess the pattern, in both order and number.
#Once placed, the codemaker provides feedback: "red peg" means a digit belongs to the solution and it's placed the right position, "white peg" means a digit belongs to the solution but is not the right position.
#If there are duplicate digits in the guess, they cannot all be awarded a correct/incorrect unless they correspond to the same number of duplicate digits in the hidden code.
#For example, if the hidden code is 1 1 2 2 and the player guesses 1 1 1 2, the game will award two red pegs for the two 1s, nothing for the third 1 as there is not a third 1 in the code, and a "correct" for the 2.
#No indication is given of the fact that the code also includes a second 2.

import random
def combination():
  a=random.randint(1,6)
  b=random.randint(1,6)
  c=random.randint(1,6)
  d=random.randint(1,6)
  solution=[a,b,c,d]
  turns=0
  while True:
    guesses=[]
    turns+=1
    a1,a2,a3,a4=input("Enter your four guesses separated by a space (1 to 6). A number may appear more than once: ").split()
    guesses=[int(a1),int(a2),int(a3),int(a4)]
    print(guesses)
    if guesses==solution:
      print(guesses,"is correct. You win.")
      print("It took you",turns,"turns to solve it.")
      break
    else:
      correct=incorrect=0
      round_guesses=[]
      round_solution=[]
      for k in range(4):        
        if solution[k]==guesses[k]:
          correct+=1
        else:
          round_guesses.append(guesses[k])
          round_solution.append(solution[k])
      for n in range(len(round_guesses)):
          if round_guesses[n] in round_solution:
            incorrect+=1
            round_solution.remove(round_guesses[n])
      
    #print(round_guesses,round_solution)
    print("red pegs: ",correct,"white pegs: ",incorrect)

combination()
