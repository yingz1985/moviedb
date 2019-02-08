# Imports
from tkinter import *
import dbview
import admin


class GUI:

    def __init__(self):
        # Create root
        self.root = Tk()
        self.root.title("Movies DataBase")
 #       self.root.configure(background=("misty rose"))

        # Creating the components
        self.mainframe = create_grid(self.root)

        self.search_choices = ['All Movies', 'Movie By Name', 'Movie By Year',
                               'Movie By Genre', 'Find Cast', 'Movie By Distributor',
                               'Distributor By Movie', 'Both Actor and Director', 'Find Person\'s Awards',
                               'Find Movie\'s Crew']
        self.drop_down_var = StringVar(self.root)
        self.drop_down = create_dropdown(self.root, self.mainframe, self.drop_down_var, choices=self.search_choices)

        # self.logo = PhotoImage(file='/Users/Dan/PycharmProjects/Movies DB/data/moviedb_logo.gif')
        self.title_label = Label(self.mainframe, text='MovieDb', font=('Impact', 30, 'bold'), background='#F5C517', width=10)
        # self.title_label = Label(self.mainframe, image=self.logo)
        self.filter_label = create_label(self.mainframe, text='Choose a Filter')

        self.search_box = create_entrybox(self.mainframe)
        self.filter_button = Button(self.mainframe, text='Filter', command=self.on_filter)
        
        self.admin_button = Button(self.mainframe,text="Admin mode",command=self.on_admin)

        # Adding components to grid
        self.title_label.grid(row=1, column=1, columnspan=3, pady=20)

        self.filter_label.grid(row=2, column=1)

        self.drop_down.grid(row=3, column=1)
        self.search_box.grid(row=3, column=2)
        self.filter_button.grid(row=3, column=3)
        self.admin_button.grid(row=0,column=5)

    def get_drop_down_value(self):
        return self.drop_down_var

    def get_search_box_text(self):
        return self.search_box.get()

    def on_filter(self):
        dbview.view(self)
    def on_admin(self):
       a = admin.adminView()
       a.mainloop()




def create_dropdown(root, parent, tk_var, choices, default=None):

    if default is None:
        default = choices[0]

    tk_var.set(default)

    drop_down = OptionMenu(parent, tk_var, *choices)
    return drop_down


def create_entrybox(parent):
    entry = Entry(parent)
    return entry


def create_button(parent, string='OK'):
    button = Button(parent, text=string)

    return button


def create_grid(parent):
    mainframe = Frame(parent)

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
 #   mainframe.configure(background="misty rose")
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    return mainframe


def create_label(parent, text, size='15'):
    font = ('Calibri', size)
    return Label(parent, text=text, font=font)


if __name__ == '__main__':
    gui = GUI()
    mainloop()


