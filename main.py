from tkinter import *
from itertools import product
from collections import Counter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


roll_values = []
roll_occurrences = []

# create a window
root = Tk()

# .geometry adjusts the size of the window
root.geometry('750x600')
# change the window name
root.title("Pixelfixation Dice Distribution")
# change the windows icon
root.iconbitmap(r'die.ico')

# create a label
banner = Label(root, text='Add some dice to roll!')
# places the label in the window
banner.grid(row=0, column=1, columnspan=6)

# images of dice
blank_die_img = PhotoImage(file='blank_die.png')
d4_img = PhotoImage(file='d4.png')
d6_img = PhotoImage(file='d6.png')
d8_img = PhotoImage(file='d8.png')
d10_img = PhotoImage(file='d10.png')
d12_img = PhotoImage(file='d12.png')
d20_img = PhotoImage(file='d20.png')
c_dice_img = PhotoImage(file='clear_dice.png')
distribution_img = PhotoImage(file='dice_cup.png')

dice = []


def add_dice(sides):
    if len(dice) <= 3:
        dice.append(sides)
        update_blank_dice()


def clear_dice():
    dice.clear()
    update_blank_dice()


def distribution_button():
    update_distribution_data()
    embed_matplotlib()


def update_distribution_data():
    roll_values.clear()
    roll_occurrences.clear()
    for item in combos(dice):
        roll_values.append(item[0])
        roll_occurrences.append(item[1])


def embed_matplotlib():
    fig = Figure(figsize=(6.7, 4.9), dpi=100)
    fig.add_subplot(111).bar(roll_values, roll_occurrences)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2,column=1,rowspan=7,columnspan=5)


def combos(dice_list):
    possible = [[y for y in range(1, x + 1)] for x in dice_list]
    result = [sum(x) for x in product(*possible)]

    count = Counter(result)
    return count.items()

def update_blank_dice(): # works but has a list index out of range error
    for i in range(len(blank_dice)):
        if dice[i] != None:
            blank_dice[i].configure(image=int_to_dice_image(dice[i]))
        if dice[i] == None:
            blank_dice[i].configure(image=blank_die_img)

def int_to_dice_image(i):
    if i == 4:
        return d4_img
    elif i == 6:
        return d6_img
    elif i == 8:
        return d8_img
    elif i == 10:
        return d10_img
    elif i == 12:
        return d12_img
    elif i == 20:
        return d20_img
    else:
        return blank_die_img

# build dice buttons
d4_button = Button(root, image=d4_img, command=lambda: add_dice(4))
d6_button = Button(root, image=d6_img, command=lambda: add_dice(6))
d8_button = Button(root, image=d8_img, command=lambda: add_dice(8))
d10_button = Button(root, image=d10_img, command=lambda: add_dice(10))
d12_button = Button(root, image=d12_img, command=lambda: add_dice(12))
d20_button = Button(root, image=d20_img, command=lambda: add_dice(20))
clear_dice_button = Button(root, image=c_dice_img, command=clear_dice)
dice_distribution_button = Button(root, image=distribution_img, command=distribution_button)

# place dice buttons
d4_button.grid(row=1,column=0)
d6_button.grid(row=2,column=0)
d8_button.grid(row=3,column=0)
d10_button.grid(row=4,column=0)
d12_button.grid(row=5,column=0)
d20_button.grid(row=6,column=0)
clear_dice_button.grid(row=7,column=0)
dice_distribution_button.grid(row=8,column=0)

# spacer label because TK is bad
blank_label = Label(root, width=75)
blank_label.grid(row=1, column=4)

# build blank dice
blank_dice = [Label(root, image=blank_die_img), Label(root, image=blank_die_img),
              Label(root, image=blank_die_img), Label(root, image=blank_die_img)]

# place blank dice
blank_dice[0].grid(row=1,column=1,sticky=W)
blank_dice[1].grid(row=1,column=2,sticky=W)
blank_dice[2].grid(row=1,column=3,sticky=W)
blank_dice[3].grid(row=1,column=4,sticky=W)



# run the window in indefinitely
root.mainloop()