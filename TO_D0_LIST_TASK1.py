import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("MY TO DO LIST")

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!", message="To add a task please enter some task")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention!", message="To delete a task, you must select a task")

list_box = tkinter.Frame(window)
list_box.pack()

todo_box = tkinter.Listbox(list_box, height=20, width=50)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_box)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)
todo_box.config(yscrollcommand=scroller.set)

task_add = tkinter.Entry(window, width=70)
task_add.pack()

add_task_button = tkinter.Button(window, text="CLICK TO ADD TASK", font=("arial", 20, "bold"), background="red", width=40, command=task_adding)
add_task_button.pack()

remove_task_button = tkinter.Button(window, text="CLICK TO DELETE TASK", font=("arial", 20, "bold"), background="yellow", width=40, command=task_removing)
remove_task_button.pack()

window.mainloop()
