#ROCK , PAPER , SCISSORS GAME
import random, sys

#keeps track of the player score
Wins = 0
Losses = 0
Ties = 0

while True:
    print('%s Wins , %s Losses , %s Ties' % (Wins , Losses , Ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit() #exit the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Please Type one of r , p , s , q')

#Display what the player chooses
    if player_move == 'r':
       print('Rock versus...')
    elif player_move == 'p':
       print('Paper versus...')
    else :
      print('Scissors versus...')

#Display what the computer chooses
    random_number = random.randint(1, 3) #random number between 1 and 3
    if random_number == 1:
      computer_move = 'r'
      print('Rock')
    elif random_number == 2:
      computer_move = 'p'
      print('Paper')
    else:
      computer_move = 's'
      print('Scissors')

#Display the result
    if player_move == computer_move:
      print('It is a tie!')
      Ties += 1
    elif player_move == 'r' and computer_move == 's':
       print('You win!')
       Wins += 1
    elif player_move == 'p' and computer_move == 'r':
      print('You win!')
      Wins += 1
    elif player_move == 's' and computer_move == 'p':
      print('You win!')
      Wins += 1
    elif player_move == 'r' and computer_move == 'p':
      print('You lose!')
      Losses += 1
    elif player_move == 'p' and computer_move == 's':
      print('You lose!')
      Losses += 1
    elif player_move == 's' and computer_move == 'r':
      print('You lose!')
      Losses += 1
    else:
      print('Invalid input')
                                