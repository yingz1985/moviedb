from tkinter import *
import movieDB
from tkinter.messagebox import showinfo


class chart:
    def info(self):
        if(len(self.name.get())==0 or len(self.budget.get())==0 or len(self.year.get())==0 or len(self.dur.get())==0 or len(self.rat.get())==0 or len(self.gen.get())==0 or len(self.lan.get())==0):
            return ""
        result = self.name.get()+"\n"+self.budget.get()+"\n"+self.year.get()+"\n"
        result+= self.dur.get()+"\n"+self.rat.get()+"\n"+self.gen.get()+"\n"+self.lan.get()
        return result
    
    def on_button(self):
        validate(self)

    def __init__(self):
        # Create root
        self.root = Tk()
        self.root.title("Edit Database")
        self.row = 0
        # Creating the components
        self.mainframe = create_grid(self.root)
        self.root.configure(background=('cornsilk'))

    
        self.createMovieEntries(self.mainframe)

    def createMovieEntries(self,grid):
        self.title_label = Label(grid, text='Movie Info', font=('Calibri', 14), width=10)
        self.title_label.grid(row=0, column=0, columnspan=2)
        
        self.movieName = create_label(grid, text='Name')
        self.movieName.grid(row=1,column=0)
        self.name = create_entrybox(grid)
        self.name.grid(row=1,column=1)

        
        self.movieBudget = create_label(grid, text='Budget')
        self.movieBudget.grid(row=2,column=0)
        self.budget = create_entrybox(grid)
        self.budget.grid(row=2,column=1)
        
        self.movieYear = create_label(grid, text='Year')
        self.movieYear.grid(row=3,column=0)
        self.year = create_entrybox(grid)
        self.year.grid(row=3,column=1)
        
        self.movieDuration = create_label(grid, text='Duration')
        self.movieDuration.grid(row=4,column=0)
        self.dur = create_entrybox(grid)
        self.dur.grid(row=4,column=1)
        
        self.movieRating = create_label(grid, text='Rating')
        self.movieRating.grid(row=5,column=0)
        self.rat = create_entrybox(grid)
        self.rat.grid(row=5,column=1)
        
        self.movieGenre = create_label(grid, text='Genre(s)')
        self.movieGenre.grid(row=6,column=0)
        self.gen = create_entrybox(grid)
        self.gen.grid(row=6,column=1)
        
        self.movieLanguage = create_label(grid, text='Language(s)')
        self.movieLanguage.grid(row=7,column=0)
        self.lan = create_entrybox(grid)
        self.lan.grid(row=7,column=1)

        self.finished = Button(self.mainframe,command=self.on_button,text="Done")
        self.finished.grid(row=8,column=0)

        
        
def validate(gui):
    string = gui.info()
    
    if(string==""):
        showinfo("Err","Please enter all the fields!")
        return 0
##    print(string)
    data = string.split("\n")
    returnVal = movieDB.insertMovie(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
    if(returnVal == False): #insert failed
        showinfo("Err","Movie already exists in database!")
        return 0
        
    
    
def create_label(parent, text, size='11'):
    font = ('Calibri', size)
    return Label(parent, text=text, font=font)

def create_entrybox(parent):
    entry = Entry(parent)
    return entry

def create_button(parent, string):
    button = Button(parent, text=string)
    return button

def create_grid(parent):
    mainframe = Frame(parent)

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)
    mainframe.configure(background='cornsilk')

    return mainframe

