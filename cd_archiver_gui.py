import csv
from operator import itemgetter
from random import choice
from tabulate import tabulate
from tkinter import *
from tkinter import ttk as ttk

# set the window
window = Tk()
window.geometry("520x480")
window.resizable(False, False)
window.title("CD Archiver")
window.rowconfigure(1, minsize=480)
window.columnconfigure([0, 1, 2], minsize=520)


# create functions
def create():
    data_label.configure(state="normal")
    data_label.delete("1.0", END)
    try:
        with open("./cd.csv") as file:
            reader = csv.DictReader(file)
            data_label.insert("1.0", "Data Exists!")
    except FileNotFoundError:
        with open("./cd.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Artist", "Album"])
            writer.writeheader()
            data_label.insert("1.0", "Data CSV file created.")
    data_label.configure(state="disabled")


def read():
    data_label.configure(state="normal")
    data_label.delete("1.0", END)
    cds = []
    try:
        with open("./cd.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cds.append({"Artist": row["Artist"], "Album": row["Album"]})
            cds.sort(key=itemgetter("Album"))
            cds.sort(key=itemgetter("Artist"))
        data_label.insert("1.0", tabulate(cds))
    except FileNotFoundError:
        data_label.insert("1.0", "Please create CSV file first")
    data_label.configure(state="disabled")


def find():
    data_label.configure(state="normal")
    data_label.delete("1.0", END)
    found = []
    request = find_entry.get().upper().strip()
    # if artist program will print all albums from sed artist, album will only print requested album if exists.
    try:
        with open("./cd.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if request in row:
                    found.append(row)
    except FileNotFoundError:
        data_label.insert("1.0", "Please create CSV file first")
    else:
        if len(found) > 0:
            data_label.insert("1.0", tabulate(found))
        else:
            data_label.insert("1.0", "No record.")
    data_label.configure(state="disabled")


def shuffle():
    data_label.configure(state="normal")
    data_label.delete("1.0", END)
    try:
        list = []
        with open("./cd.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append({"Artist": row["Artist"], "Album": row["Album"]})
            shuffle = choice(list)
            artist = [shuffle["Artist"]]
            album = [shuffle["Album"]]
            artist_album = {"Artist": artist, "Album": album}
            # had to split shuffle variable into artist/album before combining into dict. Fixed table formatting problem.
    except IndexError:
        data_label.insert(
            "1.0", "Nothing recorded."
        )  # if csv is empty of albums will return 'Nothing recorded.' message.
    except FileNotFoundError:
        data_label.insert("1.0", "Please create CSV file first")
    else:
        data_label.insert("1.0", tabulate(artist_album))
    data_label.configure(state="disabled")


def write():
    data_label.configure(state="normal")
    data_label.delete("1.0", END)
    artist = (
        write_artist.get().upper().strip()
    )  # strip surrounding blank space and convert to caps for ease of use
    album = write_album.get().upper().strip()
    try:
        with open("./cd.csv") as file:
            reader = csv.DictReader(file)
    except FileNotFoundError:
        data_label.insert("1.0", "Please create CSV file first")
    else:
        if len(artist) > 0 and len(album) > 0:
            with open("./cd.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Artist", "Album"])
                writer.writerow({"Artist": artist, "Album": album})
                data_label.insert("1.0", f"Inserted {artist} - {album}")
        else:
            data_label.insert("1.0", "Fields empty")
    data_label.configure(state="disabled")


# setup frames
option_frame = Frame(  # frame for the main options menu; create, read, shuffle and find
    master=window,
    relief=RAISED,
    bd=5,
)
option_frame.pack(
    side=TOP,
)

write_frame = Frame(  # frame for the find function- space for artist/album entry
    master=window,
    relief=RAISED,
    bd=5,
)
write_frame.pack(side=TOP)

data_frame = Frame(
    master=window,
    relief=RAISED,
    bd=5,
    width=480,
    height=520
)
data_frame.pack(side=TOP)

# setup scrollbar for textbox
scroll = ttk.Scrollbar(master=data_frame, orient="vertical")
scroll.pack(side=RIGHT, fill="y")

# setup buttons
create_button = Button(
    master=option_frame,
    text="Create",
    command=create,
    fg="green",
    height=2,
)
create_button.pack(side=LEFT)

read_button = Button(
    master=option_frame,
    text="Read",
    command=read,
    fg="green",
    height=2,
)
read_button.pack(side=LEFT)

shuffle_button = Button(
    master=option_frame,
    text="Shuffle",
    command=shuffle,
    fg="green",
    height=2,
)
shuffle_button.pack(side=LEFT)


# find
find_entry = Entry(master=option_frame, width=25, fg="green")
find_entry.pack(side=LEFT)
find_button = Button(
    master=option_frame,
    text="Find",
    command=find,
    fg="green",
    height=2,
)
find_button.pack(side=LEFT)


# write frame
artist_label = Label(
    master=write_frame,
    text="Artist:",
    fg="green"
)
artist_label.pack(side=LEFT)
write_artist = Entry(
    master=write_frame,
    width=18,
    fg="green"
)
write_artist.pack(side=LEFT)

album_label = Label(
    master=write_frame,
    text="Album:",
    fg="green"
)
album_label.pack(side=LEFT)
write_album = Entry(
    master=write_frame,
    width=19,
    fg="green"
)
write_album.pack(side=LEFT)

write_button = Button(
    master=write_frame,
    text="Write",
    command=write,
    fg="green",
    height=2,
    width=15
)
write_button.pack(side=LEFT)

# main area/data label
data_label = Text(
    master=data_frame,
    font=("Times New Roman", 12, "bold italic"),
    bg="black",
    fg="green",
    width=480,
    height=520,
    yscrollcommand=scroll.set,
)
data_label.insert(
    "1.0",
    """CD Archiver. Please choose a function by clicking on the corresponding button.
                  
    CREATE: create your data file                                                  
    READ: read from and list whole collection                                      
    SHUFFLE: get a random choice                                                   
    FIND: type in the search bar and click find to search for a specific artist or
    album                                                                    
    WRITE: add a new album to your collection- type in the artist and album before 
    hitting write""",
)
data_label.configure(state="disabled")
scroll.config(command=data_label.yview)
data_label.pack()


window.mainloop()
