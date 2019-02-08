from tkinter import *
from tkinter.ttk import *
from tkinter import font
import movieDB

def view(gui):
    db_window = Toplevel()
    db_window.wm_title("Results")

    db_info = Treeview(db_window)
    db_info.pack(fill='both', expand=True)

    dropdown_selected = gui.get_drop_down_value()
    state = dropdown_selected.get()

    query = gui.get_search_box_text()

    view_controller(db_window, db_info, state, query)


def view_controller(window, table, state, query):
    if state == 'All Movies':
        movie_search(table)
    elif state == 'Movie By Name':
        movie_name_search(table, query)
    elif state == 'Movie By Year':
        movie_year_search(table, query)
    elif state == 'Movie By Genre':
        movie_genre_search(table, query)
    elif state == 'Find Cast':
        cast_search(table, query)
    elif state == 'Movie By Distributor':
        convert_db(table, movieDB.findMoviesDistributedBy(query))
    elif state == 'Distributor By Movie':
        convert_db(table, movieDB.findDistributorsForMovie(query))
    elif state == 'Both Actor and Director':
        convert_db(table, movieDB.bothActorAndDirector())
    elif state == 'Find Person\'s Awards':
        convert_db(table, movieDB.findAwardsBy(query))
    elif state == 'Find Movie\'s Crew':
        convert_db(table, movieDB.findCrewForMovie(query))
    else:
        window.destroy()


def movie_search(table):
    convert_db(table, movieDB.viewMoviesAlpha())


def movie_name_search(table, query):
    convert_db(table, movieDB.everythingAboutMovie(query))


def movie_year_search(table, query):
    convert_db(table, movieDB.selectYear(query))


def cast_search(table, query):
    convert_db(table, movieDB.findPerson(query))


def movie_genre_search(table, query):
    convert_db(table, movieDB.findGenre(query))


def movie_distributor_search(table, query):
    convert_db(table, movieDB.findMoviesDistributedBy(query))


def convert_db(table, db):
    data = db.splitlines()
    columns = data[0].strip().split('\t')

    set_columns(table, columns)

    for row in data[1:]:
        insert_table(table, row.strip().split('\t'))

    autosize_cols(table, columns)


def set_columns(table, columns):
    table['columns'] = columns
    table.column('#0', anchor='center', width=30, stretch=1)

    for val in columns:
        table.heading(str(val), text=str(val))
        table.column(str(val), anchor='center', stretch=1)


def autosize_cols(table, columns):
    entries = table.get_children()
    default_font = font.Font(font='TkDefaultFont')

    for x in range(len(columns)):
        maxsize = 100
        maxnum_size = 30;
        for child in entries:
            # cellsize = len(str((table.item(child)['values'][x]))) * 8
            current_item = table.item(child)['values'][x]
            current_index = table.item(child)['text']
            cellsize = default_font.measure(str(current_item)) + 50
            indexsize = default_font.measure(str(current_index))

            if cellsize > maxsize:
                maxsize = cellsize
            if indexsize > maxnum_size:
                maxnum_size = indexsize
        table.column(columns[x], anchor='center', width=maxsize)
        table.column('#0', anchor='center', width=maxnum_size)


def insert_table(table, values):
    num_rows = len(table.get_children()) + 1
    table.insert('', 'end', text=num_rows, values=values)


def split_query(string):
    query = string.split()
    return query
