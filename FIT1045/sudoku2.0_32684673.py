"""
Template for Programming Assignment FIT1045 - S2 2021
Sudoku

Version 2 (2021-08-13)

Sudoku boards partially retrieved from
- https://puzzlemadness.co.uk
- https://sudokudragon.com
"""

########### Sudoku boards ##############################

small = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

small2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

big = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 8, 9, 0, 0, 0],
       [7, 8, 0, 0, 0, 0, 0, 5, 6],
       [0, 2, 0, 3, 6, 0, 8, 0, 0],
       [0, 0, 5, 0, 0, 7, 0, 1, 0],
       [8, 0, 0, 2, 0, 0, 0, 0, 5],
       [0, 0, 1, 6, 4, 0, 9, 7, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 2]]

big2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

big3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

big4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

giant = [[ 0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [ 7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [ 1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [ 0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [ 8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [ 5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [ 0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [ 2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [ 0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [ 0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [ 0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [ 0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

giant2 = [[ 0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [ 1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [ 0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [ 0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [ 4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [ 3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [ 0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [ 9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [ 0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [ 8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [ 0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

giant3 = [[ 0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [ 0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [ 0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [ 3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [ 0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [ 6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [ 0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [ 0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [ 0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [ 1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [ 0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [ 0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]

sudokus = [[], [], [small, small2], [big, big2, big3, big4], [giant, giant2, giant3]]

########### Module functions ###########################
import copy
import math
def print_board(board):


        

    """
    Prints a given board to the console in a way that aligns the content of columns and makes
    the subgrids visible.

    Input : a Sudoku board (board) of size 4x4, 9x9, or 16x16
    Effect: prints the board to the console 

    For example:

    >>> print_board(small2)
    -------
    |  |1 |
    |4 |  |
    -------
    |  | 2|
    | 3|  |
    -------
    >>> print_board(big)
    -------------
    |   |   |   |
    |4  |789|   |
    |78 |   | 56|
    -------------
    | 2 |36 |8  |
    |  5|  7| 1 |
    |8  |2  |  5|
    -------------
    |  1|64 |97 |
    |   |9  |   |
    |   | 3 |  2|
    -------------
    >>> print_board(giant2)
    ---------------------
    | 5  | 4 8| 6  |  9G|
    |1   |   D|4  7|F 8 |
    |D   | 73 |   9|5A  |
    | BCF|A   |  5 |34 D|
    ---------------------
    |F 13|  72|    | 5  |
    |   C| 3 5| B E|   9|
    |47  |    |C FG|    |
    |    |E F |69  |  C |
    ---------------------
    |3 F4| DE |   1|  78|
    |    |    |  9A|    |
    |B GA|    | 7  | 35 |
    |  D |    |E GF| 9 1|
    ---------------------
    |9 2 | E 4|8   |    |
    | E  |   A|9 3 |  17|
    |8   |G  1|2EB4|   3|
    |   1|  5 | G 6| C  |
    ---------------------
    """
    New_lst=copy.deepcopy(board)#deepcoping is to avoid to change the original table cause of the usage of other function
    for x in range (len(board)):
        for y in range (len(board)):
            if board == small or board == small2 or board == big or board==big2 or board==big3 or board == big4:
                if New_lst[x][y]==0: #changing the element inside into a space for printing
                    New_lst[x][y]=' '
                else:
                    New_lst[x][y]=str(New_lst[x][y])#saving in format string is to join up a table to print
            # changing 10~16 to A~G
            else:
                if New_lst[x][y]==0:
                    New_lst[x][y]=' '
                elif New_lst[x][y]==10:
                    New_lst[x][y]='A'
                elif New_lst[x][y]==11:
                    New_lst[x][y]='B'
                elif New_lst[x][y]==12:
                    New_lst[x][y]='C'
                elif New_lst[x][y]==13:
                    New_lst[x][y]='D'
                elif New_lst[x][y]==14:
                    New_lst[x][y]='E'
                elif New_lst[x][y]==15:
                    New_lst[x][y]='F'
                elif New_lst[x][y]==16:
                    New_lst[x][y]='G'
                else:
                    New_lst[x][y]=str(New_lst[x][y])   
    if len(board)==4:
        for x in range (len(board)):
            Alpha=New_lst[x]
            for k in range (0,len(board)+3,3):#adding | for every 2 number since it is a small table forming |xx|xx| for each list in board
                Alpha.insert(k,'|')
    elif len(board)==9:
        for x in range (len(board)):
            Alpha=New_lst[x]
            for k in range (0,len(board)+5,4):#same as above |xxx|xxx|xxx|
                Alpha.insert(k,'|')
    else:
        for x in range (len(board)):
            Alpha=New_lst[x]
            for k in range (0,len(board)+6,5):#|xxxx|xxxx|xxxx|
                Alpha.insert(k,'|')           
    for x in range (len(board)):
        New_lst[x]=''.join(New_lst[x])#joining the list in boars which has been added |    
    if len(board)==4:
        for k in range (0,len(board)+3,3):
            New_lst.insert(k,'-'*(len(New_lst[-1]))) #adding sufficient number of - which can get from the length of the list
    elif len(board)==9:
        for k in range (0,len(board)+5,4):
            New_lst.insert(k,'-'*(len(New_lst[-1])))
    else:
        for k in range (0,len(board)+6,5):
            New_lst.insert(k,'-'*(len(New_lst[-1])))
    New_lst='\n'.join(New_lst) #join with enter which form the table
    print(New_lst)


def subgrid_values(board, r, c):
                
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that are present in the subgrid of the board related to the
            field (r, c)

    For example:

    >>> subgrid_values(small2, 1, 3)
    [1]
    >>> subgrid_values(big, 4, 5)
    [3, 6, 7, 2]
    >>> subgrid_values(giant2, 4, 5)
    [7, 2, 3, 5, 14, 15]
    """
# In small board it will contain 4 subgrid which will be every 2*2 spaces. For the subgrids in small board it will be
#    index of   
#  row     column 
# (0,1)     (0,1)
# (2,3)     (0,1)
# (0,1)     (2,3)
# (2,3)     (2,3)

    New_lst=[]
    if len(board)==4:
        if r>=2:
            x=[x for x in range (2,4)]# listing the index of row
        else:
            x=[x for x in range (2)]
        if c>=2:
            y=[y for y in range (2,4)]# listing the index of column
        else:
            y=[y for y in range (2)]
        for row in x:
            for column in y:
                if board[row][column]!=0:#creating subgrid by checking if it is larger than 0. If it is larger append to a new list.
                    New_lst.append(board[row][column])
#Same for big board but it contains 9 subgrids which is 3*3 so for the index it will be (0,1,2)(3,4,5)(6,7,8)  
    elif len(board)==9:
        if r <3:
            x=[x for x in range (3)]
        elif r>=6:
            x=[x for x in range (6,9)]
        else:
            x=[x for x in range (3,6)]
        if c<3:
            y=[y for y in range (3)]
        elif c>=6:
            y=[y for y in range (6,9)]
        else:
            y=[y for y in range (3,6)]
        for row in x:
            for column in y:
                if board[row][column]!=0:
                    New_lst.append(board[row][column])
# For giant board the index will be (0,1,2,3)(4,5,6,7)(8,9,10,11)(12,13,14,15)
    else:
        if r<4:
            x=[x for x in range (4)]
        elif r>=12:
            x=[x for x in range(12,16)]
        elif r>=4 and r <8:
            x=[x for x in range (4,8)]
        else:
            x=[x for x in range (8,12)]
        if c<4:
            y=[y for y in range (4)]
        elif c>=12:
            y=[y for y in range (12,16)]
        elif c>=4 and c<8:
            y=[y for y in range (4,8)]
        else:
            y=[y for y in range (8,12)]
        for row in x:
            for column in y:
                if board[row][column]!=0:
                    New_lst.append(board[row][column])
    return New_lst


def options(board, i, j):
    
    """
    Input : Sudoku board (board), row index (r), and column index (c)
    Output: list of all numbers that player is allowed to place on field (r, c),
            i.e., those that are not already present in row r, column c,
            and subgrid related to field (r, c)

    For example:

    >>> options(small2, 0, 0)
    [2, 3]
    >>> options(big, 6, 8)
    [3, 8]
    >>> options(giant2, 1, 5)
    [2, 5, 6, 9, 11, 12, 16]
    """
    New_lst=[] 
    col=[]
    subgrid=subgrid_values(board, i, j)
    for k in range (len(board)):
            pos=board[k][j] #taking the number in the column of the board
            col.append(pos)
    for m in range (1,(len(board)+1)):
        if  board[i][j]==0 or board[i][j]=='*': #checking if the board is 0 or * since later the hint will change the table
                if (m  not in [num for num in board[i]]) and (m not in col) and (m not in subgrid): #checking row column and subgrid for none same numbers
                        New_lst.append(m)
        else :
                return 'This field is occupied.'
    return New_lst


def play(board):
    """
    Input : Sudoku board
    Effect: Allows user to play board via console
    """
    dcboard=copy.deepcopy(board)
    print_board(board)
    rc=[]
    ans=[]
    hintlst=[]
    coor=[]
    while True:
        inp = input().split(' ')
        if len(inp) == 3 and inp[0].isdecimal() and inp[1].isdecimal() and inp[2].isdecimal():
            i = int(inp[0])
            j = int(inp[1])
            x = int(inp[2])
            rc.append(i)
            rc.append(j)
            ans.append(x)
            if x in options(dcboard,i,j):
                dcboard[i][j] = x
                print_board(dcboard)
            else:
                print('Error')
        elif inp[0] == 'u' or inp [0]=='undo':
            if (len(rc))>=2:
                dcboard[rc[-2]][rc[-1]]=0
                rc.pop()
                rc.pop()
                print_board(dcboard)
            else :
                print_board(dcboard)
        elif inp[0]=='r' or inp[0]=='restart' :
                print_board(board)
        elif len(inp)==3 and (inp[0] == 'n' or inp[0] == 'new') and inp[1].isdecimal() and inp[2].isdecimal():
            k = int(inp[1])
            d = int(inp[2])
            if k < len(sudokus) and 0 < d <= len(sudokus[k]):
                board = sudokus[k][d-1]
                dcboard=copy.deepcopy(board)
                print_board(board)
                check_lst=[]
                rc=[]
                ans=[]
            else:
                print('board not found')
        elif inp[0] == 'q' or inp[0] == 'quit':
            return
        elif len(inp)==3 and  (inp[0] == 'o' or inp[0] == 'options')and inp[1].isdecimal() and inp[2].isdecimal():
            r=int(inp[1])
            c=int(inp[2])
            print (options(dcboard,r,c)) 
        elif inp[0]=='h' or inp[0]=='hint':
            for i in range (len(dcboard)):
                for j in range(len(dcboard)):
                    Hint=options(dcboard,i,j)
                    COORDINATE=[i,j]
                if Hint != 'This field is occupied.':
                    hintlst.append(len(Hint))
                    coor.append(COORDINATE)
            ind=hintlst.index(min(hintlst))
            coordinate=coor[ind]
            dcboard[coordinate[0]][coordinate[1]]='*'
            print_board(dcboard)
            print (coordinate)
        elif inp[0]=='i'or inp[0]=='infer':
            print_board(inferred(dcboard))
        elif inp[0]=='s'or inp[0]=='solve':
            solving(dcboard)   
        else:
            print('Invalid input')
        check_lst=[]
        for n in range (len(dcboard)):
            for m in range (len(dcboard)):
                num=dcboard[n][m]
                check_lst.append(num)
        if 0 not in check_lst:
            print ('Congrats.')

########### Functions only relevant for Part II ########

def value_by_single(board, i, j):
    """
    Input : board, row, and column index
    Output: The correct value for field (i, j) in board if it can be inferred as
            either a forward or a backward single; or None otherwise. 
    
    For example:

    >>> value_by_single(small2, 0, 1)
    2
    >>> value_by_single(small2, 0, 0)
    3
    >>> value_by_single(big, 0, 0)
    """
    lstr=[]
    lstc=[]
    lsts=[]
    n = len(board)
    k = round(math.sqrt(n))
    if board[i][j]:
        return board[i][j]
    if len(options(board,i,j))==1:
        return options(board,i,j)[0]
    for num in options(board,i,j):
        for n in range (len(board)):
            if num not in [options(board,i,n)]:
                lstr.append(num)
            if num not in [options(board,n,j)]:
                lstc.append(num)
            ## referenced from subgrid in part 1 assignment solution
        for a in range((i // k) * k, ((i // k) + 1) * k):
            for b in range((j // k) * k, ((j // k) + 1) * k):
                if [a,b]!=[i,j] and options(board,a,b)!='This field is occupied.':
                    for x in options(board,a,b):
                        lsts.append(x)
        if num not in lsts:
            return num
    if all(lstr[0]==n for n in lstr):
            return lstr[0]
    elif all(lstc[0]==n for n in lstc):
            return lstc[0]
    else :
            return None
"""<For this value by single function we will get the value which is only the value taht is suitable in row/column/subgrid if it is we will return the value.
     so we will take if the value if the options return only a value that is length of one which represent that is only one value is suitable in this row/column/subgrid
     if not we will get the whole row/columns/subgrid options then take the only value which is listed down in the seperate list if the value inside the list is the same 
     value then it will return the value as the value by single.>"""

def inferred(board):
    """
    Input : Sudoku board
    Output: new Soduko board with all values field from input board plus
            all values that can be inferred by repeated application of 
            forward and backward single rule

    For example board big can be completely inferred:

    >>> inferred(big) # doctest: +NORMALIZE_WHITESPACE
    [[2, 1, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [1, 2, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]]

    But function doesn't modify input board:

    >>> big # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 7, 8, 9, 0, 0, 0],
     [7, 8, 0, 0, 0, 0, 0, 5, 6],
     [0, 2, 0, 3, 6, 0, 8, 0, 0],
     [0, 0, 5, 0, 0, 7, 0, 1, 0],
     [8, 0, 0, 2, 0, 0, 0, 0, 5], 
     [0, 0, 1, 6, 4, 0, 9, 7, 0],
     [0, 0, 0, 9, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 0, 0, 2]]

    In board big4 there is nothing to infer:
    
    >>> inferred(big4) # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 6, 0, 0, 2, 0, 0],
     [8, 0, 4, 0, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 9, 0, 0, 0], 
     [4, 0, 5, 0, 0, 0, 0, 0, 7],
     [7, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 0, 5, 0, 0, 0, 8],
     [3, 0, 0, 0, 7, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 1, 9, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 6, 0]]

    <In the inferred function will will need to make a copy of board for rewrite the board then we will check for every boxes by using valued by single then recursive this function
    until the board return the same value as the last recursion.>
    """
    cpboard=copy.deepcopy(board)
    for a in range (len(board)):
        for b in range (len(board)):
            if value_by_single(cpboard,a,b)!=None:
                cpboard[a][b]=value_by_single(cpboard,a,b)
               
    if cpboard==board:
        return cpboard
    
    else:
        return inferred(cpboard)

def complete(board):
    lst=[]
    for n in board:
        for m in n:
            lst.append(m)
    if all(lst):
        return True 
def safe(addedboard,x,y,n):
    if n in options(addedboard,x,y):
        return True
    else:
        return False
def solving(board):
    if complete(board):
         print_board(board)
    addedboard=copy.deepcopy(board)
    for x in range(len(addedboard)):
        for y in range(len(addedboard)):
            if addedboard[x][y]==0:
                for n in range (1,len(addedboard)+1):
                    if safe(addedboard,x,y,n):
                        addedboard[x][y]=n
                        solving(addedboard)
                        addedboard[x][y]=0
                return
""" For my backtracking i will use another two function which is two complete the backtracking which is complete which check if it is completed, safe which check if it is
    safe too put the specific number into the box. So in my solving function the base case is if the function complete return TRUE then we will end the solving function, else 
    it will continue backtracking until the first solution appears.

    For the selection strategy, we could start the backtracking by using the smallest posible options in the board then backtrack for the result this will reduce the the backtraking length
    for example if the the backtracking started with two options the main backtrack will be just two instead if u started with the blank with more options it will backtrack to the start 
    then start over until the solution was found.

    For the inference included in the backtracking function if we put inference function inside the function we can shorten the time since we will always replace all the zero in with the values which is 
    the only posible in that space then we can continue backtrack and inference until ther is no options for a blank then we will return back to the board which haven't inference then continue doing this
    until the solution was found. By using this method we can shorthen the total blanks by calling the inference function the length of backtracking will be shorthen. The time complexity will be 
    shorthen as well. So when we always call the inference function after a backtrack we will shorthen the total time of finding the solution.
"""
########### Driver code (executed when running module) #

import doctest
doctest.testmod()

solving(giant2)