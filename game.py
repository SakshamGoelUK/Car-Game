# PLEASE ENSURE THAT YOU USE SCREEN RESOLUTION OF
# 1980*1080 FOR THE BEST EXPERIENCE

# MODULES IMPORTED
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
from tkinter import font


root = Tk()
app_width = 1980
app_height = 1080
screen_width = 1980
screen_height = 1080
# center_x = (screen_width/2) - (app_width/2)
# center_y = (screen_height/2) - (app_height/2)
style = ttk.Style()
style.configure("Treeview",
                font=('Helvetica', 13,),
                background="purple",
                foreground="white",
                rowheight=30,
                fieldbackground="black")
style.map('Treeview', background=[('selected', 'purple')])
# JSON FILE FOR STORING GAME AND PLAYER DATA
f = open("data.json")
player_data = f.read()
player_data = json.loads(player_data)
newlist = sorted(player_data["players"],
                 key=lambda d: d["Score"], reverse=True)
player_no = len(newlist)
resume_list = player_data["resume"]


# Global Variables and Lists Used
restart1 = False
final_score = 0
canvas2 = False
canvas1 = True
b_pressed = False
allow_change = True
cheatcode = False
loading_screen = True
game_over1 = False
load = False
welcome_screen = True
pause_pressed = False
game1 = False
entry_stage = True
h = -20
over_wt = 2200
car_up = "Up"
car_down = "Down"
car_right = "Right"
car_left = "Left"
boss_key = "b"
pause_key = "p"
loading_screen_timer = [3]
ht = 400
wt = 0
height3 = 400
width3 = 2800
width1 = 2400
width2 = 2000
height1 = 700
height2 = 100
button_wt = 1340
button_ht = 1000
enter_ht = -300
y = 0
score1 = 0
time1 = ["time"]
keypress = []
large_font = ("Verdana", 20)
game_name = "Dangerous Driver"
bossprogram = "Microsoft Excel"
root.title(game_name)

# Images Used (Attributions in .txt file)
how_button = PhotoImage(file="dazzle.png")
about_game = PhotoImage(file="the_game.png")
car12 = PhotoImage(file='car9.png')
loading_pro = PhotoImage(file="loading.png")
video = PhotoImage(file="roads6.png")
vid = Label(root, image=video, bg="black")
car = PhotoImage(file="car7.png")
over = PhotoImage(file="over_screen.png")
play_again = PhotoImage(file="play_again.png")
car1 = PhotoImage(file="untitled_design__10_.png")
carr2 = Label(root, image=car1, bg="black")
button3 = PhotoImage(file="btn2.png")
button4 = PhotoImage(file="btn3.png")
button5 = PhotoImage(file="btn4.png")
instructions = PhotoImage(file="instructions.png")
car2 = PhotoImage(file="untitled_design__11_.png")
car3 = PhotoImage(file="untitled_design__12_.png")
car4 = PhotoImage(file="untitled_design__13_.png")
start = PhotoImage(file="start.png")
no_game = Label(root, text="Sorry No previous Game Stored")
img = PhotoImage(file="hello.png")
btn_image1 = PhotoImage(file="btn1.png")
carr = Label(root, image=car, bg="black")
car5 = PhotoImage(file="image14.png")

# Widgets Used
welcome_img = Label(root, image=loading_pro)
score_player = Label(root, bg="black", fg="white",
                     font=("Courier", 24, "italic"))
name123 = Label(root, bg="black", fg="white",
                font=("Courier", 24, "italic"))
highscore = Label(root, bg="black", fg="white",
                  font=("Courier", 24, "italic"))
position1 = Label(root, bg="black", fg="white",
                  font=("Courier", 24, "italic"))
score = Label(root, text="SCORE: " + str(score1),
              bg="black", fg="white", font=large_font)
enter4 = Button(root, image=how_button,
                command=lambda: how(), borderwidth=0, bd=0)
enter2 = Button(root, image=button3,
                command=lambda: options('load'), borderwidth=0)
enter1 = Button(root, image=button5,
                command=lambda: options('reset'), borderwidth=0)
enter3 = Button(root, image=button4,
                command=lambda: options('new'), borderwidth=0)
