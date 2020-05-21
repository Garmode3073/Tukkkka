from tkinter import *
import tkinter.messagebox
import random

# tkinter window create and edit
window = Tk()
window.title("Tukkkka")
window.geometry("800x500")
window.config(bg='DarkOrchid4')
window.iconbitmap('guess.ico')


# important functions
def about_us():
    tkinter.messagebox.showinfo('About us', 'This is a number guessing game created by Gaurav Garmode. If new in this '
                                            'game please read the instructions. Enjoyeeee!!!!!!')


def change(choice, level2):
    global center_panel_main
    global center_panel_instruction
    global current
    global difficulty
    global chosen_one
    global score
    global lives
    global range_dict
    global range_dict2
    range_dict = {'Easy': 'Range:  0 to 10', 'Medium': 'Range:  0 to 20', 'Hard': 'Range:  0 to 30'}
    range_dict2 = {'Easy': 10, 'Medium': 20, 'Hard': 30}
    center_panel_main.pack_forget()
    if choice == 'inst':
        center_panel_instruction.pack(fill=BOTH)
    elif choice == 'new':
        center_panel_new.pack(fill=BOTH)
    elif choice == 'new2':
        center_panel_new.pack_forget()
        center_panel_new2.pack(fill=BOTH)
        chosen_one = random.randint(0, range_dict2[level2])
        print(chosen_one)
        difficulty.set(level2)
        range_val.set(range_dict[level2])
    elif choice == 'new3':
        center_panel_new2.pack_forget()
        center_panel_new3.pack(fill=BOTH)
    elif choice == 'high':
        center_panel_high_score.pack(fill=BOTH)
    else:
        return
    current = choice


def back():
    global center_panel_main
    global center_panel_instruction
    global current
    global difficulty
    global score
    global lives
    center_panel_instruction.pack_forget()
    center_panel_new.pack_forget()
    center_panel_new2.pack_forget()
    center_panel_new3.pack_forget()
    center_panel_high_score.pack_forget()
    center_panel_main.pack(fill=BOTH)
    current = 'main'
    lives = 3
    score = 0
    difficulty.set('')
    answer.set('')


def check():
    global lives
    global score
    try:
        limit = range_dict2[difficulty.get()]
        if int(answer.get()) > limit:
            answer.set('')
            tkinter.messagebox.showerror('Invalid answer!!', 'Do you even think, Monkey!')
            return
        if int(answer.get()) == chosen_one:
            score = lives * range_dict2[difficulty.get()]
            message_text = 'You won the game breaking the high score. Your score is\n' + str(
                score) + ' with difficulty level ' + difficulty.get() + '. Enter your name:'
            tkinter.messagebox.showinfo('Congratulations',
                                        'You won in a difficulty: ' + difficulty.get() + ' and score: ' + str(score))
            message_var.set(message_text)
            s = difficulty.get() + '.txt'
            level_file = open(s, 'r')
            content = level_file.read()
            g = content.index(',') + 1
            string_score = content[g + 1] + content[g + 2]
            current_score = int(string_score)
            level_file.close()
            if score >= current_score:
                change('new3', level2=difficulty.get())
            else:
                back()
                return
        else:
            if lives == 1:
                back()
                tkinter.messagebox.showerror('Game Over!!!', 'You Tried 3 times. Unfortunately you are not so good or '
                                                             'maybe lucky. Answer in ' + str(chosen_one))
                lives = 3
                return
            string_use = ''
            if int(ans_text.get()) < chosen_one:
                string_use = 'Wrong Answer!! You tried well but the chosen one is larger than one you guessed'
            elif int(ans_text.get()) > chosen_one:
                string_use = 'Wrong Answer!! You tried well but the chosen one is smaller than one you guessed'
            else:
                return
            lives = lives - 1
            lives_str.set('LIVES: ' + str(lives))
            tkinter.messagebox.showerror('OOOOPPSS!!!', string_use)
            answer.set('')
    except:
        answer.set('')
        tkinter.messagebox.showerror('Invalid answer!!', 'Do you even think, Monkey!')


def submit_fun():
    s = difficulty.get() + '.txt'
    level_file = open(s, 'w')
    level_file.write(f'{name.get(), score}')
    level_file.close()
    name.set('')
    back()


