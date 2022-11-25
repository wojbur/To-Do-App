import os


FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return list of to-do items """
    if not os.path.exists(filepath):
        with open(filepath, mode="w") as f:
            pass
    with open(filepath, mode="r") as f:
        return f.read().splitlines()


def save_todos(todo_lst, filepath=FILEPATH):
    """ Save to-do items list to a text file """
    with open(filepath, "w") as f:
        f.writelines([line + "\n" for line in todo_lst])


# if __name__ == "__main__":
#     pass
