# Mancala
> This program will replicate a Mancala game in console. Up to 2 users will be able to play against each other and follows the general rules of mancala. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information.
- This project allows 2 users to play Mancala against each other in console.
- The purpose of this project is to demonstrate an understanding of coding algorithms and concepts learned in the 2nd level intro programming class.



## Technologies Used
- N/A


## Features
List the ready features here:
- print_board() allows the user to obtain current board information, and how many pieces are in each persons store.
- return_winner() will allow the user to check to see if there is a winner and print the appropriate message if a winner is found, there is a tie, or if the game has not ended.
- play_game() allows each user to make a move. It takes as parameters the player number that is taking their turn, and the pit number that they choose.


## Screenshots
![Example screenshot](https://user-images.githubusercontent.com/50156212/207260956-2c9b2de3-dcc7-4b09-b1bb-9765bd0aa6d5.PNG)

## Setup
IDE needed to run python code. Link to pyCharm provided.
https://www.jetbrains.com/pycharm/


## Usage
The user must follow these steps to begin playing mancala
- Initialize the mancala class. Ex. game = Mancala()
- Create two different players that will be partaking in the game. Ex. player1 = game.create_player("Michael") && player2 = game.create_player("Andrew")
- Use the play_game(player_num, pit_num) method to start making moves. Ex. game.play_game(1,3) which means player 1 will choose pit number 3 to take and divide stones from.
- Utilize print_board() method to see the status of the stores and pits of each player. Ex. game.print_board()
- Utilize return_winner() method to check for winners 


## Project Status
Project is: _in progress_


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- The user must input play_game and choose which user to begin making the move. I'd like to change this so that the program will print out who's turn it is.
- Instead of using a print_board, I'd like to always print the status of the board after every move so users can play more dynamically instead of trying to remmeber.

To do:
- Eventually after learning more frontend, add a way to play this game more visually instead of in console.
- Have a score count that will keep track of each user's store.
- End the game automatically when the conditions are fulfilled.


## Acknowledgements
Give credit here.
- This project created by OSU CS 162 course.


## Contact
Created by Michael Vuong. https://www.linkedin.com/in/vuong-michael/ - feel free to contact me!

<!-- ## License -->
- N/A
