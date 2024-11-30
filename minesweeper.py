"""
Timothy Russoniello
CSC 110
Extended Project 10
I made a playable minesweeper game
where X's are bombs and ■'s are zeros
"""

import random

# letters is used a few times-- I wanted global scopage
letters = "abcdefghijklmnopqrstuvwxyz"

def generate_board(x,y):
    """
    This function takes user inputs to generate a board
    Args:
        x (str): desired width of board
        y (str): desired length of board

    Returns:
        list: 2d list board
    """
    board = []
    # generates 2 d list with random bombs
    for i in range(0,x):
        row = []
        for j in range(0, y):
            mine_factor = random.randint(0,7)
            if mine_factor == 0:
                row.append('X')
            else:
                row.append('0')
            
        board.append(row)
    return board

def make_empty_grid(grid):
    """
    This function takes the board and returns an empty
    board for the player to play on
    Args:
        grid (list): 2d list board of AxB dimensions

    Returns:
        list: empty board of AxB dimensions
    """
    empty = []
    for i in range(len(grid)):
        subempty = []
        for j in range(len(grid[i])):
            subempty.append('')
        empty.append(subempty)
    return empty


def update_grid(grid):
    """
    This function converts squares within an area to display
    their bomb counts. 
    Args:
        grid (list): 2d list board
    Returns:
        none: updates grid to display bombcounts
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if theres a bomb, theres a bomb
            if grid[i][j] == "X":
                grid[i][j] = "X"
            # if theres not a bomb count bombs around square
            else:
                bomb_count = 0
                for h in range(i-1, i+2):
                    for k in range(j-1,j+2):
                        if h >= 0 and h < len(grid):
                            if k >= 0 and k < len(grid[i]):
                                if grid[h][k] == "X":
                                    bomb_count += 1
                # make square equal bomb count
                grid[i][j] = bomb_count

def print_grid(emptygrid):
    """
    This function does all the gross formatting
    Args:
        emptygrid (list): the users view of the board
    Returns:
        none: prints board
    """
    # set up empty variables and letters
    result = ""
    final_row = ""
    # for each row of board
    for i in range(len(emptygrid)):
        for j in range(len(emptygrid[i])):
            if i == 0:
                if j == 0:
                    final_row += '{:>4}'.format(letters[j])
                else:
                    final_row += '{:>3}'.format(letters[j])
    for i in range(len(emptygrid)):
        row = ''
        # edit final row by adding letter of colum
        # for each item-index in each row of board
        for j in range(len(emptygrid[i])):
            # add a blank space and fill it with whats in user_view board
            row += "[{:>1}]".format(emptygrid[i][j])
        # add string generated in last for and label to result
        result += "{:>2}{}\n".format(len(emptygrid)-(i+1),row)
    # add final row to end of list and print
    result += final_row +"  "
    print(result) 

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
    print(f'coord reads {coord}')
    print(f'coord read len is {len(coord)}')
    # the b index is the first input, it is a letter
    b = coord[0]
    # the index of that letter in letters is the desired index
    b = letters.index(b)
    # if our digit coord is 1 digit just assign index
    if len(coord) == 2:
        a = len(updategrid)- 1 - int(coord[1])
    elif len(coord) == 3 and coord[2] == " ":
        a = len(updategrid)- 1 - int(coord[1])
    # if our digit coord is 2 digits, concatenate them together, then assign index
    elif len(coord) == 4 and coord[3] == " ":
        a = len(updategrid)-1 - int(coord[1]+coord[2])
    elif len(coord) == 3 and coord[2].isnumeric() == True:
        a = len(updategrid)-1 - int(coord[1]+coord[2])

    # if this spot isn't flagged
    if emptygrid[a][b] != '?':
        # update this spot to the answer key
        emptygrid[a][b] = updategrid[a][b]
        # then if we didnt just lose the game
        if updategrid[a][b] != "X":
            # for 3x3 area around a,b
            for c in range(a-1,a+2):
                for d in range(b-1,b+2):
                    # if this area does not exceed board limits
                    if c >=0 and c < len(updategrid):
                        if d >=0 and d < len(updategrid):
                            # if c,d is not a bomb update it to match updategrid
                            if updategrid[c][d] != "X":
                                emptygrid[c][d] = updategrid[c][d]
                                # if c,d is a zero on updategrid
                                if updategrid[c][d] == 0:
                                    # for 3x3 area around that zero
                                    for e in range(c-1, c+2):
                                        for f in range(d-1, d+2):
                                            # if e,f is within board limits
                                            if 0 <= e < len(updategrid) and 0 <= f < len(updategrid[c]):
                                                # and e,f is not a bomb in the key but empty on the userview
                                                if updategrid[e][f] != "X" and emptygrid[e][f] == "":
                                                    # dig there again with our coord being f,e
                                                    dig(updategrid, letters[f]+ str(len(updategrid)-1-e), emptygrid)
                            # if our coord is a zero, make it pretty
                            if updategrid[c][d] == 0:
                                emptygrid[c][d] = '■'
    return emptygrid


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
    # counts user empty spaces
    count = 0
    # counts bombs in answer key
    net_bombs = 0
    # for each list on board
    for list_ in user_view:
        # for each item in list
        for item in list_:
            # if any bombs have been revealed you lose
            if item == "X":
                return "You lose..."
            # count non-bomb empties
            if item == "" or item == "?":
                count += 1
    # for list in answerkey, for item in list
    for list_ in grid:
        for item in list_:
            # if bomb count bombs
            if item == "X":
                net_bombs += 1
    # if the #/o/bombs is equal to the #/0/empty spaces on the user's board, game win.
    if count == net_bombs:
        return "You win!"
    return True

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
    # as seen earlier, converts coords to indices
    b = coord[0]
    b = letters.index(b)
    if len(coord) == 2:
        a = len(user_view)- 1 - int(coord[1])
    elif len(coord) == 3:
        a = len(user_view)-1 - int(coord[1]+coord[2])
    # if this is an empty square for the user, flag it
    if user_view[a][b] == '':
        user_view[a][b] = "?"
    # print board
    print_grid(user_view)

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
    # as seen earlier, converts coords to indices
    b = coord[0]
    b = letters.index(b)
    if len(coord) == 2:
        a = len(user_view)- 1 - int(coord[1])
    elif len(coord) == 3:
        a = len(user_view)-1 - int(coord[1]+coord[2])
    # if this is a flagged square, unflag it
    if user_view[a][b] == '?':
        user_view[a][b] = ""
    # print board
    print_grid(user_view)

def play_game():
    """
    This function runs the game
    """
    # rules screen containing inputs, which we print
    rules= '\n\nWelcome to minesweeper! Clear the game by entering cordinate pairs\n\
that connect to squares on the board. Coordinate pairs are written\n\
as such: a1, b4, c12 etc etc. Type \'flag\' or \'unflag\' in coordinate\n\
input prompts to enter flag or unflag mode. Good luck, have fun!\n'
    print(rules)
    # takes inputs for board construction
    x = int(input("how wide would you like the board? "))
    y = int(input("how tall would you like the board? "))
    # builds board
    grid = generate_board(x,y)
    # makes user view
    user_view = make_empty_grid(grid)
    # mutates original board to answer key
    update_grid(grid)
    # prints user_view
    print_grid(user_view)
    # while game is ongoing
    while determine_game_status(grid, user_view) == True:
        # take inputm if input is flag or unflag enter those modes
        coord = input("Enter a cordinate pair: ")
        coord += " "
        if coord == "flag ":
            coord = input("Enter cordinate to flag: ")
            coord += " "
            # if coord not valid reask
            while len(coord) < 2 or coord[0].isnumeric() == True \
                or coord[1].isalpha() == True or int(str(coord[1])+str(coord[2]))>=x\
                    or letters.index(coord[0])>=y:    
                coord = input('Enter cordinate to flag : ')
                coord += " "
            flag(user_view,coord)
        elif coord == 'unflag ':
            coord = input("Enter a cordinate to unflag: ")
            while len(coord) < 2 or coord[0].isnumeric() == True \
                or coord[1].isalpha() == True or int(str(coord[1])+str(coord[2]))>=x\
                    or letters.index(coord[0])>=y:
                coord = input('Enter a coordinate to unflag: ')
            unflag(user_view,coord)
        # else dig in specified spot
        else:
            while len(coord) < 2 or coord[0].isnumeric() == True \
                or coord[1].isalpha() == True or int(str(coord[1])+str(coord[2]))>=x\
                    or letters.index(coord[0])>=y:
                coord = input('Enter a cordinate pair: ')
                coord += " "
            print_grid(dig(grid, coord,user_view))
    # when game is no longer ongoing print returned string
    print(determine_game_status(grid,user_view))

# runs game
play_game()
