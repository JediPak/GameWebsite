#
# Project 3 - Calcudoku Solver
#
# Name: Jedi Pak
# Instructor: Workman
#

from solverFuncs import *

## you will be writing a solver for 5x5 Calcudoku puzzles##

cageOrderW = [[0,  1,  2,  3,  4],
              [5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19],
              [20, 21, 22, 23, 24]]

cageOrder=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

puzzle = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

def main(puzzle,cages):
   row=col=checks=backtracks=0
   while row<5:
      puzzle[row][col]+=1
      result=check_valid(puzzle,cages)
      checks+=1
      if result==True:
         if col<4:
            col+=1
         elif col==4:
            row+=1
            col=0
      else:
         while puzzle[row][col]==5:
            puzzle[row][col]=0
            if col!=0:
               col-=1
            else:
               row-=1
               col=4
            backtracks+=1
     
 
   print("\n---Solution---\n")
   string1="\n".join(["".join([str(j) + " " for j in i]) for i in puzzle])

   print (string1)

   #print(string1[0])            # NEED TO JOIN THE LIST TOGETHER WITH JUST A SINGLE SPACE IN BETWEEN
   #print(string1[1])
   #print(string1[2])
   #print(string1[3])
   #print(string1[4])

   print("\nchecks: %d backtracks: %d"%(checks, backtracks))
                                # NEED TO HAVE A SEPERATE LINE FOR EVERY PUZZLE LINE
#############################################################################################################################################################
#def main1(puzzle,cages):
#   row=0
#   col=0
#   while row<5:
#   backtracks=0
#   checks=0
#   i=0
#
#   while i < 25:
#      result=validating(i,puzzle, cages)
#      checks+=1
#      row=i//5
#
#      col=i%5
#         movingForward(row,col,puzzle,result):
#      moving(row,col,puzzle,result)
#
#   print("\n--Solution--\n")
#
#   string=[i for i in puzzle]
#   string1=[" ".join(str(i)) for i in string]
#
#   print(string1[0])            # NEED TO JOIN THE LIST TOGETHER WITH JUST A SINGLE SPACE IN BETWEEN
#   print(string1[1])
#   print(string1[2])
#   print(string1[3])
#   print(string1[4])
#
#   print("\nchecks: %d backtracks: %d"%(checks, backtracks))
#                                # NEED TO HAVE A SEPERATE LINE FOR EVERY PUZZLE LINE
#
#
#
#def cells(puzzle,cages):
#   backtracks=0
#   checks=0
#
#
#def validating(i,puzzle,cages):
#      row=i//5
#      col=i%5
#      result=check_valid(puzzle,cages)
#      return result 
#
#def movingForward(row,col,puzzle,result):
#   #forward   
#   if puzzle[row][col]<5 and result==False:
#      puzzle[row][col]+=1            # for i in row ... then... i=1 wont make it permanent!!!
#      i+=1
#      #return i
#      #break
#def movingBackward(row,col,puzzle,result):
#   #backward
#   elif puzzle[row][col]==5 and result==False:
#      #if col==0:
#      puzzle[row][col]=0
#      i-=1 
#      backtracks+=1
#      #return i backtrackers
#      #break      #
#def moveBackward(row,col,puzzle):
#      resu
#
#      print("i value")
#      print(i)
#
#      while puzzle[row][col]<5 and result==True:
#         puzzle[row][col]+=1  		# for i in row ... then... i=1 wont make it permanent!!!
#         print(puzzle)
#
#         result=check_valid(puzzle,cages)
#
#         print(result)
#
#         checks+=1
#         if result==True:
#
#            print("Returning True")
#
#            i+=1
#            print(i)
#            break
#         elif result==False:
#
#            print("Returning False")
#
#            if puzzle[row][col]==5:
#               puzzle[row][col]=0
#               i-=1
#               print(i)
#               backtracks+=1
#               break			   # this doesn't end it right?
#
#   print("\n--Solution--\n")
#   
#   string=[i for i in puzzle]
#   string1=[" ".join(str(i)) for i in string]
#
#   print(string1[0]) 		# NEED TO JOIN THE LIST TOGETHER WITH JUST A SINGLE SPACE IN BETWEEN
#
#   print(string1[1]) 
#   print(string1[2])    
#   print(string1[3]) 
#   print(string1[4]) 
#
#   print("\nchecks: %d backtracks: %d"%(checks, backtracks))
#				# NEED TO HAVE A SEPERATE LINE FOR EVERY PUZZLE LINE
#

   
cages=get_cages()
main(puzzle,cages)


# i need to make it backtrack the CORRECT way!            
# need to track backtrack              

# how do you make puzzle BACKTRACK?!
##pos=0
##while not done:
##   puzzle[pos]+=1
##   check
##   pos+=1
##
##   puzzle[pos]=0
##   pos-=1

