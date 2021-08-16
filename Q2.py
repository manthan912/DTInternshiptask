import random


def rps( n, x, y ):
    print("-----------------------------------")
    print(" ! ROCK, PAPER AND SCISSORS ! ")
    mode = int( input( " 1 for (vs) computer & 2 for Multiplayer " ) )
    if mode == 1:
        print(" wins : " + str(n))
        user = str( input( " Rock(R/r), Paper(P/p), Scissors(S/s)? " ) ).lower()
        choices = ["rock", "paper", "scissor"]
        comp = random.choice(choices)
        if user == 'R' or user == 'r':
            user = "rock"
        elif user == 'P' or user == 'p':
            user = "paper"
        elif user == 'S' or user == 's':
            user = "scissor"
        if user == comp:
            print("Tie!!")
            again = str( input( "Play again? Y or N" ) )
            again = again.upper()
            if again == 'Y':
                rps( n, x, y )
        elif user != comp:
            print( "Player : " + user, " Computer :  " + comp  )
            if user == "rock" and comp == "scissor":
                print(" ***You Win!*** ")
                again = str(input("Play again? Y or N"))
                again = again.upper()
                if again == 'Y':
                    rps(n+1, x, y)
            elif user == "paper" and comp == "rock":
                print(" ***You Win!*** ")
                again = str(input("Play again? Y or N"))
                again = again.upper()
                if again == 'Y':
                    rps(n+1, x, y)
            elif user == "scissor" and comp == "paper":
                print(" ***You Win!*** ")
                again = str(input("Play again? Y or N"))
                again = again.upper()
                if again == 'Y':
                    rps(n+1, x, y)
            else:
                print("***You Lose!***")
                again = str(input("Play again? Y or N"))
                again = again.upper()
                if again == 'Y':
                    rps(n, x, y)
    if mode == 2:
        print('Player 1: ' + str(x) + ' Player 2: ' + str(y))
        user1 = str(input('PLAYER 1: Rock, Paper or Scissors?')).lower()
        user2 = str(input('PLAYER 2: Rock, Paper or Scissors?')).lower()

        if user1 == 'R' or user1 == 'r':
            user1 = 'rock'
        elif user1 == 'P' or user1 == 'p':
            user1 = 'paper'
        elif user1 == 'S' or user1 == 's':
            user1 = 'scissors'

        if user2 == 'R' or user2 == 'r':
            user2 = 'rock'
        elif user2 == 'P' or user2 == 'p':
            user2 = 'paper'
        elif user2 == 'S' or user2 == 's':
            user2 = 'scissors'

        if user1 == user2:
            print('Tie!')
            again = str(input('Play again? Y or N'))
            again = again.upper()
            if again == 'Y':
                rps(n, x, y)
        elif user1 != user2:
            print('Player 1: ' + user1, ' Player 2: ' + user2)
            if user1 == 'rock' and user2 == 'scissors':
                print('***Player 1 wins!***')
                again = str(input('Play again? Y or N'))
                again = again.upper()
                if again == 'Y':
                    rps(n, x + 1, y)
            elif user1 == 'scissors' and user2 == 'paper':
                print('***Player 1 wins!***')
                again = str(input('Play again? Y or N'))
                again = again.upper()
                if again == 'Y':
                    rps(n, x + 1, y)
            elif user1 == 'paper' and user2 == 'rock':
                print('***Player 1 wins!***')
                again = str(input('Play again? Y or N'))
                again = again.upper()
                if again == 'Y':
                    rps(n, x + 1, y)
            else:
                print('***Player 2 wins!***')
                again = str(input('Play again? Y or N'))
                again = again.upper()
                if again == 'Y':
                    rps(n, x, y + 1)
rps(0,0,0)