def check_score(level):
    s = level + '.txt'
    file = open(s, 'r')
    content = file.read()
    name_champ = ''
    for char in range(content.index("'") + 1, content.index(',') - 1):
        name_champ = name_champ + content[char]
    g = content.index(',') + 1
    string_score = content[g + 1] + content[g + 2]
    tkinter.messagebox.showinfo('High Score', 'Level: ' + level + '\nName: ' + name_champ + '\nScore: ' + string_score)


# Menu Bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# submenu
submenu = Menu(menu_bar, tearoff=0, bg='MediumOrchid', fg='White')
menu_bar.add_cascade(menu=submenu, label='Help')
submenu.add_command(label='About Us', command=about_us)

# center panels and common elements
center_panel_main = Canvas(window, bg='MediumOrchid', relief=SOLID, border=5, height=550, width=745)
center_panel_new = Canvas(window, bg='MediumOrchid', relief=SOLID, border=5, height=550, width=745)
center_panel_new2 = Canvas(window, bg='MediumOrchid', relief=SOLID, border=5, height=550, width=745)
center_panel_new3 = Canvas(window, bg='MediumOrchid', relief=SOLID, border=5, height=550, width=745)
center_panel_high_score = Canvas(window, bg='MediumOrchid', relief=SOLID, border=5, height=550, width=745)
center_panel_instruction = Canvas(window, bg='MediumOrchid', relief=SOLID, border=5, height=550, width=745)
center_panel_main.pack(fill=BOTH)
range_dict = {}
range_dict2 = {}
difficulty = StringVar()
score = 0
lives = 3
chosen_one = 0
current = 'main'
back_image = PhotoImage(file=r'F:\python\Tukkkka\back.png')
title_image = PhotoImage(file=r'F:\python\Tukkkka\title.png')

# main panel content
title_button = Button(center_panel_main, image=title_image, width=550, height=150, relief=SUNKEN, border=3)
title_button.place(x=125, y=20)
new_button = Button(center_panel_main, bg='DarkOrchid4', relief=GROOVE, fg='White', text='New Game',
                    font=('Small Fonts', 26), width=9, command=lambda: change('new', level2=''))
new_button.place(x=300, y=200)
high_score_button = Button(center_panel_main, bg='DarkOrchid4', relief=GROOVE, fg='White', text='High Score',
                           font=('Small Fonts', 26), width=9, command=lambda: change('high', level2=''))
high_score_button.place(x=300, y=300)
instruction_button = Button(center_panel_main, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Instruction',
                            font=('Small Fonts', 26), width=9, command=lambda: change('inst', level2=''))
instruction_button.place(x=300, y=400)

# instruction panel content
ins = StringVar()
ins_stuff = "This is quite a simple game. First of all you get three options, EASY, MEDIUM\nand HARD. The range of " \
            "game " \
            "for 'Easy' is 0 to 10, for 'Medium' is 0 to 20\nand for 'Hard' is 0 to 30. The system will choose a " \
            "number " \
            "and you gotta\nguess what that number is. You will get 3 lives for one game. After every\nwrong answer " \
            "you " \
            "will know whether the chosen number is smaller than number\nyou guessed or larger. For finishing game " \
            "with " \
            "all 3 lives remaining you will\nhave (30 in easy, 60 in medium, 90 in hard) points, similarly with 2 " \
            "lives\n" \
            "you will have (20 in easy, 40 in medium, 60 in hard) points," \
            "(10 in easy, 20\nin medium, 30 in hard) points if 1 life remaining and 0 for loosing.\n\n\n\nGood Luck, " \
            "now go break some eggs. "
ins.set(ins_stuff)
ins_label = Label(center_panel_instruction, text='Instruction', font=('Fixedsys', 36), bg='DarkOrchid4',
                  fg='MediumOrchid', relief=RAISED)
ins_label.place(x=240, y=10)
ins_label_inf = Label(center_panel_instruction, textvar=ins, font=('Fixedsys', 17), bg='DarkOrchid4', fg='White',
                      relief=RAISED, justify=LEFT)
ins_label_inf.place(x=12, y=100)
ins_image = PhotoImage(file=r'F:\python\Tukkkka\ins_below.png')
ins_button = Button(center_panel_instruction, image=ins_image, width=770, height=112)
ins_button.place(x=12, y=370)
ins_back = Button(center_panel_instruction, image=back_image, width=60, height=60, command=back)
ins_back.place(x=12, y=12)