reset_label = Label(root, text="Data Erased.",
                    bg="black", fg="yellow", font=("Courier", 24, "italic"))
starting = Label(root,
                 text=f"Loading game in {loading_screen_timer[0]} seconds",
                 bg="black", fg="yellow", font=("Courier", 24, "italic"))
carr4 = Label(root, image=car4, bg='black')
carr3 = Label(root, image=car2, bg="black")
label1 = Label(root, image=img)
label2 = Label(root, text="Your Game is Paused!!",
               font=large_font, bg="black", fg="red")
key_change = Label(root, text="Press a key", font=("Courier", 24, "italic"),
                   bg="black", fg="white")


# FUNCTIONS

# This function changes the cars(Personalization Feauture)
def change_car1(x=1):
    if x == 1:
        carr.configure(image=car)
    elif x == 2:
        carr.configure(image=car5)
    elif x == 3:
        carr.configure(image=car12)

# Function to destroy labels after changing game screens.


def destroy():
    position1.destroy()
    name123.destroy()
    score_player.destroy()
    highscore.destroy()
    position1.destroy()

# These 3 functions together work
# to change the key bindings according to the user preference.


def options(x):
    global score1, car_left, car_down, car_right
    global car_up, car_down, boss_key, pause_key
    welcome_img.place(x=4000, y=4000)
    root.after(4000, destroy)
    enter1.destroy()
    enter2.destroy()
    enter3.destroy()
    enter4.destroy()
    for j in newlist:
        name3 = j['name']
        if name3 == name.upper() and x != 'reset':
            for f in root.bind():
                root.unbind(f)
            car_up = j['Up']
            car_down = j['Down']
            car_right = j['Right']
            car_left = j['Left']
            boss_key = j['Boss']
            pause_key = j['Pause']
            root.bind(f"<{car_up}>", goup)
            root.bind(f"<{car_down}>", godown)
            root.bind(f"<{car_right}>", gort)
            root.bind(f"<{car_left}>", golf)
            root.bind(f"<{boss_key}>", keyup)
            root.bind(f"<{pause_key}>", pause)
        elif x == 'reset':
            reset_label.place(x=950, y=250)
    for i in resume_list:
        if i['name'] == name.upper():
            if x == 'load':
                score1 = i['Score']
                break
            elif x == 'new':
                score1 = 0
    loading()


def loading(event=None):
    global loading_screen
    if loading_screen:
        if loading_screen_timer[0] == 0:
            reset_label.destroy()
            starting.configure(text="Lets Play!!!")
            starting.place(x=1100, y=300)
            loading_screen = False
            root.after(1000, loading)
        else:
            welcome_img.place(x=0, y=0, relheight=1, relwidth=1)
            starting.configure(
                text=f"Loading game in {loading_screen_timer[0]} seconds")
            starting.place(x=950, y=300)
            loading_screen_timer[0] -= 1
            if loading_screen_timer[0] == -1:
                starting.pack_forget()
            root.after(1000, loading)
    else:
        welcome_img.destroy()
        game()


# This function collects data from the json file
# and name of the player to create a user profile of the user.

def get_name(event=None):
    global user_profile, canvas1, allow
    global position1, name, welcome_screen
    global entry_stage, name
    name = e.get()
    if name == '':
        name = f"Player {player_no+1}"
    user_profile = True
    welcome_screen = False
    entry_stage = False
    canvas1 = False
    hello = f"Name: {name.upper()}"
    my_canvas.destroy()
    player_score = 'N/A'
    position = 'N/A'
    x = 0
    if len(newlist) != 0:
        high = newlist[0]["Score"]
    else:
        high = 'N/A'
    for i in newlist:
        x += 1
        if(i["name"] == name.upper()):
            player_score = str(i["Score"])
            position = str(x)
    highscore.config(text=f'Score to beat:{high}')
    position1.config(text=f"Current Position: {position}")
    score_player.config(text=f"Score: {player_score}")
    tree_frame.config(bg="black")
    tree_frame.place(x=975, y=500)
    tree_scroll.pack(side=RIGHT, fill=Y)
    my_tree.pack()
    name123.config(text=hello)
    highscore.place(x=400, y=450)
    position1.place(x=400, y=400)
    score_player.place(x=400, y=350)
    name123.place(x=400, y=300)
    enter1.place(x=1000, y=200)
    enter3.place(x=1000, y=300)
    enter2.place(x=1000, y=400)
    enter4.place(x=420, y=590)
    enter_button.pack_forget()
    e.destroy()
    enter.pack_forget()
    root.unbind("<Return>")
    welcome_img.place(x=0, y=0, relheight=1, relwidth=1)
    about()


