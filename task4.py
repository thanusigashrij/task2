from tkinter import *

def register():
    print("Registered")

root = Tk()
root.title("Registration Form")
root.geometry("300x200")

Label(root, text="Username").pack()
username = Entry(root)
username.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Button(root, text="Register", command=register).pack(pady=10)

root.mainloop()