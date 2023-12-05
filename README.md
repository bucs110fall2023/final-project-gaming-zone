[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803390&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Saloni Paresh Mahyavanshi
Athira Unnikrishnan

***

## Project Description

It is a game of tic tac toe. There will be two players. The players will be assigned X or O. Player 1 will be X and player 2 will be O. The players will draw X/O wherever they want on the grid, alternatively. The first to have X/O in 3 consecutive boxes (horizontally, vertically or diagonally) wins.

***    

## GUI Design



### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Menu
2. Choosing X and O player
3. 
4. 
5. Game Over and Start Again

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

Test Case 1: Tic Tac Toe

Test Description: Verify that the next page to show up would be the instructions or the game according to what the player chooses.

Test Steps:
1. Start the game.
2. Press the 'Start Game' key.
3. Verify that the game starts asking to choose the shape.
4. Press the 'Instructions' key.
5. Verify that the next page shows the instructions of how to play the game.

Expected Outcome: the next page to show up would be the instructions or the game according to what the player chooses.

Test Case 2: 3 in a Row Pattern

Test Description: Verify that the "O"s are three in a row vertically, horizontically, or diagonally.

Test Steps:
1. Start the game.
2. Choose "O" or "X"
3. First the player would occupy a space then the computer would occupy a space. The game would continue until "O"s or "X"s appear three in a row vertically, horizontically, or diagonally.
4. Verify the game identify's the pattern by making sure the display changes to Game Over page. 

Expected Outcome: The display would change when either the player or the computer occupies three spaces in a row vertically, horizontically, or diagonally.

Test Case 3: Choose the shape for the player

Test Description: Saving what shape the player chooses

Test Steps:
1. Start the game
2. Press the 'Start Game; button
3. A page with two options - 'O' and 'X'- will appear.
4. Player can choose whichever shape they like.
5. The shape they choose will be saved for them and the other shape is assignemed to the computer by default.

Expected Outcome: When the game starts, and the player clicks a spot to enter their shape, the chosen shape only will be inserted

Test Case 4: Game Over Condition

Test Description: Confirm that the game ends when the player wins, loses, or ties with the computer.
Test Steps:
1. Start the game.
2. Play until either the player or the computer wins.
3. Verify that the game displays "You Win!", "You Lose. Try Again.", or "It's a tie." message.

Expected Outcome: The game should display a "You Win!", "You Lose. Try Again.", or "It's a tie." message when the game ends.

