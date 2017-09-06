#/Users/JediPak 
# Project 3 - Calcudoku Solver
#
# Name: Jedi Pak
# Instructor: Workman
#

# all True/False except get_cages!

def check_valid(puzzle, cages):
   if check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle):
      return True
   else:
      return False

## puzzle is the position of the cage parts

def check_cages_valid(puzzle, cages):
   valid = False
   for lists in cages:
      positionsListString=lists[2:]			# []<---DOES!!!; Does this always return a string???
      positionsListInt=[int(n) for n in positionsListString]
      sum=0
      for i in positionsListInt:
         row=i//5
         col=i%5
         value=puzzle[row][col]
         zero=value==0
         sum+=value
            
      if sum==lists[0] and zero==False or sum<lists[0] and zero==True:		#no zeros  
         valid =  True
      else:
         return False
   return valid
   
         

'''
def check_cages_valid(puzzle, cages): # more than one cage... how do you split them up wo a specifc numerical amount?!
   for list in cages:
      value=get_value(list,puzzle)
      if value <= list[2]:
         return True
      else:
         return False
   ## checks to see that all other cages (the non-complete ones) add up to a value less than the required sum.

cageOrder= [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

def get_value2(single_cage,puzzle):
   sum=0
   s

def get_value(single_cage,puzzle):                    # wrote this 
   sum=0
   for n in single_cage[3:]:
      if 0<=n<=4:
         value=puzzle[0][n]
         return value
      elif 5<=n<=9:
         value=puzzle[1][n-5]
         return value
      elif 10<=n<=14:
         value=puzzle[2][n-10]
         return value
      elif 15<=n<=19:
         value=puzzle[3][n-15]
         return value
      elif 20<=n<-24:
         value=puzzle[4][n-20]
         return value
      sum+=value
'''



def check_columns_valid(puzzle):
   for col in range(len(puzzle[0])):  # this goes to row zero and counts how many potential columns there will be, assuming its square 
      seen=[]
      for row in puzzle:		## no need to do this! --->how do you make it puzzle[:,columns]
         value=row[col]
         if value in seen and value !=0:
            return False
         seen.append(value)
   return True


def check_rows_valid(puzzle):    #puzzle as in the row of puzzles
   for row in puzzle: 			# without range in here it will treat "row" as a LIST not an integer
      for number in range(len(row)): # limit is 5-1
         #puzzle[row][number]
         for chosen_one in range(number+1, len(row)):  
            #puzzle[row][chosen_one]
            if row[number] == row[chosen_one] and row[number]!=0:
               return False
   return True
          

# returns the list of cages (each cage is a list)

def get_cages():		       	# need to return a LIST OF LIST!!!
   cageAmount=int(input("Number of cages: "))
   cagesList=[]
   for n in range(cageAmount):
      cages=input("Cage number %d: "%n).split()		# REMEBER THIS IS A LIST OF LIST OF STRING!!!
      cages=[int(n) for n in cages]							# is there way to convert lists ALL into a int
      cagesList.append(cages)    
   return cagesList




"""

## cages can't have same value inside?
def check_cage(puzzle,cage):
   sum=0
   complete true or FAls
   r:
   c:0




"""