# This function pauses the Game.
def pause(e=None):
    if enter_button and not entry_stage:
        global pause_pressed
        if not pause_pressed and load:
            pause_pressed = True
            if(len(keypress) == 0):
                label2.place(x=800, y=200)
        else:
            pause_pressed = False
            label2.place(x=2000, y=2000)


# Function to make the Boss Key work
def keyup(e):

    global b_pressed, ht, pause_pressed
    if not entry_stage and not canvas2:
        if e.char == f'{boss_key}' and len(keypress) == 0:
            pause_pressed = True
            label1.pack()
            root.title(bossprogram)
            if(load and not game_over1):
                vid.place(x=2000, y=2000, relwidth=1, relheight=1)
                carr.pack_forget()
                score.pack_forget()
            root.config(menu="")
            keypress.append("b")
            b_pressed = True
            label2.place(x=2000, y=2000)
            if user_profile:
                tree_frame.place(x=2000, y=2000)
        elif e.char == f'{boss_key}' and len(keypress) != 0:
            pause_pressed = False
            b_pressed = False
            label1.pack_forget()
            root.title(game_name)
            if(load and not game_over1):
                vid.place(x=0, y=0, relwidth=1, relheight=1)
                carr.place(y=ht)
                score.place(x=1700)
                root.config(menu=menubar)
            if user_profile:
                tree_frame.place(x=975, y=500)
            del keypress[0]
            pause()
    elif canvas1:
        if e.char == f'{boss_key}' and len(keypress) == 0:
            my_canvas.pack_forget()
            label1.pack()
            root.title(bossprogram)
            keypress.append("b")
            b_pressed = True
        elif e.char == f'{boss_key}' and len(keypress) != 0:
            b_pressed = False
            label1.pack_forget()
            my_canvas.pack()
            del keypress[0]
    if canvas2:
        if e.char == f'{boss_key}' and len(keypress) == 0:

            end_canvas.place(x=4000, y=4000)
            label1.pack()
            root.title(bossprogram)
            keypress.append("b")
            b_pressed = True
        elif e.char == f'{boss_key}' and len(keypress) != 0:
            end_canvas.place(x=2000, y=2000)
            b_pressed = False
            label1.pack_forget()
            end_canvas.pack()
            del keypress[0]

# This function initialises everything before the game starts.


def game():
    global user_profile, load
    user_profile = False
    tree_frame.place(x=2000, y=2000)
    root.config(menu=menubar)
    load = True
    starting.destroy()
    vid.place(x=0, y=0, relwidth=1, relheight=1)
    carr.place(y=400)
    score.place(x=1700)
    carr4.place(y=height3, x=width3)
    carr2.place(y=height1, x=width1)
    carr3.place(y=height2, x=width2)
    score12()
    random1()

# This function creates a TopLevel containing the playing instructions.


def how():
    top_width = 610
    top_height = 610
    top_x = (app_width/2) - (top_width/2)
    top_y = (app_height/2) - (top_height/2)
    how_to = Toplevel()
    how_to.resizable(False, False)
    how_to.geometry(f'{top_width}x{top_height}+{int(top_x)}+{int(top_y)}')
    txt = Label(how_to, image=instructions)
    txt.place(x=4, y=3)
    how_to.title('Playing Instructions')
    if not pause_pressed and not user_profile:
        pause()
        root.unbind(f'{pause_key}')
        root.wait_window(how_to)
        root.bind(f'{pause_key}', pause)

# The function spawns the cars at different location and intervals.
# Also checks for collisions.Checks to make sure
# that two cars dont overlap each other.
# Also checks for if cheatcode is activated


