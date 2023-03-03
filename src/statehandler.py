from .plate import Board

class BaseStateHandler:
    def __init__(self, board: Board) -> None:
        self.board = board
    
    def next_iteration(self) -> Board:
        self.board.array = self.next_array()
        return self.board
    
    def next_array(self) -> list[list[int]]:
        raise NotImplementedError()
    
    def after_iterations(self, n: int) -> Board:
        for _ in range(n):
            self.next_iteration()
        return self.board
    
class ConwaysStateHandler(BaseStateHandler):
    def next_array(self):
        board = self.board
        new_array = board.new_array()
        for i, line in enumerate(board.array):
            for j, cell in enumerate(line):
                neighbours = len(board.neighborhood(i, j))
                case = int(cell or (neighbours == 3)) if neighbours in (2, 3) else 0
                new_array[i][j] = case
        return new_array
    
# class AlternateStateHandler(BaseStateHandler):
#     ...