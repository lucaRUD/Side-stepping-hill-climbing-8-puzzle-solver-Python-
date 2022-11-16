'''
Solution of 8 Puzzle Problem
Heuristic function : min(h1,h2)
Hill Climbing with side-stepping
'''
import random
from copy import deepcopy

initial_state = [
    # [0, 3, 2],
    # [1, 4, 6],
    # [7, 8, 5]

    [1, 3, 2],
    [0, 4, 6],
    [7, 8, 5]

    # [0, 2, 4],
    # [1, 3, 6],
    # [7, 8, 5]

    # [2, 0, 3],
    # [1, 6, 4],
    # [7, 8, 5]
]

# 0 is considered empty space

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Store the previously visited states to avoid infinite loops
state_history = []

INF = 9999


def manhattan(current_state):
    "Function to find the Manhattan distance"

    total_distance = 0

    for i in range(len(current_state)):
        for j in range(len(current_state[i])):

            # Calculate position in current state
            cur_pos = (i * 3) + j + 1

            if current_state[i][j] == 0:
                continue

            for k in range(len(goal_state)):
                for l in range(len(goal_state[k])):

                    if current_state[i][j] == goal_state[k][l]:

                        # Calculate position in goal state
                        goal_pos = (k * 3) + l + 1

                        abs_diff = abs(goal_pos - cur_pos)

                        if abs_diff >= 3:
                            total_distance += int(abs_diff / 3) + abs_diff % 3
                        else:
                            total_distance += abs_diff

    return total_distance


def misplacedTiles(current_state):
    # function to find misplaced tiles number
    misplace = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            # make sure we don't check blank
            if (current_state[i][j] != 0):
                # if it's not at it's proper place, it's misplaced
                if current_state[i][j] != goal_state[i][j]:
                    misplace += 1

    return misplace

def heuristicValue(current_state):
    return min(misplacedTiles(current_state),manhattan(current_state))



def sideStepping(initial_state,possible_moves):
    if initial_state == state_history[len(state_history) - 2] or initial_state == state_history[len(state_history) - 3]:
        print("Before pop:",possible_moves)
        possible_moves.pop(0)
        print("After pop:", possible_moves)
        randomMove = random.choice(possible_moves)
        print("Random move:", randomMove)
        return randomMove
    else:
        return possible_moves[0]

    #

def display():
    'Displays the current state'
    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            tile = initial_state[i][j]
            if tile == 0:
                print(" ", end=" ")
            else:
                print(tile, end=" ")
        print()
    print()


def moves():
    "Function to find all possible moves."
    # Returns integer array of all possible moves
    # 0 - up
    # 1 - right
    # 2 - down
    # 3 - left

    possible_moves = [0, 1, 2, 3]

    # Finding the position of the empty space
    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if initial_state[i][j] == 0:
                if j == 2: possible_moves.remove(1)
                if j == 0: possible_moves.remove(3)
                if i == 0: possible_moves.remove(0)
                if i == 2: possible_moves.remove(2)

                return possible_moves


def explore(move):
    'Function to explore a move and return its heuristic score'
    # Returns INF if the move has already been performed i.e if it exists in state history.

    current_state = deepcopy(initial_state)
    # Deepcopy is used to copy the list by value (recursively) instead of just copying the reference.

    # Finding the position of the empty space
    for i in range(len(current_state)):
        for j in range(len(current_state[i])):
            if current_state[i][j] == 0:
                if move == 0:
                    # Swap it with the element above
                    current_state[i][j] = current_state[i - 1][j]
                    current_state[i - 1][j] = 0
                    if current_state not in state_history:
                        return heuristicValue(current_state)
                    return INF
                elif move == 1:
                    # Swap it with the element right
                    current_state[i][j] = current_state[i][j + 1]
                    current_state[i][j + 1] = 0
                    if current_state not in state_history:
                        return heuristicValue(current_state)
                    return INF
                elif move == 2:
                    # Swap it with the element down
                    current_state[i][j] = current_state[i + 1][j]
                    current_state[i + 1][j] = 0
                    if current_state not in state_history:
                        return heuristicValue(current_state)
                    return INF
                elif move == 3:
                    # Swap it with the element left
                    current_state[i][j] = current_state[i][j - 1]
                    current_state[i][j - 1] = 0
                    if current_state not in state_history:
                        return heuristicValue(current_state)
                    return INF


def execute(move):
    'Function to execute a move passed as arguement'

    state_history.append(deepcopy(initial_state))

    # Finding the position of the empty space
    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if initial_state[i][j] == 0:
                if move == 0:
                    # Swap it with the element above
                    initial_state[i][j] = initial_state[i - 1][j]
                    initial_state[i - 1][j] = 0
                elif move == 1:
                    # Swap it with the element right
                    initial_state[i][j] = initial_state[i][j + 1]
                    initial_state[i][j + 1] = 0
                elif move == 2:
                    # Swap it with the element down
                    initial_state[i][j] = initial_state[i + 1][j]
                    initial_state[i + 1][j] = 0
                elif move == 3:
                    # Swap it with the element left
                    initial_state[i][j] = initial_state[i][j - 1]
                    initial_state[i][j - 1] = 0

                return


def __main__():
    'Solution of 8 Puzzle problem'

    display()
    step=1
    print("Step number: ",step)

    while (initial_state != goal_state):
        step += 1
        possible_moves = moves()
        print(possible_moves,"\n")

        if(step>10):
            best_move=sideStepping(initial_state,possible_moves)
            smallest_score = explore(best_move)
        else:
            best_move = possible_moves[0]
            smallest_score = explore(best_move)

        for move in possible_moves:
            move_score = explore(move)
            if move_score < smallest_score:
                smallest_score = move_score
                best_move = move

        execute(best_move)
        display()
        print("Step number: " ,step)

    print(state_history[len(state_history)-2])



__main__()