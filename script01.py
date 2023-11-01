import time
 
def conflict_checker(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i][0] == board[j][0] or board[i][1] == board[j][1] or abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return True
    return False
 
def generate_children(board, n):
    children = []
    for i in range(n):
        for j in range(n):
            if [i, j] not in board and not conflict_checker(board + [[i, j]]):
                children.append(board + [[i, j]])
    return children
 
def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['[]' for _ in range(n)]
        row[board[i][1]] = 'H'
        print(" ".join(row))
 
def solver(n, algorithm):
    board = []
    stack = [board]
    open_list = []
    closed_list = []
    while True:
        if algorithm == 'DFS':
            current_board = stack.pop()
        elif algorithm == 'BFS':
            current_board = stack.pop(0)
 
        if len(current_board) == n and not conflict_checker(current_board):
            return current_board, open_list, closed_list
        children = generate_children(current_board, n)
        open_list.extend(children)
        closed_list.append(current_board)
 
        stack.extend(children)
        if not stack:
            return None
 
n = 6
 
bfs_start = time.time()
bfs, bfs_open, bfs_closed = solver(n, 'BFS')
bfs_end = time.time()
print_board(bfs)
print("BFS open:", len(bfs_open))
print("BFS closed:", len(bfs_closed))
print("BFS time:", bfs_end - bfs_start)
 
 
bfs_start = time.time()
dfs, dfs_open, dfs_closed = solver(n, 'DFS')
bfs_end = time.time()
print_board(dfs)
print("DFS open:", len(dfs_open))
print("DFS closed:", len(dfs_closed))
print("BFS time:", bfs_end - bfs_start)