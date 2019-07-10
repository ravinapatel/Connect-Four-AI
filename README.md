# Connect-Four-AI
## Introduction
The aim for this project was to

(1) create a Connect Four game with a gui that looks like the real game

(2) build an AI that can respectably compete with a human player.

## AI
Originally, I planned to have the AI simulate all possible moves for a certain depth of turns and use a minimax function to choose the best move. However, with the standard 7 column board, looking ahead n moves would take 7^n board simulations, so creating an effective board would take exponentially more time.

Instead, I decided to use heuristics to determine the next move. The AI searches for 3-in-a-rows from either player. If the fourth spot is empty and playable, the AI completes the move, effectively winning the game or blocking the opponent's winning move. Though the process is pretty rudimentary right now, it is able to beat humans sometimes due to human error.

### Demo
Here is a demo of a player (yellow) against the AI (red). In this play, the AI blocks the player from winning a few times and ultimately wins with a horizontal four in a row.


![board-gif](https://user-images.githubusercontent.com/48966108/61003917-dcd2b700-a332-11e9-9ca0-104b087bdeab.gif)

## Improvements
MIT's VICTOR AI is extremely effective at solving Connect Four using 9 heuristic rules. Currently, if the AI does not find any playable 3-in-a-rows, it makes a random play. Adding more heuristics to check will make the play more strategic.