def random1():
    global width3, width1, width2, height1, height3, height2, pause_pressed
    if (1 < 2 and not pause_pressed and not game_over1 and not b_pressed):
        if width1 > -350:
            carr2.place(x=width1, y=height1)
            width1 -= 5
        elif width1 <= -350:
            width1 = 2400
            d = random.randint(1, 3)
            if d == 1:
                height1 = 700
            elif d == 2:
                height1 = 400
            elif d == 3:
                height1 = 100
            if (height1 != height2 and
                    height2 != height3 and height1 != height3):
                if width1 >= width2-600 and width1 <= width2 + 600:
                    if height1 != 700:
                        height1 += 300
                    else:
                        height1 -= 300
                if width1 >= width3 - 600 and width1 <= width3 + 600:
                    if height1 != 700:
                        height1 += 300
                    else:
                        height1 -= 300
            s = (random.randint(1, 4))
            if s == 1:
                carr2.configure(image=car1)
            elif s == 2:
                carr2.configure(image=car2)
            elif s == 3:
                carr2.configure(image=car3)
            elif s == 4:
                carr2.configure(image=car4)
        if height2 == height1 and width3 >= width2 - 300 and width3 <= width2 + 300:
            width1 -= 400
        if height3 == height1 and width3 <= width1 + 300 and width3 >= width1 - 300:
            width1 += 400
        if score1 > 200:
            if width2 > -350:
                carr3.place(x=width2, y=height2)
                width2 -= 5
            elif width2 <= -350:
                width2 = 2000
                y = random.randint(1, 3)
                if y == 1:
                    height2 = 700
                elif y == 2:
                    height2 = 400
                elif y == 3:
                    height2 = 100
                if height1 != height2 and height2 != height3 and height1 != height3:

                    if width2 >= width1-600 and width2 <= width1 + 600:
                        if height2 != 700:
                            height2 += 300
                        else:
                            height2 -= 300
                    if width2 >= width3 - 600 and width2 <= width3 + 600:
                        if height2 != 700:
                            height2 += 300
                        else:
                            height2 -= 300
                r = (random.randint(1, 4))
                if r == 1:
                    carr3.configure(image=car1)
                elif r == 2:
                    carr3.configure(image=car2)
                elif r == 3:
                    carr3.configure(image=car3)
                elif r == 4:
                    carr3.configure(image=car4)
            if height2 == height3 and width2 >= width3 - 300 and width2 <= width3 + 300:
                width2 -= 400
            if height2 == height1 and width2 <= width1 + 300 and width2 >= width1 - 300:
                width2 -= 400
        if score1 > 400:
            if width3 > -350:
                carr4.place(x=width3, y=height3)
                width3 -= 5
            elif width3 <= -350:
                width3 = 2800
                z = random.randint(1, 3)
                if z == 1:
                    height3 = 700
                elif z == 2:
                    height3 = 400
                elif z == 3:
                    height3 = 100
                if height1 != height2 and height2 != height3 and height1 != height3:

                    if width3 >= width1-600 and width3 <= width2 + 600:
                        if height3 != 700:
                            height3 += 300
                        else:
                            height3 -= 300
                    if width3 >= width2 - 600 and width3 <= width2 + 600:
                        if height3 != 700:
                            height3 += 300
                        else:
                            height3 -= 300
                t = (random.randint(1, 4))
                if t == 1:
                    carr4.configure(image=car1)
                elif t == 2:
                    carr4.configure(image=car2)
                elif t == 3:
                    carr4.configure(image=car3)
                elif t == 4:
                    carr4.configure(image=car4)
            if height3 == height1 and width3 >= width1 - 300 and width3 <= width1 + 300:
                width3 -= 400
            if height1 == height3 and width3 <= width2 + 300 and width3 >= width2 - 300:
                width3 += 400
        if(cheatcode):
            if ht == height1 and wt >= width1 - 285 and wt <= width1 + 285:
                width1 = 2600
                if height1 == 700:
                    height1 -= 300
                else:
                    height1 += 300
                carr2.place(x=width1, y=height1)
            if ht == height2 and wt <= width2 + 285 and wt >= width2 - 285:
                width2 = 3000
                if height2 == 700:
                    height2 -= 300
                else:
                    height2 += 300
                carr3.place(x=3000, y=height2)
            if ht == height3 and wt <= width3 + 285 and wt >= width3 - 285:
                width3 = 3400
                if height3 == 700:
                    height3 -= 300
                else:
                    height3 += 300
                carr4.place(x=3400, y=height3)
        else:
            if ht == height1 and wt >= width1 - 285 and wt <= width1 + 285:
                game_over()
            if ht == height2 and wt <= width2 + 285 and wt >= width2 - 285:
                game_over()
            if ht == height3 and wt <= width3 + 285 and wt >= width3 - 285:
                game_over()
        if score1 > 1200:
            width1 -= 2
            width2 -= 2
            width3 -= 2
        if score1 > 1300:
            width1 -= 2
            width2 -= 2
            width3 -= 2
        if score1 > 1300:
            width1 -= 1
            width2 -= 1
            width3 -= 1
    root.bind("<c>", cheatcode1)
    carr2.after(1, random1)


