import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    functions.save_todos(todos)


st.title("To-Do App")
st.subheader("Make a list of things you need To-Do")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter todo", label_visibility="collapsed",
              placeholder="Add a new todo...", on_change=add_todo, key='new_todo')
