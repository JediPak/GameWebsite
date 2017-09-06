#Meghana Jain 29185439
#Project 5 - Othello Tkinter GUI


#Meghana Jain 29185439
#Project 4

import sys

EMPTY = 0
BLACK = 1
WHITE = 2

################################################################################
#OTHELLO GAME LOGIC
################################################################################


class InvalidMoveError(Exception):
    pass



class Othello:
    def __init__(self, board, turn, invalid_list: list):
        self.board = board
        self.turn = turn
        self.invalid = invalid_list
        



    def num_rows_cols(self) -> int:
        '''Returns the number of rows and columns in the board'''
        count = 0
        row = len(self.board)
        for row in self.board:
            for col in row:
                count += 1

        return count
        return row





    def find_piece(self, row: int, col: int):
        '''Returns the value of the space at a specific location'''
        return self.board[row - 1][col - 1]



    

    def value_of_player(self):
        '''Returns the player on the current turn'''
        if self.turn == "W":
            return WHITE
        elif self.turn == "B":
            return BLACK



        

    def print_board(self) -> None:
        '''Prints the game board given an Othello object'''
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == EMPTY:
                    print(".", end = " ")
                elif self.board[row][col] == BLACK:
                    print("B", end = " ")
                elif self.board[row][col] == WHITE:
                    print("W", end = " ")
            print()

       






    def print_turn(self) -> None:
        '''Prints out the current turn'''
        print("TURN: ", self.turn)



        


    def count_pieces(self) -> int:
        '''Prints the number of pieces of each color'''
        count_black = 0
        count_white = 0

        for row in self.board:
            for col in row:
                if col == BLACK:
                    count_black += 1
                elif col == WHITE:
                    count_white += 1

        print("B: ", count_black, "W: ", count_white)

        return count_black
        return count_white




    def count_pieces_black(self) -> int:
        '''Counts the number of black pieces'''
        count_black = 0

        for row in self.board:
            for col in row:
                if col == BLACK:
                    count_black += 1

        return count_black





    def count_pieces_white(self) -> int:
        '''Counts the number of white pieces'''
        count_white = 0

        for row in self.board:
            for col in row:
                if col == WHITE:
                    count_white += 1

        return count_white
                    
                    



    def opposite_turn(self) -> str:
        '''Returns the opposite turn, given the current turn'''
        if self.turn == "B":
            self.turn = "W"
            return self.turn
        elif self.turn == "W":
            self.turn = "B"
            return self.turn


        


    def determine_winner(self) -> bool:
        '''Takes a board and sees if it is full. If so, it returns true, else false'''
        full_rows = 0
        
        for row in self.board:
            if EMPTY not in row:
                full_rows += 1

        if full_rows == len(self.board):
            return True
        else:
            return False


        


    def declare_winner(self, winning_condition: str) -> str:
        '''Counts the number of pieces for each color and checks the values against each
        other given a winning condition'''
        black = 0
        white = 0

        for row in self.board:
            for col in row:
                if col == BLACK:
                    black += 1
                if col == WHITE:
                    white += 1
  
        if winning_condition == ">":
            if black > white:
                return "WINNER: BLACK"
                sys.exit()

            elif black < white:
                return "WINNER: WHITE"
                sys.exit()

            else:
                return "WINNER: NONE"
                sys.exit()
            
        elif winning_condition == "<":
            if black < white:
                return "WINNER: BLACK"
                sys.exit()
            
            elif black > white:
                return "WINNER: WHITE"
                sys.exit()

            else:
                return "WINNER: NONE"
                sys.exit()


        
                    

    def check_valid_moves(self) -> bool:
        '''Checks the whole board for a turn and evaluates whether there are any valid moves
        in the empty spaces'''
        spaces = 0
        invalid_spaces = 0
        
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == EMPTY:
                    spaces += 1
                    if (self.board[row][col] == EMPTY and
                        self.determine_validity_overall(row + 1, col + 1)):
                        continue
                    else:
                        invalid_spaces += 1

        if invalid_spaces == spaces:
            self.invalid.append(self.value_of_player())
            return False
        else:
            return True





    def both_turn_invalid(self) -> bool:
        '''Checks to see if either player has valid moves, and if not, it returns false'''
        count_black = 0
        count_white = 0

        for item in self.invalid:
            if item == WHITE:
                count_white += 1
            elif item == BLACK:
                count_black += 1

        if count_white >= 1 and count_black >= 1:
            return False

        else:
            return True

        
        
        

    def determine_validity_overall(self, row: int, col: int) -> bool:
        '''Determines validity for all directions given a certain space'''
        up, up_pieces = self.determine_validity_up(row, col)
        down, down_pieces = self.determine_validity_down(row, col)
        right, right_pieces = self.determine_validity_right(row, col)
        left, left_pieces = self.determine_validity_left(row, col)
        right_up, right_up_pieces = self.determine_validity_right_up(row, col)
        right_down, right_down_pieces = self.determine_validity_right_down(row, col)
        left_up, left_up_pieces = self.determine_validity_left_up(row, col)
        left_down, left_down_pieces = self.determine_validity_left_down(row, col)
        

        if (not up and not down and not right and not left and not right_up
            and not right_down and not left_up and not left_down):
    
            return False

        else:  
            return True


        


    def flip_pieces(self, current_turn: int, row: int, col: int) -> None:
        '''Flips the pieces for a certain space'''
        up, up_pieces = self.determine_validity_up(row, col)
        down, down_pieces = self.determine_validity_down(row, col)
        right, right_pieces = self.determine_validity_right(row, col)
        left, left_pieces = self.determine_validity_left(row, col)
        right_up, right_up_pieces = self.determine_validity_right_up(row, col)
        right_down, right_down_pieces = self.determine_validity_right_down(row, col)
        left_up, left_up_pieces = self.determine_validity_left_up(row, col)
        left_down, left_down_pieces = self.determine_validity_left_down(row, col)

        
        if len(up_pieces) > 0:    
            for piece in up_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(down_pieces) > 0:    
            for piece in down_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(right_pieces) > 0:    
            for piece in right_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(left_pieces) > 0:    
            for piece in left_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(right_up_pieces) > 0:    
            for piece in right_up_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(left_up_pieces) > 0:    
            for piece in left_up_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(right_down_pieces) > 0:    
            for piece in right_down_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        if len(left_down_pieces) > 0:    
            for piece in left_down_pieces:
                self.board[piece[0]][piece[1]] = current_turn

        
        

    def determine_validity_up(self, row: int, col: int) -> tuple: 
        '''Determines validity in the up direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 2
        pieces = []
        empty_list = []

        while row - index_define != -1:
            
            if (self.board[row - index_define][col - 1] == opposite_turn
                and (row - index_define) - 1 != -1):
                
                pieces.append((row - index_define, col - 1))
                index_define += 1

            elif self.board[row - index_define][col - 1] == current_turn:
                break
                  
            elif self.board[row - index_define][col - 1] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list


        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list




    def determine_validity_down(self, row: int, col: int) -> tuple:
        '''Determines validity in the down direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 1
        pieces = []
        empty_list = []

        while (row - 1) + index_define != len(self.board):
            
            if (self.board[(row - 1) + index_define][col - 1] == opposite_turn
                and ((row - 1) + index_define) + 1 != len(self.board)):
                
                pieces.append(((row - 1) + index_define, col - 1))
                index_define += 1

            elif self.board[(row - 1) + index_define][col - 1] == current_turn:
                break
                
            elif self.board[(row - 1) + index_define][col - 1] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list

        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list




        
    def determine_validity_right(self, row: int, col: int) -> tuple:
        '''Determines validity in the right direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 1
        pieces = []
        empty_list = []

        while ((col - 1) + index_define) != len(self.board[row - 1]):
            
            if (self.board[row - 1][(col - 1) + index_define] == opposite_turn
                and ((col - 1) + index_define) + 1 != len(self.board[row - 1])):
                
                pieces.append((row - 1, (col - 1) + index_define))
                index_define += 1

            elif self.board[row - 1][(col - 1) + index_define] == current_turn:
                break
                
            elif self.board[row - 1][(col - 1) + index_define] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list
            

        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list




    def determine_validity_left(self, row: int, col: int) -> tuple: 
        '''Determines validity in the left direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 2
        pieces = []
        empty_list = []

        while col - index_define != -1:
            
            if (self.board[row - 1][col - index_define] == opposite_turn
                and (col - index_define) - 1 != -1):
                
                pieces.append((row - 1, col - index_define))
                index_define += 1

            elif self.board[row - 1][col - index_define] == current_turn:
                break
                
            elif self.board[row - 1][col - index_define] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list


        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list






    def determine_validity_left_up(self, row: int, col: int) -> tuple:
        '''Determines validity in the left and up direction for a given space'''
        current_turn = self.value_of_player()

        
        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK


        index_define = 2
        pieces = []
        empty_list = []

        while row - index_define != -1 and col - index_define != -1:
            
            if (self.board[row - index_define][col - index_define] == opposite_turn
                and (row - index_define) - 1 != -1
                and (col - index_define) - 1 != -1):

    
                pieces.append((row - index_define, col - index_define))
                index_define += 1

            elif self.board[row - index_define][col - index_define] == current_turn:
                break
                
            elif self.board[row - index_define][col - index_define] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list

        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list



    def determine_validity_right_up(self, row: int, col: int) -> tuple:
        '''Determines validity in the right and up direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 2
        pieces = []
        empty_list = []

        while row - index_define != -1 and ((col - 2) + index_define) != len(self.board[row - 1]):
            
            if (self.board[row - index_define][(col - 2) + index_define] == opposite_turn
                and (row - index_define) - 1 != -1
                and ((col - 2) + index_define) + 1 != len(self.board[row - 1])):
                
                pieces.append((row - index_define, (col - 2) + index_define))
                index_define += 1

            elif self.board[row - index_define][(col - 2) + index_define] == current_turn:
                break
                
            elif self.board[row - index_define][(col - 2) + index_define] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list

        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list





    def determine_validity_left_down(self, row: int, col: int) -> tuple:
        '''Determines validity in the left and down direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 2
        pieces = []
        empty_list = []


        while (row - 2) + index_define != len(self.board) and col - index_define != -1:
            
            if (self.board[(row - 2) + index_define][col - index_define] == opposite_turn
                and ((row - 2) + index_define) + 1 != len(self.board)
                and (col - index_define) - 1 != -1):
                
                pieces.append(((row - 2) + index_define, col - index_define))
                index_define += 1

            elif self.board[(row - 2) + index_define][col - index_define] == current_turn:
                break
                
            elif self.board[(row - 2) + index_define][col - index_define] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list
            
        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list





    def determine_validity_right_down(self, row: int, col: int) -> tuple:
        '''Determines validity in the right and down direction for a given space'''
        current_turn = self.value_of_player()


        if current_turn == BLACK:
            opposite_turn = WHITE
        elif current_turn == WHITE:
            opposite_turn = BLACK

        index_define = 2
        pieces = []
        empty_list = []

        while ((row - 2) + index_define) != len(self.board) and ((col - 2) + index_define) != len(self.board[row - 1]):
            
            if (self.board[(row - 2) + index_define][(col - 2) + index_define] == opposite_turn
                and ((row - 2) + index_define) + 1 != len(self.board)
                and ((col - 2) + index_define) + 1 != len(self.board[row - 1])):

                pieces.append(((row - 2) + index_define, (col - 2) + index_define))
                index_define += 1

            elif self.board[(row - 2) + index_define][(col - 2) + index_define] == current_turn:
                break
                
            elif self.board[(row - 2) + index_define][(col - 2) + index_define] == EMPTY:
                return False, empty_list

            else:
                return False, empty_list
            
        if len(pieces) > 0:
            return True, pieces
        
        else:
            return False, empty_list



    
    def black_turn(self, winning_condition: str):
        '''Executes the black player turn'''
        while True:

            if self.both_turn_invalid():
                if self.check_valid_moves():
                    
                    move = input()
                    row = int(move.split()[0])
                    col = int(move.split()[1])
                    
                    if self.determine_validity_overall(row, col):
                        if self.board[row - 1][col - 1] == EMPTY:
                            
                            print("VALID")
                            self.board[row - 1][col - 1] = BLACK
                            self.flip_pieces(self.value_of_player(), row, col)

                            if self.determine_winner():
                                self.count_pieces()
                                self.print_board()
                                self.declare_winner(winning_condition)

                            else:
                                self.turn = self.opposite_turn()
                                self.count_pieces()
                                self.print_board()
                                self.print_turn()

                                self.white_turn(winning_condition)
                            

                        else:
                            print("INVALID")
                    else:
                        print("INVALID")
                        #raise InvalidMoveError()
                        
                else:
                    print("BLACK PASSES")
                    self.turn = self.opposite_turn()

                    self.count_pieces()
                    self.print_board()
                    self.print_turn()
                    
                    self.white_turn(winning_condition)
                    
                    
            else:
                print("NO VALID MOVES LEFT")
                self.declare_winner(winning_condition)                    





    def white_turn(self, winning_condition: str):
        '''Executes the white player turn'''
        while True:

            if self.both_turn_invalid():
                if self.check_valid_moves():
                    
                    move = input()
                    row = int(move.split()[0])
                    col = int(move.split()[1])
                    
                    if self.determine_validity_overall(row, col):
                        if self.board[row - 1][col - 1] == EMPTY:

                            print("VALID")
                            self.board[row - 1][col - 1] = WHITE
                            self.flip_pieces(self.value_of_player(), row, col)

                            if self.determine_winner():
                                self.count_pieces()
                                self.print_board()
                                self.declare_winner(winning_condition)

                            else:
                                self.turn = self.opposite_turn()
                                self.count_pieces()
                                self.print_board()
                                self.print_turn()

                                self.black_turn(winning_condition)

                        else:
                            print("INVALID")

                    else:
                        print("INVALID")
                        #raise InvalidMoveError()                        
                else:
                    print("WHITE PASSES")
                    self.turn = self.opposite_turn()
                    self.count_pieces()
                    self.print_board()
                    self.print_turn()

                    self.black_turn(winning_condition)
                    
                    
            else:
                print("NO VALID MOVES LEFT")
                self.declare_winner(winning_condition)