def over_screen1():
    global score1, canvas2
    canvas2 = True
    final_score = score1
    score1 = 0
    name_label = Label(
        root, text=f'Your final score is {str(final_score)}', bg="blue", fg="Black", font=("Courier", 26, "italic"))

    score.configure(text="SCORE:" + str(score1))
    name_window = end_canvas.create_window(
        110, 300, anchor="nw", window=name_label)
    global h, over_wt
    end_canvas.pack(fill="both", expand=True)


def score12():
    global restart1, game_over1, score1, score, final_score
    if not pause_pressed:
        if restart1:
            score1 = 0
            restart1 = False
        elif not game_over1:
            score.configure(text="SCORE:" + str(score1))
            score1 += 10

    score.after(500, score12)

# Move Car to above lane


def goup(e):
    global ht
    if ht > 100 and load and not pause_pressed:
        carr.place(y=ht - 300)
        ht = ht - 300

# Move Car to the below lane


def godown(e):
    global ht
    if ht < 700 and load and not pause_pressed:
        carr.place(y=ht + 300)
        ht = ht + 300

# Move Car faster


def gort(e):
    global ht
    global wt
    if wt < 1200 and load and not pause_pressed:
        carr.place(y=ht, x=wt + 10)
        wt += 10

# Move Car backwards


def golf(e):
    global ht
    global wt
    if wt > 0 and load and not pause_pressed:
        carr.place(y=ht, x=wt - 10)
        wt -= 10


tree_frame = Frame(root)
tree_scroll = Scrollbar(tree_frame)
# Adding the scrollbar
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
# Configure the scrollbar
tree_scroll.config(command=my_tree.yview)
# Define Columns
my_tree["columns"] = ("Position", "Name", "Score")
# Format Columns
my_tree.column("#0", width=0, minwidth=25, stretch=NO)
my_tree.column("Position", anchor=W, width=80)
my_tree.column("Name", anchor=CENTER, width=120)
my_tree.column("Score", anchor=W, width=80)
# HEADINGS
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Position", text="Position", anchor=W)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Score", text="Score", anchor=W)
# Add Data
for i in range(len(newlist)):
    my_tree.insert(
        parent="",
        index="end",
        text="",
        values=(i + 1, newlist[i]["name"], newlist[i]["Score"]),
    )


def restart():
    global restart1, game_over1, score1, wt, ht, height2, height1, height3, width3, width2, width1, canvas2
    restart1 = True
    canvas2 = False
    height3 = 400
    width3 = 2200
    width1 = 2700
    width2 = 3500
    height1 = 700
    height2 = 100
    ht = 400
    wt = 0
    carr4.place(y=height3, x=width3)
    carr2.place(y=height1, x=width1)
    carr3.place(y=height2, x=width2)
    carr.place(x=0, y=400)
    vid.place(x=0, y=0, relheight=1, relwidth=1)
    if(game_over1):
        root.config(menu=menubar)
        end_canvas.pack_forget()
        score.place(y=0, x=1700)
        vid.place(x=0, y=0, relwidth=1, relheight=1)
        carr.place(y=400)
        carr4.place(y=height3, x=width3)
        carr2.place(y=height1, x=width1)
        carr3.place(y=height2, x=width2)
        game_over1 = False
        root.bind(f"<{car_up}>", goup)
        root.bind(f"<{car_down}>", godown)
        root.bind(f"<{car_right}>", gort)
        root.bind(f"<{car_left}>", golf)
        root.bind(f"<{boss_key}>", keyup)
        root.bind(f"<{pause_key}>", pause)


