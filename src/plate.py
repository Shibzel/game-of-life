import random

class CaseNeighborhood:
    def __init__(self, area: list[int] = None) -> None:
        self._area = area or []
    
    @property
    def area(self) -> list[int]:
        return self._area
    
    @property
    def neighbors(self) -> int:
        return sum(self.area)
    
    def __len__(self) -> int:
        return self.neighbors
    
    def __str__(self) -> str:
        return str(self.area)

class Board:
    def __init__(self, lines: int = 10, columns: int = 10, randomized: bool = False) -> None:
        super().__init__()
        self.lines = lines
        self.columns = columns
        self.array = []
        self.randomize() if randomized else self.clear()
        
    def __str__(self) -> str:
        string = ""
        for l in self.array:
            string += " ".join("◻️" if c else "◼️" for c in l) + "\n"
        return string
    
    def neighborhood(self, line: int, column: int):
        area = []
        for l in range(line-1, line+2):
            for c in range(column-1, column+2):
                if (line, column) != (l, c) and (0 <= l < self.lines) and (0 <= c < self.columns):
                    area.append(self.array[l][c])
        return CaseNeighborhood(area)
        
    def clear(self) -> None:
        self.array = self.new_array()
        
    def randomize(self, chance: float = 0.3) -> None:
        self.array = [
            [int(random.random() < chance) for _ in range(self.lines)]
            for _ in range(self.columns)
        ]
    
    @classmethod
    def from_array(cls, array: list[list[int]]) -> "Board":
        lines, columns = len(array), len(array[0])
        board = cls(lines=lines, columns=columns)
        board.array = array
        return board
    
    def new_array(self) -> list[list[int]]:
        return [[0]*self.columns for _ in range(self.lines)]
        
if __name__ == "__main__":
    board = Board()
    array = board.new_array()
    for l in array:
        print(id(l))
    print(array)