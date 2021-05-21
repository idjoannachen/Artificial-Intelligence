from engines import Engine
from copy import deepcopy
import time

class StudentEngine(Engine):
    """ Game engine that you should you as skeleton code for your 
    implementation. """

    alpha_beta = False
    depth_cutoff = 2
    num_generated_nodes = 0
    num_duplicate_nodes = 0
    num_leaf_nodes = 0
    num_rounds = 0
    total_time = 0
    boards_previously_seen = set()
    
    def get_move(self, board, color, move_num=None,
                 time_remaining=None, time_opponent=None):
        """ Wrapper function that chooses either vanilla minimax or 
        alpha-beta. """
        f = self.get_ab_minimax_move if self.alpha_beta else self.get_minimax_move
        return f(board, color, move_num, time_remaining, time_opponent)

    def print_summary(self):
        total_num_nodes = self.num_generated_nodes / self.num_rounds
        total_num_dup_nodes = self.num_duplicate_nodes / self.num_rounds
        avg_branching_factors = self.num_generated_nodes / (self.num_generated_nodes - self.num_leaf_nodes)
        runtime_per_round = self.total_time / self.num_rounds
        print("""\
        Depth D = {}.
        Total # of nodes generated per round = {}.
        Total # of duplicate nodes per round = {}.
        Average branching factors = {}.
        Runtime per round = {}.
        """.format(
            self.depth_cutoff, total_num_nodes, total_num_dup_nodes, avg_branching_factors, runtime_per_round))

    def get_minimax_move(self, board, color, move_num=None,
                         time_remaining=None, time_opponent=None):
        start_time = time.time()

        # Get a list of all legal moves.
        moves = board.get_legal_moves(color)
        self.num_rounds += 1
        # Return the best move according to our utility function minimax_score
        move = max(moves, key=lambda move: self.minimax_score(board, move, color, color, 1))

        end_time = time.time()
        self.total_time += end_time - start_time
        self.print_summary()
        return move

    def check_duplicate(self, board, color_curr):
        states = ''
        for i in range(8):
            for j in range(8):
                states += str(board[i][j])

        states += str(color_curr)

        if states in self.boards_previously_seen:
            self.num_duplicate_nodes += 1

        self.boards_previously_seen.add(states)

    def minimax_score(self, board, move, color_init, color_curr, depth):
        self.num_generated_nodes += 1
        self.check_duplicate(board, color_curr)

        # Create a deepcopy of the board to preserve the state of the actual board
        newboard = deepcopy(board)
        newboard.execute_move(move, color_curr)

        oppo_moves = newboard.get_legal_moves(color_curr * -1)
        if depth == self.depth_cutoff or len(oppo_moves) == 0:
            self.num_leaf_nodes += 1
            return self.calc_utility(newboard, color_init)

        move, score = self.search_best_from_moves(newboard, oppo_moves, color_init, color_curr, depth)

        return score

    def search_best_from_moves(self, board, moves, color_init, color_curr, depth):
        if len(moves) == 0:
            if color_curr == color_init:
                return float('-inf')
            else:
                return float('inf')

        move2score = {}

        for move in moves:
            move2score[move] = self.minimax_score(board, move, color_init, color_curr * -1, depth + 1)

        if color_curr == color_init:
            move = max(moves, key=lambda k: move2score[k])
        else:
            move = min(moves, key=lambda k: move2score[k])

        score = move2score[move]
        return move, score

    def calc_utility(self, board, color):
        piece_difference = len(board.get_squares(color)) - len(board.get_squares(color*-1))
        legal_move_difference =  len(board.get_legal_moves(color)) - len(board.get_legal_moves(color*-1))

        num_my_corners = 0
        num_oppo_corners = 0
        if board[0][0] == color:
            num_my_corners += 1
        elif board[0][0] == color*-1:
            num_oppo_corners += 1

        if board[0][7] == color:
            num_my_corners += 1
        elif board[0][7] == color*-1:
            num_oppo_corners += 1

        if board[7][0] == color:
            num_my_corners += 1
        elif board[7][0] == color*-1:
            num_oppo_corners += 1

        if board[7][7] == color:
            num_my_corners += 1
        elif board[7][7] == color*-1:
            num_oppo_corners += 1

        corner_occupancy_difference = num_my_corners - num_oppo_corners
        return 0.01 * piece_difference + 1 * legal_move_difference + 10 * corner_occupancy_difference

    def get_ab_minimax_move(self, board, color, move_num=None,
                            time_remaining=None, time_opponent=None):
        start_time = time.time()
        # Get a list of all legal moves.
        moves = board.get_legal_moves(color)
        self.num_rounds += 1
        # Return the best move according to our utility function ab_minimax_score
        move = max(moves, key=lambda move: self.ab_minimax_score(board, move, color, color, 1, float('-inf'), float('inf')))
        end_time = time.time()
        self.total_time += end_time - start_time
        self.print_summary()
        return move

    def ab_minimax_score(self, board, move, color_init, color_curr, depth, alpha, beta):
        self.num_generated_nodes += 1
        self.check_duplicate(board, color_curr)

        newboard = deepcopy(board)
        newboard.execute_move(move, color_curr)

        oppo_moves = newboard.get_legal_moves(color_curr * -1)
        if depth == self.depth_cutoff or len(oppo_moves) == 0:
            self.num_leaf_nodes += 1
            return self.calc_utility(newboard, color_init)

        if color_init == color_curr:
            best_score = float("-inf")
            for oppo_move in oppo_moves:
                temp = self.ab_minimax_score(newboard, oppo_move, color_init, color_curr * -1, depth + 1, alpha, beta)
                if temp > best_score:
                    best_score = temp
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float("inf")
            for oppo_move in oppo_moves:
                temp = self.ab_minimax_score(newboard, oppo_move, color_init, color_curr * -1, depth + 1, alpha, beta)
                if temp < best_score:
                    best_score = temp
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score

engine = StudentEngine