repeat = "no"

# This function saves the game data to the json file


def save_game():
    global repeat
    if not welcome_screen:
        with open("data.json", "r+") as file:
            player_data = json.load(file)
            length = len(player_data["resume"])
            i = 0
            k = 0
            position1 = 0
            position2 = 0
            while i < length and repeat == "no" and length != 0:
                if player_data["resume"][i]["name"] == name.upper():
                    repeat = "yes"
                    position1 = i
                    break
                i += 1
            while k < len(player_data["players"]) and repeat == "no":
                if player_data["players"][k]["name"] == name.upper():
                    repeat = "yes"
                    position2 = k
                    break
                k += 1
            player_data1 = {"name": name.upper(), "Score": score1, "Boss": boss_key, "Pause": pause_key,
                            'Up': car_up, 'Down': car_down, 'Right': car_right, 'Left': car_left}
            if length == 0:
                for h in player_data["players"]:
                    if h["name"] == player_data1['name']:
                        if h["Score"] < player_data1["Score"]:
                            h["Score"] = player_data1["Score"]
                        h["Boss"] = boss_key
                        h["Pause"] = pause_key
                        h["Up"] = car_up
                        h["Down"] = car_down
                        h["Right"] = car_right
                        h["Left"] = car_left
                        break
                    else:
                        player_data["players"].append(player_data1)
                        break
                if(len(player_data['players']) == 0):
                    player_data["players"].append(player_data1)
                player_data["resume"].append(player_data1)

            elif repeat == "yes" and length != 0:
                if length != 0:
                    player_data["resume"][position1]["Score"] = score1
                    for h in player_data["players"]:
                        if h["name"] == player_data["resume"][position1]["name"]:
                            if h["Score"] < player_data["resume"][position1]["Score"]:
                                h["Score"] = player_data["resume"][position1]["Score"]
                            h["Boss"] = boss_key
                            h["Pause"] = pause_key
                            h["Up"] = car_up
                            h["Down"] = car_down
                            h["Right"] = car_right
                            h["Left"] = car_left
                    if len(player_data['players']) != 0:
                        if player_data["players"][position2]["Score"] < score1:
                            player_data["players"][position2]["Score"] = score1
                        player_data["players"][position2]["Boss"] = boss_key
                        player_data["players"][position2]["Pause"] = pause_key
                        player_data['players'][position2]["Up"] = car_up
                        player_data['players'][position2]["Down"] = car_down
                        player_data['players'][position2]["Right"] = car_right
                        player_data['players'][position2]["Left"] = car_left
                    else:
                        player_data["players"].append(player_data1)
            elif repeat == "no" and length != 0:
                player_data["resume"].append(player_data1)
                player_data["players"].append(player_data1)
            file.seek(0)
            with open('data.json', 'w') as data_file:
                json.dump(player_data, file, indent=4)


def game_over():
    key_change.place(x=2000, y=2000)
    tree_frame.pack_forget()
    tree_scroll.pack_forget()
    my_tree.pack_forget()
    root.config(menu="")
    global repeat, game_over1
    game_over1 = True
    with open("data.json", "r+") as file:
        player_data = json.load(file)
        length = len(player_data["players"])
        i = 0
        position = 0
        while i < length and repeat == "no":
            if player_data["players"][i]["name"] == name.upper():
                repeat = "yes"
                position = i
            i += 1
        if repeat == "yes":
            if player_data["players"][position]["Score"] < score1:
                player_data["players"][position]["Score"] = score1
            player_data["players"][position]["Boss"] = boss_key
            player_data["players"][position]["Pause"] = pause_key
            player_data["players"][position]["Up"] = car_up
            player_data["players"][position]["Down"] = car_down
            player_data["players"][position]["Right"] = car_right
            player_data["players"][position]["Left"] = car_left
            for fi in player_data["players"]:
                if fi["name"] == player_data["players"][position]["name"] and int(len(player_data['players']) > 0):
                    del fi
                    player_data["resume"] = resume_list
                    break
        elif repeat == "no":
            player_data1 = {"name": name.upper(), "Score": score1, "Boss": boss_key, "Pause": pause_key,
                            'Up': car_up, 'Down': car_down, 'Right': car_right, 'Left': car_left}
            player_data["players"].append(player_data1)
        elif len(player_data["players"]) == 0:
            player_data1 = {"name": name, "Score": score1}
            player_data["players"] = player_data["players"].append(
                player_data1)
        file.seek(0)
        with open('data.json', 'w') as data_file:
            json.dump(player_data, file, indent=4)
        carr.place(x=4000, y=4000)
        carr2.place(x=4000, y=4000)
        carr3.place(x=4000, y=4000)
        carr4.place(x=4000, y=4000)
        vid.place(x=4000, y=4000)
        score.place(x=4000, y=4000)
        root.unbind(f"<{car_up}>")
        root.unbind(f"<{car_down}>")
        root.unbind(f"<{car_right}>")
        root.unbind(f"<{car_left}>")
        root.unbind(f"<{pause_key}>")
        over_screen1()

