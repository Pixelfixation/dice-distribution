from tkinter import *
import matplotlib.pyplot
import Plotter


class Ui:
    # create a window
    root = Tk()
    # images of dice
    blank_die_img = PhotoImage(file='blank_die.png')
    d4_img = PhotoImage(file='d4.png')
    d6_img = PhotoImage(file='d6.png')
    d8_img = PhotoImage(file='d8.png')
    d10_img = PhotoImage(file='d10.png')
    d12_img = PhotoImage(file='d12.png')
    d20_img = PhotoImage(file='d20.png')
    bar_img = PhotoImage(file="blank_bar.png")
    c_dice_img = PhotoImage(file='clear_dice.png')
    distribution_img = PhotoImage(file='dice_cup.png')

    bar_label = Label(root, width=640, height=480, image=bar_img)
    dice = []
    dice_slot_labels = []

    def __init__(self, max_dice, geometry_size, plotter):
        self.max_dice = max_dice
        for i in range(max_dice):
            self.dice.append(0)
            self.dice_slot_labels.append(Label(self.root, image=self.blank_die_img))
        self.geometry_size = geometry_size
        self.plotter = plotter

    def add_dice(self, value):
        i = self.open_die_slot()
        if i is not None:
            self.dice[i] = value
            self.update_dice_slots()

    def clear_dice(self):
        for i in range(self.max_dice):
            self.dice[i] = 0
        self.update_dice_slots()

    def distribution_button(self):
        self.plotter.update_distribution_data(self.dice)
        self.embed_plot(self.plotter.get_roll_values(), self.plotter.get_roll_occurrences())

    def generate_bar_plot(self, roll_values, roll_occurrences):
        plt = matplotlib.pyplot
        plt.style.use('dark_background')
        plt.title("Out of {} possible rolls".format(self.plotter.get_iterations(self.dice)))
        plt.ylabel("Occurrences of Unique Values")
        plt.xlabel("Roll Values")
        plt.bar(roll_values, roll_occurrences)
        plt.savefig("tmp_bar.png")
        plt.close("all")

    def generate_pie_plot(self, roll_values, roll_occurrences):
        pass

    def embed_plot(self, roll_values, roll_occurrences):
        self.generate_bar_plot(roll_values, roll_occurrences)
        self.bar_img = PhotoImage(file="tmp_bar.png")
        self.bar_label.configure(image=self.bar_img)

    def update_dice_slots(self):  # works but has a list index out of range error
        for i in range(len(self.dice)):
            if self.dice[i] != 0:
                self.dice_slot_labels[i].configure(image=self.int_to_dice_image(self.dice[i]))
            if self.dice[i] == 0:
                self.dice_slot_labels[i].configure(image=self.blank_die_img)

    def int_to_dice_image(self, i):
        if i == 4:
            return self.d4_img
        elif i == 6:
            return self.d6_img
        elif i == 8:
            return self.d8_img
        elif i == 10:
            return self.d10_img
        elif i == 12:
            return self.d12_img
        elif i == 20:
            return self.d20_img
        else:
            return self.blank_die_img

    def open_die_slot(self):
        for i in range(len(self.dice)):
            if self.dice[i] == 0:
                return i
        return None

    def setup_ui(self):
        # .geometry adjusts the size of the window
        self.root.geometry(self.geometry_size)
        # change the window name
        self.root.title("Pixelfixation Dice Distribution")
        # change the windows icon
        self.root.iconbitmap(r'die.ico')

        # create a label
        banner = Label(self.root, text='Add some dice to roll!')
        # places the label in the window
        banner.grid(row=0, column=1, columnspan=6)
        # build dice buttons
        d4_button = Button(self.root, image=self.d4_img, command=lambda: self.add_dice(4))
        d6_button = Button(self.root, image=self.d6_img, command=lambda: self.add_dice(6))
        d8_button = Button(self.root, image=self.d8_img, command=lambda: self.add_dice(8))
        d10_button = Button(self.root, image=self.d10_img, command=lambda: self.add_dice(10))
        d12_button = Button(self.root, image=self.d12_img, command=lambda: self.add_dice(12))
        d20_button = Button(self.root, image=self.d20_img, command=lambda: self.add_dice(20))
        clear_dice_button = Button(self.root, image=self.c_dice_img, command=self.clear_dice)
        dice_distribution_button = Button(self.root, image=self.distribution_img, command=self.distribution_button)

        # place dice buttons
        d4_button.grid(row=1, column=0)
        d6_button.grid(row=2, column=0)
        d8_button.grid(row=3, column=0)
        d10_button.grid(row=4, column=0)
        d12_button.grid(row=5, column=0)
        d20_button.grid(row=6, column=0)
        clear_dice_button.grid(row=7, column=0)
        dice_distribution_button.grid(row=8, column=0)

        # spacer label because TK is bad
        blank_label = Label(self.root, width=75)
        blank_label.grid(row=1, column=self.max_dice+2)

        spacer_label = Label(self.root,width=10)
        spacer_label.grid(row=1, column=1)

        # place blank dice
        for i in range(self.max_dice):
            self.dice_slot_labels[i].grid(row=1, column=i+2, sticky=W)

        self.bar_label.grid(row=2, column=1, rowspan=7, columnspan=self.max_dice+2, sticky=W)


        # run the window in indefinitely
        self.root.mainloop()
