# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:

# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!

# My Solution

def rps(p1, p2):
    sc = 'scissors'
    pp = 'paper'
    rc = 'rock'

    winner1 = 'Player 1 won!'
    winner2 = "Player 2 won!"
    if (p1 == sc and p2 == pp) or (p1 == pp and p2 == rc) or (p1 == rc and p2 == sc):
        return winner1
    if p1 == p2:
        return 'Draw!'
    else:
        return winner2