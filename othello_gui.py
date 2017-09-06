#Meghana Jain 29185439
#Project 5 - Othello Tkinter GUI

import tkinter
import othello


DEFAULT_FONT = ('Comic Sans MS', 10)
LARGER_FONT = ('Comic Sans MS', 15)


class Dialog_Box:
    def __init__(self):
        '''Creates and sets up the Dialog Box for the initial parts of the game'''
        self.dialog_window = tkinter.Tk()
        self.dialog_window.title("Othello FULL VERSION")
        self.dialog_window.configure(background = 'PaleGreen')
        

        ###ROWS LABEL
        rows_label = tkinter.Label(
            master = self.dialog_window,
            bg = 'PaleGreen',
            text = 'Number of rows (even # between 4 and 16)',
            font = DEFAULT_FONT)

        rows_label.grid(
            row = 0, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        
        
        ###COLUMNS LABEL
        cols_label = tkinter.Label(
            master = self.dialog_window,
            bg = 'PaleGreen',
            text = 'Number of columns (even # between 4 and 16)',
            font = DEFAULT_FONT)

        cols_label.grid(
            row = 1, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        
        ###PLAYER LABEL
        player_label = tkinter.Label(
            master = self.dialog_window,
            bg = 'PaleGreen',
            text = 'Who is the first player? B or W?',
            font = DEFAULT_FONT)

        player_label.grid(
            row = 2, column = 0 , columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)


        ###WINNING CONDITION LABEL
        condition = tkinter.Label(
            master = self.dialog_window,
            bg = 'PaleGreen',
            text = 'Winning Condition (Piece Count)',
            font = DEFAULT_FONT)


        condition.grid(
            row = 4, column = 0, columnspan = 1, padx = 10, pady = 10,
            sticky = tkinter.W)
        
            
        ###ROWS ENTRY

        self.rows_entry = tkinter.Spinbox(master = self.dialog_window,
                                            values = (4, 6, 8, 10, 12, 14, 16))

        self.rows_entry.grid(
            row = 0, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        
        ###COLUMNS ENTRY
        self.cols_entry = tkinter.Spinbox(master = self.dialog_window,
                                            values = (4, 6, 8, 10, 12, 14, 16))
        

        self.cols_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        
        
        ###PLAYER ENTRY

        self.is_checked_black = tkinter.IntVar()
        self.is_checked_white = tkinter.IntVar()
        
        self.player_entry_black = tkinter.Checkbutton(
            master = self.dialog_window,
            width = 2,
            text = "B",
            bg = 'PaleGreen',
            font = DEFAULT_FONT,
            variable = self.is_checked_black)
        

        self.player_entry_black.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)


        self.player_entry_white = tkinter.Checkbutton(
            master = self.dialog_window,
            width = 2,
            text = "W",
            bg = 'PaleGreen',
            font = DEFAULT_FONT,
            variable = self.is_checked_white)
        

        self.player_entry_white.grid(
            row = 2, column = 2, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        


        ###WINNING CONDITIONS

        self.is_checked_most = tkinter.IntVar()
        self.is_checked_least = tkinter.IntVar()
        
        self.condition_most = tkinter.Checkbutton(
            master = self.dialog_window,
            width = 3,
            text = "Most",
            bg = 'PaleGreen',
            font = DEFAULT_FONT,
            variable = self.is_checked_most)


        self.condition_least = tkinter.Checkbutton(
            master = self.dialog_window,
            width = 3,
            text = "Least",
            bg = 'PaleGreen',
            font = DEFAULT_FONT,
            variable = self.is_checked_least)



        self.condition_most.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)
        

        self.condition_least.grid(
            row = 4, column = 2, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        


        ###START GAME/CANCEL
        button_frame = tkinter.Frame(
            master = self.dialog_window,
            bg = 'PaleGreen')

        button_frame.grid(
            row = 6, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.S)


        start = tkinter.Button(
            master = button_frame,
            text = 'Ok',
            font = DEFAULT_FONT,
            command = self.on_start_clicked)

        start.grid(row = 1, column = 0, padx = 10, pady = 10)


        cancel = tkinter.Button(
            master = button_frame,
            text = 'Cancel',
            font = DEFAULT_FONT,
            command = self.on_button_cancel)


        cancel.grid(row = 1, column = 1, padx = 10, pady = 10)


        self.rows = 0
        self.cols = 0
        self.first_player = ""
        self.winning_condition = ""


        self.dialog_window.rowconfigure(0, weight = 1)
        self.dialog_window.rowconfigure(1, weight = 1)
        self.dialog_window.rowconfigure(2, weight = 1)
        self.dialog_window.rowconfigure(3, weight = 1)
        self.dialog_window.rowconfigure(4, weight = 1)
        self.dialog_window.columnconfigure(0, weight = 1)
        self.dialog_window.columnconfigure(1, weight = 1)
        self.dialog_window.columnconfigure(2, weight = 1)




    def on_start_clicked(self) -> None:
        '''When start is clicked, the info in the window is collected and used to create an Othello GUI
        object'''

        self.rows = int(self.rows_entry.get())
        self.cols = int(self.cols_entry.get())

        if self.is_checked_black.get() == 1:
            self.first_player = "B"
        elif self.is_checked_white.get() == 1:
            self.first_player = "W"

        if self.is_checked_most.get() == 1:
            self.winning_condition = ">"
        elif self.is_checked_least.get() == 1:
            self.winning_condition = "<"


        self.dialog_window.destroy()

        game = Play_Othello(self.rows, self.cols, self.first_player,
                            self.winning_condition)

        game.play()

        

        
    def on_button_cancel(self) -> None:
        '''Destroys the window is cancel is clicked'''
        self.dialog_window.destroy()

        
            
    def run(self):
        '''Runs the dialog box'''
        self.dialog_window.mainloop()



##############################################################################################
##############################################################################################
##############################################################################################


class Play_Othello:
    def __init__(self, rows, cols, first_player, winning_condition):
        '''Creates the Othello Game Window'''
        self.rows = rows
        self.cols = cols
        self.first_player = first_player
        self.winning_condition = winning_condition
        self.game_board = []
        self.invalid_moves = []
        
        self.piece_color = ''
        
        self.width = 500
        self.height = 500

        self.col_interval = self.width/self.cols
        self.row_interval = self.height/self.rows

        
        self.display = tkinter.Tk()
        self.display.title("Othello FULL VERSION")
        self.board = tkinter.Canvas(master = self.display,
                                    width = 500, height = 500,
                                    background = 'green')

        self.display.rowconfigure(0, weight = 1)
        self.display.rowconfigure(1, weight = 1)
        self.display.rowconfigure(2, weight = 1)
        self.display.rowconfigure(3, weight = 1)
        self.display.rowconfigure(4, weight = 1)
        self.display.rowconfigure(5, weight = 1)
        self.display.rowconfigure(6, weight = 1)
        self.display.rowconfigure(7, weight = 1)
        self.display.rowconfigure(8, weight = 1)
        self.display.columnconfigure(0, weight = 1)


        self.make_othello_board()

        self.board.bind('<Button-1>', self.get_tile_clicked)
        self.board.bind('<Button-1>', self.on_board_click)
        self.board.bind('<Configure>', self.resize_board)


        self.game = othello.Othello(self.game_board, self.first_player, self.invalid_moves)


        self.board.grid(row = 1, column = 0,
                        sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)

        

        game_tag = tkinter.Label(master = self.display,
                                 text = "Othello Full Version",
                                 font = LARGER_FONT)

        game_tag.grid(row = 0, column = 0,
                      sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)

        
        

        self.turn_name = tkinter.StringVar()
        self.turn_name.set(self.game.turn  + "'s Turn")

        self.turn_tag = tkinter.Label(master = self.display,
                                      textvariable = self.turn_name,
                                      font = LARGER_FONT)

        self.turn_tag.grid(row = 2, column = 0,
                           sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)


        

        frame = tkinter.Frame(master = self.display)

        frame.grid(row = 3, column = 0, 
                   sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)

        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure(0, weight = 1)
        frame.columnconfigure(1, weight = 1)

        

        self.count_white = tkinter.StringVar()
        self.count_black = tkinter.StringVar()

        self.count_black.set("Black: " + str(self.game.count_pieces_black()))
        self.count_white.set("White: " + str(self.game.count_pieces_white()))


        self.white_count = tkinter.Label(master = frame,
                                         textvariable = self.count_white,
                                         font = LARGER_FONT)

        self.white_count.grid(row = 0, column = 0, 
                              sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)
        

        self.black_count = tkinter.Label(master = frame,
                                         textvariable = self.count_black,
                                         font = LARGER_FONT)

        self.black_count.grid(row = 0, column = 1,
                              sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)


        self.place_piece = tkinter.Label(master = self.display,
                                         text = "Use the buttons below to set the piece color, then click on the board to place that piece",
                                         font = DEFAULT_FONT)

        self.place_piece.grid(row = 5, column = 0,
                              sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)
        

        self.black_pieces = tkinter.Button(master = self.display, text = 'Place Black Pieces',
                                           font = DEFAULT_FONT, command = self.draw_black_pieces)

        self.black_pieces.grid(row = 6, column = 0,
                               sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)

        self.white_pieces = tkinter.Button(master = self.display, text = 'Place White Pieces',
                                           font = DEFAULT_FONT, command = self.draw_white_pieces)

        self.white_pieces.grid(row = 7, column = 0,
                               sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)

        self.start_game = tkinter.Button(master = self.display, text = 'Start Game',
                                           font = DEFAULT_FONT, command = self.on_start_click)

        self.start_game.grid(row = 8, column = 0,
                               sticky = tkinter.W + tkinter.N + tkinter.E + tkinter.S)



        

        self.state = tkinter.StringVar()
        self.state.set("")

        self.game_state = tkinter.Label(master = self.display, textvariable = self.state,
                                        font = LARGER_FONT)

        self.game_state.grid(row = 4, column = 0,
                        sticky = tkinter.W + tkinter.E + tkinter.S + tkinter.N)




        


    def make_othello_board(self) -> None:
        '''Makes the 2D list/board for the game logic'''
        
        for row in range(self.rows):
            self.game_board.append([])
            for col in range(self.cols):
                self.game_board[row].append(0)

                

                


    def on_board_click(self, event: tkinter.Event) -> None:
        '''When the board is clicked, an oval is drawn in regards to the size of the space it is placed
        in'''
        row, col = self.get_tile_clicked(event)

        width = self.board.winfo_width()
        height = self.board.winfo_height()

        col_interval = width/self.cols
        row_interval = height/self.rows
        
        if self.piece_color == "B" and self.game.board[row - 1][col - 1] == othello.EMPTY:

            
            self.board.create_oval((col - 1) * col_interval,
                                   (row - 1)* row_interval,
                                   col * col_interval,
                                   row * row_interval,
                                   fill = 'black')


            self.game_board[row - 1][col - 1] = othello.BLACK

            self.count_black.set("Black: " + str(self.game.count_pieces_black()))




        elif self.piece_color == "W" and self.game.board[row - 1][col - 1] == othello.EMPTY:
            
            self.board.create_oval((col - 1) * col_interval,
                                   (row - 1)* row_interval,
                                   col * col_interval,
                                   row * row_interval,
                                   fill = 'white')

            self.game_board[row - 1][col - 1] = othello.WHITE

            self.count_white.set("White: " + str(self.game.count_pieces_white()))
            



    
            
            
    def draw_grid(self) -> None:
        '''Given a width and height of a canvas, draws the lines to assemble the spaces of the board'''

        width = self.board.winfo_width()
        height = self.board.winfo_height()

        col_interval = width/self.cols
        row_interval = height/self.rows
        
        for i in range(self.cols + 1):
            #i += 1
            self.board.create_line(i * col_interval, 0, i * col_interval, height)

        for j in range(self.rows + 1):
            #j += 1
            self.board.create_line(0, j * row_interval, width, j * row_interval)

            

            
            


    def get_tile_clicked(self, event: tkinter.Event) -> tuple:
        '''Given a width and height of a canvas, gets the click point in terms of a board space,
        row and col'''

        width = self.board.winfo_width()
        height = self.board.winfo_height()

        col_interval = width/self.cols
        row_interval = height/self.rows
        
        for col in range(self.cols + 1):
            for row in range(self.rows + 1):
                if event.x < col * col_interval and event.y < row * row_interval:
                    return row, col
                else:
                    continue
                
    
                


    def redraw_board(self) -> None:
        '''Given a width and height of the canvas, the spaces and current pieces
        are drawn on the canvas'''

        width = self.board.winfo_width()
        height = self.board.winfo_height()

        col_interval = width/self.cols
        row_interval = height/self.rows

        self.board.delete(tkinter.ALL)
        self.draw_grid()
        
        for row in range(len(self.game.board)):
            for col in range(len(self.game.board[row])):
                if self.game.board[row][col] == othello.BLACK:
                    self.board.create_oval((col + 1) * col_interval,
                                   (row + 1)* row_interval,
                                   col * col_interval,
                                   row * row_interval,
                                   fill = 'black')

                    
                elif self.game.board[row][col] == othello.WHITE:
                    self.board.create_oval((col + 1) * col_interval,
                                   (row + 1)* row_interval,
                                   col * col_interval,
                                   row * row_interval,
                                   fill = 'white')


                    


    def resize_board(self, event: tkinter.Event) -> None:
        '''Redraws the board when it is resized'''
        self.board.delete(tkinter.ALL)
        self.redraw_board()

                    


                

    def draw_white_pieces(self) -> None:
        '''Sets the piece color to white'''
        self.piece_color = "W"

    def draw_black_pieces(self) -> None:
        '''Sets the piece color to black'''
        self.piece_color = "B"
        
            




    def on_start_click(self) -> None:
        '''When the Start Game Button is clicked, the buttons in the window are destroyed and button-1
        is bound to the first player's turn'''
        
        self.start_game.destroy()
        self.black_pieces.destroy()
        self.white_pieces.destroy()
        self.place_piece.destroy()
        
        self.piece_color = self.first_player

        self.board.unbind('<Button-1>')


        if self.game.turn == "B":
            self.board.bind('<Button-1>', self.black_turn)
        elif self.game.turn == "W":
            self.board.bind('<Button-1>', self.white_turn)


            
        

  
    def black_turn(self, event: tkinter.Event) -> None:
        '''Executes the black player's turn through the game logic of othello.py'''

        if self.game.both_turn_invalid():
            if self.game.check_valid_moves():

                row, col = self.get_tile_clicked(event)


                if self.game.determine_validity_overall(row, col):
                    if self.game.board[row - 1][col - 1] == othello.EMPTY:

                        self.state.set("")

                        self.on_board_click(event)

                        self.game.board[row - 1][col - 1] = othello.BLACK
                        self.game.flip_pieces(self.game.value_of_player(), row, col)
                        self.redraw_board()
                        self.count_black.set("Black: " + str(self.game.count_pieces_black()))
                        self.count_white.set("White: " + str(self.game.count_pieces_white()))

                        if self.game.determine_winner():
                            self.state.set(self.game.declare_winner(self.winning_condition))
                            self.board.unbind('<Button-1>')

                        else:
                            self.game.turn = self.game.opposite_turn()
                            self.turn_name.set(self.game.turn + "'s Turn")
                            self.piece_color = self.game.turn
                            self.board.unbind('<Button-1>')
                            self.board.bind('<Button-1>', self.white_turn)
                            

                    else:
                        self.state.set("INVALID")

                else:
                    self.state.set("INVALID")


            else:
                self.board.unbind('<Button-1>')
                self.game.turn = self.game.opposite_turn()
                self.state.set("BLACK PASSES -> WHITE TURN")
                self.turn_name.set(self.game.turn + "'s Turn")
                self.piece_color = self.game.turn
                self.board.bind('<Button-1>', self.white_turn)

        else:
            self.state.set("NO VALID MOVES LEFT")
            self.state.set(self.game.declare_winner(self.winning_condition))
            self.board.unbind('<Button-1>')




                


    def white_turn(self, event: tkinter.Event) -> None:
        '''Executes the white player's turn through the game logic of othello.py'''

        if self.game.both_turn_invalid():
            if self.game.check_valid_moves():

                row, col = self.get_tile_clicked(event)

                if self.game.determine_validity_overall(row, col):
                    if self.game.board[row - 1][col - 1] == othello.EMPTY:

                        self.state.set("")

                        self.on_board_click(event)

                        self.game.board[row - 1][col - 1] = othello.WHITE
                        self.game.flip_pieces(self.game.value_of_player(), row, col)
                        self.redraw_board()
                        self.count_black.set("Black: " + str(self.game.count_pieces_black()))
                        self.count_white.set("White: " + str(self.game.count_pieces_white()))

                        if self.game.determine_winner():
                            self.state.set(self.game.declare_winner(self.winning_condition))
                            self.board.unbind('<Button-1>')

                        else:
                            self.game.turn = self.game.opposite_turn()
                            self.turn_name.set(self.game.turn + "'s Turn")
                            self.piece_color = self.game.turn
                            self.board.unbind('<Button-1>')
                            self.board.bind('<Button-1>', self.black_turn)

                    else:
                        self.state.set("INVALID")

                else:
                    self.state.set("INVALID")

            else:
                self.board.unbind('<Button-1>')
                self.game.turn = self.game.opposite_turn()
                self.state.set("WHITE PASSES -> BLACK TURN")
                self.turn_name.set(self.game.turn + "'s Turn")
                self.piece_color = self.game.turn
                self.board.bind('<Button-1>', self.black_turn)

        else:
            self.state.set("NO VALID MOVES LEFT")
            self.state.set(self.game.declare_winner(self.winning_condition))
            self.board.unbind('<Button-1>')



    
        

    def play(self) -> None:
        '''Runs the Othello tkinter Game'''
        self.display.mainloop()


if __name__ == '__main__':
    Dialog_Box().run
