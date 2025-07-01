def relationship_status(from_member, to_member, social_graph):
    first_case = to_member in social_graph[from_member]["following"]
    second_case = from_member in social_graph[to_member]["following"]
    if first_case and second_case:
        return("friends")
    elif first_case:
        return("follower")
    elif secondcase:
        return("followed by")
    else:
        return("no relationship")
    
def tic_tac_toe(board):
    first_case = 0
    board_size = len(board)

    for i in range(board_size):
        first_case = 0
        for second_case in range(board_size - 1):
            if board[i][second_case] == board[i][second_case + 1] and board[i][second_case] != "":
                first_case += 1
            else:
                break
        if first_case == board_size - 1:
            return board[i][0]

    for i in range(board_size):
        first_case = 0
        for second_case in range(board_size - 1):
            if board[second_case][i] == board[second_case + 1][i] and board[second_case][i] != "":
                first_case += 1
            else:
                break
        if first_case == board_size - 1:
            return board[0][i]

    first_case = 0
    for i in range(board_size - 1):
        if board[i][i] == board[i + 1][i + 1] and board[i][i] != "":
            first_case += 1
        else:
            break
    if first_case == board_size - 1:
        return board[0][0]

    first_case = 0
    for i in range(board_size - 1):
        if board[i][board_size - 1 - i] == board[i + 1][board_size - 2 - i] and board[i][board_size - 1 - i] != "":
            first_case += 1
        else:
            break
    if first_case == board_size - 1:
        return board[0][board_size - 1]

    return "NO WINNER"

def eta(stop_one, stop_two, map):
    total_time = 0
    stop = stop_one

    while stop != stop_two:
        for leg in map:
            if leg[0] == stop:
                total_time += map[leg]['travel_time_mins']
                stop = leg[1]
                break

    return total_time