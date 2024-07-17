from tkinter import *
import random

#function for strong password
def strong_password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']
    

    length = int(entry_length.get())
    password_list = []
    
    for i in range(length):
        if i%2==0:
            password_list+=random.choice(letters)
        else:
            password_list+=random.choice(numbers)
   
    random.shuffle(password_list)
    password="".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#function for moderate password
def moderate_password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    

    length = int(entry_length.get())
    password_list = []
    
    for i in range(length):
        if i%2==0:
            password_list+=random.choice(letters)
        else:
            password_list+=random.choice(numbers)
    
    random.shuffle(password_list)
    password="".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#function for simple password
def easy_password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   
    length = int(entry_length.get())
    password_list = []
    
    for i in range(length):
        password_list+=random.choice(letters)
    
    random.shuffle(password_list)
    password="".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)    

#tkinter widgets
root = Tk()
root.config (padx=50, pady=50)
root.title("Password Generator")

root.resizable(False, False)

#canvas for logo
canvas = Canvas(root, width=400, height=200)
password_image = PhotoImage(file="./password_generator/logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1 ,columnspan=2)

#label and entry for the data
label_length=Label(root, text="Password Length")
label_length.grid(row=1, column=0)

entry_length = Entry(root, font="Arial 10 bold")
entry_length.grid(row=1, column=1)

password_length = Label(root, text="Generated Password")
password_length.grid(row=2, column=0)

password_entry = Entry(root, font="Ariel 10 bold")
password_entry.grid(row=2, column=1)

#button for different type of password
simple_password = Button(text = "Simple Password", pady=5, command= easy_password_generator)
moderate_password = Button(text = "Moderate Password", pady=5, command= moderate_password_generator)
strong_password = Button(text = "Strong Password", pady=5, command= strong_password_generator ) 

simple_password.grid(row=3, column=0)
moderate_password.grid(row=3, column=1)
strong_password.grid(row=3, column=2)

root.mainloop()

