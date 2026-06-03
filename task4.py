from tkinter import *

def register():
    lbl_result.config(text="Registered")

root = Tk()
root.title("Registration Form")
root.geometry("300x200")

Label(root, text="Username").pack(pady=5)
entry_user = Entry(root)
entry_user.pack()

Label(root, text="Password").pack(pady=5)
entry_pass = Entry(root, show="*")
entry_pass.pack()

Button(root, text="Register", command=register).pack(pady=10)

lbl_result = Label(root, text="")
lbl_result.pack()

root.mainloop()