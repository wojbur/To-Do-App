import functions
import PySimpleGUI as sg
import time

sg.theme("DefaultNoMoreNagging")

label = sg.Text("Type in a to-do")
clock = sg.Text("", key="clock")
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=34)
add_button = sg.Button("Add", size=10)
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10)
listbox = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))

col_l = [[clock],
         [label],
         [input_box, add_button],
         [listbox],
         [exit_button]]
col_r = [[edit_button], [complete_button]]

layout = [[sg.Col(col_l), sg.Col(col_r)]]

window = sg.Window("To-Do App",
                   layout=layout,
                   font=("Helvetica", 12))

while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y, %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"])
            functions.save_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            try:
                selected_todo = values["todos"][0]
            except IndexError:
                sg.popup("Select an item to edit", font=("Helvetica", 12))
                continue
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(selected_todo)
            todos[index] = new_todo
            functions.save_todos(todos)
            window["todos"].update(values=todos)

        case "Complete":
            try:
                selected_todo = values["todos"][0]
            except IndexError:
                sg.popup("Select an item to complete", font=("Helvetica", 12))
                continue
            todos = functions.get_todos()
            todos.remove(selected_todo)
            functions.save_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "todos":
            selected_todo = values["todos"][0]
            window["todo"].update(value=selected_todo)

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
