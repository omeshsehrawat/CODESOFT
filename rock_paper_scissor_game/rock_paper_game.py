from tkinter import *
import random
from PIL import Image, ImageTk

user_score = 0
computer_score = 0


def rock():

    global user_score
    global computer_score

    rock='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    R O C K
    '''
    user_text_field.delete('0.0', END)
    user_text_field.insert(INSERT, rock)
    result = computer_choice()
    if result==2:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 100, image=win_image)
        user_score += 1
        user_score_field.delete('0.0', END)
        user_score_field.insert(INSERT, user_score)
    
    elif result==1:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 90, image=lose_image)
        computer_score += 1
        computer_score_field.delete('0.0', END)
        computer_score_field.insert(INSERT, computer_score)

    else:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 100, image=tie_image)
    

def paper():

    global user_score
    global computer_score

    paper='''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    P A P E R
    '''
    user_text_field.delete('0.0', END)
    user_text_field.insert(INSERT, paper)
    result = computer_choice()
    if result==0:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 100, image=win_image)
        user_score+=1
        user_score += 1
        user_score_field.delete('0.0', END)
        user_score_field.insert(INSERT, user_score)

    elif result==2:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 90, image=lose_image)
        computer_score += 1
        computer_score_field.delete('0.0', END)
        computer_score_field.insert(INSERT, computer_score)
    else:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 100, image=tie_image)

def scissor():

    global user_score
    global computer_score

    scissor='''
        _______
    ---'   ____)____
              ______)
          __________)
         (____)
    ---.__(___)
    S C I S S O R
    '''
    user_text_field.delete('0.0', END)
    user_text_field.insert(INSERT, scissor)
    result = computer_choice()
    if result==1:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 90, image=win_image)
        user_score += 1
        user_score_field.delete('0.0', END)
        user_score_field.insert(INSERT, user_score)

    elif result==0:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 90, image=lose_image)
        computer_score += 1
        computer_score_field.delete('0.0', END)
        computer_score_field.insert(INSERT, computer_score)
    
    else:
        decision_canvas.delete('all')
        decision_canvas.create_image(100, 100, image=tie_image)
        

def computer_choice():
    choice = random.randint(0,2)
    #print(choice) 
    if choice==0:
        rock="""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        R O C K
        """
        computer_text_field.delete('0.0', END)
        computer_text_field.insert(INSERT, rock)
        return choice
    
    elif choice==1:
        paper="""
            _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        P A P E R
        """
        computer_text_field.delete('0.0', END)
        computer_text_field.insert(INSERT, paper)
        return choice
    
    else:
        scissor="""
            _______
        ---'   ____)____
                  ______)
              __________)
             (____)
        ---.__(___)
        S C I S S O R
        """
        computer_text_field.delete('0.0', END)
        computer_text_field.insert(INSERT, scissor)
        return choice



#GUI WINDOW

window = Tk()
window.config(padx=50, pady=50)
window.title("Rock Paper Scissor Game")

window.resizable(False, False)

#command to the fullscreen while running the program
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
# root.geometry("%dx%d"%(w,h))

image_1 = Image.open("./rock_paper_scissor_game/start_image.png")
image_resize_1 = image_1.resize((200, 170))
start_image = ImageTk.PhotoImage(image_resize_1)

image_2 = Image.open("./rock_paper_scissor_game/win_image.png")
image_resize_2 = image_2.resize((200, 170))
win_image = ImageTk.PhotoImage(image_resize_2)

image_3 = Image.open("./rock_paper_scissor_game/lose_image.png")
image_resize_3 = image_3.resize((200, 170))
lose_image = ImageTk.PhotoImage(image_resize_3)

image_4 = Image.open("./rock_paper_scissor_game/tie_image.png")
tie_image = ImageTk.PhotoImage(image_4)

image_5 = Image.open("./rock_paper_scissor_game/background_image.png")
image = image_5.resize((900,700))
background_image = ImageTk.PhotoImage(image)

#background label
root = Label(window, image=background_image)
root.pack()

#logo canvas
logo_canvas = Canvas(root, width=300, height=320, bg="BLACK")
game_image = PhotoImage(file="./rock_paper_scissor_game/game_logo.png")
logo_canvas.create_image(153, 158, image=game_image)
logo_canvas.grid(row=0, column=1)

decision_canvas = Canvas(root, width=200, height=170)
decision_canvas.grid(row=2 ,column=1)
decision_canvas.create_image(100, 90, image=start_image)

#Score Frame
user_score_frame = Frame(root)
user_score_frame.grid(row=6, column=0)

computer_score_frame = Frame(root)
computer_score_frame.grid(row=6, column=2)


#label for user and computer
user_label = Label(root, text="Select your Choose", font="Script 40 bold", bg="lightblue")
user_label.grid(row=1, column=0)

computer_label = Label(root, text="Computer Choice", font="Script 40 bold", bg="lightblue")
computer_label.grid(row=1, column=2)

user_score_label = Label(user_score_frame, text="User Score", font="Serif 20 bold", bg="lightblue")
user_score_label.pack(side='left')

computer_score_label = Label(computer_score_frame, text="Computer Score", font="Serif 20 bold", bg="lightblue")
computer_score_label.pack(side='left')

decision_label = Label(root, text="Decision", font="Script 40 bold", bg="lightblue")
decision_label.grid(row=1, column=1)

#text field for showing the choice
user_text_field = Text(root, height=10, width=25)
user_text_field.grid(row=2, column=0)

computer_text_field = Text(root, height=10, width=30)
computer_text_field.grid(row=2, column=2)

user_score_field = Text(user_score_frame, width=2, height=1, font="Arial 20 bold")
user_score_field.pack(side='right')

computer_score_field = Text(computer_score_frame, width=2, height=1, font="Arial 20 bold")
computer_score_field.pack(side='right')

#emty frames
frame_1 = Frame(root, height=10, bg="black")
frame_1.grid(row=3, column=0)

frame_2 = Frame(root, height=10, bg="black")
frame_2.grid(row=5, column=0)

#Frames
button_frame = Frame(root, width=20)
button_frame.grid(row=4, column=0)


#different choice button
scissor_button = Button(button_frame, text="Scissor", padx=5, pady=5, command=scissor)
scissor_button.pack(side='left')

paper_button = Button(button_frame, text="Paper", padx=5, pady=5, command=paper)
paper_button.pack(side='left')

rock_button = Button(button_frame, text="Rock", padx=5, pady=5, command=rock)
rock_button.pack(side='left')


window.mainloop()