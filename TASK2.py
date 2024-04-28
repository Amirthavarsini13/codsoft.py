from tkinter import *

root = Tk()

root.title("Calculator")

root.configure(bg='gray10')

lbl_welcome = Label(root, text="Welcome", bg="gray10", fg="white")
lbl_welcome.grid(row=0, column=0)

lbl_n1 = Label(root, text="Enter the first number:", bg="gray10", fg="white")
lbl_n1.grid(row=1, column=0)

entry_n1 = Entry(root)
entry_n1.grid(row=1, column=1)

lbl_operator = Label(root, text="Enter operator (+,-,*,/,%):", bg="gray10", fg="white")
lbl_operator.grid(row=2, column=0)

entry_operator = Entry(root)
entry_operator.grid(row=2, column=1)

lbl_n2 = Label(root, text="Enter the second number:", bg="gray10", fg="white")
lbl_n2.grid(row=3, column=0)

entry_n2 = Entry(root)
entry_n2.grid(row=3, column=1)

lbl_result = Label(root, text="", bg="gray10", fg="white")
lbl_result.grid(row=5, column=0, columnspan=2)

def calculate_result():
    n1 = int(entry_n1.get())
    n2 = int(entry_n2.get())
    operator = entry_operator.get()
    
    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 / n2
    elif operator == "%":
        result = n1 % n2
    else:
        result = "Invalid Operator"
    
    lbl_result["text"] = f"Result: {result}"

btn_calculate = Button(root, text="Calculate", bg="dark green", command=calculate_result)
btn_calculate.grid(row=4, column=0, columnspan=2)

root.mainloop()
