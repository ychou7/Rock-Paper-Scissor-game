from random import choice

# print a game menu

# RPS Menu:
# 1. Play game
# 2. Show score
# 3. Quit

#define global variables to human's score and computer's score
human_score = 0
computer_score = 0


def display_menu():
  menu = "\nRPS Menu:\n1. Play game\n2. Show score\n3. Quit"
  print(menu)


# Final Score:
# 1. Player = 4
# 2. Computer = 2
def show_scores():
  print('\nFinal Score:')
  if (human_score > computer_score):
    print("1. Player = " + str(human_score),
          "\n2. Computer = " + str(computer_score))
  else:
    print("1. Computer = " + str(computer_score),
          "\n2. Player = " + str(human_score))


def display_weapon_menu():
  menu = "\nChoose you weapon:\nR. Rock\nP. Paper\nS. Scissors\nB. Back"
  print(menu)

def whoWins(human, computer):
  '''return h when human wins, c as computer wins, f as fair'''
  if human == computer:
    return 'f'
  if (human == 'r' and computer == 's') or (human == 'p' and computer == 'r') or (human == 's' and computer == 'p'):
    return 'h'
  return 'c'
  
def rps(ch):
  if ch == 'r':
    return "Rock"
  if ch == 'p':
    return "Paper"
  if ch == 's':
    return "Scissors"

def game():
  global human_score
  global computer_score
  print("Welcome to the Rock Paper Scissors game: ")
  while True:
    display_menu()
    selection = int(input())
    if (selection == 3):
      break
    elif (selection == 2):
      show_scores()
    else:
      while True:
        display_weapon_menu()
        human = input().lower()
        if human == 'b':
          break
        # computer choice
        computer = choice(['r','p','s'])

        # todo - print choices of human and computer
        # Human chose Rock/Paper/Scissors
        # Computer chose Rock/Paper/Scissors
        print(f"Human chose {rps(human)}")
        print(f"Computer chose {rps(computer)}")
        winner = whoWins(human, computer)
        # todo - add one point to winner, and display who wins, or if it's a fair print fair game
        # human win, human + 1point, print Human Win 
        # computer ......
        # Fair, print fair game
        if winner == 'h':
            human_score += 1
            print("Human Wins")
        elif winner == 'c':
            computer_score += 1
            print("Computer Wins")
        else:
            print('Fair game!')

game()
