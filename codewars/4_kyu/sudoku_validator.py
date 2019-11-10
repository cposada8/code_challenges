# https://www.codewars.com/kata/sudoku-solution-validator/train/python/5dc439f102aae40020ae2633

def get_row_items(board, row):
    return board[row]
    
def get_col_items(board, col):
    items = [row[col] for row in board]
    return items
    
def validate_list(row_col):
    # this function validates if a row or column of 9 numbers contains all the numbers between 1 and 9
    num_dif = len(set(row_col))
    if num_dif == 9:
        return True
    else:
        return False

def contain_zeroes(board):
    # this function returns true if board contains zeroes
    if any(0 in row for row in board):
        return True
    return False
    
def validate_3x3(square):
    elems = [elem for row in square for elem in row]
    return validate_list(elems)

def sub_set(board, row_ini, row_end, col_ini, col_end):
    sub_set = []
    for i in range(row_ini, row_end):
        # select all the rows
        whole_row = board[i]
        row = whole_row[col_ini:col_end]
        sub_set.append(row)
    return sub_set



def validSolution(board):
    # validate zeroes
    if contain_zeroes(board):
        return False
    
    # validate rows
    for i in range(9):
        actual_row = get_row_items(board, i)
        valid = validate_list(actual_row)
        if not valid:
            return False
          
    # validate cols
    for i in range(9):
        actual_col = get_col_items(board, i)
        valid = validate_list(actual_col)
        if not valid:
            return False 
            
    # validate 3x3 subsets
    for i in range(3):
        for j in range(3):
            sub_3x3 = sub_set(board, 3*i, 3*i+3, 3*j, 3*j+3)
            valid_square = validate_3x3(sub_3x3)
            if not valid_square:
                return False

    return True
    
    
    