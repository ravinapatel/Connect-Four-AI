# Connect-Four-AI
## Introduction
The aim for this project was to

(1) create a Connect Four game with a gui that looks like the real game

(2) build an AI that can respectably compete with a human player.

## AI
### Minimax
This AI simulates all possible moves for a certain depth of turns and assigns each potential board a score. Using the minimax algorithm, it then chooses the best move. I have found that a depth of 4 plays quickly, while beating human players pretty consistently. A depth of 3 is a decent player and a depth of 5 takes quite long to play.


![minimax-gif](https://user-images.githubusercontent.com/48966108/63031821-ad0f5580-be82-11e9-9363-43fee263ec0a.gif)

### Aggressive
This AI uses heuristics to determine the next move. It searches for 3-in-a-rows from either player. If the fourth spot is empty and playable, the AI completes the move, effectively winning the game or blocking the opponent's winning move. Though the process is pretty rudimentary right now, it is able to occasionally beat humans due to human error.

Here is a demo of a player (yellow) against the AI (red). In this play, the AI blocks the player from winning a few times and ultimately wins with a horizontal four in a row.


![board-gif](https://user-images.githubusercontent.com/48966108/61003917-dcd2b700-a332-11e9-9ca0-104b087bdeab.gif)

### Random
This bot chooses a valid column at random to drop a chip into.


## Improvements
The minimax AI performs pretty well, but with the standard 7 column board, looking ahead n moves takes 7^n board simulations. Implementing alpha-beta pruning will be able to speed up the processing, allowing it to look further ahead and play even better.


MIT's VICTOR AI is extremely effective at solving Connect Four using 9 heuristic rules. Currently, if the aggresive AI does not find any playable 3-in-a-rows, it makes a random play. Adding more heuristics to check will make the play more strategic.

## Technology
* Python 3.6.5
* Tkinter
* NumPy
