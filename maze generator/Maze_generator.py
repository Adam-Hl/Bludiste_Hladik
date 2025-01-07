import numpy as np
from random import randint
from classes.flood_fill_algorithm import FloodFill


class Maze_generator:
    def __init__(self, size):
        self.y, self.x = size
        self.directions = [(1,0),(0,-1),(-1,0),(0,1)]   # y, x
        self.file = None
        self.tries = 0

    def create_maze(self):
        maze = np.zeros((self.y, self.x), dtype=int)
        maze = self.place_start(maze)
        maze = self.place_end(maze)
        maze = self.wall_placer(maze)
        return maze

    def place_start(self, maze):
        y = randint(0, self.y-1)
        x = randint(0, self.x-1)
        maze[y][x] = 8
        return maze

    def place_end(self, maze):
        while True:
            y = randint(0, self.y - 1)
            x = randint(0, self.x - 1)
            if self.check_for(maze, (y, x), 0):
                maze[y][x] = 3
                return maze

    def place_wall(self, maze):
        y = randint(0, self.y - 1)
        x = randint(0, self.x - 1)
        if self.check_for(maze, (y, x), 0):
            maze[y][x] = 1
        return maze

    def wall_placer(self, maze_input):
        maze_old = maze_input.copy()
        maze_new = self.place_wall(maze_input)
        flood_fill = FloodFill(maze_new)
        self.tries += 1
        if self.tries > (self.y * self.x):
            return maze_old
        elif flood_fill.flood(True):
            return self.wall_placer(maze_new)
        else:
            return maze_old

    def check_for(self, maze, cell, value):
        if maze[cell[0]][cell[1]] == value:
            return True


class App:
    def __init__(self):
        self.y = None
        self.x = None
        self.dialogue()
        self.maze_generator()

    def dialogue(self):
        print("---Maze generator---")
        print("Enter the size of the maze:")
        self.y = int(input("Enter number of rows\n>"))
        self.x = int(input("Enter number of columns\n>"))

    def maze_generator(self):
        print(f"\nGenerating maze with size {self.y}x{self.x}...")
        generator = Maze_generator((self.y, self.x))
        maze = generator.create_maze()
        print(maze)
        choice = input("Do you want to save this maze? (y/n)\n>")
        if choice == "y":
            np.save('generated_temp.npy', maze)
            from classes.Maze_file_creator_class import main
            main()
        if choice == "n":
            self.maze_generator()


if __name__ == "__main__":
    app = App()