# This functions quits the game without saving data.


def endgame():
    root.quit()

# This checks during the process of changing the
# controls if the key is already in use


def txt_length(e=None):
    global allow_change
    if allow_change:
        global text1
        txt1 = e.keysym
        key_change.place(x=500, y=500)
        key_change.config(
            text=f'This particular control will now be activated using key {txt1}')
        if txt1 == boss_key or txt1 == car_down or txt1 == car_left or txt1 == car_up or txt1 == car_right or txt1 == pause_key or txt1 == 'c':
            allow_change = False
            key_change.config(
                text=f'This particular key is in use already.')
            if txt1 == 'c':
                key_change.config(
                    text=f'I cannot allow you to use this key.Think about why!')
        else:
            change(txt1)
        root.after(2000, lambda: key_change.place(x=2000, y=2000))
        root.bind(f"<{car_up}>", goup)
        root.bind(f"<{car_down}>", godown)
        root.bind(f"<{car_right}>", gort)
        root.bind(f"<{car_left}>", golf)
        root.bind(f"<{boss_key}>", keyup)
        root.bind(f"<{pause_key}>", pause)

# This functions checks which control the user will
# like to change and then changes it accordingly.


def change(x):
    global allow_change, pause_pressed, ktb_changed, car_up, car_down, car_left, car_right, pause_key, boss_key
    root.unbind("<KeyRelease>")
    allow_change = False
    if ktb_changed == 1:
        root.unbind(f'<{car_up}>')
        car_up = x
        root.bind(f'<{car_up}>', goup)
    if ktb_changed == 2:
        root.unbind(f'<{car_down}>')
        car_down = x
        root.bind(f'<{car_down}>', godown)
    if ktb_changed == 3:
        root.unbind(f'<{car_right}>')
        car_right = x
        root.bind(f'<{car_right}>', gort)
    if ktb_changed == 4:
        root.unbind(f'<{car_left}>')
        car_left = x
        root.bind(f'<{car_left}>', golf)
    if ktb_changed == 5:
        root.unbind(f'<{boss_key}>')
        boss_key = x
        root.bind(f'<{boss_key}>', keyup)
    if ktb_changed == 6:
        root.unbind(f'<{pause_key}>')
        pause_key = x
        root.bind(f'<{pause_key}>', pause)
    root.after(2000, pause)

# This unbinds all keys temporarily while the process of changing the controls
# is running.Sends the data of which key to change to txt_length function


def change_control1(x):
    global pause_pressed
    pause_pressed = True
    for f in root.bind():
        root.unbind(f'<{f}>')
    global allow_change
    key_change.config(text="Press a key")
    key_change.place(x=800, y=500)
    allow_change = True
    global ktb_changed
    ktb_changed = x
    # pause()
    root.bind("<KeyRelease>", txt_length)

# This checks when cheatcode is activated and when it is not


def cheatcode1(e):
    global cheatcode
    if (cheatcode):
        cheatcode = False
    else:
        cheatcode = True

# Function to open TopLevel with info about the game


