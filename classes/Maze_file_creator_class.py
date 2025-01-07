import numpy as np
from classes.FactoryDAO import FactoryDAO

def get_maze_input():
    file_path = "../maze generator/generated_temp.npy"
    if file_path:
        maze = np.load(file_path)
        return maze
    else:
        print("No file selected.")
        return None

def main():
    file_type = input("Enter the file type (txt, csv, xml):\n> ")
    filename = "levels"
    database = "saved_levels"

    maze = get_maze_input()

    factory = FactoryDAO(database, filename)
    dao = factory.create_dao(file_type)

    if dao:
        dao.save_maze(maze)
    else:
        print("Unsupported file type.")

if __name__ == "__main__":
    main()