def minimax(board, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate_board(board)

    if is_maximizing_player:
        max_eval = float('-inf')
        for move in get_all_legal_moves(board):
            board.make_move(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.undo_move(move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_all_legal_moves(board):
            board.make_move(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.undo_move(move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def evaluate_board(board):
    # Simplified evaluation logic
    return sum(piece.value for piece in board.current_pieces())



def get_all_legal_moves(board):
    # Placeholder for legal move generation
    return board.generate_legal_moves()

def game_over(board):
    # Placeholder for game over check
    return board.is_game_over()


# Example usage
# ai_move = minimax(chess_board, 3, True, float('-inf'), float('inf'))
