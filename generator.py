import random
import string
import tkinter

def generate_password():
    password_min = 8
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(all_chars) for x in range(random.randint(password_min, password_max)))
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

window = tkinter.Tk()
window.title("Password Generator")
window.geometry("500x300")
window.config(background="white")

frame = tkinter.Frame(window)
frame.pack(expand=True)

title = tkinter.Label(frame, text="Password Generator", font=("Courrier", 25), bg="white")
title.pack(expand=True)

password_entry = tkinter.Entry(frame, font=("Courrier", 25), bg="lightgrey")
password_entry.pack(expand=True)

button = tkinter.Button(frame, text="Generate", font=("Courrier", 25), bg="lightgrey", command=generate_password)
button.pack(expand=True)

window.mainloop()


