import sys
import csv
from tabulate import tabulate  # third-party library
from operator import itemgetter  # third-party library
from random import choice


def main():
    if len(sys.argv) != 2:
        sys.exit("Invalid Arguements. Did you include function name?")
        # run program takes 2 commandline arguements: 'program.py' plus function caller.
    file_exist_check()
    print(arguements())


def arguements():
    match sys.argv[1]:
        case "read":
            return read()  # funtion to read csv file. Will output all data as table.
        case "write":
            return write()  # function to write csv file.
        case "find":
            return find()  # function to search contents of csv file.
        case "shuffle":
            return shuffle()  # funtion to return one random value from csv file.
        case _:
            return "Invalid Request"


def file_exist_check():
    # a function to check if 'cd.csv' exists in directory, if not it will create one with appropriate headers
    try:
        with open("./cd.csv") as file:
            reader = csv.DictReader(file)
    except FileNotFoundError:
        with open("./cd.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["Artist", "Album"])
            writer.writeheader()
    pass


def read():
    cds = []
    with open("./cd.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cds.append({"Artist": row["Artist"], "Album": row["Album"]})
        cds.sort(key=itemgetter("Album"))
        cds.sort(key=itemgetter("Artist"))
        if len(cds) < 1: # checks if any albums have been recorded, if nil will return 'Nothing recorded.' message
            sys.exit("Nothing recorded.")
    return tabulate(cds, headers="keys", tablefmt="heavy_grid")


def write():
    while True:
        try:
            artist = input("Artist: ").upper().strip() # strip surrounding blank space and convert to caps for ease of use
            album = input("Album: ").upper().strip()
            with open("./cd.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Artist", "Album"])
                writer.writerow({"Artist": artist, "Album": album})
        except EOFError:
            break
        # (ctrl + D) to interupt write loop. Allows multiple entries per run of program.
    return "\nDone." # once interupt has been initialised will end program with 'Done.' message.


def find():
    find = []
    request = input("Artist/Album: ").upper().strip()
    # if artist program will print all albums from sed artist, album will only print requested album if exists.
    with open("./cd.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if request in row:
                find.append(row)
    if len(find) > 0:
        return tabulate(find, headers=["Artist", "Album"], tablefmt="heavy_grid")
    sys.exit("No record.") # if no record of artist/album will end program with 'No record.' message.


def shuffle():
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
        sys.exit("Nothing recorded.") # if csv is empty of albums will return 'Nothind recorded.' message.
    else:
        return tabulate(artist_album, headers="keys", tablefmt="heavy_grid")


if __name__ == "__main__":
    main()
