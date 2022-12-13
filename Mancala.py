# Author Michael Vuong
# GitHub username: mvuo
# Date: 11/22/2022
# Description: This program is a recreation of the hit board game that everyone loves, Mancala! Utilize one small
# class called Player to initialize a player object. The other class Mancala will be where the game is played.
# Users may create up to 2 players to vs each other for a game of mancala. The current board information can be seen
# using the print_board method. A play_game method will allow users to choose the player doing the turn and
# choose the space where they would like to move on their side. The user may call the return_winner method to
# see the status of the game at any time and see if a winner has come up.

class Player:
    """
    This class creates the player object. That will be used to play against another player object during the game.
    This class is primarily only used to create a player object that the Mancala class will use when playing the game.
    The only method in this class will be get_name, where it will return the name of the player.
    """

    def __init__(self, name):
        """Initializes the player with a name"""
        self._name = name

    def get_name(self):
        """Returns the name of the player"""
        return self._name


class Mancala:
    """
    This class creates the game object as played. The methods within this class include create_player, which will
    create a player object and store it. It will need to access the Player class to create a player object to
    be used during the game There will also be a print_board method, which will print what the current board
    looks like. It will have a method to print the winner if the game is over, and print other differing messages
    depending on the status of the game.
    """

    def __init__(self):
        """Initializes a list for the two players and the layout of the board."""
        self._players = []
        self._first_player_side = [4, 4, 4, 4, 4, 4]
        self._first_player_store = 0
        self._second_player_side = [4, 4, 4, 4, 4, 4]
        self._second_player_store = 0
        self._current = []

    def create_player(self, name):
        """Takes in a name for the parameter, adds it to the list of current players, and returns the player object"""
        self._players.append(Player(name))
        return Player(name)

    def get_players(self):
        """returns the list of player objects within the list initialized in this class"""
        return self._players

    def print_board(self):
        """Prints the current board information. Will print each player's store and seed number from pit 1-6 in
            the form of a list. Will most likely just print self._board"""
        print("player1:")
        print("store:", self._first_player_store)
        print(self._first_player_side)
        print("player2:")
        print("store:", self._second_player_store)
        print(self._second_player_side)

    def return_winner(self):
        """ Return a message depending on if a winner is found, there is a tie, or the game has not ended yet.
            Will utilize if else checks to check the player objects to determine who the winner is or if there
            is a tie. Will also do a check to see if there are any remaining numbers in the board list that are
            not in a player's store. These checks will determine what is being printed"""
        if self.winner_check():
            if self._first_player_store > self._second_player_store:
                name = self._players[0].get_name()
                return "Winner is player 1: " + name
            elif self._first_player_store == self._second_player_store:
                return "It's a tie"
            else:
                name = self._players[1].get_name()
                return "Winner is player 2: " + name
        else:
            return "Game has not ended"

    def winner_check(self):
        """
        checks to see if the sum of a player's side is 0 yet. If either side becomes 0 then returns False
        Which indicates to the rest of the program that the game has ended.
        """
        if sum(self._first_player_side) == 0 or sum(self._second_player_side) == 0:
            return True
        else:
            return False

    def play_game(self, player_num, pit_num):
        """Takes two parameters, the player number, and the pit number. Will play out the game based on the player
            selection of the pit number and update the seed numbers in each pit including the store.  Will iterate over
            the self._board list and change values with a generator depending on the user input. If the user inputs
            a value outside the range of 1-6, will print out an error message "Invalid number for pit index."
            It will check if the game is over with an if else at the beginning, checking if there are no stones in
            any of the outside pits and update the seed and store numbers accordingly."""
        if pit_num not in range(1, 7):
            return "Invalid number for pit index"
        if self.winner_check():
            return "Game is ended"
        elif not self.winner_check():
            board = self.create_board_list(player_num)
            value = board[pit_num - 1]
            board[pit_num - 1] = 0
            for num in range(pit_num, pit_num + value):  # loop to place rocks down
                if num == pit_num + value - 1:  # check to see if this is the last rock
                    board[num % len(board)] += 1
                    if board[num % len(board)] == board[6]:
                        print("player " + str(player_num) + " take another turn")
                    if board[num % len(board)] == 1 and num % len(board) < 6:  # if the last rock ends on empty space
                        board[6] += board[num % len(board)]
                        board[6] += board[len(board) - 1 - num % len(board)]
                        board[num % len(board)] = 0
                        board[len(board) - 1 - num % len(board)] = 0
                else:
                    board[num % len(board)] += 1
            self.update_info(player_num, board)
            # Checks to see if the game has ended. If is has, then each player's store and side will be updated
            if self.winner_check():
                self._first_player_store += sum(self._first_player_side)
                self._first_player_side = [0, 0, 0, 0, 0, 0]
                self._second_player_store += sum(self._second_player_side)
                self._second_player_side = [0, 0, 0, 0, 0, 0]
            current = self.create_board_list(1)
            self.update_info(1, current)
            current.append(self._second_player_store)
            return current

    def create_board_list(self, player_num):
        """
        creates a long list that will be used to iterate over which spaces will be given a stone. Used within
        the play_game method
        """
        if player_num == 1:
            playing_board = self._first_player_side
            playing_board.append(self._first_player_store)
            playing_board.extend(self._second_player_side)
        else:
            playing_board = self._second_player_side
            playing_board.append(self._second_player_store)
            playing_board.extend(self._first_player_side)
        return playing_board

    def update_info(self, player_num, board):
        """
        Will update the board and the store numbers to the current info. Used within the play_game method.
        """
        if player_num == 1:
            self._first_player_side = board[:6]
            self._first_player_store = board[6]
            self._second_player_side = board[7:]
        else:
            self._second_player_side = board[:6]
            self._second_player_store = board[6]
            self._first_player_side = board[7:]
