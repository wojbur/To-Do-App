from functions import get_todos, save_todos
import time

now = time.strftime("%b %d, %Y, %H:%M:%S")
print(f"It is {now}")
todos = get_todos()
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.lower().startswith("add"):
        todo = user_action[4:]
        todos.append(todo)
        save_todos(todos)

    elif user_action.lower().startswith("show"):
        for i, todo in enumerate(todos, 1):
            print(f'{i}: {todo}')

    elif user_action.lower().startswith("edit"):
        try:
            number = int(user_action[5:])
            todos[number-1] = input("Enter a new todo: ")
            save_todos(todos)
        except ValueError:
            print("Please enter number of todo to edit.")
        except IndexError:
            print(f"Please enter a correct todo number.")

    elif user_action.lower().startswith("complete"):
        try:
            number = int(user_action[9:])
            removed_todo = todos.pop(number-1)
            save_todos(todos)
            print(f'Todo "{removed_todo}" was removed from the list')
        except ValueError:
            print("Please enter number of todo to complete.")
        except IndexError:
            print(f"Please enter a correct todo number.")

    elif user_action.lower().startswith("exit"):
        break

    else:
        print("I don't understand. Try again.")

print("Bye!")
