import sys # needed to read command line

def readSudoku(textfile):
    f=open(textfile,'r')
    i=0
    j=0
    l=int(len(f.readline()))-1
    f.seek(0)
    print(l)
    matrix=[[0 for x in range(l)] for y in range(l)]
    #print(matrix)
    while True:
        j=0
        char=f.readline()
        for c in char:
            #print(i,j)
            matrix[i][j]=int(c)
            j=j+1
            if j==l:
                i=i+1
                break
        if i==l:
            break
    return matrix

def check_soduku(row,column,number,matrix_board,l):
    check=0
    for i in range(0,l):
        if matrix_board[row][i]==number:
            check=1
    for i in range(0,l):
        if matrix_board[i][column]==number:
            check=1
    
    if l%3 == 0:
        m=3
    if l%2 == 0:
        m=2
    row=row-row%m
    column=column-column%m

    for i in range(0,m):
        for j in range(0,m):
            if matrix_board[row+i][column+j]==number:
                check=1
    if check==1:
        return False
    else:
        return True

class calls:
    number_of_calls=0
c = calls()
def sudoku_solver(matrix,textfile):
    f=open(textfile,"r")
    l=int(len(f.readline()))-1
    c.number_of_calls=c.number_of_calls+1
    break_condition=0
    for i in range(0,l):
        for j in range(0,l):
            if matrix[i][j]==0:
                break_condition=1
                row=i
                column=j
                break
    if break_condition==0:
        print("Naive Backtracking Algorithm Solution: ")
        for i in matrix:
            print(i)
        print("Amount of Recursions")
        print(c.number_of_calls)
        exit(0)

    #print("hello")
    for i in range(0,10):
        if check_soduku(row,column,i,matrix,l):
            matrix[row][column]=i
            if sudoku_solver(matrix,textfile):
                return True
            matrix[row][column]=0
    return False

matrix=readSudoku(sys.argv[1])
sudoku_solver(matrix,sys.argv[1])

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''matrix'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(sudoku_solver)