from abc import ABC, abstractmethod

class Platform(ABC):
    @abstractmethod
    def available_blocks(self) -> list[list[int]]:
        pass
    @abstractmethod
    def max_dimensions(self) -> tuple[int, int]:
        pass

class Table(Platform):
    def __init__(self, width:int, height:int):
        self.width:int = width
        self.height:int = height
    def available_blocks(self) -> list[list[int]]:
        # [      5x5
        #    [0,0,0,0,0],
        #    [0,0,0,0,0],
        # -> [0,0,0,0,0],
        #    [0,0,0,0,0],
        #    [0,0,0,0,0]
        # ]
        height = [1 for i in range(self.height)]
        return [height for i in range(self.width)]

    def max_dimensions(self) -> tuple[int, int]:
        return self.width, self.height