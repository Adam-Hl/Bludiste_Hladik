import numpy as np
from random import randint
from classes.flood_fill_algorithm import FloodFill


class Maze_generator:
    def __init__(self, size):
        self.y, self.x = size
        self.directions = [(1,0),(0,-1),(-1,0),(0,1)]   # y, x
        self.file = None

    def create_maze(self):
        maze = np.zeros((self.y, self.x), dtype=int)
        maze = self.place_start(maze)
        maze = self.place_end(maze)
        flood_fill = FloodFill(maze)
        while flood_fill.can_be_solved:
            maze = self.place_wall(maze)
            print("check")
            flood_fill.flood()
        print(maze)

    def place_start(self, maze):
        y = randint(0, self.y-1)
        x = randint(0, self.x-1)
        maze[y][x] = 8
        return maze

    def place_end(self, maze):
        y = randint(0, self.y-1)
        x = randint(0, self.x-1)
        if self.check_for(maze, (y,x), 0):
            maze[y][x] = 3
            return maze

    def place_wall(self, maze):
        y = randint(0, self.y-1)
        x = randint(0, self.x-1)
        if self.check_for(maze, (y,x), 0):
            maze[y][x] = 1
            return maze

    def check_for(self, maze, cell, value):
        if maze[cell[0]][cell[1]] == value:
            return True





if __name__ == "__main__":
    generator = Maze_generator((3,3))
    generator.create_maze()