def about():
    if not pause_pressed and not user_profile:
        pause()
        root.unbind(f'{pause_key}')
        abt = Toplevel()
        abt_width = 610
        abt_height = 610
        top_x = (app_width/2) - (abt_width/2)
        top_y = (app_height/2) - (abt_height/2)

        abt.geometry(f'{abt_width}x{abt_height}+{int(top_x)}+{int(top_y)}')
        abt.resizable(False, False)
        txt = Label(abt, image=about_game)
        txt.place(x=4, y=3)
        abt.title('About the Game')
        root.wait_window(abt)
        pause()
        root.bind(f'{pause_key}', pause)
    elif user_profile:
        abt = Toplevel()
        abt.resizable(False, False)
        abt_width = 610
        abt_height = 610
        top_x = (app_width/2) - (abt_width/2)
        top_y = (app_height/2) - (abt_height/2)
        abt.geometry(f'{abt_width}x{abt_height}+{int(top_x)}+{int(top_y)}')
        txt = Label(abt, image=about_game)
        txt.place(x=4, y=3)
        abt.title('About the Game')


def animate():
    button_window = my_canvas.create_window(
        button_wt, 610, anchor="nw", window=enter_button
    )
    enter_window = my_canvas.create_window(
        1200, enter_ht, anchor="nw", window=enter
    )


# NAVIGATION BAR
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_command(label="Pause", command=pause)
menubar.add_command(label="Resume", command=pause)
menubar.add_command(label="New Game", command=restart)
menubar.add_command(label="Save Game for Later", command=save_game)
change_car = Menu(menubar, tearoff=0)
change_car.add_command(label="Car-1", command=lambda: change_car1(1))
change_car.add_command(label="Car-2", command=lambda: change_car1(2))
change_car.add_command(label="Car-3", command=lambda: change_car1(3))
menubar.add_cascade(label="Change Car", menu=change_car)
change_controls = Menu(menubar, tearoff=0)
change_controls.add_command(
    label="Car Up Key", command=lambda: change_control1(1))
change_controls.add_command(
    label="Car Down Key", command=lambda: change_control1(2))
change_controls.add_command(label="Car Right Key",
                            command=lambda: change_control1(3))
change_controls.add_command(
    label="Car Left Key", command=lambda: change_control1(4))
change_controls.add_command(
    label="Boss Key", command=lambda: change_control1(5))
change_controls.add_command(
    label="Pause Key", command=lambda: change_control1(6))
menubar.add_cascade(label="Change Controls", menu=change_controls)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About the Game", command=about)
helpmenu.add_command(label="How to Play", command=how)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_command(label="Exit Game", command=endgame)


# Canvas for the Welcome Page
name_enter = PhotoImage(file="enter_name.png")
end_canvas = Canvas(root, width=1920, height=1080,
                    highlightthickness=0, bg="black")
replay = Button(root, image=play_again, command=restart)
end_canvas.create_window(130, 650, anchor="nw", window=replay)
end_canvas.create_rectangle(650, 100, 100, 850, fill="blue")

over_window = end_canvas.create_image(
    1000, 100, anchor="nw", image=over)
my_canvas = Canvas(root, width=1920, height=1080, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=start, anchor="nw")
enter = Label(root, image=name_enter, border=0)
name_e = Label(root, text="Enter your name:", bg="black",
               fg="#fca503", font=("Courier", 24, "italic"))
e = Entry(
    root, width=20, border=0, bg="#2e082c", fg="#fca503", font=("Courier", 24, "italic")
)
label_e = my_canvas.create_window(1230, 450, anchor="nw", window=name_e)
input_window = my_canvas.create_window(
    1230, 490, anchor="nw", window=e, height=50)
enter_window = my_canvas.create_window(
    1200, enter_ht, anchor="nw", window=enter)
enter_button = Button(root, command=get_name,
                      image=btn_image1, border=0, bg="yellow")
animate()


# KEY BINDINGS WITH VARIABLES TO SWITCH CONTROLS
root.bind(f"<{car_up}>", goup)
root.bind(f"<{car_down}>", godown)
root.bind(f"<{car_right}>", gort)
root.bind(f"<{car_left}>", golf)
root.bind(f"<{boss_key}>", keyup)
root.bind(f"<{pause_key}>", pause)
root.bind("<Return>", get_name)
root.configure(bg="black")
root.geometry('1980x1080')
# Formula to center the window when it is opened up on a screen.
# root.geometry(f'{app_width}x{app_height}+{int(center_x)}+{int(center_y)}')
root.mainloop()
