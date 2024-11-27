This game has a few rules you should know before playing.

General minesweeper rules:
  - The goal is to remove all non-mine cells from the board.
  - You can "flag" unopened tiles to avoid calling them by accident.
  - calling a mined square ends the game.
  - The number on a cell indicates how many mines are adjacent to it.
  - Use the number clues to solve the game by opening safe squares

For each action you take this program will ask you to enter a coordinate. Entering
"flag" or "unflag" into this prompt allows you to enter flag and unflag modes.
Bombs will be recognized for win conditioning regardless of whether or not the player
has manually flagged them yet. 

Contents (this section contains summaries of all functions in this file):


def generate_board(x,y):
    """
    This function takes user inputs to generate a board
    Args:
        x (str): desired width of board
        y (str): desired length of board
    Returns:
        list: 2d list board
    """
def make_empty_grid(grid)
    """
    This function takes the board and returns an empty
    board for the player to play on
    Args:
        grid (list): 2d list board of AxB dimensions
    Returns:
        list: empty board of AxB dimensions
    """
def update_grid(grid):
    """
    This function converts squares within an area to display
    their bomb counts. 
    Args:
        grid (list): 2d list board
    Returns:
        none: updates grid to display bombcounts
    """
def print_grid(emptygrid):
    """
    This function does all the gross formatting
    Args:
        emptygrid (list): the users view of the board
    Returns:
        none: prints board
    """
def dig(updategrid,coord,emptygrid):
    """
    This function digs on a point. Then, if there are any zeros on
    the edge of dug area it digs again on all adjacent tiles to 
    the zero. This allows for efficient gameplay.
    Args:
        updategrid (list): answer key to game
        coord (str): user input for where to dig (format a1, k12, etc.)
        emptygrid (list): current userview of grid
    Returns:
        list: updated userview of grid
    """
def determine_game_status(grid, user_view):
    """
    This function compares the answer key to the 
    user's current board state to determine game status
    Args:
        grid (list): The game's answer key
        user_view (list): The user's current board
    Returns:
        bool or str: 
            True: the game is ongoing
            str: message stating whether the game was won or lost
    """
def flag(user_view, coord):
    """
    This function takes args user_view and coord to flag
    a specific coordinate
    Args:
        user_view (_type_): user's current board state
        coord (_type_): user input for where to flag 
    Returns:
        None: prints board
    """
def unflag(user_view, coord):
    """
    I had realized after a bit of play testing, that if you
    accidentally flagged the wrong square, you lost. After 
    realizing that I added this deflag mode.
    Args:
        user_view (list): User's current board state
        coord (str): user input for where to unflag
    Returns:
        None: prints board
    """
def play_game():
    """
    This function runs the game
    """
