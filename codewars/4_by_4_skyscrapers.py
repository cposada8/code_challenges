import numpy as np
import random

class Individual:
    def __init__(self, vector):
        self.vector = vector
        self.matrix = vector2matrix(self.vector)
        self.get_score()

    def get_score(self):
        score, r_score, c_score = score_solution(self.matrix)
        self.score = score
        self.r_score = r_score
        self.c_score = c_score
        

def get_col_items(board, col):
    items = [row[col] for row in board]
    return items


def rand_int_list(start, end, num):
    rand_list = []
    for _ in range(num):
        rand_list.append(random.randint(start, end))
    return rand_list


def create_random_solution():
    # solution for a 4x4 matrix
    n = 4
    matrix = []
    for _ in range(n):
        row = rand_int_list(1, 4, n)
        matrix.append(row)
    return matrix


def is_valid_list(row_col):
    # this function returns True if the 4 numbers
    # of the input are different between them
    n = 4
    if len(set(row_col)) == n:
        return True
    return False


def is_valid_matrix(solution):
    # validates that every row and column contain diferent numbers
    
    # 1. validate rows:
    for row in solution:
        if not is_valid_list(row):
            print("row invalid")
            return False
            
    # 2. validate columns:
    for i in range(4):
        col = get_col_items(solution, i)
        if not is_valid_list(col):
            print("col invalid")
            return False
    
    return True
 

def validate_solution(solution, clues):
    # the solution must contain different numbers on each row
    # and column, and must acomplish the clues
    
    # 1. validate matrix
    if not is_valid_matrix(solution):
        print("invalid matrix")
        return False
        
    # 2. validate clues
    pass
    
    return True
    
def score_solution(solution, clues = []):
    """
    this function will give points to a solution
    It will give points for every row, and column
    that has no repeated numbers.
    """
    n = 4
    row_score = 0
    col_score = 0
    
    # score of rows
    for row in solution:
        if is_valid_list(row):
            row_score += 1
    
    # score of columns
    for i in range(n):
        col = get_col_items(solution, i)
        if is_valid_list(col):
            col_score += 1
    total_score = row_score+col_score
    return total_score, row_score, col_score

def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])


def vector2matrix(vector):
    # this function takes a vector of 16 positions
    # and transforms it into a matrix (list o lists)
    # of 4x4
    n = 4
    matrix = []
    
    for _ in range(n):
        row = vector[:n]
        matrix.append(row)
        vector = vector[n:]
    return matrix


def matrix2vector(matrix):
    # this functions takes a matrix and return a vector. 
    # its like a flatten function
    vector = [elem for row in matrix for elem in row]
    return vector


def generate_population(num):
    # this function creates the population for the genetic algorithm
    # it will create 'num' individuals from that population
    indiv_len = 16
    start = 1
    end = 4

    population = []
    for _ in range(num):
        vector = rand_int_list(start, end, indiv_len)
        indiv = Individual(vector)
        population.append(indiv)
    
    return population

def copulate_indiv(indiv1, indiv2):
    # this function generates the childs of 2 individuals
    n = len(indiv1.vector)
    vector1 = indiv1.vector[:n//2] + indiv2.vector[n//2:]
    vector2 = indiv2.vector[:n//2] + indiv1.vector[n//2:]
    
    vector3 = [] # gens intercalated
    vector4 = [] # gens intercalated
    for i in range(n):
        if i%2==0:
            vector3.append(indiv1.vector[i])
            vector4.append(indiv2.vector[i])
        else:
            vector3.append(indiv2.vector[i])
            vector4.append(indiv1.vector[i])

    vector5 = random.choices(indiv1.vector+indiv2.vector, k=n) # totally random gens
    vector6 = random.choices(indiv1.vector+indiv2.vector, k=n) # totally random gens

    child1 = Individual(vector1)
    child2 = Individual(vector2)
    child3 = Individual(vector3)
    child4 = Individual(vector4)
    child5 = Individual(vector5)
    child6 = Individual(vector6)
    


    return child1, child2, child3, child4, child5, child6

def solve_puzzle (clues):
    # solution = ( (1, 2, 3, 4), (2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3) )
    # print(is_valid_matrix(solution))

    # rand_sol = create_random_solution()
    # print(rand_sol)
    # print_matrix(rand_sol)
    # print("is valid?", validate_solution(rand_sol, clues))
    # print("score", score_solution(rand_sol, clues))



    print("experiments with population")
    
    population = generate_population(200)

    # sort the population
    population.sort(key=lambda x: x.score, reverse=True)

    max_population = 800
    num_generations = 100
    for generation in range(num_generations):
        # generate new generation
        
        next_gen = []
        num_copulators = 100 # num of indivituals that will copulate
        for i in range(0, num_copulators, 2):
            ind1 = population[i]
            ind2 = population[i+1]
            chld1, chld2, chld3, chld4, chld5, chld6 = copulate_indiv(ind1, ind2)
            next_gen.append(chld1)
            next_gen.append(chld2)
            next_gen.append(chld3)
            next_gen.append(chld4)
            next_gen.append(chld5)
            next_gen.append(chld6)
        
        population = population + next_gen

        # kill the worst
        population.sort(key=lambda x: x.score, reverse=True)
        population = population[:max_population]

        # print the best of the generation
        if generation%10 ==0:
            print("best of gen", generation)
            print_matrix(population[0].matrix)
            print("score:", population[0].score)
    

    # for i, indiv in enumerate(population):
    #     print("indivial", i)
    #     print_matrix(indiv.matrix)
    #     print("score", indiv.score)

    return ( (1, 2, 3, 4), (2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3) )


if __name__ == "__main__":
    solve_puzzle("")