# new panel 1 content
title_button2 = Button(center_panel_new, image=title_image, width=550, height=150, relief=SUNKEN, border=3)
title_button2.place(x=125, y=20)
easy_button = Button(center_panel_new, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Easy',
                     font=('Small Fonts', 26), width=9, command=lambda: change('new2', level2='Easy'))
easy_button.place(x=300, y=200)
med_button = Button(center_panel_new, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Medium',
                    font=('Small Fonts', 26), width=9, command=lambda: change('new2', level2='Medium'))
med_button.place(x=300, y=300)
hard_button = Button(center_panel_new, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Hard',
                     font=('Small Fonts', 26), width=9, command=lambda: change('new2', level2='Hard'))
hard_button.place(x=300, y=400)
new_back = Button(center_panel_new, image=back_image, width=60, height=60, command=back)
new_back.place(x=12, y=12)

# new panel 2 content
range_val = StringVar()
answer = StringVar()
lives_str = StringVar()
lives_str.set('LIVES: 3')
new2_label = Label(center_panel_new2, textvar=difficulty, font=('Fixedsys', 36), bg='DarkOrchid4',
                   fg='MediumOrchid', relief=RAISED, width=9)
new2_label.place(x=260, y=10)
new2_back = Button(center_panel_new2, image=back_image, width=60, height=60, command=back)
new2_back.place(x=12, y=12)
question = Label(center_panel_new2, text='Hello There, I just chose a number. The range is given\nbelow, lets see if '
                                         'you can guess', font=('Comic Sans MS', 20), bg='DarkOrchid4',
                 fg='White', relief=SUNKEN)
question.place(x=55, y=100)
range_label = Label(center_panel_new2, textvar=range_val, font=('Comic Sans MS', 20), bg='DarkOrchid4',
                    fg='White', relief=SUNKEN)
range_label.place(x=305, y=185)
ans_text = Entry(center_panel_new2, textvar=answer, width=2, font=('Times New Roman', 44), relief="solid")
ans_text.place(x=450, y=285)
lives_label = Label(center_panel_new2, textvar=lives_str, font=('Small Fonts', 20), bg='DarkOrchid4',
                    fg='White', relief=SUNKEN, width=9, height=2)
lives_label.place(x=290, y=285)
check_ans = Button(center_panel_new2, bg='DarkOrchid4', relief=GROOVE, fg='White', text='CHECK',
                   font=('Small Fonts', 22), width=9, command=check)
check_ans.place(x=562, y=412)

# new3 panel content
new3_label = Label(center_panel_new3, text='Congratulations, you have high score!!', font=('Fixedsys', 30),
                   bg='DarkOrchid4',
                   fg='MediumOrchid', relief=RAISED)
new3_label.place(x=15, y=10)
message_var = StringVar()
message = Label(center_panel_new3, textvar=message_var, font=('Comic Sans MS', 20), bg='DarkOrchid4',
                fg='White', relief=SUNKEN)
message.place(x=45, y=150)
name = StringVar()
name_text = Entry(center_panel_new3, textvar=name, width=20, font=('Times New Roman', 36), relief="solid")
name_text.place(x=155, y=235)
submit = Button(center_panel_new3, bg='DarkOrchid4', relief=GROOVE, fg='White', text='SUBMIT',
                font=('Small Fonts', 22), width=9, command=submit_fun)
submit.place(x=562, y=412)

# high score panel
high_score_label = Label(center_panel_high_score, text='High Scores', font=('Fixedsys', 36), bg='DarkOrchid4',
                         fg='MediumOrchid', relief=RAISED)
high_score_label.place(x=230, y=10)
high_back = Button(center_panel_high_score, image=back_image, width=60, height=60, command=back)
high_back.place(x=12, y=12)
easy_button_score = Button(center_panel_high_score, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Easy',
                           font=('Small Fonts', 26), width=9, command=lambda: check_score('Easy'))
easy_button_score.place(x=300, y=160)
med_score_button = Button(center_panel_high_score, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Medium',
                          font=('Small Fonts', 26), width=9, command=lambda: check_score('Medium'))
med_score_button.place(x=300, y=260)
hard_button_score = Button(center_panel_high_score, bg='DarkOrchid4', relief=GROOVE, fg='White', text='Hard',
                           font=('Small Fonts', 26), width=9, command=lambda: check_score('Hard'))
hard_button_score.place(x=300, y=360)

# activate window
window.mainloop()
